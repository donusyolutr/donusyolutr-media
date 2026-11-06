# Kontrol raporu: 05_sure_dolunca_ne_olur

Kontrolcü: bağımsız KONTROLCÜ (6 Kasım 2026)
Okunan dosyalar: kurallar/hukuki_cerceve.md, kurallar/marka.md, icerik/taslak/05_sure_dolunca_ne_olur.json

## 1. Listede olmayan olgusal iddia: GEÇTİ
Seslendirme, 6 sahne ve caption cümle cümle tarandı. Bütün olgusal cümleler `iddialar` listesindeki 7 maddeden birine karşılık geliyor (1/4 idari para cezası, el konulabilir, emanet teslim süreyi durdurur, il gümrük idaresi, 7 gün, memur refakati/çekici, e-Devlet sorgusu). Geri kalan cümleler hizmet ya da yönlendirme cümlesi: "Teslimi ve çıkışı birlikte planlıyoruz", "süreci takip ediyoruz", "DM'den yazın". Kapak cümlesi "sakin bir yol var" genel bir ifade, tek başına mevzuat iddiası sayılmadı.

## 2. H-xx dayanaklarının kapsamı: KALDI
- H-06: "uygulanır" ve "el konulabilir" kuraldaki kipleri koruyor. Uygun.
- H-07, H-10, H-11: Kuralla birebir aynı. Uygun.
- H-08 seslendirmede ve caption'da doğru ("İç gümrüğe teslimden sonra"). "Çekiciyle" ifadesi, kuraldaki "başka araç üzerinde (çekici)" ifadesinden daha dar. Kapsamı genişletmediği için kabul edildi.
- **İhlal: 5. sahnenin `ust` alanı "Teslimden sonra 7 gün" diyor.** H-08 yalnızca *iç gümrüğe* teslimden sonraki 7 günü kapsıyor. Bu sahne, hemen önündeki 3. sahnenin ("Emaneten teslim") devamı olarak okunuyor. İzleyici "emaneten teslimden sonra 7 gün içinde çıkarmak zorundayım" diye anlar. Emanet teslimi (H-07) ile iç gümrüğe teslimi (H-08) birbirine bağlayan bir kural yok. Kısaltma kuralın kapsamını genişletiyor ve iki kuralı listede olmayan bir şekilde bağlıyor. Şüpheli olduğu için KALDI.
  - Düzeltme önerisi: `ust`: "İç gümrüğe teslim sonrası" (25 karakter), `metin`: "7 gün içinde çıkış: memur refakatinde ya da çekiciyle" (53 karakter).

## 3. URL dayanakları: GEÇTİ
`kaynaklar` alanı boş. Taslaktaki rakamların hepsi (1/4, 7 gün) H-xx kurallarında geçiyor. Açılacak URL yok.

## 4. Açık sorular: GEÇTİ
Vekilin iç gümrükten aracı alıp sürerek çıkarması, şirket aracı ve servise bırakma istisnası hakkında hiçbir hüküm yok. "Teslimi ve çıkışı birlikte planlıyoruz" cümlesi aracı kimin çıkaracağını söylemiyor.

## 5. Dil kuralları: GEÇTİ (notlarla)
- Yasak ifadeler ("beyanname veririz", "işlemlerinizi biz yaparız", "temsil ederiz") yok. Kullanılan dil "planlıyoruz" ve "takip ediyoruz".
- Satış, devir ya da kiralama imâsı yok.
- Korku dili yok. Ceza bilgisi sakin bir tonla veriliyor ve "el konulabilir" ifadesiyle yumuşatılmış.
- Siz dili tutarlı.
- Emoji sayısı 0 (python ile sayıldı).
- WhatsApp geçmiyor. CTA "DM'den yazın".
- Caption 3 metin paragrafı ve 6 hashtag içeriyor.
- Not (50+ okuyucu): "sevk", "memur refakatinde", "idari para cezası" ve "emaneten" jargona yakın terimler. Kuraldaki ifadeyle aynı oldukları için hata sayılmadı. Yine de altyazıda sadeleştirmek düşünülebilir (ör. "gümrük memuru eşliğinde").
- Not: cta sahnesinin metni ("çıkışı birlikte planlayalım") "DM'den yazın" ifadesini içermiyor. Seslendirme ve caption'da CTA doğru olduğu için ihlal sayılmadı. Sahnenin de "DM'den yazın" ile kapanması önerilir.

## 6. Uzunluk ve yapı: GEÇTİ
Sayımlar python ile yapıldı.
- Seslendirme 66 kelime. Görevdeki 45-90 aralığına da, marka.md'deki 45-80 aralığına da uyuyor.
- İlk cümle bir kanca: "Aracınızın süresi dolmak üzere mi?"
- Son cümle "DM'den yazın."
- 6 sahne var. İlki cover, sonuncusu cta.
- `ust` uzunlukları: 21, 13, 15, 7, 21, 22 (hepsi 25 veya altı).
- `metin` uzunlukları: 47, 49, 51, 41, 46, 47 (hepsi 60 veya altı).

## Özet
Tek engelleyici sorun 5. sahnenin `ust` alanı ("Teslimden sonra 7 gün"). Bu ifade H-08'i iç gümrük şartından bağımsız gösteriyor ve emanet teslimine bağlıyor.

KARAR: RED
