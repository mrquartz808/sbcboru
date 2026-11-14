# SBC Boru — kurumsal web sitesi tasarımı (v1)

`figcraft-master-prompt.md` brief'ine göre hazırlanmış, duyarlı (1440 px masaüstü / 390 px mobil) statik HTML tasarımı.
FigCraft/Figma bu oturumda erişilebilir olmadığı için tasarım doğrudan koda dökülmüştür.

- `docs/index.html` … `docs/stil-kilavuzu.html` — 19 sayfa (site burada; GitHub Pages `/docs` klasöründen yayınlar) (Ana Sayfa, Hakkımızda, Yönetim Kurulu, Markalarımız, Bizi Tanıyın, Ürünler, Ürün Detayı, Teklif Listesi, Katalog, Referanslar, Belgelerimiz, İ.K, Haberler, Blog Detayı, İletişim, Hizmetler, 404, Form gönderildi, Stil Kılavuzu)
- `docs/assets/css/site.css` — tasarım sistemi (renk/tipografi/bileşen token'ları)
- `docs/assets/js/site.js` — menü, fade-up, sayaç, lightbox, teklif listesi (localStorage), form doğrulama
- `docs/assets/img/` — canlı siteden alınan gerçek fotoğraflar (web boyutuna indirildi)
- `src/build.py` — sayfaları üretir: `python3 src/build.py` (ikon seti burada tanımlı)

## Yerelde çalıştırma (localhost)

```bash
git clone -b claude/new-session-ozifx1 https://github.com/mrquartz808/sbcboru.git
cd sbcboru/docs
python3 -m http.server 8000
```

Sonra tarayıcıda `http://localhost:8000` adresini açın. Güncellemeleri almak için aynı klasörde `git pull`, sayfayı da `Cmd+Shift+R` ile yenileyin.
Python yoksa: `npx serve .` ya da `docs/index.html`'e çift tıklamak da çalışır (Google Fonts için internet gerekir).
Sayfaları yeniden üretmek için (ikon veya metin değişince): `python3 src/build.py`.

Yer tutucular (gri "Görsel eklenecek"): yönetim kurulu, marka/referans logoları, sertifikalar, blog görselleri, ürün adları/kodları/ölçüleri.
Doğrulanacak: personel sayısı (60+ / 70+), faaliyet alanı sayısı (üç / dört), hizmet metinleri (taslak).

## GitHub Pages ile yayın
Settings → Pages → Source: **Deploy from a branch** → Branch: `claude/new-session-ozifx1`, klasör: `/docs` → Save.
Adres: `https://mrquartz808.github.io/sbcboru/` (her push'tan 1–2 dk sonra güncellenir). Site `noindex` ve `robots.txt` ile arama motorlarından gizlidir.
İç belgeler (brief, görsel prompt rehberi) `internal/` klasöründedir ve Pages'te yayınlanmaz.

## Scroll sürümü (scroll-craft)
`docs/scroll/` altında, scroll-craft becerisiyle kurulmuş ikinci bir ana sayfa var: kapaktaki boru kesiti büyüyüp tesise geçiyor ("bore" imza hareketi).
Kaynak: `scrollcraft/builds/sbc-boru/` (BRIEF.md, index.html, varlıklar), katman üretici: `scrollcraft/tools/make_layers.py`.
Yayında: `https://mrquartz808.github.io/sbcboru/scroll/` · yerelde: `cd docs && python3 -m http.server 8000` → `http://localhost:8000/scroll/`
Önizleme için kaynak klasöründe: `node <skill>/scripts/serve.mjs --root . --port 4500`.
