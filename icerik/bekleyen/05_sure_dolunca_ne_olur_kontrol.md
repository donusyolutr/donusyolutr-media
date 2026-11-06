# Kontrol raporu — 05_sure_dolunca_ne_olur

Kontrol tarihi: 2026-11-06. Kaynaklar: `kurallar/hukuki_cerceve.md`, `kurallar/marka.md`, taslak JSON. Sayımlar python ile yapıldı.

## 1. Listede olmayan olgusal iddia — KALDI
- Seslendirmede, caption'da ve sahnelerde 1/4 ceza, el koyma, emanet teslim, il gümrük idaresi, 7 gün, sevk ve e-Devlet cümlelerinin her biri `iddialar` listesinde var.
- Ancak cümlelerin art arda dizilişi listede olmayan bir **birleşik iddia** kuruyor: "Aracı emaneten teslim edersiniz → süre durur → (teslimden sonra) 7 gün içinde çıkarırsınız". Yani "emaneten teslim = iç gümrüğe teslim" ve "emanet tesliminden sonra 7 gün içinde yurt dışı etmek gerekir" iddiası. Bu iddia `iddialar` listesinde yok, H-07 ile H-08'in hiçbiri bunu söylemiyor.
- Kapak metnindeki "Yabancı plakalı aracınız için sakin bir yol var" cümlesi her duruma çözüm olduğu izlenimi veren genel bir iddia. Listede karşılığı yok (sınırda, tek başına RED gerekçesi sayılmadı).

## 2. H-xx dayanaklarının yeterliliği — KALDI
- **H-10 bağlamı daraltılıp kesinleştirilmiş:** Kuralda yalnızca "İşlem aracın bulunduğu ildeki gümrük idaresinde yapılır" yazıyor ve hangi işlem olduğu belirtilmiyor. Kural listede H-09'dan (vekâletle sürerek çıkarma) hemen sonra geliyor. Taslak ise "**Bu** işlem" diyerek kuralı açıkça emaneten teslime bağlıyor (seslendirme: emanet cümlesinden hemen sonra; sahne 3 → sahne 4 "Nerede?"). Kuralın söylemediği bir bağlam kurulmuş.
- **H-07 ile H-08 yanlış bağlamda yan yana:** H-07 "emaneten teslim"den, H-08 "iç gümrüğe teslim"den söz ediyor. Kural ikisinin aynı işlem olduğunu söylemiyor. Sahne 3 ("süreyi durdurur") ile sahne 5 ("İç gümrüğe teslim sonrası, 7 gün içinde çıkış") art arda gelince izleyici "süre durdu" ile "7 gün içinde çıkmalıyım" arasında çelişkili ya da yanlış bir sonuç çıkarabiliyor.
- **H-06 genişletilmiş (sahne 2):** "Vergilerin 1/4'ü kadar ceza" ifadesinde kuraldaki "**gümrük** vergilerinin" ve "**idari para** cezası" sözleri düşmüş. "Vergilerin" kuraldan daha geniş okunabiliyor (bütün vergiler gibi). Seslendirme ve caption'da ifade doğru, sorun yalnızca sahne metninde.
- H-11 ve H-08'deki "çekici" ifadesi kurala uygun.

## 3. URL dayanakları — GEÇTİ
`kaynaklar` alanı boş. Rakamların (1/4 ve 7 gün) ikisi de H-06 ile H-08'de var, URL gerekmiyor.

## 4. Açık sorularda kesin hüküm — GEÇTİ (notla)
Şirket aracı ve servise bırakma konularına hiç girilmemiş. "Sevk, memur refakatinde ya da çekiciyle yapılır" cümlesi H-08'in birebir karşılığı. Yine de bu cümle sevkin yolları tam listesiymiş gibi sunuluyor ve böylece birinci açık soruya ("iç gümrüğe teslimden sonra vekil aracı sürerek çıkarabilir mi") dolaylı olarak "hayır" yanıtı veriyor. Kuraldan alıntı olduğu için KALDI sayılmadı, ama düzeltmede "bu soru henüz netleşmedi" çekincesi eklenmeli ya da bu iddia ihtiyatlı biçimde verilmeli.

## 5. Dil kuralları — KALDI
- Yasak ifade ("beyanname veririz" vb.) yok. "Planlıyoruz" ve "takip ediyoruz" ifadeleri uygun.
- Satış, devir ya da kiralama imâsı yok. Korku dili yok, ton sakin. Siz dili kullanılmış.
- Emoji: 0. WhatsApp geçmiyor.
- **CTA ihlali:** cta sahnesinde çağrı "çıkışı birlikte planlayalım". Bu, "DM'den yazın" dışında bir çağrı ve kurala göre çağrı yalnızca "DM'den yazın" olabilir. Sahnede "DM'den yazın" hiç yok.
- Caption: 3 metin paragrafı ve hashtag satırı var (2-4 aralığında). 6 hashtag var (4-8 aralığında).
- 50 yaş üstü okur için anlaşılırlık: "emaneten teslim", "iç gümrük" ve "sevk" açıklanmadan kullanılmış jargon. Bu, 1. ve 2. maddedeki karışıklığı da artırıyor (ek gözlem).

## 6. Uzunluk ve yapı — GEÇTİ
- Seslendirme 66 kelime (45-80 ve 45-90 aralıklarının ikisinde de). İlk cümle kanca ("Aracınızın süresi dolmak üzere mi?"), son cümle "DM'den yazın."
- 6 sahne var. İlki cover, sonuncusu cta.
- ust uzunlukları: 21, 13, 15, 7, 25, 22. Hepsi ≤25 ("İç gümrüğe teslim sonrası" tam 25).
- metin uzunlukları: 47, 49, 51, 41, 53, 47. Hepsi ≤60.

## Düzeltme önerileri (taslak değiştirilmedi)
1. Emaneten teslim (H-07) ile iç gümrüğe teslim ve 7 gün (H-08) arasında ilişki kurulmamalı. Ya ikisi ayrı ve bağımsız bilgiler olarak verilmeli ya da Ahmet `hukuki_cerceve.md` dosyasına bu ilişkiyi açıkça yazmalı.
2. H-10 emanet teslime bağlanmamalı ("Bu işlem" ifadesi kaldırılmalı). Hangi işlem olduğu belirsizse cümle çıkarılmalı.
3. Sahne 2 şöyle olmalı: "Gümrük vergilerinin 1/4'ü kadar idari para cezası" (60 karakter sınırı içinde kalacak biçimde).
4. cta sahnesindeki çağrı yalnızca "DM'den yazın" olmalı.

KARAR: RED
