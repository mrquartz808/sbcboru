# SBC Boru — kurumsal web sitesi tasarımı (v1)

`figcraft-master-prompt.md` brief'ine göre hazırlanmış, duyarlı (1440 px masaüstü / 390 px mobil) statik HTML tasarımı.
FigCraft/Figma bu oturumda erişilebilir olmadığı için tasarım doğrudan koda dökülmüştür.

- `index.html` … `stil-kilavuzu.html` — 19 sayfa (Ana Sayfa, Hakkımızda, Yönetim Kurulu, Markalarımız, Bizi Tanıyın, Ürünler, Ürün Detayı, Teklif Listesi, Katalog, Referanslar, Belgelerimiz, İ.K, Haberler, Blog Detayı, İletişim, Hizmetler, 404, Form gönderildi, Stil Kılavuzu)
- `assets/css/site.css` — tasarım sistemi (renk/tipografi/bileşen token'ları)
- `assets/js/site.js` — menü, fade-up, sayaç, lightbox, teklif listesi (localStorage), form doğrulama
- `assets/img/` — canlı siteden alınan gerçek fotoğraflar (web boyutuna indirildi)
- `src/build.py` — sayfaları üretir: `python3 src/build.py` (ikon seti burada tanımlı)

## Yerelde çalıştırma (localhost)

```bash
git clone https://github.com/mrquartz808/sbcboru.git
cd sbcboru
git checkout claude/new-session-ozifx1
python3 -m http.server 8000
```

Sonra tarayıcıda `http://localhost:8000` adresini açın. Güncellemeleri almak için aynı klasörde `git pull`, sayfayı da `Cmd+Shift+R` ile yenileyin.
Python yoksa: `npx serve .` ya da klasörü açıp `index.html`'e çift tıklamak da çalışır (Google Fonts için internet gerekir).
Sayfaları yeniden üretmek için (ikon veya metin değişince): `python3 src/build.py`.

Yer tutucular (gri "Görsel eklenecek"): yönetim kurulu, marka/referans logoları, sertifikalar, blog görselleri, ürün adları/kodları/ölçüleri.
Doğrulanacak: personel sayısı (60+ / 70+), faaliyet alanı sayısı (üç / dört), hizmet metinleri (taslak).
