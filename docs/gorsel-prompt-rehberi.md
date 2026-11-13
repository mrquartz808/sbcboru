# SBC Boru — Görsel Retouch Rehberi ve GPT Promptları

Hedef: sitedeki tüm fotoğrafları, attığınız **Sacem** referanslarındaki gibi "AI olduğu hiç belli olmayan", gerçek fotoğraf hissine getirmek.
Promptlar **İngilizce** (görsel modeller ayrıntıyı İngilizcede daha tutarlı uyguluyor), açıklamalar Türkçe. Her kod bloğu tek başına kopyalanıp yapıştırılabilir.

> **Orijinal dosyaları kullanın, sitedeki küçültülmüş kopyaları değil.**
> Kaynak: `https://api.sbcboru.com/public/uploads/images/<orijinal-ad>` — her kartta orijinal ad yazıyor.
> Üç havadan/tesis fotoğrafı 2812×2031 px, ürün fotoğrafları 1000×1000 px, iki görsel (bina, tabela) sadece 450×450 px.

---

## 0. Nasıl kullanılır (kısa)

1. Aşağıdaki **indirme listesinden** orijinal fotoğrafı indirin (sitedeki kopyalar küçültüldü).
2. ChatGPT'de **her fotoğraf için yeni bir sohbet** açın. Sadece o fotoğrafı yükleyin (tabelalı olanlarda `logo.png`'yi de).
3. O fotoğrafın bölümündeki **Aşama A** promptunu yapıştırın. Sonucu kontrol listesiyle denetleyin.
4. İyiyse A'nın **çıktısını** yeni mesajda yükleyip **Aşama B**'yi yapıştırın.
5. Bitenleri aynı dosya adıyla `assets/img/` klasörüne koyun.
6. Tüm görselleri veya bu dosyayı **tek seferde** yüklemeyin; model ayrıntıyı karıştırır.

### Orijinal dosya indirme listesi
Adres: `https://api.sbcboru.com/public/uploads/images/` + dosya adı

| Dosya (site adı) | Orijinal |
|---|---|
| hero-tesis | [4117101053.jpg](https://api.sbcboru.com/public/uploads/images/4117101053.jpg) |
| alt-yapi | [47152260.jpg](https://api.sbcboru.com/public/uploads/images/47152260.jpg) |
| hdpe-rulo | [02276461.jpg](https://api.sbcboru.com/public/uploads/images/02276461.jpg) |
| bina | [11537753.jpg](https://api.sbcboru.com/public/uploads/images/11537753.jpg) |
| tabela | [101713124.jpg](https://api.sbcboru.com/public/uploads/images/101713124.jpg) |
| pprc | [67445256.jpg](https://api.sbcboru.com/public/uploads/images/67445256.jpg) |
| ust-yapi | [021102135.jpg](https://api.sbcboru.com/public/uploads/images/021102135.jpg) |
| pvc | [45661375.jpg](https://api.sbcboru.com/public/uploads/images/45661375.jpg) |
| temiz-su | [351016430.jpg](https://api.sbcboru.com/public/uploads/images/351016430.jpg) |
| sessiz-boru | [201061575.jpg](https://api.sbcboru.com/public/uploads/images/201061575.jpg) |
| suzgec | [5210166104.jpg](https://api.sbcboru.com/public/uploads/images/5210166104.jpg) |
| ortu | [52143441.jpg](https://api.sbcboru.com/public/uploads/images/52143441.jpg) |
| emici-verici | [32241505.jpg](https://api.sbcboru.com/public/uploads/images/32241505.jpg) |
| galvaniz | [31631244.jpg](https://api.sbcboru.com/public/uploads/images/31631244.jpg) |
| rogar | [04176115.jpg](https://api.sbcboru.com/public/uploads/images/04176115.jpg) |
| tarimsal-sulama | [07762551.jpg](https://api.sbcboru.com/public/uploads/images/07762551.jpg) |
| hdpe-boru | [56633321.jpg](https://api.sbcboru.com/public/uploads/images/56633321.jpg) |
| bahce-peyzaj | [76565362.jpg](https://api.sbcboru.com/public/uploads/images/76565362.jpg) |
| yagmurlama | [51774445.jpg](https://api.sbcboru.com/public/uploads/images/51774445.jpg) |
| TIR (yeni) | sizdeki `FullSizeRender.jpeg` |

---

## 1. Referans görsellerin "stil DNA'sı" (hedefimiz)

Sacem görsellerinin inandırıcı olmasının nedenleri; promptlarda bunları tarif ediyoruz:

| Unsur | Referanstaki karşılığı |
|---|---|
| Kamera | Yere yakın, hafif geniş açı (~24 mm), üç-çeyrek ön görünüş; çizgiler doğal yakınsıyor, drone "kuşbakışı" yok |
| Gökyüzü | Üstte doygun ama doğal mavi, ufka doğru açılan ton; **farklı boyutlarda** bulutlar, ufka yaklaştıkça küçülen ve yassılaşan kümülüs, üstte ince sirrus telleri; bulutlar ortalanmamış, boşluk bırakılmış |
| Işık | Tek güneş, alçak ve sıcak (gün batımına 1,5–2 saat), yumuşak uzun gölgeler, kenarlarda sıcak kontur ışığı, gölge tarafı hafif soğuk mavi |
| Zemin | Koyu, ince taneli asfalt; boyalı park çizgileri; leke, su birikintisi, çatlak yok |
| Çevre | Sade bakımlı peyzaj (zeytin, çalı), uzak ufuk çizgisi; elektrik direği, çöp, tabela kirliliği yok |
| Marka | Tabela net, düz, temiz; yazı keskin |

## 2. En önemli yöntem notları (GPT ile çalışırken)

1. **Önce AI dışı düzeltme.** Lightroom/Photoshop/Snapseed ile ufku düzeltin, lens bozulmasını ve pusu (dehaze) giderin. AI'a ne kadar az iş kalırsa o kadar az "AI görünümü" olur.
2. **Tek mesajda en fazla 3–4 değişiklik.** Hepsini tek prompta yığarsak model tüm kareyi yeniden çizer ve boruları bozar. Bu yüzden dış mekân görsellerinde **Aşama A (temizlik/hizalama)** ve **Aşama B (gökyüzü + ışık)** ayrı promptlar.
3. **Her seferinde orijinal fotoğrafı yükleyin** ve "bu fotoğrafı düzenle, yeniden üretme" deyin. Mümkünse ChatGPT'nin **alan seçme (brush/select)** aracıyla sadece değişecek bölgeyi seçin (gökyüzü, zemin vb.). Borular seçime girmesin.
4. **Boruların şekli, rengi ve çizgileri kutsaldır.** Her promptta "KORU" cümlesi var. Üretimden sonra mutlaka 100% büyütüp orijinalle yan yana kontrol edin (aşağıdaki kontrol listesi).
5. **En güvenli yöntem (borular bozulursa):** GPT'ye sadece **gökyüzü plakası** ürettirin (Bölüm 3), Photoshop'ta gökyüzünü maske ile değiştirin; boruların olduğu katman **orijinal piksel** kalır. Işık/renk ayarını Camera Raw ile siz yapın. Bu, "AI belli olmaz + boru bozulmaz" için en sağlam yoldur.
6. **Yazı/logo:** Görsel modeller yazıyı bozar. Tabelalar için logo dosyasını (`assets/img/logo.png`, beyaz sürüm `logo-beyaz.png`) ikinci görsel olarak ekleyin; yine de bozulursa tabelayı Photoshop'ta logo dosyasıyla elle yerleştirin.
7. **Çıktı boyutu:** GPT ~1536×1024 verir. Sonra Topaz Gigapixel / Photoshop Super Resolution / Magnific ile 2× büyütün; **ince detayı (boru çizgileri, yazılar) orijinalden maske ile geri karıştırın.**
8. **Görsellerin içine gömülü SBC logosunu (sağ üst köşe yazısı) kaldırıyoruz.** Logo siteye CSS ile ayrı katman olarak eklenir; gömülü logo hem tekrar hem de bulanık görünüyor.
9. Çıktıları **orijinal dosya adıyla** `assets/img/` klasörüne koyun (aşağıda sitedeki ad yazıyor); site otomatik alır.

### Üretim sonrası kontrol listesi (her görsel için)
- [ ] Boru **renkleri** orijinalle aynı mı? (açık mavi PE, siyah HDPE, gri PVC, yeşil çemberler)
- [ ] **Mavi/koyu mavi çizgiler**: sayı, kalınlık, renk ve konum aynı mı?
- [ ] Boru **çapı/oranı** ve sargı sayısı değişmedi mi? Yeni yazı/numara/marka eklenmedi mi?
- [ ] Tabela: harfler net ve doğru mu? (`SBC BORU`)
- [ ] Gölgeler **tek yöne** mi gidiyor? Gökyüzündeki güneş yönüyle uyumlu mu?
- [ ] Bulutlar: tekrar eden desen, ortada toplanma, aşırı büyüklük, "pamuk" görünüm yok mu?
- [ ] %100 büyütmede doku: plastik gibi aşırı pürüzsüz yüzey, parlama/glow, HDR haleleri yok mu?
- [ ] Tüm sitede **aynı gün/ışık** hissi var mı? (Hepsi sıcak, alçak güneş; kontrast benzer)

---

## 3. Ortak bloklar (promptlara gömülü; ihtiyaç olursa tek başına kullanın)

**Gökyüzü plakası (Photoshop'ta değiştirmek için — en güvenli yol).** 3 farklı plaka üretin, tüm dış mekân görsellerinde aynı seti kullanın:
```
A photorealistic sky-only plate, 3:2 landscape, no ground, no buildings, no objects, horizon at the very bottom edge. Eastern Mediterranean, late spring, about 90 minutes before sunset, sun low on the RIGHT just outside the frame. Deep natural blue at the top fading to a paler warm blue near the horizon with faint atmospheric haze. A realistic mix of cloud types: a few medium cumulus with flat bases and softly detailed edges lit warm on the sun side, scattered small flat cumulus near the horizon that shrink in correct perspective, and thin high cirrus streaks. Uneven spacing, NOT centered, generous empty blue space. No cartoon fluffy shapes, no repeating clouds, no HDR halos, no oversaturation, no sun disk, no lens flare. Natural sensor grain, shot on a full-frame camera with a 35mm lens.
```

**KORU cümlesi (her promptta var):**
`Edit this exact photo; do not regenerate or restyle it. Do NOT redraw, reshape, resize, recolor or re-count any pipe, coil, fitting, strap, sign or building. Preserve exact pipe colors and every stripe (count, thickness, color). Add no new text, markings, logos or objects.`

**DOĞAL cümlesi:**
`The result must read as an unretouched real photograph: natural sensor grain, slightly imperfect micro-contrast, no HDR halos, no oversaturation, no glow, no plastic or over-smooth surfaces, no repeating textures, not painterly or illustrated.`

---

## 4. Yerleşim haritası — nereye hangi görsel gelmeli

Site görsel ihtiyaçları ve mevcut fotoğrafların durumu. **Durum:** ✅ iyi (hafif retouch) · 🟡 orta (ciddi retouch) · 🔴 yetersiz (yeniden çekim/yerine başka görsel).

| Alan (sitedeki yer) | Önerilen görsel | Dosya (site / orijinal) | Durum |
|---|---|---|---|
| **Ana sayfa hero** 16:9, ≥2400×1350 | Tesis havadan + tabela | `hero-tesis.jpg` / `4117101053.jpg` | 🟡 |
| Hakkımızda kolajı (büyük) | Mavi PE rulolar + tabela | `alt-yapi.jpg` / `47152260.jpg` | 🟡 |
| Hakkımızda kolajı (küçük 1) | Genel merkez binası | `bina.jpg` / `11537753.jpg` | 🔴 450 px |
| Hakkımızda kolajı (küçük 2) | Gri PVC boru istifi | `pvc.jpg` / `45661375.jpg` | ✅ |
| Üretim tesisi bandı | Lazer markalı HDPE boru | `hdpe-boru.jpg` / `56633321.jpg` | ✅ |
| Galeri (8 kare) | hero, siyah rulolar, mavi rulolar, bina, tabela, damla sulama, bahçe, PVC | yukarıdakiler + `hdpe-rulo.jpg`, `tabela.jpg` | karışık |
| Sayfa başlık bantları (1440×400) | hero / mavi rulolar / siyah rulolar kırpımları | 3 büyük havadan/tesis görseli | 🟡 |
| **PPRC GRUBU** | PPRC fitting + kaynak makinesi | `pprc.jpg` / `67445256.jpg` | ✅ |
| **ÜST YAPI** | Gri atık su fittingleri (render) | `ust-yapi.jpg` / `021102135.jpg` | 🔴 CGI + üçüncü parti marka kabartması |
| **BAHÇE PEYZAJ** (1) | Pop-up sprinkler | `bahce-peyzaj.jpg` / `76565362.jpg` | ✅ |
| **PVC GRUBU** | Gri PVC boru istifi | `pvc.jpg` / `45661375.jpg` | ✅ |
| **TEMİZ SU BORU VE PARÇALARI** | Gri/beyaz U-PVC fittingler | `temiz-su.jpg` / `351016430.jpg` | ✅ |
| **SÜZGEÇLER** | Duş giderleri (render) | `suzgec.jpg` / `5210166104.jpg` | 🔴 CGI görünüm |
| **ÖRTÜLER** | Üç ayrı kare olarak bölünecek kolaj | `ortu.jpg` / `52143441.jpg` | 🟡 stok kolaj |
| **EMİCİ VE VERİCİ** | Spiral hortumlar | `emici-verici.jpg` / `32241505.jpg` | 🟡 |
| **GALVANİZ GRUBU** | Pirinç vana/fitting + İngiliz anahtarı | `galvaniz.jpg` / `31631244.jpg` | 🟡 pirinç ≠ galvaniz |
| **BAHÇE PEYZAJ** (2) / tarla yağmurlama | Tarla sprinklerleri | `yagmurlama.jpg` / `51774445.jpg` | 🟡 |
| **TARIMSAL SULAMA** | Damla hattı + fide | `tarimsal-sulama.jpg` / `07762551.jpg` | ✅ |
| **ALT YAPI** | Mavi PE rulolar | `alt-yapi.jpg` / `47152260.jpg` | 🟡 |
| **RÖGAR KAPAK GRUBU** | Rögar kapakları (pastel arka plan kolajı) | `rogar.jpg` / `04176115.jpg` | 🔴 kolaj |
| **SESİZ BORU GRUBU** | Bebek + mavi borular (sosyal medya postu) | `sessiz-boru.jpg` / `201061575.jpg` | 🔴 kullanılamaz |
| Hizmetler → Lojistik ve Dağıtım, galeri | SBC BORU TIR'ı | `FullSizeRender.jpeg` (5.20) | 🟡 ağır filtre |
| Siyah HDPE (İK, hizmetler, galeri) | Siyah rulolar | `hdpe-rulo.jpg` / `02276461.jpg` | 🟡 aşırı HDR |
| Yönetim kurulu / ekip / sertifika / logolar / blog görselleri | — | **hiç yok** | 🔴 gerçek çekim şart |

> Sitede şu an `ortu`, `ust-yapi`, `suzgec`, `rogar`, `sessiz-boru` kartları geçici olarak bu görselleri kullanıyor; aşağıdaki promptlarla iyileştirilemeyenleri yeniden çekimle değiştirin.

---

## 5. Görsel görsel promptlar

### 5.1 `hero-tesis.jpg` — Ana sayfa hero (en önemli görsel) · orijinal `4117101053.jpg` 2812×2031

**Tespit:** Gökyüzü soluk, düz ve pus içinde (en büyük "ucuz" sinyal). Işık sert ve düz; gölgeler çok koyu. Önde kahverengi saç çatı kenarları ve üstündeki rulolar kadrajı bozuyor. Yer yer dağınık borular, paletler, naylon örtüler, asfalt lekeleri. Sağda toz toprak arsa ve çit boyunca yabani otlar. Ufukta elektrik direkleri. Tabela hafif eğik, yazı yumuşak. Kadraj 4:3'e yakın; hero için 16:9 gerekli.

**Aşama A — temizlik ve hizalama** (görseli + `logo.png`'yi yükleyin)
```
Edit this exact aerial photo of a pipe factory yard; do not regenerate the scene. Keep the buildings, the SBC BORU sign, the camera viewpoint and every pipe stack exactly as they are: cyan-blue and light-grey PVC pipes, black HDPE coils, white bagged fittings. Preserve exact pipe colors and every stripe; add no new text, markings or objects. Changes only:
1) Level the horizon and correct slight lens/perspective distortion; the sign pole must be perfectly vertical and the sign board a clean rectangle.
2) Tidy the yard: loose pipes lying at random angles become straight parallel stacks aligned with the neighbouring stacks (same pipe type, same colors, same diameter); remove stray pallets, loose plastic sheeting and debris on the ground.
3) Ground: clean dark fine-grain asphalt, remove oil stains, tire marks, patches and cracks; keep a natural subtle texture.
4) Remove the electricity pylons and thin wires on the horizon and the weeds growing along the fence on the right.
5) Sign: white face evenly lit, no dirt, no glare; the logo (blue ring-and-swoosh, white "SBC BORU" lettering on the blue band) must be crisp and exact. Use the attached logo image only as a reference for the shapes and letters; do not reinterpret them.
The result must read as an unretouched real photograph: natural sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces. Do not touch the sky in this step.
```

**Aşama B — gökyüzü ve ışık** (A'nın çıktısını yükleyin)
```
Edit this exact photo; do not change any object, pipe, building or sign. Only change the sky and the lighting.
Replace the pale hazy sky with a real-photograph Eastern Mediterranean sky, late spring, about 90 minutes before sunset: deep natural blue at the top fading to a paler warm blue near the horizon with light atmospheric haze; a realistic mix of a few medium cumulus with flat bases and softly detailed edges, small flat cumulus near the horizon that shrink in correct perspective, and thin high cirrus streaks; uneven spacing, not centered, generous empty blue space on the left half (headline text will sit there).
Lighting: a single warm low sun at about 5200K. Keep the EXISTING shadow directions on the ground and roofs; only make them slightly longer and softer, add a gentle warm rim light on roof edges and pipe stacks, give the shadow side a cool blue fill, and lower the harsh overexposure of the pale roofs. No visible sun disk, no lens flare.
The result must read as an unretouched real photograph: natural sensor grain, no HDR halos, no oversaturation, no glow.
```

**Aşama C — kadraj:** 16:9 kırpın (tabela x≈%65'te, sol %40 sakin kalsın), sonra 2× büyütün (≥2400×1350). Gerekirse üstten gökyüzü uzatın:
```
Extend the canvas upward to reach a 16:9 aspect ratio by continuing the existing sky naturally (same cloud scale, same color gradient). Do not alter anything else.
```

---

### 5.2 `alt-yapi.jpg` — Mavi PE rulolar · orijinal `47152260.jpg` 2812×2031
**Slot:** ALT YAPI kartı, Hakkımızda büyük kolaj, galeri, sayfa başlık bandı.

**Tespit:** Geniş açı bozulması ön planda rulolarda esniyor. Gökyüzü soluk, sol üst köşede aşırı pozlanmış. Soldaki üçüncü parti yeşil tabela ("BİREN"), elektrik direği ve kablolar, kamyon kabini, sağdaki kahverengi konteyner, dağınık çevre. Rulolar güzel; çemberler (yeşil bantlar) farklı açılarda.

**Aşama A**
```
Edit this exact photo of blue polyethylene pipe coils; do not regenerate the scene. Do NOT redraw, reshape, resize or recolor any coil; keep the solid cyan-blue pipe color, the green strapping bands and the sign as they are. Add no new text, markings or objects. Changes only:
1) Reduce the wide-angle stretching on the foreground coils slightly (natural 24mm look, not fisheye); keep the horizon level.
2) Remove: the green third-party roadside sign at the far left edge, the utility pole and overhead wires, the truck cab on the left, the brown shipping container on the right, and the random debris on the ground in the background. Replace with flat dry scrubland and clear horizon, consistent in perspective.
3) Make the coil strapping bands neat: one band per section, same green, evenly distributed; leave coil count and arrangement unchanged.
4) The SBC BORU sign: straighten, evenly lit white face, crisp logo exactly as in the original (use the attached logo as reference only for letter shapes).
Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```
**Aşama B**
```
Edit this exact photo; change only the sky and lighting, never the objects. Replace the sky with a real Eastern Mediterranean late-spring sky about 90 minutes before sunset: deep natural blue overhead fading to paler warm blue at the horizon; a few medium cumulus with flat bases lit warm on the sun side, small flat cumulus that shrink toward the horizon, thin high cirrus; uneven spacing, not centered. Light: single warm low sun from the right, keep the existing shadow direction, soft warm highlights on the coils, cool blue fill in shadows, reduce the burnt-out upper left corner. Keep the coil blue exactly the same hue (cyan-blue, not purple). No sun disk, no lens flare, no HDR halo.
```

---

### 5.3 `hdpe-rulo.jpg` — Siyah HDPE rulolar · orijinal `02276461.jpg` 2812×2031
**Slot:** Galeri, İK/hizmet kapakları, sayfa başlığı kırpımı (üretim bandı için alternatif).

**Tespit:** Gökyüzü aşırı HDR/turuncu, "yapay" en belli olan kare. Rulolar dağınık, uçlar rastgele; üstte tek bir boru parçası rulonun üzerinde. Solda yarı görünen kamyon (SBC BORU yazılı) kadrajı bozuyor. Zeminde baskılı kahverengi plaka. Işık sert ve kontrastlı.

**Aşama A**
```
Edit this exact photo of black HDPE pipe coils with thin cyan-blue longitudinal stripes; do not regenerate the scene. This is critical: do NOT redraw, reshape, resize or recolor any coil. Keep every thin cyan-blue stripe exactly (count, thickness, color, position along the pipe), keep the black pipe color and the green/blue strapping bands. Add no text or markings on the pipes. Changes only:
1) Remove the white truck cab cut off at the left edge and the cluttered storage behind it; replace with a clean open yard and low horizon consistent with the right side.
2) Remove the loose single pipe lying across the top of the right foreground coil and the loose pipe ends sticking out; keep coils otherwise unchanged.
3) Neaten the strapping bands: each coil gets evenly spaced bands of the same color (green), straight and tight.
4) Ground: replace the printed brown board with clean, uniform light-grey concrete with subtle realistic texture; keep the same perspective and shadows.
5) Sign in the background: keep crisp and straight with the logo exactly as in the original.
Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```
**Aşama B**
```
Edit this exact photo; change only the sky, the color grading and lighting, never the objects. Remove the heavy HDR look and the orange cloud layer. Replace the sky with a real Eastern Mediterranean late-spring afternoon sky: deep natural blue, a few medium cumulus with flat bases, small flat cumulus near the horizon, thin cirrus; uneven spacing. Light: one warm low sun from the right, keep existing shadow direction; neutral-warm grade (no orange cast), moderate contrast, lifted deep blacks so the black pipe still shows its glossy highlights and texture; keep the cyan-blue pipe stripes exactly the same hue and thickness. No glow, no halo, no lens flare.
```

---

### 5.4 `bina.jpg` — Genel merkez binası · orijinal `11537753.jpg` **450×450 (çok düşük)**
**Slot:** Hakkımızda kolajı, galeri.

**Tespit:** Çözünürlük yetersiz; büyük yerde kullanılamaz. Asfalt çatlak/lekeli, arka plan şehir silueti dağınık, gökyüzü yok. Cephe (mavi panel, "SBC BORU") güzel ve temiz.
**Öncelik:** Bu bina için **yeni çekim / daha yüksek çözünürlüklü drone karesi** isteyin (Bölüm 6). Çözünürlük yükseltilemezse:
```
Edit this exact low-resolution aerial photo of a white building with a blue "SBC BORU" facade; do not change the building design, the facade lettering, the logo or the camera angle. Upscale and rebuild fine detail faithfully (window frames, balcony rail, roof seams, planters). Clean the asphalt: remove cracks, stains and patches, make it uniform dark fine-grain asphalt. Reduce the busy background: soften the distant city so it reads as a low, hazy skyline. Keep the facade logo exactly: grey-blue ring with blue swoosh and white "SBC BORU" lettering on the blue panel, perfectly crisp and straight. Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation. Output at the highest resolution available.
```
**Opsiyonel (Sacem tarzı yeni hero, deneysel):** Bu görsel + yeni çekilmiş zemin seviyesi bir bina fotoğrafı yükleyip şu promptu kullanın. Sadece **gerçek referans fotoğraf yüklenirse** güvenilir sonuç verir; bina tasarımını uydurmasına izin vermeyin:
```
Using the attached photos of the real building as the single source of truth, create one photorealistic ground-level three-quarter view of the SBC BORU headquarters: camera at eye level, 24mm lens, slightly low, building facade and blue SBC BORU panel exactly as in the references (same proportions, windows, diagonal white wing, planters). Late-afternoon golden-hour sun from the right, deep natural blue sky with a few uneven cumulus and thin cirrus, clean dark asphalt with painted parking lines, a few olive trees and low shrubs, two white delivery vehicles in the distance. No people, no clutter. Do not invent new architecture. Natural sensor grain, no HDR halos, no oversaturation, 3:2, highest resolution.
```

---

### 5.5 `tabela.jpg` — Direk tabela ve boru istifi · orijinal `101713124.jpg` **450×450**
**Slot:** Galeri (düşük öncelik; yeni drone fotoğrafları varken gerek yok).

**Tespit:** Gökyüzü düz, aşırı doygun koyu mavi (en "ucuz" görünen sky). Çözünürlük çok düşük. Tabela doğru ama yazı bulanık.
```
Edit this exact low-resolution photo; do not regenerate. Keep the sign, the grey pipe stacks on pallets, the yellow and black pipes and the camera angle unchanged; do not alter pipe colors or stripes. Replace the flat, oversaturated deep-blue sky with a realistic Eastern Mediterranean sky: softer blue gradient, a few uneven cumulus and thin cirrus, no sun disk. Upscale and rebuild fine detail; make the sign crisp: white board, blue lower band, white "SBC BORU" lettering and the ring-and-swoosh logo exactly as in the original (attached logo is a reference for shapes). Straighten the pole vertical. Natural sensor grain, no HDR halos, no oversaturation.
```

---

### 5.6 `pprc.jpg` — PPRC fitting ve kaynak makinesi · orijinal `67445256.jpg` 1000×1000
**Slot:** PPRC GRUBU kartı (4:3).
**Tespit:** İyi kompozisyon. Sorunlar: sağ üstte gömülü SBC logosu, OSB tahta arka plan gürültülü, ışık düz, fittinglerde yumuşak odak.
```
Edit this exact product photo of grey-beige PPR pipes, fittings and a socket-welding machine on a wooden board; do not regenerate or restyle. Do NOT change the shape, size, count or color of any pipe or fitting (keep their exact beige-grey color and matte finish) or the welding machine. Add no new text, markings or objects. Changes only:
1) Remove the SBC BORU logo overlay in the top-right corner and fill with the matching wooden surface.
2) Calm the background: slightly reduce the busy OSB texture contrast and add a natural shallow depth of field so the fittings stand out.
3) Relight as a soft studio light from the upper left (large softbox look): gentle highlights on the fittings, soft natural contact shadows beneath each object, clean specular on the metal parts of the welder; keep colors neutral-warm.
4) Extend the canvas to 4:3 landscape (add wood surface on the right/top) so the group sits slightly right of center.
Natural unretouched photograph look: fine sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```

---

### 5.7 `pvc.jpg` — Gri PVC boru istifi · orijinal `45661375.jpg` 1000×1000
**Slot:** PVC GRUBU kartı, Hakkımızda kolajı.
**Tespit:** Çok iyi içerik (contalı soketli gri borular, ince koyu mavi çizgi, beyaz sargı bantları). Sorunlar: gömülü logo, kapalı gri gökyüzü, üst sıralar eğik ve dağınık, alttaki borular kadraj dışı, çekim açısı hafif yamuk.
```
Edit this exact photo of grey PVC sewer pipes with rubber-ring sockets, stacked in racks; do not regenerate. Do NOT redraw, reshape, resize, recolor or re-count any pipe. Preserve the exact grey color, the thin dark-blue stripe on the pipes, the white strapping bands and the black rubber sealing rings. Add no text or markings. Changes only:
1) Remove the SBC BORU logo overlay in the top-right corner.
2) Level the horizontal lines (correct the slight roll/perspective): the stacked rows in the background should be horizontal and straight; all socket ends in the front rows face the same direction and sit in even rows.
3) Replace the grey overcast sky with a real Eastern Mediterranean sky: soft deep-blue gradient with a few uneven small cumulus and thin cirrus, no sun disk.
4) Light: warm, low sun from the right, soft highlights along the pipe tops and on the white socket rims, cool fill in the pipe interiors; reduce flat greyness, add gentle contrast.
5) Remove stray tape ends and small debris at the bottom.
Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```

---

### 5.8 `temiz-su.jpg` — U-PVC fittingler (koyu gri/beyaz) · orijinal `351016430.jpg` 1000×1000
**Slot:** TEMİZ SU BORU VE PARÇALARI kartı.
**Tespit:** Çok iyi; ıslak beton ve su damlaları gerçekçi. Gömülü logo ve sağ kenarda kesilen parçalar dışında düzeltme az.
```
Edit this exact product photo of dark-grey and white U-PVC pressure fittings on wet concrete with water droplets; do not regenerate. Do NOT change the shape, size, count or color of any fitting (keep the dark slate-grey and white, matte finish), the threads or the union nut. Add no text or markings. Changes only:
1) Remove the SBC BORU logo overlay in the top-right corner and rebuild the fitting behind it naturally.
2) Even out the concrete: reduce blotchy stains and dirt, keep a realistic fine concrete grain and the water puddle/droplets.
3) Light: soft studio softbox from upper left, gentle highlights on the wet plastic, soft contact shadows; slightly cooler neutral color.
4) Extend the canvas to 4:3 landscape if needed so nothing important is cut off by the frame edge.
Natural unretouched photograph look: sensor grain, no HDR halos, no plastic over-smooth surfaces.
```

---

### 5.9 `emici-verici.jpg` — Spiral hortumlar · orijinal `32241505.jpg` 1000×1000
**Slot:** EMİCİ VE VERİCİ kartı.
**Tespit:** Aşırı doygun yeşil/sarı, renk bantlaşması ve keskinleştirme izi. Gömülü logo. Yapraklar dağınık ve kirli.
```
Edit this exact photo of three spiral suction hoses (clear PVC with a yellow helix, clear with a green helix, clear with a black helix) lying on grass with autumn leaves; do not regenerate. Do NOT change the shape, spiral pitch, diameter or colors of the hoses; keep the yellow, green and black helix colors true. Add no text or markings. Changes only:
1) Remove the SBC BORU logo overlay at the top-right.
2) Reduce the over-saturation, colour banding and oversharpening halos; natural, true-to-life colors.
3) Tidy the leaves: keep a few natural leaves but remove clutter around the hoses; keep the grass natural.
4) Light: soft overcast-to-warm daylight from the upper left, realistic transparent plastic reflections and soft shadows on the grass.
5) Extend the canvas to 4:3 landscape.
Natural unretouched photograph look: sensor grain, no HDR halos, no plastic over-smooth surfaces.
```

---

### 5.10 `galvaniz.jpg` — Pirinç fitting/vana ve İngiliz anahtarı · orijinal `31631244.jpg` 1000×1000
**Slot:** GALVANİZ GRUBU kartı. ⚠️ Görseldeki ürünler **pirinç (sarı metal)**; galvaniz çinko kaplı gri parlak metaldir. Gerçek galvaniz ürün fotoğrafı daha doğru olur; bu görsel geçici.
```
Edit this exact photo of brass plumbing fittings, ball valves and a red pipe wrench on dark wood; do not regenerate. Do NOT change the shape, size, count or color of the fittings, valves, wrench or handle. Add no text or markings (keep existing stamped markings on the metal unchanged). Changes only:
1) Remove the SBC BORU logo overlay at the top-right and rebuild the wood grain behind it.
2) Light: soft warm key from the upper left, clean realistic metal reflections on the brass, soft contact shadows; reduce the noisy over-sharpened wood texture slightly.
3) Extend the canvas to 4:3 landscape.
Natural unretouched photograph look: sensor grain, no HDR halos, no plastic over-smooth surfaces.
```

---

### 5.11 `tarimsal-sulama.jpg` — Damla sulama hattı ve fide · orijinal `07762551.jpg` 1000×1000
**Slot:** TARIMSAL SULAMA kartı. **Tespit:** Çok iyi, logosuz; sadece çözünürlük ve ışık.
```
Edit this exact macro photo of a black drip-irrigation line above a young eggplant seedling with water drops; do not regenerate. Keep the plant, the soil, the black drip line, the dripping water and the puddle exactly. Add no text or markings. Changes only: gentle warm late-afternoon light with natural soft shadows, a little more micro-contrast on the soil, keep shallow depth of field, then extend to 4:3 landscape by continuing soil and leaves naturally. Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```

---

### 5.12 `bahce-peyzaj.jpg` — Pop-up sprinkler · orijinal `76565362.jpg` 1000×1000
**Slot:** BAHÇE PEYZAJ (1). **Tespit:** İyi, logosuz; hafif yumuşak. 
```
Edit this exact photo of a pop-up garden sprinkler spraying water over a lawn; do not regenerate. Keep the nozzle, the black body, the water spray pattern and the lawn exactly. Changes only: warm low sunlight from the right with a subtle backlit sparkle on the water droplets, natural lawn color (not neon green), gentle sharpening and detail recovery, then extend to 4:3 landscape continuing the lawn and the blurred green background. Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```

---

### 5.13 `yagmurlama.jpg` — Tarla sprinklerleri · orijinal `51774445.jpg` 1000×1000
**Slot:** BAHÇE PEYZAJ (2) ya da TARIMSAL SULAMA alternatifi. **Tespit:** Pus/sis, üstte elektrik direkleri ve kablolar, soluk gökyüzü, gömülü logo.
```
Edit this exact photo of impact sprinklers watering a green barley field; do not regenerate. Keep the sprinklers (red heads, white risers), the water jets and the field exactly. Do not redraw the heads. Add no text or markings. Changes only:
1) Remove the SBC BORU logo overlay at the top-right.
2) Remove the electricity pylons, poles and overhead wires; keep the distant hill and a clean horizon.
3) Dehaze: replace the milky white sky with a real Eastern Mediterranean late-spring sky, soft blue, a few uneven cumulus; keep a natural light mist over the hill.
4) Light: warm low backlight from the upper right; water jets get natural glints; field colors natural, not neon.
5) Extend the canvas to 4:3 landscape.
Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation.
```

---

### 5.14 `hdpe-boru.jpg` — Lazer markalı HDPE boru (üretim hattı) · orijinal `56633321.jpg` 1000×1000
**Slot:** Üretim tesisi bandı, hizmetlerde "Yerinde Üretim". Gerçek üretim kanıtı olduğu için çok değerli: borunun üstünde **lazerle basılmış yazı** ("…FAMAGUSTA/CYPRUS TEL +90 533 8…") var, **olduğu gibi kalmalı**.
```
Edit this exact photo of a black HDPE pipe with a cyan-blue stripe being laser-marked in a production line; do not regenerate. Do NOT alter the pipe shape, the blue stripe, the laser-engraved text on the pipe (keep every character exactly as is), the red laser dot or the machine parts. Add no new text. Changes only:
1) Remove the SBC BORU logo overlay at the top-right and rebuild the soft white background behind it.
2) The background is blown out: recover subtle detail and a slightly cooler neutral grey-white so the machinery reads as a real factory environment (soft out-of-focus rollers, steel frame), keep shallow depth of field.
3) Light: soft cool factory daylight from the left, gentle specular highlight along the pipe, deep clean blacks without crushed detail.
4) Extend the canvas to 4:3 landscape.
Natural unretouched photograph look: sensor grain, no HDR halos, no plastic over-smooth surfaces.
```

---

### 5.15 `ust-yapi.jpg` — Gri atık su fittingleri (3D render) · orijinal `021102135.jpg` 🔴
**Tespit:** Bu görsel **CGI/stok render** görünüyor ve fittinglerin üzerinde **başka bir markanın kabartma yazısı** var gibi. SBC'nin gerçek ürünü olmayabilir; başka marka yazısıyla yayınlanmamalı. Bu kartı **kendi ürün fotoğrafınızla** değiştirmenizi öneririm (Bölüm 6). Yine de geçici kullanım için:
```
Edit this exact render-like image of grey drainage pipe fittings; do not regenerate. Do NOT change the shapes, proportions, count or colors of the fittings (keep the grey bodies, the pale-blue inner lining and the raised moulding ribs). Changes only:
1) Remove every embossed or printed lettering and numbers on the fittings (they belong to another brand); leave the surface smooth with natural subtle mould texture.
2) Make it look like a real studio photograph instead of CGI: realistic matte PVC microtexture, subtle surface imperfections, soft contact shadows on a neutral mid-grey sweep, a very soft gradient background (no blue vignette), slight natural depth of field.
3) Soft key light from the upper left, gentle fill.
Natural sensor grain, no HDR halos, no plastic over-smooth surfaces.
```

---

### 5.16 `suzgec.jpg` — Duş gideri (3D render) · orijinal `5210166104.jpg` 🔴
**Tespit:** Render görünümü, mozaikte moiré/tekrar desen, koyu ve soluk, hortum gölgesi yapay. Gömülü logo. Tavsiye: **gerçek süzgeç ürün fotoğrafı** (Bölüm 6).
```
Edit this exact render-like photo of a stainless steel shower floor drain on a dark mosaic tile floor; do not regenerate. Keep the drain grate design, its slot pattern, its square shape and the tile layout. Changes only:
1) Remove the SBC BORU logo overlay at the top-right.
2) Make it photorealistic: realistic brushed-stainless reflections, natural water droplets, remove the moiré/regular repeating tile pattern (add slight tile irregularity, grout variation and natural wear), remove the artificial hose-shaped shadow.
3) Light: soft bright bathroom light from the upper left, clean highlights, lift the muddy dark tones, neutral cool color.
Natural sensor grain, no HDR halos, no plastic over-smooth surfaces. Output 4:3 landscape.
```

---

### 5.17 `rogar.jpg` — Rögar kapakları (pastel arka plan kolajı) · orijinal `04176115.jpg` 🔴
**Tespit:** Gradient pastel arka plan "amatör" görünüyor; ürünler farklı ışık/ölçekte kesilmiş fotoğraflar; gölge yok; logo gömülü. En iyi çözüm **her kapağı ayrı çekmek**; geçici çözüm:
```
Edit this exact product collage of manhole covers and a chamber box; do not regenerate the products. Do NOT change the shape, relief pattern, size, colors or any embossed marking (for example "40X40" and "EN124-A15") of any product. Changes only:
1) Remove the SBC BORU logo overlay at the top-right.
2) Replace the pastel green-to-blue gradient with a clean neutral light-grey studio background (very subtle radial gradient).
3) Unify the lighting: soft overhead softbox from the upper left on every product; add natural soft contact shadows under each product so they sit on the same surface; consistent scale and perspective.
4) Arrange the seven products in a tidy aligned grid with even spacing.
Natural unretouched photograph look: fine sensor grain, no plastic over-smooth surfaces, no glow.
```

---

### 5.18 `ortu.jpg` — Örtü/sera kolajı · orijinal `52143441.jpg` 🟡
**Tespit:** Üç ayrı stok fotoğrafın kolajı. Kart için **tek kare** gerekiyor; kolajı üçe bölün: mavi branda (435×460), yeşil gölgelik sera (465×460, logolu), şeffaf tünel (900×435). Her biri düşük çözünürlük.

**Gölgelik sera kırpımı (logosu çıkacak):**
```
Edit this exact photo of a strawberry field under a green shade-net tunnel; do not regenerate. Keep the tunnel structure, the net color, the plant rows and the soil exactly. Add no text. Changes only: remove the SBC BORU logo at the top-right and rebuild the net and ribs behind it; make the light look like natural diffused daylight with soft shadows; reduce the neon green cast so colors are natural; upscale and rebuild fine detail; keep the symmetrical perspective. Natural sensor grain, no HDR halos, no oversaturation. Output 4:3 landscape.
```
**Şeffaf tünel kırpımı (kart için en iyisi, 2:1 → 4:3 uzatılacak):**
```
Edit this exact photo of rows of clear plastic low tunnels (polytunnels) in a field; do not regenerate. Keep the rows, arches and film exactly. Changes only: realistic soft daylight with natural film reflections, slightly cooler neutral color, reduce the over-bright milky white, upscale and rebuild fine detail, extend the canvas to 4:3 landscape by continuing the field and the rows naturally. Natural sensor grain, no HDR halos, no plastic over-smooth look.
```
**Mavi branda kırpımı:**
```
Edit this exact photo of a blue tarpaulin covering a pile on grass; do not regenerate. Keep the shape, folds, eyelets and the royal-blue color exactly. Changes only: natural diffused daylight, true-to-life colors (not neon), keep the grass natural, upscale and rebuild fine detail, extend the canvas to 4:3 landscape. Natural sensor grain, no HDR halos, no oversaturation.
```

---

### 5.19 `sessiz-boru.jpg` — Bebek + mavi borular (sosyal medya) · orijinal `201061575.jpg` 🔴
**Tespit:** Bebek fotoğrafı + uyku emojisi + montajlanmış kolaj; kart için kullanılamaz. Bebek yarısı sosyal medya içeriği olarak değerli ama sitede ürün kartında yeri yok. Sağ yarı (450×900) tavandaki açık mavi borular, çok düşük çözünürlük, beton + kalıp demirleri.
Sağ yarıyı kırpın ve şunu deneyin; olmuyorsa gerçek **sessiz boru** fotoğrafı çekin (Bölüm 6):
```
Edit this exact portrait photo of pale-blue drainage pipes and fittings installed under a concrete ceiling; do not regenerate. Do NOT change the shape, number, size, sockets, clamps or color of any pipe (keep the exact light-blue color and smooth matte finish). Changes only:
1) Remove the emoji and the visible rebar/formwork clutter at the edges; clean the concrete ceiling so it reads as a neat, finished installation.
2) Make the pipe runs straight and parallel, level with the ceiling.
3) Light: soft even daylight from a window on the left, realistic soft shadows on the concrete.
4) Upscale and rebuild fine detail; extend to 4:3 landscape by continuing the concrete ceiling and pipe runs naturally.
Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```

---

### 5.20 SBC BORU TIR'ı (yeni) — `FullSizeRender.jpeg` ~1320×1277
**Slot:** Hizmetler → "Lojistik ve Dağıtım" kartı, galeri, Hizmetler sayfa başlığı. Çok değerli: markalı treyler gerçek ve net okunuyor.

**Tespit:** Instagram filtresi gibi aşırı HDR/clarity, turuncu-camgöbeği renk tonu, sağdan gelen yapay lens flare ışınları. Zemin çatlak, kirli, çamurlu beton. Arkada bitmemiş inşaat binası (soldaki mavi boru güzel, kalsın). Plaka okunuyor. Çekici başlığında **üçüncü taraf yazılar** var ("Bradley", "BradleyTransport.com", "TUNÇTÜRK"): bu araç taşıyıcı firmanın çekicisi. Bunları kalsın mı kalkacak mı siz karar verin; promptta ikisi de var.

**Aşama A — temizlik (görseli yükleyin)**
```
Edit this exact photo of a blue curtain-sider semi-trailer truck parked in front of an unfinished apartment building; do not regenerate. Keep the truck, the trailer livery, the camera angle and the building exactly. Do NOT redraw, reshape or re-letter anything on the trailer: the ring-and-swoosh logo, "SBC BORU", "KIBRIS" and "www.sbcboru.com" must stay exactly as they are, same size, color and position. Add no new text. Changes only:
1) Remove the Instagram-style filter look: heavy HDR/clarity, orange-teal cast, crushed blacks; restore natural, true-to-life colors (the trailer stays its deep royal blue).
2) Remove the lens flare rays and the glow across the right side.
3) Ground: replace the cracked, dirty, muddy concrete with clean, even light-grey concrete with a subtle realistic fine texture, same perspective; remove the loose debris and rubble piles at the far left and right edges.
4) Replace the license plate with a plain blank white plate.
5) Make the vertical lines of the building perfectly vertical (slight perspective correction); keep the blue pipe on the building at the left.
Natural unretouched photograph look: sensor grain, no HDR halos, no oversaturation, no plastic over-smooth surfaces.
```
**Aşama B — ışık (A'nın çıktısını yükleyin)**
```
Edit this exact photo; do not change any object, text or logo. Only the lighting and color grade. Use a single warm low sun from the right, about 90 minutes before sunset: soft warm highlights along the trailer's top edge and the cab roof, a gentle warm light on the concrete facade, a soft realistic shadow of the truck on the ground, a cool blue fill on the shadow side, natural reflections on the windshield. Moderate contrast, no orange cast, no glow, no lens flare, no HDR halo. Output 3:2 landscape by extending the ground and the building naturally on the left and right.
```
**İsteğe bağlı — çekici yazılarını nötrleştirmek isterseniz:**
```
Edit this exact photo; do not change the trailer. On the truck cab only, remove the third-party company lettering and web address ("Bradley", "BradleyTransport.com", "TUNÇTÜRK") and replace them with clean, plain surfaces matching the cab's existing white and dark-blue paint, keeping the cab's shape, reflections and the other graphics unchanged. Add no new text.
```
> Gerçek bir araçtan başka firmanın yazısını silmek yanlış bir izlenim yaratabilir; araç gerçekte o taşıyıcı firmaya aitse bu yazıları kalmış hâliyle kullanmak daha dürüst ve sorunsuzdur.

---

## 6. Elinizde "örnek yok" olanlar — **ben şöyle yapardım**

Bu ürün/alanlarda elinizdeki fotoğraf yetersiz. Boru şekli ve üzerindeki renk/çizgiler çok kritik olduğu için bunları **yapay zekâya sıfırdan ürettirmeyin**: AI çizgi sayısını, renk tonunu ve fitting ölçüsünü kolayca yanlış çizer. Önerim: telefonla (veya fotoğrafçıyla) **gerçek çekim**, sonra AI'ı sadece arka plan ve ışık için kullanmak.

| Eksik | Neden | Çekim |
|---|---|---|
| **Bina cephesi, yer seviyesi** | `bina.jpg` 450 px | Altın saat, göz hizası, 24 mm, üç-çeyrek ön görünüş (Sacem'deki gibi); 1 kare de drone 45° (nadir değil), 60–80 m |
| **Depo içi (4500 m²)** | Hiç yok | Geniş açı, raflar düz, ışıklar açık, ortada koridor |
| **Üretim hattı (ekstrüder, soğutma, lazer markalama)** | Sadece 1 kare var | Makineler çalışırken, boru çıkışı; çalışanlar izinli |
| **SBC BORU yazılı kamyon/araç sırası** | Sadece kadraj kenarında | Yarda sıralı araçlar, altın saat, yan görünüş |
| **PPRC boru + fitting (gerçek renk/çizgi)** | Sadece fitting, uzun boru yok | Açık gri fon, borular paralel, uçlar hizalı, bir boru kesiti duvar kalınlığını gösterecek şekilde |
| **Sessiz boru (gerçek ürün)** | Bebek kolajı kullanılamaz | Aynı protokol; sürgülü/contalı soket detayı yakın çekim |
| **Üst yapı fittingleri (gerçek)** | Render başka marka | Dirsek, T, manşon; üçünden fazla ölçü |
| **Galvaniz boru/vana** | Görseldeki pirinç | Çinko kaplı gri borular ve vanalar |
| **Süzgeç ve rögar kapakları (tek tek)** | Kolaj | Her ürün ayrı, nötr fon, yukarıdan 30° |
| **Örtü rulosu / sera naylonu (SBC'nin)** | Stok kolaj | Rulo ve açılmış örtü, sahada çekim |
| **Damla sulama borusu (yakın çekim, damlalıklı)** | Sadece fide fotoğrafı | Damlalık detayı + dizili hat |
| **Yönetim kurulu portreleri, ekip, fuar, İK etkinlik** | Hiç yok | **Gerçek portre çekimi.** İnsan yüzlerini AI ile üretmeyin |
| **Sertifikalar, marka ve referans logoları** | Hiç yok | Belge taraması ve vektör logolar |

**Ürün çekim protokolü (tek tip görünüm için):**
1. Açık gri/beyaz kesintisiz fon, büyük yumuşak ışık (softbox) 45° yukarıdan-soldan, ikinci yansıtıcı sağdan.
2. Borular **paralel**, uçlar **aynı hizada**, çizgiler/şeritler kameraya dönük; en az bir boru kesit ucunu göstersin.
3. Etiket/yazı yeri kameraya dönük ve net; üstüne hiçbir logo bindirmeyin.
4. Min. 4000 px uzun kenar, RAW veya yüksek kalite JPEG; ufak çizik/parmak izi temizlenmiş.
5. Sonra GPT'ye sadece: "fonu düzelt, gölgeyi temizle, ışığı dengele; ürüne dokunma" talimatı verin.

## 7. Önerilen sıra

1. **Hero** (5.1) — A → B → C. En büyük etki.
2. `alt-yapi`, `hdpe-rulo` (5.2, 5.3) — sayfa başlıkları ve galeri.
3. Logosu çıkacak ve hafif retouch isteyen ürünler: `pvc`, `pprc`, `temiz-su`, `emici-verici`, `galvaniz`, `hdpe-boru`, `tarimsal-sulama`, `bahce-peyzaj`, `yagmurlama`.
4. Kolaj/render olanlar (`ortu`, `rogar`, `suzgec`, `ust-yapi`, `sessiz-boru`): ya 5.15–5.19'u deneyin ya da yeni çekim bekleyin.
5. Yeni çekimler geldikçe Bölüm 6'daki protokolle retouch.
