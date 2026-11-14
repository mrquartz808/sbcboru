# SBC Boru — FigCraft Master Prompt

> Kaynak: https://www.sbcboru.com (TR sayfaları, renkler/yazı tipi/görseller/bölümler canlı siteden incelendi).
> Amaç: Mevcut sitedeki **tüm bölümler ve sayfalar birebir** korunur; üzerine kurumsal, yenilikçi, premium bir tasarım dili, yeni ikon seti ve eksik kurumsal bölümler (Yönetim Kurulu, Hizmetler, Blog) eklenir.

---

## 0. KOPYALA-YAPIŞTIR PROMPT (FigCraft'a ver)

Sen kıdemli bir kurumsal web tasarımcısısın. **FigCraft** uygulamasında (Figma değil) **SBC Boru** için eksiksiz bir kurumsal web sitesi tasarlayacaksın: her sayfa **Desktop (1440 px)** ve **Mobil (390 px)** olarak, tek dosyada, düzenli sayfa/frame isimleriyle.

SBC Boru; **Kuzey Kıbrıs'ın (KKTC) en büyük boru üreticisi ve tedarikçisi**dir. 2004'te İskele'de kuruldu, 2015'te merkezini Gazimağusa Büyük Sanayi Bölgesi'ne taşıdı. Üstyapı, altyapı tesisat boruları, tarımsal sulama ve peyzaj alanlarında 3000'in üzerinde ürün çeşidi ile yapı marketlere, hırdavatçılara ve inşaat şirketlerine tedarik yapar; kendi üretim tesisinde PVC atık su, HDPE-LDPE siyah hortum, U-PVC temiz su, PPRC boruları üretir. Dil: **TR (ana) ve EN**; üst menüde dil değiştirici olacak. TR ve EN için aynı layout, metin uzunluğu farkını tasarımda düşün.

### 0.1 Tasarım yönü (kısa)
Kurumsal, güvenilir, endüstriyel ama modern. "Standart şablon" görünümünden uzak: **geniş boşluk, net tipografi, ince çizgiler, keskin ama yumuşatılmış köşeler.** Yapay zekâ görünümü yok: neon, mor-mavi gradient, glow, glassmorphism, emoji, stok "mutlu ofis" illüstrasyonu **yok**. Fotoğraf ağırlıklı: gerçek tesis, depo, ürün fotoğrafları.

**İmza öğe (tüm sitede tekrar eder):** logodaki halka/su akışı kavisinden türetilmiş ince bir **akış çizgisi** (1.5 px, marka mavisi, %100 → %0 opaklık) ve boru kesitini anlatan **eş merkezli halka** motifi. Hero'da, istatistik rakamlarının arkasında, bölüm başlıklarının yanında ve CTA bandında çok hafif kullan. Arka planlarda %4 opaklıkta **teknik çizim (blueprint) ızgarası**.

### 0.2 Renkler (canlı siteden alındı, bunlara sadık kal)
| Token | Hex | Kullanım |
|---|---|---|
| Marka mavisi | `#0096D4` | Birincil buton, linkler, ikon vurgusu, rakamlar |
| Mavi koyu (hover/pressed) | `#007BB0` | Hover |
| Mavi derin | `#0B4F7A` | Gradient bitişi (yalnızca hero overlay ve CTA bandı, çok az) |
| Lacivert-gri (başlık) | `#343F52` | Başlıklar |
| Gövde metni | `#60697B` | Paragraf |
| Soluk metin | `#959CA9` | Yardımcı/placeholder |
| Açık mavi zemin | `#EDF2FC` | Alternatif bölüm zemini (istatistik, hizmetler) |
| Sayfa zemini | `#FEFEFE` | Ana zemin |
| Çizgi/kenarlık | `#E3E8F0` (orijinal `#CACACA` daha açıkla) | Kart kenarı, ayırıcı |
| Footer zemini | `#21262C` | Footer, koyu bantlar |
| Başarı / hata | `#198754` / `#DC3545` | Form durumları |
Mavi + koyu lacivert-gri + beyaz dışında **başka renk ekleme.** Gradient: yalnızca hero fotoğraf overlay'i (`#0E1A26` %88 → %25) ve CTA bandında `#0096D4 → #0B4F7A`.

### 0.3 Tipografi
**Manrope** (orijinalle aynı). H1 64/72 w700 −2% · H2 44/52 w700 −1.5% · H3 28/36 w700 · H4 20/28 w700 · Gövde 17/28 w400 · Küçük 14/22 · Etiket (üst başlık, eyebrow) 13/16 w700 **büyük harf, +8% harf aralığı, marka mavisi**. Mobil: H1 38/44, H2 30/38. Rakamlar (istatistik) 72–96 w800, tabular.

### 0.4 Grid ve ölçüler
Desktop 1440, içerik **1240 px**, 12 kolon, 24 boşluk. Mobil 390, kenar 20. Bölüm dikey boşluk 120 (mobil 72). Köşe yarıçapı: **kart 16, buton 10, input 10, görsel 20** (orijinaldeki tam yuvarlak "pill" butonlar yerine daha kurumsal 10). Gölge: tek seviye `0 12 32 rgba(52,63,82,.08)`. Kenarlık 1 px `#E3E8F0`.

### 0.5 Bileşenler
- **Buton:** Birincil (mavi dolu, beyaz yazı, 52 px yükseklik, sağda ok ikonu), İkincil (beyaz zemin, 1 px lacivert kenar), Hayalet (hero üstü: beyaz kenar). Hover: 2 px yukarı + hafif koyu mavi.
- **Kart:** beyaz, 1 px kenar, 16 radius, hover'da gölge + üst kenarda 3 px mavi çizgi açılır.
- **İkon seti (YENİ, özel):** 1.75 px çizgi, 32 px grid, **düz çizgi + tek mavi vurgu parçası**, yuvarlatılmış uç. Tutarlı tek aile. Gereken ikonlar: damla, boru kesiti, dirsek, T-parça, vana, manşon, pompa, filtre/süzgeç, damla sulama hattı, yağmurlama/sprinkler, rögar kapağı, depo, fabrika, kamyon/dağıtım, sertifika/rozet, teklif/liste, katalog indir, telefon, WhatsApp, e-posta, konum, saat, kullanıcılar, hedef, göz, el sıkışma, eğitim/şapka, fuar/stand, ok, artı, kapat, menü, dil, arama.
- **Form alanı:** 56 px, 10 radius, etiket üstte, odak halkası 2 px mavi %30.
- **Ürün grubu kartı:** 4:3 fotoğraf üstte, altında grup adı (büyük harf, w700), sağ altta ok ikonu; hover'da fotoğraf %103 zoom + ok mavi daire.
- **Hareket (az ve ince):** bölümler görünürken 16 px aşağıdan fade-up (400 ms), istatistik rakamları sayarak artar, referans/marka logoları yavaş yatay marquee (hover'da durur), hero fotoğraf çok hafif paralaks. Gereksiz animasyon yok.

---

## 1. SAYFALAR (her biri Desktop + Mobil)

Üst menü (sticky, scroll'da beyaz zeminli gölgeli): Logo · **Ana Sayfa · Kurumsal ▾ · Ürünler ▾ · Hizmetler · İ.K · Haberler / Blog · İletişim** · sağda: TR/EN değiştirici, **Teklif Listesi** ikonu + sayaç (orijinaldeki sepet yerine; "0"), **Katalog İndir** butonu. Mobilde hamburger + tam ekran menü (akordeonlu).
Kurumsal alt menüsü: Hakkımızda · **Yönetim Kurulu** · Markalarımız · Bizi Tanıyın · Belgelerimiz · Referanslar.
Ürünler mega menüsü: 14 ürün grubu, ikonlarıyla 2 sütun.
Sabit **WhatsApp** butonu sağ altta (yeşil `#25D366` yuvarlak, +90 533 841 78 80).

### 1.1 ANA SAYFA — bölüm sırası (orijinal sıra korunur, yeniler işaretli)
1. **Hero** (tam genişlik fotoğraf, yükseklik ~760): arka plan olarak tesis/depo havadan fotoğrafı (SBC BORU tabelalı depo). Sol hizalı başlık: **"Suyun Aktığı Her Yerdeyiz…"**, alt metin: *"Ürettiğimiz ürünlerin uzun ömürlü olmasıyla övünen bir şirketiz."* Butonlar: **Ürünleri İncele** (birincil) + **Katalog İndir** (hayalet). Altta hero'ya gömülü 4'lü ince bilgi şeridi: *2004'ten beri · 3000+ ürün çeşidi · 4500 m² depo · KKTC geneli teslimat.*
2. **Biz Kimiz / Hakkımızda özeti:** solda 3 fotoğraflı kolaj (ofis/bina, depo, ürün istifi; biri büyük, ikisi küçük, hafif kaydırılmış), sağda eyebrow "HAKKIMIZDA", H2 "Güvenilir altyapının üreticisi", orijinal iki paragraf (aşağıda metin), 3 madde (Üstyapı · Altyapı · Tarımsal sulama & peyzaj) ikonlu, buton **Daha fazlası**.
3. **Ürün Grupları** (eyebrow "ÜRÜN GRUPLARI", başlık "Birbirinden güzel tasarımlara sahip harika ürün gruplarımıza göz atın." sadeleştirilebilir: "Ürün gruplarımız"): **14 kart**, 4 kolon desktop / 2 mobil: PPRC GRUBU · ÜST YAPI · BAHÇE PEYZAJ · PVC GRUBU · TEMİZ SU BORU VE PARÇALARI · SÜZGEÇLER · ÖRTÜLER · EMİCİ VE VERİCİ · GALVANİZ GRUBU · BAHÇE PEYZAJ · TARIMSAL SULAMA · ALT YAPI · RÖGAR KAPAK GRUBU · SESİZ BORU GRUBU. Her kartta fotoğraf + özel ikon + ad. (İki "BAHÇE PEYZAJ" orijinalde de var; tasarımda ikincisini "BAHÇE PEYZAJ 2" yerine aynı bırak, not düş.)
4. **Yeni üretim tesisi bandı** (koyu `#21262C` zemin, sağda fabrika fotoğrafı): başlık "Yenilikçi üretim tesisi ile boru sektöründe atılım", metin ve üretilen ürün chip'leri: PVC atık su boruları · Siyah hortum (HDPE-LDPE) · Mandallı borular · U-PVC temiz su boruları · PPRC.
5. **Şirket İstatistikleri** (zemin `#EDF2FC`): eyebrow "ŞİRKET İSTATİSTİKLERİ", başlık "Eserlerimizle gurur duyuyoruz." Rakamlar: **%99** Proje Başarısı · **60+** Çalışan · **200** Dünya Çapında Müşteri · (ek) **2004** Kuruluş · **3000+** Ürün Çeşidi. Her birinin önünde özel ikon, arkada halka motifi.
6. **YENİ — Hizmetlerimiz** (6 kart, ikonlu): Toptan Tedarik · Yerinde Üretim · Proje ve Keşif Desteği · Tarımsal Sulama Çözümleri · Peyzaj ve Otomatik Sulama · Lojistik ve Dağıtım. *(Metinler taslak; kısa 1–2 cümle.)*
7. **Kurumsal şerit:** Kalite belgeleri özeti (3 sertifika kartı + "Belgelerimiz" linki) ve **Markalarımız** logo marquee'si.
8. **Referanslar:** logo duvarı / marquee (12 yer tutucu logo, gri tonlu, hover'da renkli).
9. **Şirketimizden Görüntüler:** galeri (masonry, 6–8 fotoğraf, tıklayınca lightbox) — orijinaldeki bölüm başlığı birebir.
10. **YENİ — Haberler & Blog:** 3 kart (ilk kart gerçek: *"SBC Boru olarak 46. Yapı Fuarı – Turkeybuild İstanbul'a katıldı"*), "Tümünü gör".
11. **İK şeridi:** "Ekibimize katılın" CTA'sı, açık pozisyon sayısı ve **Şimdi Başvur**.
12. **Bizimle İletişime Geçin:** sol metin *"Herhangi bir sorunuz var mı? İletişim formumuzdan bize ulaşın, kısa süre içinde size geri döneceğiz."*, sağ form: **İsim\*, Soyisim\*, Telefon\*, E-Posta\*, Mesajınız\*, Gönder**. Yanında harita kartı.
13. **Footer** (`#21262C`): logo (beyaz sürüm) + *"2004 yılında kurulmuş olup; üstyapı, altyapı tesisat boruları ve tarımsal sulama olmak üzere üç alanda faaliyet göstermektedir."* · **Kurumsal** (Hakkımızda, Yönetim Kurulu, Markalarımız, Bizi Tanıyın, Referanslar, Belgelerimiz, İletişim, Haberler) · **Ürünler** (14 grup) · **Bize Ulaşın:** Lefkoşa-Mağusa bağlantı yolu üzeri, Büyük Sanayi Bölgesi, Gazimağusa, KKTC · **Yol Tarifi Al** · info@sbcboru.com · +90 533 841 78 80 · sosyal ikonlar (X, Facebook, Instagram, YouTube) · alt çizgi: "© 2026 SBC Boru. Tüm Hakları Saklıdır."

### 1.2 DİĞER SAYFALAR (hepsi Desktop + Mobil)
Ortak: üstte 280 px sayfa başlığı bandı (fotoğraf + koyu overlay, breadcrumb: Ana Sayfa › Sayfa), altta İletişim formu + Footer.

1. **Hakkımızda:** "SBC Boru 2004 yılında kurulmuş olup ilk olarak İskele bölgesinde faaliyete geçmiştir." · **Biz Kimiz?** (metin) · **Zaman çizgisi** (2004 İskele → 2015 Gazimağusa'ya taşınma, 1500 m² çalışma alanı + 4500 m² depo → Yeni üretim tesisi) · **Misyonumuz** ve **Vizyonumuz** (iki büyük kart, aşağıdaki metinler) · **Ürün Çeşitliliği** (PVC Boru ve Aksamları, Damlama Borusu ve Aksamları, Peyzaj ve Otomatik Sulama, PPRC Boru ve Aksamları, Gübre Tankları ve Filtreler, Galvaniz Vana ve Aksamları — ikonlu 6 kutu) · **Yenilikçi Üretim Tesisi** · **İstatistiksel Başarılar**.
2. **YENİ — Yönetim Kurulu:** Üstte kısa tanıtım; **Yönetim Kurulu Başkanı** için büyük kart (portre fotoğraf yer tutucusu, ad-soyad, unvan, 2 cümle mesaj/alıntı), altında 4–6 üye kartı (portre, ad, unvan, LinkedIn ikonu). **Ad ve fotoğraflar yer tutucu**, gerçek isimleri sonra eklenecek. Üst yönetim/departman şeması (organizasyon çizelgesi) için basit bir blok.
3. **Markalarımız:** marka logoları grid'i (4×3, yer tutucu), her logoya tıklayınca marka açıklaması (modal).
4. **Bizi Tanıyın:** iki büyük kart — **Bizi Tanıyın (Türkçe)** "Yüksek kaliteli, yenilikçi plastik çözümler üreten bir fabrika olarak hizmet veriyoruz. Olağanüstü ürünler ve hizmetlerimizle tanışın." → **Sunumu Görüntüle**; **Bizi Tanıyın (English)** "We specialize in creating high-quality, innovative plastic solutions tailored to your needs. Experience exceptional products and service with us." → **See the Presentation**. Sunum önizleme görseli (PDF kapağı) ve tam ekran görüntüleyici modalı.
5. **Ürünler (liste):** solda **Kategoriler** (14, sayaçlı, mobilde filtre çekmecesi), üstte sıralama (Artan Fiyat / Azalan Fiyat), arama, ürün grid'i (3 kolon): fotoğraf, ad, kod, kısa spesifikasyon (çap, basınç), **Teklif Listesine Ekle** butonu. Yükleniyor ve boş durum tasarımı. Alt bilgi: "Daha fazla ürün görüntüleyebilmek için sol menüden kategorilere tıklayabilirsiniz."
6. **Ürün detayı:** galeri, ad, kod, kategori, spesifikasyon tablosu (çap, SDR/PN, uzunluk, standart), uygulama alanları ikonlu, teknik dosya indir, adet + **Teklif Listesine Ekle**, benzer ürünler.
7. **Teklif Listesi / Sepet:** ürün satırları, adet, not alanı, iletişim bilgileri, **Teklif İste** (WhatsApp ve e-posta seçenekli).
8. **Katalog:** büyük katalog kapağı mockup'ı + **Katalog İndir** (PDF) + önizleme sayfaları.
9. **Referanslar:** logo duvarı (6×4) + 3 proje vaka kartı (proje adı, bölge, kullanılan ürün grubu, fotoğraf).
10. **Belgelerimiz:** giriş paragrafı *"SBC BORU olarak, üstün kalite anlayışımızı ve müşteri memnuniyetini her zaman ön planda tutuyoruz. Aşağıda, sahip olduğumuz kalite belgelerini inceleyerek ürün ve hizmetlerimizin yüksek standartlarda olduğunu görebilirsiniz."* + sertifika kartları (dikey A4 önizleme, tıklayınca büyür, belge adı/yıl yer tutucu — **gerçek belge adı uydurma**).
11. **İnsan Kaynakları (İ.K):** başlık "Geliştirmenin geleceğini şekillendirmeye yardımcı olmak için ekibimize katılın." · **SBC'li Olmak** (metin) · **İş Başvurusu** (Üniversite mezunları, Meslek Lisesi mezunları, yeni mezunlar, tecrübeli çalışanlar) + **Açık pozisyonlar** listesi: Genel Başvuru · Dağıtım Personeli · Satış Destek Personeli · Stajyer · **Eğitim** (oryantasyon → fabrika ve ofis tanıtımı → fuar/kongre ziyaretleri; etkinlik kartları: *Depo & Stok Yönetimi Eğitimi – 3 Şubat 2023*, *Growtech Fuarı – 23–26 Kasım 2022*) · **Kariyer** (terfi değerlendirmesi) · **Aktiviteler** (fotoğraf galerisi) · **Şimdi Başvur** formu: Başvuru Pozisyonu\* (açılır), İsim\*, Soyisim\*, Uyruk\* (açılır), Telefon, E-posta, CV yükle (sürükle-bırak alanı), KVKK onay kutusu, Gönder.
12. **Haberler / Blog (liste):** öne çıkan büyük kart + grid, kategori filtreleri (Haberler, Fuarlar, Rehber, Sektör), arama. **Blog detayı:** kapak, başlık, tarih, okuma süresi, içerik, paylaş, ilgili yazılar. SEO blog başlık önerileri (yer tutucu içerik, 3 satır): "PPRC boru nedir, nerelerde kullanılır?", "Tarımsal sulamada damla sulama borusu seçimi", "PVC atık su borusu ölçü ve basınç sınıfları rehberi", "KKTC'de yapı için doğru tesisat borusu seçimi".
13. **İletişim:** sol bilgi kartları (Adres, Telefon, WhatsApp, E-posta, Çalışma saatleri yer tutucu), sağ form, altta tam genişlik **harita** (Gazimağusa Büyük Sanayi Bölgesi pini) + **Yol Tarifi Al** butonu.
14. **404** ve **Form gönderildi** başarı durumu.

---

## 2. SİTE METİNLERİ (orijinalden, birebir kullan)

- **Hero:** Suyun Aktığı Her Yerdeyiz… / Ürettiğimiz ürünlerin uzun ömürlü olmasıyla övünen bir şirketiz. / Ürünleri İncele
- **Hakkımızda özeti:** SBC Boru, 2004 yılında kurulmuş bir şirket olarak, üstyapı, altyapı tesisat boruları, tarımsal sulama, bahçe peyzaj alanlarında faaliyet gösteren köklü bir şirkettir. Sektördeki deneyimi ve geniş ürün yelpazesi ile beraber, yapı marketleri, hırdavatçılar ve inşaat şirketleri gibi çeşitli müşteri gruplarına ürün tedarik etmekte ve bu alanda lider konumunu sürdürmektedir. — 2015 yılında merkezini Gazimağusa'ya taşıyan SBC Boru, sahip olduğu satış ofisi, 1500 metrekarelik çalışma alanı ve 4500 metrekarelik depo kapasitesi ile toplamda 60'ı aşkın personeliyle Kuzey Kıbrıs Türk Cumhuriyeti genelinde kapsamlı hizmetler sunmaktadır.
- **Misyon:** Çevre dostu bir perspektifle su tesisatı ve tarımsal sulama alanında, üstyapı ve altyapı sektörlerinde de müşterilerimize güvenilir ve yüksek kaliteli hizmet sunarak onların ihtiyaçlarını karşılamak. Sürekli değişen piyasa dinamiklerini dikkate alarak ürün portföyümüzü sürekli olarak geliştirmek, teknolojik gelişmelere uyum sağlayarak büyümek ve yeni ulaşılabilir pazarlar oluşturarak SBC Boru'nun temel hedeflerini belirlemekteyiz.
- **Vizyon:** İçe kapalı ekonomimize ekonomik kalkınma sağlayarak istihdamı artırmak, personelimizin yaşam standardını yükseltmek ve iş ortaklarımıza uygun fiyatlarla yüksek kalitede ürünler sunarak onları rekabetçi bir konuma getirmek.
- **Yeni üretim tesisi:** Gurur duyduğumuz en son başarı, yeni kurulan üretim tesisimizdir. Bu tesis sayesinde PVC atık su boruları, siyah hortum (HDPE-LDPE), mandallı borular, U-PVC temiz su boruları, PPRC gibi birçok ürünü üretmeye başladık. Bu atılım, yerli üretimi artırarak sektördeki etkimizi daha da güçlendirmemize yardımcı oldu.
- **İstatistik:** Şirketimizin proje başarısı %99'dur ve 60'ın üzerinde uzman çalışanı ile dünya genelinde 200'ü aşkın müşteriye hizmet sunmaktadır.
- **İK — SBC'li Olmak:** Mağusa'da Büyük Sanayi Bölgesinde bulunan … 3000'in üzerinde ürün çeşidi ile yapı marketlere, hırdavatçılara ve inşaat şirketlerine ürün tedarik eden firmamızda en değerli sermayesi insan kaynakları olarak kabul etmektedir. Bu nedenle de, çalışma arkadaşlarımıza, mutlu olacakları, mesleki ve insani açılardan kendilerini geliştirebilecekleri bir çalışma ortamı sunmayı birinci hedefimiz olarak görüyoruz.
- **Haber:** SBC Boru olarak 46. Yapı Fuarı – Turkeybuild İstanbul'a katıldı. (TÜYAP, 2024; KTSO ve Sanayi Dairesi katkısıyla Kıbrıs'tan katılan 5 sanayici firmadan biri.)
- **Not (tutarsızlık):** Orijinalde personel sayısı ana sayfada "60'ı aşkın", Hakkımızda'da "70'i aşkın"; faaliyet alanı bazı yerde "üç", İK'da "dört" alan. Tasarımda **60+** ve **üç alan** kullan, bu noktayı "doğrulanacak" diye not et.

---

## 3. GÖRSELLER
Orijinal siteden alınan gerçek fotoğraflar kullanılacak (şirketin kendi materyali). Kaynak: `https://api.sbcboru.com/public/uploads/images/` altında — logo `sbcboru-logo.png`; hero/tesis/depo/ürün fotoğrafları `11537753.jpg`, `101713124.jpg`, `33344444.png`, `67445256.jpg`, `021102135.jpg`, `76565362.jpg`, `45661375.jpg`, `351016430.jpg`, `5210166104.jpg`, `52143441.jpg`, `32241505.jpg`, `31631244.jpg`, `51774445.jpg`, `07762551.jpg`, `56633321.jpg`, `04176115.jpg`, `201061575.jpg`, `16157127.png`, `71663671.png`, `310261142.png`, `47152260.jpg`, `4117101053.jpg`, `02276461.jpg`. Önce hepsini indir, **her birine tek tek bak**, hangisinin hangi ürün grubu/tesis/hero/galeri olduğuna sen karar ver ve ilgili yere yerleştir. Düşük çözünürlüklüleri büyük alanlarda kullanma. Logo koyu zeminde beyaz sürüm gerektirir (şimdilik yer tutucu). Yönetim kurulu portreleri, referans/marka logoları, sertifikalar, blog görselleri **yer tutucu** (gri, "Görsel eklenecek"), sonra gelecek.

## 4. İŞ AKIŞI VE TESLİM
1. Önce **stil kılavuzu sayfası**: renkler, tipografi, ikon seti (hepsi), buton/form/kart bileşenleri, ızgara.
2. Sonra Ana Sayfa (Desktop + Mobil), ardından yukarıdaki sayfalar sırayla. Sayfa isimleri: `01 Ana Sayfa`, `02 Hakkımızda`, … `Mobil` ekleriyle.
3. Tüm metinler TR. Her sayfanın üstüne küçük bir not: "EN sürümü aynı layout".
4. Tutarlılık: her sayfada aynı üst menü, aynı footer, aynı bölüm boşlukları. Kopyalanan bileşenler gerçek bileşen (component) olarak kurulsun.
5. Bitince tüm sayfaların ekran görüntüsünü al, taşma/üst üste binen metin/kopuk hizalama varsa düzelt, dosyayı `sbc-boru-v1.figcraft` olarak kaydet.

Ürün adları, çaplar, fiyatlar, yönetim kurulu isimleri, sertifika adları **uydurma**; gerçek olmayan her şey açıkça yer tutucu görünsün.
