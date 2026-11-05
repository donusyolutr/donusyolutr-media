# Marka ve içerik kuralları — @donusyolutr

## Kitle ve konu eksenleri (Ahmet'in kararı, 5 Kasım 2026)
1. Gurbetçiler — Almanya/Hollanda/Avusturya'da yaşayan Türkler
2. Sıla yolu — gurbetçilerin Türkiye'ye araçla geliş-dönüş yol sorunları
3. Alman/yabancı plakalı araçların Türkiye'de yaşadığı zorluklar
4. 50 yaş üstü okuyucu — sade dil, kısa cümle, büyük yazı, jargon yok

Konu dağılımı: haftada en az 2 gönderi eksen 3 (yabancı plaka), en fazla 1 doğrudan hizmet tanıtımı.

## Dil kuralları — ihlal = RED
- Gümrük müşavirliği ruhsatlı meslektir. YASAK: "beyanname veririz", "işlemlerinizi biz yaparız",
  "gümrükte sizi temsil ederiz". DOĞRU: "organize ediyoruz", "takip ediyoruz", "planlıyoruz".
- Satış/devir/kiralamayı ima eden ifade yok ("aracınızı alalım", "Türkiye'de satın" vb.).
- Gerçek belge görüntüsü/kopyası yok. Belgeden bahsedilecekse sadece adıyla.
- Korku/panik dili yok ("hapse girersiniz" gibi). Sakin, bilgilendirici ton.
- Siz dili. Emoji en fazla 2, sadece açıklamada (görselde yok).
- Çağrı (CTA): sadece "DM'den yazın". WhatsApp Business bağlanana kadar WhatsApp yazılmaz.

## Doğruluk kuralları — ihlal = RED
- Her hukuki iddia `kurallar/hukuki_cerceve.md` içindeki bir H-xx kuralına dayanmalı.
- Rakam, ücret, tarih, sınır kapısı kuralı, başka ülke mevzuatı (vinyet, ehliyet, sigorta vb.):
  ya H-xx'te olmalı ya da resmi kaynaktan (devlet sitesi, ADAC, ÖAMTC, resmi otoyol işletmesi)
  o çalışmada doğrulanıp `kaynaklar` alanına URL ile yazılmalı. Doğrulanamayan rakam yazılmaz.
- "Açık sorular" listesindeki konularda kesin hüküm verilmez.

## Görsel standardı
Ana format REELS: 1080x1920, 4-7 sahne, Türkçe seslendirme + altyazı. Üretim: `otomasyon/reels.py` + Descript. (Carousel: `otomasyon/render.py`, şu an kullanılmıyor.)
Sahne alanları: ton (cover|yes|no|info|cta), ust (en fazla 25 karakter), metin (en fazla 60 karakter).
Seslendirme: 20-35 saniye (45-80 kelime), ilk cümle kanca, son cümle "DM'den yazın".

## Açıklama (caption)
2-4 kısa paragraf + 4-8 hashtag (#gurbetçi #sılayolu #yabancıplaka #almanyaplaka #gümrük ...).
