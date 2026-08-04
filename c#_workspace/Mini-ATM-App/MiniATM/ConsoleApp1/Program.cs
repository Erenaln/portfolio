using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MiniATM
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Giriş bölümü / Anasayfa
            //Kullanıcıdan gitmek istediği menüyü alır.

            Console.WriteLine("Hoşgeldiniz!");
            Console.WriteLine("Lütfen işlem yapmak istediğiniz menüyü tuşlayın.");
            Console.WriteLine();
            Console.WriteLine("1 - Bakiye görüntüleme.");
            Console.WriteLine("2 - Para Çek");
            Console.WriteLine("3 - Para yatır.");
            Console.WriteLine("x - Çıkış yap.");
            String secim = Console.ReadLine();
            double bakiye = 543.32;

            // 1 yazıldığında mevcut bakiyeyi gösterir
            if (secim == "1")
            {
                Console.WriteLine("Mevcut bakiyeniz = " + bakiye);
                Console.WriteLine("Çıkmak için bir tuşa basın.");
                Console.ReadKey(true);
            }

            // 2 yazıldığında bir tutar ister ve girilen tutarı mevcut bakiyeye ekler.
            else if (secim == "2")
            {
                Console.WriteLine("Çekmek istediğiniz tutarı giriniz.");
                int cekilecek_tutar = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine("İşleminiz tamamlanıyor, lütfen bekleyiniz.");
                double yeniBakiye = (bakiye - cekilecek_tutar);
                if (cekilecek_tutar > bakiye)
                {
                    Console.WriteLine();
                    Console.WriteLine("Yetersiz bakiye.");
                }
                else 
                {
                    Console.WriteLine("");
                    Console.WriteLine("İşleminiz tamamlanmıştır.");
                    Console.WriteLine("");
                    Console.WriteLine("Yeni bakiyeniz = " + yeniBakiye);
                    Console.WriteLine("Çıkmak için bir tuşa basın.");
                    Console.ReadKey(true);
                }

            }

            // 3 yazıldığında bir tutar ister ve girilan tutarı mevcut bakiyeden çıkarır
            else if (secim == "3")
            {
                Console.WriteLine("Yatırılacak tutarı giriniz");
                int yatirilacak_tutar = Convert.ToInt32((Console.ReadLine()));
                Console.WriteLine("İşleminiz yapılıyor, lütfen bekleyiniz.");
                double yeniBakiye = (bakiye + yatirilacak_tutar);
                Console.WriteLine("");
                Console.WriteLine("İşleminiz tamamlanmıştır.");
                Console.WriteLine("");
                Console.WriteLine("Yeni bakiyeniz = " + yeniBakiye);
                Console.WriteLine("Çıkmak için bir tuşa basın.");
                Console.ReadKey(true);

            }

            // x girildiğinde bu mesajı oynatır ve 3 saniye sonra program kapanır.
            else if (secim == "x")
            {
                Console.WriteLine("Çıkış yapılıyor. Tekrar bekleriz!");
                System.Threading.Thread.Sleep(3000);

            }

            // yukarıda belirtilen tuşlar haricinde herhangi bir tuşa basılırsa bu metin oynatılır ve 3 saniye sonra program kapanır
            else 
            {
                Console.WriteLine("Beklenmeyen bir durum oluştu. Uygulama kapanıyor!");
                System.Threading.Thread.Sleep(3000);

            }
        }
    }
}
