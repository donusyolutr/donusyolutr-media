# Otomatik üretim hattı — çalıştırma talimatı

Bu dosyayı zamanlanmış görev her çalıştığında baştan sona uygular.
Roller: ORKESTRATÖR (ana oturum) · YAZAR (ayrı agent) · KONTROLCÜ (ayrı, yazarı görmemiş agent).

## 0. Hazırlık
- Depo: `donusyolutr/donusyolutr-media`. Metricool brandId: `7497966`, saat dilimi `Europe/Istanbul`.
- `pip install --break-system-packages -q cairosvg` (yoksa).
- Oku: `kurallar/hukuki_cerceve.md`, `kurallar/marka.md`, `yayin_log.csv`.

## 1. Hedef slotu bul (ORKESTRATÖR)
- Hedef: bugünden sonraki ilk iş günü (Pzt-Cuma) saat 10:00, `yayin_log.csv`'de o tarihte kayıt yoksa.
  Metricool'da `getScheduledPosts` ile o gün başka planlı gönderi var mı kontrol et; varsa sonraki iş gününe geç
  (en fazla 3 iş günü ileri bak).
- Aylık sınır: `yayin_log.csv`'de hedef ayda durum=planlandi kayıt sayısı ≥ 20 ise DUR, bildirim gönder:
  "Aylık 20 sınırı doldu, <ay> için üretim durdu."

## 2. Yazım (YAZAR agent'ı)
Agent tool ile yeni bir agent başlat. Ona ver: iki kural dosyasının TAM metni, `yayin_log.csv`'deki
son 15 konu başlığı, sayfa şeması. Görevi:
- Önceki konuları tekrar etmeyen, eksen dağılımına uyan BİR konu seç.
- `icerik/taslak/<NN>_<kisa_ad>.json` üret: `{id, eksen, caption, slides[], iddialar[], kaynaklar[]}`.
  `iddialar`: gönderideki her olgusal iddia için `{metin, dayanak}` — dayanak bir H-xx kodu ya da kaynak URL.
- Rakam/kural içeren ve H-xx'te olmayan her bilgi için WebSearch/WebFetch ile resmi kaynak bul;
  bulamazsa o bilgiyi gönderiden ÇIKAR.
NN = `yayin_log.csv`'deki en büyük numara + 1 (iki haneli).

## 3. Kontrol (KONTROLCÜ agent'ı — yazarın bağlamını görmez)
Yeni bir Agent başlat. Ona SADECE ver: iki kural dosyasının tam metni + taslak JSON'un yolu.
Yazarın gerekçesini verme. Görevi, her madde için GEÇTİ/KALDI ve kısa gerekçe yazmak:
1. Gönderideki HER cümleyi tara; olgusal iddia içeren ama `iddialar`da olmayan cümle var mı? → KALDI
2. Her H-xx dayanağı, iddiayı gerçekten karşılıyor mu (kuraldan geniş/farklı bir şey söylemiyor mu)? → değilse KALDI
3. Her URL dayanağını WebFetch ile aç; kaynak resmi mi, iddiayı birebir destekliyor mu? → değilse KALDI
4. "Açık sorular"da kesin hüküm var mı? → KALDI
5. Dil kuralları (yasak ifadeler, CTA, ton, 50+ okunabilirlik) → ihlal KALDI
6. Uzunluk sınırları.
Çıktı: `icerik/taslak/<id>_kontrol.md` + son satırda tek kelime: `KARAR: ONAY` veya `KARAR: RED`.

RED ise: kontrol notunu YAZAR'a (yeni agent, notla birlikte) ver, düzeltsin, KONTROLCÜ'yü YENİDEN (yeni agent)
çalıştır. En fazla 2 düzeltme turu. Hâlâ RED → taslağı `icerik/bekleyen/`a taşı, push et, bildirim:
"<id> kontrolden geçmedi, bekleyen klasöründe." ve DUR (o gün gönderi planlanmaz).

## 4. Görsel üretim ve görsel kontrol (ORKESTRATÖR)
- `python3 otomasyon/render.py icerik/taslak/<id>.json gonderiler/`
- Her PNG'yi Read ile aç: taşan/kesilen metin, üst üste binen satır, boş sayfa var mı? Varsa JSON'da metni
  kısalt (anlamı değiştirmeden) ve yeniden render et. Anlam değişecekse → bekleyen/ ve dur.
- JSON'u `icerik/onayli/`a taşı (kontrol notuyla birlikte).

## 5. Yükleme ve planlama
- `git add -A && git commit -m "<id>: <başlık>" && git push`
- `createScheduledPost`: blogId 7497966, providers instagram, type POST, autoPublish true,
  media = `https://raw.githubusercontent.com/donusyolutr/donusyolutr-media/main/gonderiler/<id>_NN.png` sırayla,
  text = caption, isAiGenerated false (metin grafiği).
- Yanıttaki media listesi `static.metricool.com` adreslerine dönmediyse → hata say, bildirim gönder.
- `yayin_log.csv`'ye satır ekle: `numara,id,baslik,eksen,tarih,durum=planlandi,metricool_id`. Commit + push.

## 6. Bildirim
Tek kısa mesaj (PushNotification varsa onunla): "<tarih> 10:00 için planlandı: <başlık>. Beğenmezsen
Metricool'dan sil." + plannerUrl.
