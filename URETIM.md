# Otomatik üretim hattı — çalıştırma talimatı (REELS)

Zamanlanmış görev her iş günü ~10:00'da çalışır ve bu dosyayı baştan sona uygular.
Roller: ORKESTRATÖR (ana oturum) · YAZAR (ayrı agent) · KONTROLCÜ (ayrı, yazarı görmemiş agent).
Ana format: Instagram REELS (dikey video + Türkçe seslendirme + altyazı). Carousel üretilmez.

## 0. Hazırlık
- Depo: `donusyolutr/donusyolutr-media`. Metricool brandId `7497966`, saat dilimi `Europe/Istanbul`.
- `pip install --break-system-packages -q cairosvg` (yoksa). ffmpeg kurulu olmalı.
- Oku: `kurallar/hukuki_cerceve.md`, `kurallar/marka.md`, `yayin_log.csv`.
- AĞ KISITI: Bu ortam elevenlabsusercontent / descriptusercontent adreslerinden dosya İNDİREMEZ. İndirmeye
  çalışma. Ses ve son video sadece URL olarak servisler arasında taşınır (ElevenLabs → Descript → Metricool).

## 1. Hedef slotu bul (ORKESTRATÖR)
- Yayın saati: **19:00 İstanbul** (Almanya'da 17:00 — gurbetçi kitle iş çıkışı; Türkiye'de akşam yoğunluğu).
- Hedef: BUGÜN 19:00 (bugün iş günü ve `yayin_log.csv`'de bugüne kayıt yoksa). Değilse sonraki iş günü 19:00.
  Metricool `getScheduledPosts` ile o gün başka planlı gönderi var mı kontrol et; varsa sonraki iş gününe geç.
- Aylık sınır: hedef ayda `durum=planlandi` kayıt sayısı ≥ 20 ise DUR, bildirim: "Aylık 20 sınırı doldu."

## 2. Yazım (YAZAR agent'ı)
Agent tool ile yeni agent. Ona ver: iki kural dosyasının TAM metni, `yayin_log.csv`'deki son 15 konu, aşağıdaki şema.
- Tekrar etmeyen, eksen dağılımına uyan BİR konu seç.
- `icerik/taslak/<NN>_<kisa_ad>.json` üret:
  `{id, eksen, baslik, caption, reels: {seslendirme, sahneler: [{ton, ust, metin}]}, iddialar: [{metin, dayanak}], kaynaklar: []}`
  - `seslendirme`: 20-35 saniyelik (yaklaşık 45-80 kelime) konuşma metni. İlk cümle soru veya çarpıcı tespit (kanca).
    Son cümle "DM'den yazın" ile biter. Sade, kısa cümleler; 50+ dinleyici.
  - `sahneler`: 4-7 sahne. ton ∈ cover|yes|no|info|cta; ilk sahne cover, son sahne cta. `ust` en fazla 25 karakter,
    `metin` en fazla 60 karakter. Sahneler seslendirmenin sırasını izler.
  - `iddialar`: seslendirme + sahneler + caption'daki her olgusal iddia; dayanak = H-xx kodu veya resmi kaynak URL.
- H-xx'te olmayan rakam/kural için WebSearch/WebFetch ile resmi kaynak bul; bulamazsa o bilgiyi ÇIKAR.
NN = `yayin_log.csv`'deki en büyük numara + 1 (iki haneli).

## 3. Kontrol (KONTROLCÜ agent'ı — yazarın bağlamını görmez)
Yeni Agent. Ona SADECE: iki kural dosyasının tam metni + taslak JSON yolu. Her madde için GEÇTİ/KALDI + gerekçe:
1. Seslendirme, sahneler ve caption'daki HER cümle: olgusal iddia içerip `iddialar`da olmayan var mı? → KALDI
2. Her H-xx dayanağı iddiayı gerçekten karşılıyor mu (kuraldan geniş/farklı değil)? → değilse KALDI
3. Her URL dayanağını WebFetch ile aç; resmi mi, iddiayı birebir destekliyor mu? → değilse KALDI
4. "Açık sorular"da kesin hüküm var mı? → KALDI
5. Dil kuralları (yasak ifadeler, CTA, ton, 50+ anlaşılırlık) → ihlal KALDI
6. Uzunluk: seslendirme 45-90 kelime, sahne sınırları.
Çıktı: `icerik/taslak/<id>_kontrol.md`, son satır `KARAR: ONAY` veya `KARAR: RED`.
RED → kontrol notuyla YAZAR'ı (yeni agent) düzelttir, KONTROLCÜ'yü yeni agent olarak tekrar çalıştır.
En fazla 2 düzeltme turu. Hâlâ RED → `icerik/bekleyen/`a taşı, push, bildirim, DUR.

## 4. Seslendirme (ElevenLabs bağlantısı)
- `creative_generate_speech`: model `eleven_v4`, voice_id `qHdpkLDluFJPQyEvzZ5E` (Mehmet Akif), generations_count 1,
  prompt = `reels.seslendirme`. ASLA tekrar çağırma (her çağrı kredi harcar).
- `creative_get_flow_run_status` ile tamamlanana kadar bekle. `duration_secs` ve `content_url`'yi al.
- Hata → bildirim, DUR.

## 5. Sessiz video (ORKESTRATÖR)
- `python3 otomasyon/reels.py icerik/taslak/<id>.json <duration_secs> gonderiler/`
  → `gonderiler/<id>_reels.mp4` (sessiz, 1080x1920) + `<id>_kapak.jpg`.
- Kontrol: `ffmpeg -ss <t> -frames:v 1` ile her sahneden bir kare al, Read ile bak: taşan/kesilen metin,
  @donusyolutr imzası görünür mü? Sorun varsa sahne metnini anlamı değiştirmeden kısalt, yeniden üret.
- JSON'u (ve kontrol notunu) `icerik/onayli/`a taşı. `git add -A && git commit && git push`.

## 6. Birleştirme ve altyazı (Descript bağlantısı)
- `import_media`: project_name `donusyolutr reels <id>`, add_media:
  `video.mp4` = raw.githubusercontent URL'si (`https://raw.githubusercontent.com/donusyolutr/donusyolutr-media/main/gonderiler/<id>_reels.mp4`),
  `ses.mp3` = ElevenLabs content_url (language "tr"),
  `reels` = tracks [{media: ses.mp3}, {media: video.mp4, mute: true}].
  add_compositions: [{name "Reels", width 1080, height 1920, fps 30, clips [{media "reels"}]}]. `wait_for_job`.
- `prompt_project_agent` (composition_id = oluşan kompozisyon):
  "Bu dikey Reels kompozisyonuna Türkçe altyazı ekle: transkripte birebir, 2 kelimelik gruplar, büyük kalın beyaz
  yazı, koyu yarı saydam zemin, alttan ~%22 yukarıda, ortadaki başlık metniyle çakışmasın. Video, sıra ve sese
  dokunma, kesme yapma, müzik ekleme." `wait_for_job`.
- `publish_project`: media_type Video, resolution 1080p, access_level unlisted. `wait_for_job` → `download_url`, `share_url`.

## 7. Planlama (Metricool)
- `createScheduledPost`: blogId 7497966, date = hedef slot, info:
  providers [instagram], instagramData {type "REEL", showReelOnFeed true, isAiGenerated true},
  media [download_url], text = caption, autoPublish true, draft false.
- Yanıttaki media `static.metricool.com/...mp4` değilse → hata, bildirim.
- `yayin_log.csv`'ye satır: `numara,id,baslik,eksen,tarih,planlandi,metricool_id`. Commit + push.

## 8. Bildirim
Tek kısa mesaj: "<tarih> 19:00 için reels planlandı: <başlık>. İzle: <share_url>. Beğenmezsen Metricool'dan sil."
