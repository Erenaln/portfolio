import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import yt_dlp

load_dotenv()
BotToken = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Kuyrukta artık hem URL'yi hem de şarkı adını (title) sözlük (dictionary) olarak tutacağız.
queue = []

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")
    await bot.tree.sync()

@bot.tree.command(name="play", description="Şarkı çalar veya sıraya ekler")
async def play(interaction: discord.Interaction, url: str):
    # İşlemin 3 saniyeden uzun süreceğini Discord'a bildiriyoruz (Timeout hatasını engeller)
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.followup.send("Bir ses kanalına girin!")
        return
    
    channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client
    
    try:
        # Askıda kalan bağlantıları temizleyip, 20 saniye toleransla kanala bağlanıyoruz
        if voice_client is None or not voice_client.is_connected():
            if voice_client:
                await voice_client.disconnect()
            voice_client = await channel.connect(timeout=20.0)       
    except Exception as e:
        await interaction.followup.send("Kanala bağlanırken bir zaman aşımı oluştu. Lütfen botu sesten atıp tekrar deneyin.")
        return

    await interaction.followup.send(f"Şarkı işleniyor... ⏳")

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,          # Uyarıları kapatarak arka planı yormasını engelleriz
        'default_search': 'auto',     # Eğer link değil de "Tarkan" gibi isim yazılırsa anında aramaya zorlar
        'source_address': '0.0.0.0'   # İnternet bağlantısını IPv4'e zorlar (IPv6 bazen YouTube'da ciddi yavaşlama yapar)
    }

    try:
        # YouTube aramasını botu dondurmamak için arka plana alıyoruz (Takılmaları engeller)
        loop = asyncio.get_event_loop()
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))
            audio_url = info['url']
            title = info.get('title', 'Bilinmeyen Şarkı')

        if voice_client.is_playing() or voice_client.is_paused():
            # URL ve Başlığı beraber kaydediyoruz
            queue.append({"url": audio_url, "title": title}) 
            await interaction.followup.send(f"Sıraya eklendi: **{title}** 📝")

        else:
            ffmpeg_options = {'options': '-vn'}

            voice_client.play(
                discord.FFmpegPCMAudio(audio_url, **ffmpeg_options), 
                after=lambda e: play_next(interaction)
            )
            await interaction.followup.send(f"Şu an çalıyor: **{title}** 🎶")

    except Exception as e:
        await interaction.followup.send(f"Şarkı yüklenirken bir hata oluştu: {e}")


def play_next(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client
    
    if len(queue) > 0:
        # Kuyruktan sıradaki şarkının verilerini alıyoruz
        next_item = queue.pop(0)
        next_audio_url = next_item["url"]
        
        ffmpeg_options = {
            # Bu ayar müziğin ses verisini daha hızlı önbelleğe almasını ve kopmamasını sağlar
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn' # Görüntüyü yoksay, sadece sesi al
        }
        
        voice_client.play(
            discord.FFmpegPCMAudio(next_audio_url, **ffmpeg_options), 
            after=lambda e: play_next(interaction)
        )

@bot.tree.command(name="pause", description="Mevcut şarkıyı duraklatır")
async def pause(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await interaction.response.send_message("Şarkı duraklatıldı! ⏸️")
    else:
        await interaction.response.send_message("Şu anda çalan şarkı yok!")
    
@bot.tree.command(name="resume", description="Mevcut şarkıyı devam ettirir")
async def resume(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await interaction.response.send_message("Şarkı devam ediyor! ▶️")
    else:
        await interaction.response.send_message("Devam edecek şarkı bulunamadı!")
    
@bot.tree.command(name="skip", description="Mevcut şarkıyı atlar")
async def skip(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await interaction.response.send_message("Sıradaki şarkıya geçiliyor... ⏭️")
    else:
        await interaction.response.send_message("Geçilecek şarkı bulunamadı!")
    
@bot.tree.command(name="remove", description="Belirtilen sıradaki şarkıyı listeden kaldırır")
async def remove(interaction: discord.Interaction, queue_no: int):
    # Eğer kuyruk boşsa işlemi durduruyoruz
    if len(queue) == 0:
        await interaction.response.send_message("Sırada silinecek şarkı yok!")
        return
    
    # Kullanıcının girdiği sayının listede olup olmadığını kontrol ediyoruz
    if queue_no < 1 or queue_no > len(queue):
        await interaction.response.send_message(f"Lütfen `1` ile `{len(queue)}` arasında geçerli bir numara girin.")
        return

    # Yazılım dillerinde listeler 0'dan, insanlar 1'den saymaya başlar. 
    # Bu yüzden kullanıcının girdiği sayıdan 1 çıkararak (pop) doğru şarkıyı siliyoruz.
    removed_item = queue.pop(queue_no - 1)
    await interaction.response.send_message(f"**{removed_item['title']}** sıradan çıkarıldı! 🗑️")


@bot.tree.command(name="list", description="Sıraya eklenen şarkıları listeler")
async def list(interaction: discord.Interaction):
    if len(queue) == 0:
        await interaction.response.send_message("Şu an sırada hiç şarkı yok. 🎵")
        return
    
    # Listedeki şarkıları numaralandırarak alt alta ekliyoruz
    liste_metni = "**🎶 Şarkı Kuyruğu:**\n"
    for index, item in enumerate(queue):
        liste_metni += f"`{index + 1}.` {item['title']}\n"
    
    await interaction.response.send_message(liste_metni)


@bot.tree.command(name="stop", description="Botu ses kanalından çıkarır")
async def stop(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message("Bir ses kanalına girin!")
        return
    
    channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client

    if voice_client is not None and voice_client.is_connected():
        queue.clear() # Bot çıkarken sıradaki şarkıları da temizliyoruz
        await voice_client.disconnect()
        await interaction.response.send_message(f"{channel.name} kanalından çıkıldı ve sıra temizlendi! 🛑")
    else:
        await interaction.response.send_message("Ses kanalı bulunamadı!")

bot.run(BotToken)