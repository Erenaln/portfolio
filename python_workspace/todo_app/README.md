# TODO App (CLI)

Python ile geliştirilen, komut satırı (CLI) tabanlı bir görev yönetim uygulaması. Kullanıcının görev ekleyip, listeleyip, güncelleyip silebildiği basit ama işlevsel bir CRUD uygulaması.

## Özellikler

- **Görev Ekleme** — Yeni görev oluşturma
- **Görev Silme** — Numarayla belirtilen görevi listeden çıkarma
- **Görev Güncelleme** — Var olan bir görevi düzenleme
- **Görev Listeleme** — Tüm görevleri numaralandırılmış şekilde görüntüleme
- **Hata Kontrolü** — Boş liste ve geçersiz numara girişlerine karşı kontrol
- **Kullanıcı Deneyimi** — Terminal ekranını otomatik temizleme, işlem sonrası bilgilendirme mesajları

## Kullanılan Teknolojiler

- Python 3
- `os` modülü (terminal ekranı temizleme)
- `time` modülü (kullanıcı bilgilendirme gecikmeleri)

## Nasıl Çalıştırılır

```bash
python todo.py
```

Program açıldığında ekrandaki menüden bir seçenek girerek (1-4 ve çıkış için 0) işlem yapabilirsiniz.

## Geliştirme Günlüğü

- Proje, fonksiyonlara bölünerek modüler hale getirildi (add/delete/update/list ayrı fonksiyonlarda)
- Kullanıcı girişleri için hata kontrolü (geçersiz/aralık dışı numara, boş liste) eklendi
- Terminal deneyimini geliştirmek için ekran temizleme ve zamanlamalı bilgilendirme mesajları eklendi

## Sırada Ne Var

- Verinin kalıcı olması için JSON/dosya tabanlı kayıt sistemi
- SQLite ile veritabanı entegrasyonu
- Flask ile web arayüzüne taşıma