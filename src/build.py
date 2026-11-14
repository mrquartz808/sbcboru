#!/usr/bin/env python3
"""SBC Boru statik tasarım sitesi üreticisi.  Kullanım: python3 src/build.py"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------ İKONLAR
def a(d):  # tek mavi vurgu parçası
    return f'<path style="stroke:var(--ic-accent,#0096D4)" d="{d}"/>'
def p(d):
    return f'<path d="{d}"/>'
def circ(cx, cy, r, acc=False):
    s = ' style="stroke:var(--ic-accent,#0096D4)"' if acc else ''
    return f'<circle{s} cx="{cx}" cy="{cy}" r="{r}"/>'
def rect(x, y, w, h, rx=0, acc=False):
    s = ' style="stroke:var(--ic-accent,#0096D4)"' if acc else ''
    return f'<rect{s} x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'

ICONS = {
 'drop': p("M16 4c4.5 6 8 9.8 8 14a8 8 0 0 1-16 0c0-4.2 3.5-8 8-14z") + a("M12 19a4 4 0 0 0 4 4"),
 'pipe': circ(16,16,11) + circ(16,16,5.5,True),
 'elbow': p("M5 8h10a12 12 0 0 1 12 12v4M5 16h6a4 4 0 0 1 4 4v4") + a("M5 8v8M15 24h12"),
 'tee': p("M4 8h24M4 16h8v10h8V16h8") + a("M4 8v8M28 8v8"),
 'valve': p("M3 21h4M25 21h4M7 15l9 6-9 6zM25 15l-9 6 9 6z") + a("M16 21V9M11 9h10"),
 'coupling': rect(9,9,14,14,2) + p("M3 12v8M29 12v8M3 16h6M23 16h6") + a("M13 9v14M19 9v14"),
 'pump': circ(14,16,8) + p("M22 16h7M14 8V4h-4M6 25h16") + a("M12 12l5 4-5 4"),
 'filter': p("M5 6h22l-8 10v9l-6 3V16z") + a("M9 10h14"),
 'drip': p("M3 9h26M3 13h26") + a("M9 17c1.5 2 2.5 3.2 2.5 4.5a2.5 2.5 0 0 1-5 0C6.5 20.2 7.5 19 9 17zM21 19c1.2 1.6 2 2.6 2 3.6a2 2 0 0 1-4 0c0-1 .8-2 2-3.6z"),
 'sprinkler': p("M13 29v-8h6v8M11 29h10M14 21v-3h4v3") + a("M16 15V9M16 9c-3 0-6 1-8 3M16 9c3 0 6 1 8 3M16 9c-1.5-2-2-3.500-2-5M16 9c1.5-2 2-3.500 2-5"),
 'warehouse': p("M3 13L16 5l13 8v14H3z") + a("M10 27V17h12v10M10 22h12"),
 'factory': p("M3 27V14l8 5v-5l8 5v-5l8 5v8z") + a("M22 12V5h4v10"),
 'truck': p("M3 8h15v14H3zM18 13h6l4 4v5H18z") + circ(9,23,3,True) + circ(23,23,3,True),
 'badge': circ(16,13,8) + p("M11 20l-3 9 8-4 8 4-3-9") + a("M12.5 13l2.5 2.5 4.5-5"),
 'quote': rect(6,4,20,24,3) + p("M11 11h10M11 16h10") + a("M11 21h5"),
 'download': p("M16 5v15M9 14l7 7 7-7") + a("M5 27h22"),
 'phone': p("M8 4h5l2 6-3 2a14 14 0 0 0 8 8l2-3 6 2v5a3 3 0 0 1-3 3A21 21 0 0 1 5 7a3 3 0 0 1 3-3z") + a("M20 5a7 7 0 0 1 7 7M20 9a3 3 0 0 1 3 3"),
 'whatsapp': p("M5 27l2-6a11 11 0 1 1 4 4z") + a("M12 12c0 4 4 8 8 8l1.500-2-3-1.500-1 1c-1-.5-2.500-2-3-3l1-1L14 11z"),
 'mail': rect(3,7,26,18,3) + a("M4 10l12 9 12-9"),
 'pin': p("M16 29s-9-8-9-15a9 9 0 0 1 18 0c0 7-9 15-9 15z") + circ(16,14,3.5,True),
 'clock': circ(16,16,12) + a("M16 9v7l5 3"),
 'users': circ(12,11,5) + p("M3 27c0-5 4-8 9-8s9 3 9 8") + circ(23,12,3.5,True) + a("M24 19c3 .5 5 3 5 7"),
 'target': circ(16,16,12) + circ(16,16,6) + circ(16,16,1.5,True),
 'eye': p("M2 16s5-9 14-9 14 9 14 9-5 9-14 9S2 16 2 16z") + circ(16,16,4,True),
 'handshake': p("M3 14l7-6 6 2 6-2 7 6M3 14l9 11 3-2M29 14l-8 10-4 2-3-3") + a("M12 17l4 4"),
 'grad': p("M2 12l14-7 14 7-14 7z") + p("M8 15v7c0 2 4 4 8 4s8-2 8-4v-7") + a("M30 12v8"),
 'booth': p("M4 12h24l-2-7H6zM6 12v15h20V12") + a("M12 27v-8h8v8"),
 'cover': p("M3 25l5-14h16l5 14z") + a("M8 11l-2 14M24 11l2 14M16 11v14"),
 'arrow': p("M5 16h22M19 8l8 8-8 8"),
 'plus': p("M16 6v20M6 16h20"),
 'close': p("M7 7l18 18M25 7L7 25"),
 'menu': p("M5 9h22M5 16h22") + a("M5 23h14"),
 'globe': circ(16,16,12) + p("M4 16h24") + a("M16 4c-5 4-5 20 0 24M16 4c5 4 5 20 0 24"),
 'search': circ(14,14,9) + a("M21 21l7 7"),
 'check': p("M6 17l7 7L26 9"),
 'chev': p("M8 12l8 8 8-8"),
 'doc': p("M8 3h11l7 7v19H8z") + a("M19 3v7h7M12 17h10M12 22h10"),
 'upload': p("M16 21V6M9 12l7-7 7 7") + a("M5 27h22"),
 'user': circ(16,11,6) + a("M5 28c0-6 5-9 11-9s11 3 11 9"),
 'x': p("M6 5l20 22M26 5L6 27"),
 'facebook': p("M18 28V16h4l1-5h-5V8c0-1.500 1-2 2.500-2H23V2h-4c-4 0-6 2-6 6v3H9v5h4v12z"),
 'instagram': rect(4,4,24,24,7) + circ(16,16,6) + p("M23 9v.01"),
 'youtube': rect(3,7,26,18,6) + p("M13 12l7 4-7 4z"),
 'linkedin': p("M6 12v14M6 6v.5M12 26V12M12 18c0-4 3-6 6-6s5 2 5 6v8"),
 'ext': p("M12 6h14v14M26 6L8 24"),
}
ICONS['manhole'] = rect(4,4,24,24,4) + circ(16,16,8) + a("M12 13h8M11 16h10M12 19h8")

def sprite():
    s = ''.join(f'<symbol id="i-{k}" viewBox="0 0 32 32">{v}</symbol>' for k, v in ICONS.items())
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
            '<linearGradient id="fg" x1="0" x2="1"><stop offset="0" stop-color="#0096D4"/><stop offset="1" stop-color="#0096D4" stop-opacity="0"/></linearGradient>'
            '<linearGradient id="fw" x1="0" x2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            f'</defs>{s}</svg>')

def ic(name, cls=''):
    return f'<svg class="ic {cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def flow(cls='', grad='fg', d="M0 90 C 300 20, 600 130, 900 60 S 1300 30, 1440 70"):
    return (f'<svg class="flow {cls}" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="{d}" fill="none" stroke="url(#{grad})" stroke-width="1.5" vector-effect="non-scaling-stroke"/></svg>')

# ------------------------------------------------------------------ VERİ
IMG = 'assets/img/'
GROUPS = [  # (ad, ikon, görsel)
 ('PPRC GRUBU','coupling','pprc.jpg'), ('ÜST YAPI','warehouse','ust-yapi.jpg'), ('BAHÇE PEYZAJ','sprinkler','bahce-peyzaj.jpg'),
 ('PVC GRUBU','pipe','pvc.jpg'), ('TEMİZ SU BORU VE PARÇALARI','drop','temiz-su.jpg'), ('SÜZGEÇLER','filter','suzgec.jpg'),
 ('ÖRTÜLER','cover','ortu.jpg'), ('EMİCİ VE VERİCİ','pump','emici-verici.jpg'), ('GALVANİZ GRUBU','valve','galvaniz.jpg'),
 ('BAHÇE PEYZAJ','sprinkler','yagmurlama.jpg'), ('TARIMSAL SULAMA','drip','tarimsal-sulama.jpg'), ('ALT YAPI','elbow','alt-yapi.jpg'),
 ('RÖGAR KAPAK GRUBU','manhole','rogar.jpg'), ('SESİZ BORU GRUBU','tee','sessiz-boru.jpg'),
]
PHONE = '+90 533 841 78 80'
WA = 'https://wa.me/905338417880'
MAIL = 'info@sbcboru.com'
ADDR = 'Lefkoşa-Mağusa bağlantı yolu üzeri, Büyük Sanayi Bölgesi, Gazimağusa, KKTC'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Gazimağusa+Büyük+Sanayi+Bölgesi'

# ------------------------------------------------------------------ ORTAK PARÇALAR
def header(active=''):
    def on(k): return ' class="on"' if active == k else ''
    kurumsal = [('Hakkımızda','hakkimizda.html','users'),('Yönetim Kurulu','yonetim-kurulu.html','target'),('Markalarımız','markalarimiz.html','badge'),
                ('Bizi Tanıyın','bizi-taniyin.html','eye'),('Belgelerimiz','belgelerimiz.html','doc'),('Referanslar','referanslar.html','handshake')]
    kd = ''.join(f'<a href="{h}">{ic(i)}{t}</a>' for t, h, i in kurumsal)
    mega = ''.join(f'<a href="urunler.html">{ic(i)}{n}</a>' for n, i, _ in GROUPS)
    mk = ''.join(f'<a href="{h}">{ic(i)}{t}</a>' for t, h, i in kurumsal)
    mm = ''.join(f'<a href="urunler.html">{ic(i)}{n}</a>' for n, i, _ in GROUPS)
    return f'''
<header class="hdr"><div class="wrap hdr-in">
  <a class="logo" href="index.html" aria-label="SBC Boru"><img class="d" src="{IMG}logo.png" alt="SBC Boru"><img class="w" src="{IMG}logo-beyaz.png" alt="SBC Boru"></a>
  <ul class="nav">
    <li{on('home')}><a href="index.html">Ana Sayfa</a></li>
    <li{on('kurumsal')}><button type="button">Kurumsal {ic('chev')}</button><div class="drop">{kd}</div></li>
    <li{on('urunler')}><button type="button">Ürünler {ic('chev')}</button><div class="drop mega">{mega}</div></li>
    <li{on('hizmetler')}><a href="hizmetler.html">Hizmetler</a></li>
    <li{on('ik')}><a href="insan-kaynaklari.html">İ.K</a></li>
    <li{on('haberler')}><a href="haberler.html">Haberler / Blog</a></li>
    <li{on('iletisim')}><a href="iletisim.html">İletişim</a></li>
  </ul>
  <div class="hdr-r">
    <div class="lang" title="EN sürümü aynı layout"><a class="on" href="#">TR</a><a href="#">EN</a></div>
    <a class="cart" href="teklif-listesi.html" aria-label="Teklif listesi">{ic('quote','md')}<span class="cnt">0</span></a>
    <a class="btn btn-secondary sm" href="katalog.html">{ic('download')}Katalog İndir</a>
    <button class="burger" aria-label="Menü">{ic('menu','md')}</button>
  </div>
</div></header>
<div class="mnav" role="dialog" aria-label="Menü">
  <div class="mnav-top"><img src="{IMG}logo.png" alt="SBC Boru"><button class="x" aria-label="Kapat">{ic('close','md')}</button></div>
  <nav>
    <a href="index.html">Ana Sayfa</a>
    <details><summary>Kurumsal {ic('chev','md')}</summary>{mk}</details>
    <details><summary>Ürünler {ic('chev','md')}</summary>{mm}</details>
    <a href="hizmetler.html">Hizmetler</a><a href="insan-kaynaklari.html">İ.K</a><a href="haberler.html">Haberler / Blog</a><a href="iletisim.html">İletişim</a>
  </nav>
  <div class="btns"><a class="btn btn-primary" href="katalog.html">{ic('download')}Katalog İndir</a><a class="btn btn-secondary" href="teklif-listesi.html">{ic('quote')}Teklif Listesi</a>
  <div class="lang" style="justify-self:start"><a class="on" href="#">TR</a><a href="#">EN</a></div></div>
</div>'''

def footer():
    kurum = ['Hakkımızda','Yönetim Kurulu','Markalarımız','Bizi Tanıyın','Referanslar','Belgelerimiz','İletişim','Haberler']
    kh = ['hakkimizda','yonetim-kurulu','markalarimiz','bizi-taniyin','referanslar','belgelerimiz','iletisim','haberler']
    k = ''.join(f'<li><a href="{h}.html">{t}</a></li>' for t, h in zip(kurum, kh))
    u = ''.join(f'<li><a href="urunler.html">{n.capitalize() if False else n}</a></li>' for n, _, _ in GROUPS)
    return f'''
<footer class="ftr"><div class="blueprint"></div><div class="wrap">
  <div class="ftr-g">
    <div><img class="fl" src="{IMG}logo-beyaz.png" alt="SBC Boru">
      <p class="small" style="font-size:15px;line-height:24px">2004’te kurulduk; üstyapı, altyapı tesisat boruları ve tarımsal sulama alanlarında hizmet veriyoruz.</p>
      <div class="soc"><a href="#" aria-label="X">{ic('x')}</a><a href="#" aria-label="Facebook">{ic('facebook')}</a><a href="#" aria-label="Instagram">{ic('instagram')}</a><a href="#" aria-label="YouTube">{ic('youtube')}</a></div></div>
    <div><h5>Kurumsal</h5><ul>{k}</ul></div>
    <div><h5>Ürünler</h5><ul style="columns:1">{u}</ul></div>
    <div class="ct"><h5>Bize Ulaşın</h5><ul>
      <li>{ic('pin')}<span>{ADDR}</span></li>
      <li><a class="link-arrow" style="color:#fff" href="{MAPS}">Yol Tarifi Al {ic('arrow')}</a></li>
      <li>{ic('mail')}<a href="mailto:{MAIL}">{MAIL}</a></li>
      <li>{ic('phone')}<a href="tel:+905338417880">{PHONE}</a></li></ul></div>
  </div>
  <div class="ftr-b"><span>© 2026 SBC Boru. Tüm Hakları Saklıdır.</span><span>EN sürümü aynı layout · Tasarım taslağı v1 · yer tutucu içerikler işaretlidir</span></div>
</div></footer>
<a class="wa" href="{WA}" aria-label="WhatsApp ile yazın">{ic('whatsapp')}</a>
<div class="lb" aria-hidden="true"><button aria-label="Kapat">{ic('close','md')}</button><img alt=""></div>'''

def page(slug, title, body, active='', hero=False, desc=''):
    out = f'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — SBC Boru</title><meta name="description" content="{html.escape(desc or 'SBC Boru — Kuzey Kıbrıs’ın en büyük boru üreticisi ve tedarikçisi.')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css"></head>
<body class="{'has-hero' if hero else ''}">{sprite()}
{header(active)}
<main>
{body}
</main>
{footer()}
<script src="assets/js/site.js"></script></body></html>'''
    with open(os.path.join(ROOT, slug), 'w', encoding='utf-8') as f:
        f.write(out)

def head(title, crumb, img='hero-tesis.jpg'):
    return f'''<section class="pagehead" style="background-image:url({IMG}{img})"><div class="wrap">
  <div class="crumb"><a href="index.html">Ana Sayfa</a>{ic('chev')}<span>{crumb}</span></div><h1>{title}</h1></div></section>'''

def sec_head(eyebrow, title, p='', center=False):
    return f'<div class="sec-head fu{" center" if center else ""}"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{("<p>"+p+"</p>") if p else ""}</div>'

def group_cards(n=14, cols='g4'):
    return f'<div class="grid {cols}">' + ''.join(
        f'<a class="card pg fu" href="urunler.html"><div class="ph"><img src="{IMG}{im}" alt="{nm}" loading="lazy"><span class="badge">{ic(i)}</span></div>'
        f'<div class="bd"><span>{nm}</span><span class="go">{ic("arrow")}</span></div></a>' for nm, i, im in GROUPS[:n]) + '</div>'

def field(label, name, typ='text', req=True, ph='', cls=''):
    star = '*' if req else ''
    r = ' required' if req else ''
    return f'<div class="fld {cls}"><label for="{name}">{label}{star}</label><input id="{name}" name="{name}" type="{typ}" placeholder="{ph}"{r}><div class="em">Bu alan zorunludur.</div></div>'

def contact_form(action='tesekkurler.html'):
    return f'''<form class="form" data-demo="{action}" novalidate>
  {field('İsim','ad')}{field('Soyisim','soyad')}{field('Telefon','tel','tel')}{field('E-Posta','mail','email')}
  <div class="fld full"><label for="msg">Mesajınız*</label><textarea id="msg" required></textarea><div class="em">Bu alan zorunludur.</div></div>
  <div class="full"><button class="btn btn-primary" type="submit">Gönder {ic('arrow')}</button></div></form>'''

def contact_section(with_map=True):
    m = f'''<div class="mapcard"><div class="grid-bg"></div><div class="road" style="left:-5%;top:58%;width:110%;height:16px;transform:rotate(-8deg)"></div><div class="road" style="left:34%;top:-5%;width:12px;height:110%;transform:rotate(14deg)"></div>
      <div class="pinwrap">{ic('pin')}<span class="lbl">SBC Boru · Büyük Sanayi Bölgesi</span></div>
      <a class="btn btn-primary sm" href="{MAPS}">{ic('pin')}Yol Tarifi Al</a></div>''' if with_map else ''
    return f'''<section class="sec" id="iletisim-formu"><div class="wrap"><div class="contact-grid">
  <div class="fu"><span class="eyebrow">İletişim</span><h2>Bizimle İletişime Geçin</h2>
    <p style="margin-top:16px">Herhangi bir sorunuz var mı? İletişim formumuzdan bize ulaşın, kısa süre içinde size geri döneceğiz.</p>{m}</div>
  <div class="card card-pad fu">{contact_form()}</div></div></div></section>'''

PLACE = '<div class="ph"><span>Görsel eklenecek</span></div>'
def logo_ph(n, label='Logo'):
    return ''.join(f'<div class="logo-ph">{label} {i+1:02d}</div>' for i in range(n))

# ------------------------------------------------------------------ SAYFALAR
def home():
    stats = [('target','99','%','','Proje Başarısı'),('users','60','','+','Çalışan'),('globe','200','','','Dünya Çapında Müşteri'),('clock','2004','','','Kuruluş'),('pipe','3000','','+','Ürün Çeşidi')]
    st = ''.join(f'<div class="stat fu">{ic(i)}<div class="n" data-to="{n}" data-pre="{pre}" data-suf="{suf}">{pre}{n}{suf}</div><div class="l">{l}</div></div>' for i, n, pre, suf, l in stats)
    svcs = [('warehouse','Toptan Tedarik','Yapı market, hırdavat ve inşaat firmalarına geniş stoktan toptan boru ve tesisat tedariği.'),
            ('factory','Yerinde Üretim','Kendi üretim tesisimizde PVC, HDPE-LDPE, U-PVC ve PPRC ürünleri üretiyoruz.'),
            ('target','Proje ve Keşif Desteği','Ürün seçimi ve ihtiyaç planlaması için teknik yönlendirme.'),
            ('drip','Tarımsal Sulama Çözümleri','Damla sulama hatları ve aksamlarıyla verimli sulama sistemleri.'),
            ('sprinkler','Peyzaj ve Otomatik Sulama','Bahçe ve peyzaj alanları için yağmurlama ve otomatik sulama ürünleri.'),
            ('truck','Lojistik ve Dağıtım','KKTC geneline planlı sevkiyat ve dağıtım hizmeti.')]
    sv = ''.join(f'<div class="card svc fu"><div class="ic-box">{ic(i)}</div><h4>{t}</h4><p>{d}</p></div>' for i, t, d in svcs)
    posts = [('Haberler','46. Yapı Fuarı – Turkeybuild İstanbul’a katıldık','SBC Boru olarak 46. Yapı Fuarı – Turkeybuild İstanbul’a katıldı.'),
             ('Rehber','PPRC boru nedir, nerelerde kullanılır?','Yer tutucu içerik — yazı taslağı eklenecek.'),
             ('Rehber','Tarımsal sulamada damla sulama borusu seçimi','Yer tutucu içerik — yazı taslağı eklenecek.')]
    po = ''.join(f'<a class="card post fu" href="blog-detay.html"><div class="ph">Görsel eklenecek</div><div class="bd"><div class="meta"><span class="tag">{c}</span></div><h4>{t}</h4><p class="small">{d}</p></div></a>' for c, t, d in posts)
    gal = ['hero-tesis.jpg','hdpe-rulo.jpg','bina.jpg','tarimsal-sulama.jpg','alt-yapi.jpg','tabela.jpg','bahce-peyzaj.jpg','pvc.jpg']
    ga = ''.join(f'<a href="{IMG}{g}" data-lb class="fu"><img src="{IMG}{g}" alt="Şirketimizden görüntü" loading="lazy"></a>' for g in gal)
    certs = ''.join(f'<div class="cert fu">{ic("badge")}Belge adı<br>yer tutucu</div>' for _ in range(3))
    brands = ''.join(f'<div class="logo-ph">Marka {i+1:02d}</div>' for i in range(8))
    refs = ''.join(f'<div class="logo-ph">Referans {i+1:02d}</div>' for i in range(12))
    return f'''
<section class="hero"><div class="hero-bg" style="background-image:url({IMG}hero-tesis.jpg)"></div>
  <div class="wrap"><h1 class="fu">Suyun Aktığı Her Yerdeyiz…</h1>
  <p class="lead fu">Uzun ömürlü ürünler üretiyor, KKTC’nin dört bir yanına ulaştırıyoruz.</p>
  <div class="btns fu"><a class="btn btn-primary" href="urunler.html">Ürünleri İncele {ic('arrow')}</a><a class="btn btn-ghost" href="katalog.html">{ic('download')}Katalog İndir</a></div></div>
  {flow(grad='fw')}
  <div class="hero-strip"><div class="wrap"><ul>
    <li>{ic('clock')}<span><b>2004’ten beri</b>sektörde</span></li><li>{ic('pipe')}<span><b>3000+</b>ürün çeşidi</span></li>
    <li>{ic('warehouse')}<span><b>4500 m²</b>depo</span></li><li>{ic('truck')}<span><b>KKTC geneli</b>teslimat</span></li></ul></div></div>
</section>

<section class="sec"><div class="blueprint"></div><div class="wrap"><div class="about">
  <div class="collage fu"><div class="rings"></div><img class="c1" src="{IMG}hero-tesis.jpg" alt="SBC Boru tesis" loading="lazy"><img class="c2" src="{IMG}bina.jpg" alt="SBC Boru ofis binası" loading="lazy"><img class="c3" src="{IMG}pvc.jpg" alt="Ürün istifi" loading="lazy"></div>
  <div class="fu"><span class="eyebrow">Hakkımızda</span><h2>Güvenilir altyapının üreticisi</h2>
    <p style="margin-top:20px">SBC Boru, 2004’te kuruldu. Üstyapı, altyapı tesisat boruları, tarımsal sulama ve bahçe peyzaj alanlarında faaliyet gösteren köklü bir firmayız. Yılların deneyimi ve geniş ürün yelpazemizle yapı marketlerine, hırdavatçılara ve inşaat şirketlerine ürün tedarik ediyor, sektördeki lider konumumuzu sürdürüyoruz.</p>
    <p>2015’te merkezimizi Gazimağusa’ya taşıdık. Satış ofisimiz, 1.500 m² çalışma alanımız ve 4.500 m² depomuzla, 60’ı aşkın çalışanımızla KKTC genelinde hizmet veriyoruz.</p>
    <div class="pts"><div class="pt"><div class="ic-box">{ic('warehouse')}</div>Üstyapı</div><div class="pt"><div class="ic-box">{ic('elbow')}</div>Altyapı</div><div class="pt"><div class="ic-box">{ic('drip')}</div>Tarımsal sulama &amp; peyzaj</div></div>
    <a class="btn btn-primary" href="hakkimizda.html">Daha fazlası {ic('arrow')}</a></div></div></div></section>

<section class="sec tint"><div class="wrap">{sec_head('Ürün Grupları','Ürün gruplarımız')}{group_cards()}
  <p class="note">Not: “BAHÇE PEYZAJ” orijinal sitede iki kez yer alıyor; tasarımda da aynen bırakıldı.</p></div></section>

<section class="sec dark" style="padding:0"><div class="blueprint"></div><div class="wrap"><div class="plant">
  <div class="tx fu"><span class="eyebrow">Yeni üretim tesisi</span><h2>Yeni üretim tesisimizle yerli üretimi büyütüyoruz</h2>
    <p>Yeni kurduğumuz üretim tesisi, en son büyük adımımız. Burada PVC atık su boruları, siyah hortum (HDPE-LDPE), mandallı borular, U-PVC temiz su boruları ve PPRC boruları üretiyoruz. Yerli üretimi artırarak sektördeki gücümüzü büyütüyoruz.</p>
    <div class="chips"><span class="chip">PVC atık su boruları</span><span class="chip">Siyah hortum (HDPE-LDPE)</span><span class="chip">Mandallı borular</span><span class="chip">U-PVC temiz su boruları</span><span class="chip">PPRC</span></div></div>
  <div class="ph fu"><img src="{IMG}hdpe-rulo.jpg" alt="HDPE boru rulolar" loading="lazy"></div></div></div></section>

<section class="sec tint" style="overflow:hidden"><div class="wrap">{sec_head('Şirket İstatistikleri','Rakamlar kendi adına konuşuyor.','%99 proje başarı oranı, 60’ı aşkın uzman çalışan ve dünya genelinde 200’ü aşkın müşteri.')}
  <div class="stats"><div class="rings"></div>{st}</div></div></section>

<section class="sec"><div class="wrap">{sec_head('Hizmetlerimiz','Ürünün ötesinde, çözüm ortağınız')}<div class="grid g3 keep1">{sv}</div>
  <p class="note">Hizmet metinleri taslaktır; kısa metinler onay bekliyor.</p></div></section>

<section class="sec tint"><div class="wrap">{sec_head('Kurumsal','Kalite belgelerimiz ve markalarımız')}
  <div class="certs">{certs}<div class="cta-side fu"><p>Kalite anlayışımızı belgelerimizle ortaya koyuyoruz.</p><a class="link-arrow" href="belgelerimiz.html">Belgelerimiz {ic('arrow')}</a><p class="note">Belge adları/yılları yer tutucu</p></div></div>
  <div style="margin-top:64px" class="marq"><div class="marq-t">{brands}</div></div>
  <div style="margin-top:20px;text-align:center"><a class="link-arrow" href="markalarimiz.html">Markalarımız {ic('arrow')}</a></div></div></section>

<section class="sec"><div class="wrap">{sec_head('Referanslar','Bizimle çalışanlar')}<div class="marq"><div class="marq-t">{refs}</div></div>
  <div style="margin-top:32px;text-align:center"><a class="link-arrow" href="referanslar.html">Tüm referanslar {ic('arrow')}</a></div></div></section>

<section class="sec tint"><div class="wrap">{sec_head('Galeri','Şirketimizden Görüntüler')}<div class="masonry">{ga}</div></div></section>

<section class="sec"><div class="wrap"><div class="sec-row">{sec_head('Haberler & Blog','Son yazılar')}<a class="link-arrow" href="haberler.html">Tümünü gör {ic('arrow')}</a></div>
  <div class="grid g3 keep1">{po}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="cta fu">{flow(grad='fw')}<div><h3 style="font-size:36px;line-height:44px">Ekibimize katılın</h3><p>Geleceği birlikte şekillendirelim. Şu an 4 açık pozisyonumuz var.</p></div>
  <a class="btn btn-white" href="insan-kaynaklari.html#basvuru">Şimdi Başvur {ic('arrow')}</a></div></div></section>

{contact_section()}'''

def hakkimizda():
    tl = [('2004','İskele’de kuruluş','SBC Boru, 2004’te İskele bölgesinde faaliyete geçti.'),
          ('2015','Gazimağusa’ya taşınma','Merkez Gazimağusa Büyük Sanayi Bölgesi’ne taşındı: 1500 m² çalışma alanı ve 4500 m² depo.'),
          ('Bugün','Yeni üretim tesisi','PVC atık su, HDPE-LDPE, mandallı, U-PVC temiz su ve PPRC boruları kendi tesisimizde üretiliyor.')]
    t = ''.join(f'<div class="tl fu"><div class="yr">{y}</div><h4>{a_}</h4><p class="small" style="margin-top:6px">{b}</p></div>' for y, a_, b in tl)
    pr = [('pipe','PVC Boru ve Aksamları'),('drip','Damlama Borusu ve Aksamları'),('sprinkler','Peyzaj ve Otomatik Sulama'),('coupling','PPRC Boru ve Aksamları'),('filter','Gübre Tankları ve Filtreler'),('valve','Galvaniz Vana ve Aksamları')]
    p6 = ''.join(f'<div class="card card-pad fu" style="display:flex;gap:18px;align-items:center"><div class="ic-box">{ic(i)}</div><h4>{n}</h4></div>' for i, n in pr)
    return head('Hakkımızda','Hakkımızda','bina.jpg' if False else 'hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap"><div class="two-col"><div class="fu"><span class="eyebrow">Biz Kimiz?</span><h2>2004’te İskele’de başladık, bugün KKTC genelinde hizmet veriyoruz.</h2></div>
<div class="fu"><p>SBC Boru, 2004’te kuruldu. Üstyapı, altyapı tesisat boruları, tarımsal sulama ve bahçe peyzaj alanlarında faaliyet gösteren köklü bir firmayız. Yılların deneyimi ve geniş ürün yelpazemizle yapı marketlerine, hırdavatçılara ve inşaat şirketlerine ürün tedarik ediyor, sektördeki lider konumumuzu sürdürüyoruz.</p><br>
<p>2015’te merkezimizi Gazimağusa’ya taşıdık. Satış ofisimiz, 1.500 m² çalışma alanımız ve 4.500 m² depomuzla, 60’ı aşkın çalışanımızla KKTC genelinde hizmet veriyoruz.</p>
<span class="note">Doğrulanacak: orijinal sitede Hakkımızda’da “70’i aşkın”, ana sayfada “60’ı aşkın” yazıyor; tasarımda 60+ kullanıldı.</span></div></div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Yolculuğumuz','Zaman çizgisi')}<div class="timeline">{t}</div></div></section>
<section class="sec"><div class="wrap"><div class="grid g2 keep1">
<div class="card mv fu"><div class="ic-box">{ic('target')}</div><h3>Misyonumuz</h3><p style="margin-top:14px">Çevre dostu bir bakış açısıyla su tesisatı, tarımsal sulama, üstyapı ve altyapı alanlarında müşterilerimize güvenilir ve yüksek kaliteli hizmet sunmayı, ihtiyaçlarını karşılamayı hedefliyoruz. Değişen piyasa koşullarını izleyerek ürün portföyümüzü sürekli geliştiriyor, teknolojik gelişmelere uyum sağlayarak büyüyor ve yeni pazarlara açılıyoruz.</p></div>
<div class="card mv fu"><div class="ic-box">{ic('eye')}</div><h3>Vizyonumuz</h3><p style="margin-top:14px">Ekonomik kalkınmaya katkı sağlayarak istihdamı artırmak, çalışanlarımızın yaşam standardını yükseltmek ve iş ortaklarımıza uygun fiyatla yüksek kaliteli ürünler sunarak onları rekabette güçlü kılmak.</p></div></div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Ürün Çeşitliliği','3000’in üzerinde ürün çeşidi')}<div class="grid g3 keep1">{p6}</div></div></section>
<section class="sec dark" style="padding:0"><div class="blueprint"></div><div class="wrap"><div class="plant"><div class="tx fu"><span class="eyebrow">Yenilikçi Üretim Tesisi</span><h2>Yerli üretimi büyütüyoruz</h2>
<p>Yeni kurduğumuz üretim tesisi, en son büyük adımımız. Burada PVC atık su boruları, siyah hortum (HDPE-LDPE), mandallı borular, U-PVC temiz su boruları ve PPRC boruları üretiyoruz. Yerli üretimi artırarak sektördeki gücümüzü büyütüyoruz.</p></div>
<div class="ph fu"><img src="{IMG}hdpe-boru.jpg" alt="HDPE boru" loading="lazy"></div></div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('İstatistiksel Başarılar','Rakamlarla SBC Boru','%99 proje başarı oranı, 60’ı aşkın uzman çalışan ve dünya genelinde 200’ü aşkın müşteri.')}
<div class="stats" style="grid-template-columns:repeat(3,1fr)">
<div class="stat fu">{ic('target')}<div class="n" data-to="99" data-pre="%">%99</div><div class="l">Proje Başarısı</div></div><div class="stat fu">{ic('users')}<div class="n" data-to="60" data-suf="+">60+</div><div class="l">Çalışan</div></div><div class="stat fu">{ic('globe')}<div class="n" data-to="200">200</div><div class="l">Dünya Çapında Müşteri</div></div></div></div></section>
{contact_section()}'''

def person(role, n=0):
    return f'''<div class="card person fu"><div class="pt">{ic('user')}Görsel eklenecek</div><div class="bd"><h4>Ad Soyad</h4><div class="role">{role}</div>
<a href="#" aria-label="LinkedIn" style="display:inline-flex;margin-top:10px;color:var(--ink)">{ic('linkedin','md')}</a></div></div>'''

def yonetim():
    mem = ''.join(person(r) for r in ['Yönetim Kurulu Üyesi','Yönetim Kurulu Üyesi','Genel Müdür','Üretim Müdürü','Satış ve Pazarlama Müdürü','Finans Müdürü'])
    return head('Yönetim Kurulu','Yönetim Kurulu','alt-yapi.jpg') + f'''
<section class="sec"><div class="wrap">{sec_head('Yönetim Kurulu','Güvenilir altyapıyı birlikte kuruyoruz','Yönetim kurulumuz, SBC Boru’nun üretimden dağıtıma tüm süreçlerini sürdürülebilir ve kaliteli biçimde yönetir. Kişi adları ve fotoğrafları yer tutucudur.')}
<div class="card chair fu"><div class="person" style="display:contents"><div class="pt" style="aspect-ratio:auto;min-height:480px;background:linear-gradient(160deg,#E6ECF6,#D7E0EE);display:grid;place-items:center;color:var(--mute);font-weight:700;gap:10px;align-content:center;text-align:center">{ic('user','lg')}Portre — görsel eklenecek</div></div>
<div class="bd"><span class="eyebrow" style="margin:0">Yönetim Kurulu Başkanı</span><h2>Ad Soyad</h2><blockquote>Yer tutucu mesaj: Başkanın kısa iletisi buraya eklenecek. İki cümlelik bir kurumsal mesaj/alıntı.</blockquote></div></div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Ekip','Yönetim kurulu üyeleri ve üst yönetim')}<div class="grid g3 keep1" style="grid-template-columns:repeat(3,1fr)">{mem}</div></div></section>
<section class="sec"><div class="wrap">{sec_head('Organizasyon','Organizasyon şeması','Basit yer tutucu şema; gerçek yapı eklenecek.',True)}
<div class="org fu"><div class="node top">Yönetim Kurulu</div><div class="ln"></div><div class="node">Genel Müdür</div><div class="ln"></div>
<div class="row"><div class="node">Üretim</div><div class="node">Satış &amp; Pazarlama</div><div class="node">Depo &amp; Lojistik</div><div class="node">Finans</div><div class="node">İnsan Kaynakları</div></div></div></div></section>
{contact_section()}'''

def markalar():
    cells = ''.join(f'<button class="logo-ph" style="cursor:pointer" data-modal="brandm" data-title="Marka {i+1:02d}">Marka {i+1:02d}</button>' for i in range(12))
    return head('Markalarımız','Markalarımız','hdpe-rulo.jpg') + f'''
<section class="sec"><div class="wrap">{sec_head('Markalarımız','Birlikte çalıştığımız markalar','Bir markaya tıklayarak açıklamasını görüntüleyin. Logolar yer tutucudur.')}
<div class="logo-wall" style="grid-template-columns:repeat(4,1fr)">{cells}</div></div></section>
<div class="modal" id="brandm"><div class="box"><button class="x-btn x" aria-label="Kapat">{ic('close','sm')}</button><div class="logo-ph" style="width:200px;margin-bottom:20px">Logo</div><h3 data-mt>Marka</h3><p style="margin-top:12px">Marka açıklaması buraya eklenecek (yer tutucu içerik).</p></div></div>
{contact_section()}'''

def tanitim():
    return head('Bizi Tanıyın','Bizi Tanıyın','bina.jpg' if False else 'hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap"><div class="grid g2 keep1">
<div class="card card-pad fu"><div class="ic-box" style="margin-bottom:20px">{ic('doc')}</div><h3>Bizi Tanıyın (Türkçe)</h3><p style="margin:14px 0 28px">Yüksek kaliteli, yenilikçi plastik çözümler üreten bir fabrikayız. Ürünlerimizle ve hizmetlerimizle tanışın.</p>
<div class="cat-cover" style="aspect-ratio:16/10;max-width:none;margin-bottom:28px"><img src="{IMG}logo-beyaz.png" alt=""><h3 style="font-size:28px;line-height:34px">Şirket Sunumu — TR<br><small style="font-size:14px;font-weight:600;opacity:.8">PDF kapağı yer tutucu</small></h3></div>
<button class="btn btn-primary" data-modal="viewer">Sunumu Görüntüle {ic('arrow')}</button></div>
<div class="card card-pad fu"><div class="ic-box" style="margin-bottom:20px">{ic('globe')}</div><h3>Bizi Tanıyın (English)</h3><p style="margin:14px 0 28px">We specialize in creating high-quality, innovative plastic solutions tailored to your needs. Experience exceptional products and service with us.</p>
<div class="cat-cover" style="aspect-ratio:16/10;max-width:none;margin-bottom:28px"><img src="{IMG}logo-beyaz.png" alt=""><h3 style="font-size:28px;line-height:34px">Company Presentation — EN<br><small style="font-size:14px;font-weight:600;opacity:.8">PDF cover placeholder</small></h3></div>
<button class="btn btn-primary" data-modal="viewer">See the Presentation {ic('arrow')}</button></div></div></div></section>
<div class="modal" id="viewer"><div style="position:relative;width:100%;display:grid;place-items:center"><button class="x-btn x" style="position:absolute;top:-52px;right:0" aria-label="Kapat">{ic('close','sm')}</button><div class="viewer">Tam ekran sunum görüntüleyici — PDF eklenecek</div></div></div>
{contact_section()}'''

def urunler():
    side = ''.join('<li><a href="#"' + (' class="on"' if k == 0 else '') + f'>{n}<small>(—)</small></a></li>' for k, (n, _, _) in enumerate(GROUPS))
    imgs = [g[2] for g in GROUPS]
    def prod(k):
        im = imgs[k % len(imgs)]
        return f'''<div class="card prod fu"><div class="ph"><img src="{IMG}{im}" alt="" loading="lazy"></div><div class="bd"><div class="code">SBC-0000 · kod yer tutucu</div><h4>Ürün adı (yer tutucu)</h4>
<div class="spec"><span>Çap: —</span><span>Basınç: —</span></div><button class="btn btn-secondary sm" data-add="p{k}" data-name="Ürün adı (yer tutucu) {k+1}" data-img="{IMG}{im}">{ic('plus')}Teklif Listesine Ekle</button></div></div>'''
    ps = ''.join(prod(k) for k in range(9))
    return head('Ürünler','Ürünler','alt-yapi.jpg') + f'''
<section class="sec"><div class="wrap"><div class="shop">
<aside class="card side"><h4>Kategoriler</h4><ul>{side}</ul></aside>
<div><div class="tools"><div class="search">{ic('search')}<input placeholder="Ürün ara…" aria-label="Ürün ara"></div>
<select class="sel" aria-label="Sırala"><option>Sırala</option><option>Artan Fiyat</option><option>Azalan Fiyat</option></select>
<button class="btn btn-secondary sm filter-btn" data-toggle=".side">{ic('menu')}Kategoriler</button></div>
<div class="grid g3 keep1" style="grid-template-columns:repeat(3,1fr)">{ps}</div>
<p class="small" style="margin-top:32px;text-align:center">Daha fazla ürün görüntüleyebilmek için sol menüden kategorilere tıklayabilirsiniz.</p>
<h4 style="margin:64px 0 16px">Yükleniyor durumu</h4><div class="grid g3" style="grid-template-columns:repeat(3,1fr)">{''.join('<div class="card"><div class="skel" style="aspect-ratio:1;border-radius:0"></div><div style="padding:20px;display:grid;gap:10px"><div class="skel" style="height:14px;width:40%"></div><div class="skel" style="height:22px"></div><div class="skel" style="height:44px"></div></div></div>' for _ in range(3))}</div>
<h4 style="margin:48px 0 16px">Boş durum</h4><div class="empty">{ic('search')}<h4>Sonuç bulunamadı</h4><p>Aramanızla eşleşen ürün yok. Farklı bir anahtar kelime veya kategori deneyin.</p></div></div></div></div></section>
{contact_section(False)}'''

def urun_detay():
    return head('Ürün adı (yer tutucu)','<a href="urunler.html">Ürünler</a> <span>›</span> Ürün detayı','alt-yapi.jpg') + f'''
<section class="sec"><div class="wrap"><div class="two-col" style="align-items:start">
<div class="gal fu"><div class="th"><div class="on"><img src="{IMG}hdpe-boru.jpg" alt=""></div><div><img src="{IMG}pvc.jpg" alt=""></div><div><img src="{IMG}hdpe-rulo.jpg" alt=""></div></div><div class="big"><img src="{IMG}hdpe-boru.jpg" alt="Ürün görseli"></div></div>
<div class="fu"><span class="tag">Kategori (yer tutucu)</span><h2 style="margin:14px 0 8px">Ürün adı (yer tutucu)</h2><div class="small" style="margin-bottom:20px">Kod: SBC-0000</div>
<p>Ürün açıklaması buraya eklenecek. Gerçek teknik değerler ve ürün adları onay sonrası girilecek.</p>
<table class="spec-table" style="margin:28px 0"><tr><th>Çap</th><td>—</td></tr><tr><th>SDR / PN</th><td>—</td></tr><tr><th>Uzunluk</th><td>—</td></tr><tr><th>Standart</th><td>—</td></tr></table>
<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center"><div class="qty"><button aria-label="Azalt">−</button><input value="1" aria-label="Adet"><button aria-label="Arttır">+</button></div>
<button class="btn btn-primary" data-add="detay" data-name="Ürün adı (yer tutucu)" data-img="{IMG}hdpe-boru.jpg">{ic('plus')}Teklif Listesine Ekle</button><a class="btn btn-secondary" href="#">{ic('download')}Teknik dosya</a></div></div></div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Uygulama Alanları','Nerelerde kullanılır?')}<div class="grid g4" style="grid-template-columns:repeat(4,1fr)">
{''.join(f'<div class="card card-pad fu" style="display:grid;gap:14px"><div class="ic-box">{ic(i)}</div><h4>{t}</h4></div>' for i, t in [('warehouse','Üstyapı'),('elbow','Altyapı'),('drip','Tarımsal sulama'),('sprinkler','Peyzaj')])}</div></div></section>
<section class="sec"><div class="wrap">{sec_head('Benzer Ürünler','Bunlar da ilginizi çekebilir')}<div class="grid g3 keep1" style="grid-template-columns:repeat(3,1fr)">{''.join(f'<a class="card pg" href="urunler.html"><div class="ph"><img src="{IMG}{im}" alt=""></div><div class="bd"><span>Ürün adı (yer tutucu)</span><span class="go">{ic("arrow")}</span></div></a>' for im in ['pvc.jpg','temiz-su.jpg','tarimsal-sulama.jpg'])}</div></div></section>'''

def teklif():
    return head('Teklif Listesi','Teklif Listesi','hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap"><div class="contact-grid" style="grid-template-columns:7fr 5fr;align-items:start">
<div><h3 style="margin-bottom:8px">Seçtiğiniz ürünler</h3><div id="qlist"></div>
<div class="fld" style="margin-top:24px"><label for="note">Not</label><textarea id="note" placeholder="Adet, ölçü veya teslimat notlarınız…"></textarea></div></div>
<div class="card sum"><h4 style="margin-bottom:16px">İletişim bilgileriniz</h4><form class="form" style="grid-template-columns:1fr" data-demo="tesekkurler.html" novalidate>{field('İsim Soyisim','ad')}{field('Telefon','tel','tel')}{field('E-Posta','mail','email')}
<button class="btn btn-primary" type="submit">Teklif İste {ic('arrow')}</button><a class="btn btn-secondary" href="{WA}" style="background:#fff">{ic('whatsapp')}WhatsApp ile iste</a><a class="btn btn-secondary" href="mailto:{MAIL}">{ic('mail')}E-posta ile iste</a></form></div></div></div></section>'''

def katalog():
    return head('Katalog','Katalog','pvc.jpg' if False else 'alt-yapi.jpg') + f'''
<section class="sec"><div class="wrap"><div class="two-col"><div class="fu"><div class="cat-cover"><img src="{IMG}logo-beyaz.png" alt="SBC Boru"><div><h3>Ürün Kataloğu</h3><p style="color:#DDF1FB;margin-top:6px">3000’in üzerinde ürün çeşidi</p></div></div></div>
<div class="fu"><span class="eyebrow">Katalog</span><h2>Tüm ürün gruplarımız tek dosyada</h2><p style="margin:16px 0 28px">PDF kataloğumuzu indirerek ürün gruplarımızı ve teknik bilgileri inceleyebilirsiniz.</p><a class="btn btn-primary" href="#">{ic('download')}Katalog İndir (PDF)</a><p class="note">PDF dosyası eklenecek</p></div></div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Önizleme','Katalog sayfaları')}<div class="pages">{''.join(f'<div class="fu">Sayfa {i}</div>' for i in range(1,4))}</div></div></section>'''

def referanslar():
    cases = ''.join(f'<div class="card case fu"><div class="ph">Proje fotoğrafı — eklenecek</div><div class="bd"><h4>Proje adı {i} (yer tutucu)</h4><div class="kv"><span>Bölge: —</span><span>Ürün grubu: —</span></div></div></div>' for i in (1,2,3))
    return head('Referanslar','Referanslar','hdpe-rulo.jpg') + f'''
<section class="sec"><div class="wrap">{sec_head('Referanslar','Bize güvenen firmalar','Logolar yer tutucudur.')}<div class="logo-wall" style="grid-template-columns:repeat(6,1fr)" id="refwall">{logo_ph(24,'Referans')}</div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Vaka çalışmaları','Öne çıkan projeler')}<div class="grid g3 keep1" style="grid-template-columns:repeat(3,1fr)">{cases}</div></div></section>
{contact_section()}'''

def belgeler():
    cs = ''.join(f'<button class="cert fu" style="cursor:pointer" data-modal="certm" data-title="Belge adı {i}">{ic("badge")}Belge adı {i}<br><span style="font-weight:600">Yıl — yer tutucu</span></button>' for i in range(1,9))
    return head('Belgelerimiz','Belgelerimiz','pvc.jpg' if False else 'alt-yapi.jpg') + f'''
<section class="sec"><div class="wrap"><div class="sec-head fu"><span class="eyebrow">Belgelerimiz</span><h2>Kalite anlayışımızın kanıtı</h2><p>SBC Boru olarak kaliteyi ve müşteri memnuniyetini her zaman ön planda tutuyoruz. Sahip olduğumuz kalite belgelerini aşağıda inceleyebilirsiniz.</p></div>
<div class="grid g4" style="grid-template-columns:repeat(4,1fr)">{cs}</div><p class="note">Gerçek belge adları ve yılları eklenecek; uydurma belge yazılmadı.</p></div></section>
<div class="modal" id="certm"><div class="box" style="max-width:480px"><button class="x-btn x" aria-label="Kapat">{ic('close','sm')}</button><h4 data-mt style="margin-bottom:16px">Belge</h4><div class="cert" style="aspect-ratio:3/4">{ic('doc')}A4 önizleme — eklenecek</div></div></div>'''

def ik():
    aud = ''.join(f'<div class="card card-pad fu" style="display:flex;gap:16px;align-items:center"><div class="ic-box">{ic(i)}</div><h4>{t}</h4></div>' for i, t in [('grad','Üniversite mezunları'),('factory','Meslek Lisesi mezunları'),('user','Yeni mezunlar'),('users','Tecrübeli çalışanlar')])
    jobs = ''.join(f'<li>{j}<a class="link-arrow" href="#basvuru">Başvur {ic("arrow")}</a></li>' for j in ['Genel Başvuru','Dağıtım Personeli','Satış Destek Personeli','Stajyer'])
    steps = ''.join(f'<div class="card s fu"><h4>{t}</h4></div>' for t in ['Oryantasyon','Fabrika ve ofis tanıtımı','Fuar ve kongre ziyaretleri'])
    ev = ''.join(f'<div class="card ev fu"><div class="date">{d}</div><h4>{t}</h4></div>' for d, t in [('3 Şubat 2023','Depo & Stok Yönetimi Eğitimi'),('23–26 Kasım 2022','Growtech Fuarı')])
    act = ''.join(f'<div class="cert" style="aspect-ratio:4/3">Aktivite fotoğrafı<br>eklenecek</div>' for _ in range(4))
    return head('İnsan Kaynakları','İnsan Kaynakları','hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap"><div class="two-col"><div class="fu"><span class="eyebrow">İ.K</span><h2>Geleceği birlikte şekillendirmek için ekibimize katılın.</h2></div>
<div class="fu"><h4 style="margin-bottom:10px">SBC’li Olmak</h4><p>Gazimağusa Büyük Sanayi Bölgesi’ndeki firmamız, 3.000’den fazla ürün çeşidiyle yapı marketlerine, hırdavatçılara ve inşaat şirketlerine ürün tedarik ediyor. En değerli sermayemiz insan kaynağımız; bu yüzden çalışma arkadaşlarımıza mutlu olacakları, mesleki ve kişisel olarak gelişebilecekleri bir ortam sunmayı birinci hedefimiz olarak görüyoruz.</p>
<span class="note">Doğrulanacak: İK sayfasında “dört alan”, diğer yerlerde “üç alan” yazıyor; tasarımda üç alan kullanıldı.</span></div></div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('İş Başvurusu','Kimler başvurabilir?')}<div class="grid g2 keep1" style="grid-template-columns:repeat(4,1fr)">{aud}</div>
<h3 style="margin:56px 0 20px">Açık pozisyonlar</h3><ul class="jobs">{jobs}</ul></div></section>
<section class="sec"><div class="wrap">{sec_head('Eğitim','Gelişim her gün devam eder')}<div class="steps">{steps}</div><div class="grid g2 keep1" style="margin-top:24px">{ev}</div></div></section>
<section class="sec tint"><div class="wrap"><div class="two-col"><div class="fu"><span class="eyebrow">Kariyer</span><h2>Terfi değerlendirmesi</h2><p style="margin-top:16px">Çalışanlarımızın gelişimi düzenli olarak değerlendirilir ve terfi süreçleri şeffaf biçimde yürütülür.</p></div><div class="card card-pad fu" style="display:flex;gap:18px;align-items:center"><div class="ic-box">{ic('target')}</div><h4>Performansa dayalı kariyer yolu</h4></div></div></div></section>
<section class="sec"><div class="wrap">{sec_head('Aktiviteler','Ekibimizden kareler')}<div class="grid g4">{act}</div></div></section>
<section class="sec tint" id="basvuru"><div class="wrap"><div class="two-col" style="align-items:start"><div class="fu"><span class="eyebrow">Şimdi Başvur</span><h2>Başvuru formu</h2><p style="margin-top:16px">Bilgilerinizi ve CV’nizi paylaşın, size dönüş yapalım.</p></div>
<form class="form card card-pad fu" data-demo="tesekkurler.html" novalidate>
<div class="fld full"><label for="poz">Başvuru Pozisyonu*</label><select id="poz" required style="width:100%;height:56px;border:1px solid var(--line);border-radius:10px;padding:0 16px;background:#fff"><option value="">Seçiniz</option><option>Genel Başvuru</option><option>Dağıtım Personeli</option><option>Satış Destek Personeli</option><option>Stajyer</option></select><div class="em">Bu alan zorunludur.</div></div>
{field('İsim','ad')}{field('Soyisim','soyad')}
<div class="fld full"><label for="uy">Uyruk*</label><select id="uy" required style="width:100%;height:56px;border:1px solid var(--line);border-radius:10px;padding:0 16px;background:#fff"><option value="">Seçiniz</option><option>T.C.</option><option>K.K.T.C.</option><option>Diğer</option></select><div class="em">Bu alan zorunludur.</div></div>
{field('Telefon','tel','tel',False)}{field('E-posta','mail','email',False)}
<div class="full drop-zone">{ic('upload','lg')}<b style="color:var(--ink)">CV’nizi sürükleyip bırakın</b><span class="small">veya dosya seçin (PDF, DOC)</span></div>
<label class="chk full"><input type="checkbox" required><span>Kişisel verilerimin KVKK kapsamında işlenmesini kabul ediyorum.</span></label>
<div class="full"><button class="btn btn-primary" type="submit">Gönder {ic('arrow')}</button></div></form></div></div></section>'''

def haberler():
    po = ''.join(f'<a class="card post fu" href="blog-detay.html"><div class="ph">Görsel eklenecek</div><div class="bd"><div class="meta"><span class="tag">{c}</span><span>Yer tutucu tarih</span></div><h4>{t}</h4></div></a>' for c, t in [
        ('Rehber','PPRC boru nedir, nerelerde kullanılır?'),('Rehber','Tarımsal sulamada damla sulama borusu seçimi'),('Rehber','PVC atık su borusu ölçü ve basınç sınıfları rehberi'),('Rehber','KKTC’de yapı için doğru tesisat borusu seçimi'),('Sektör','Yazı başlığı eklenecek'),('Fuarlar','Yazı başlığı eklenecek')])
    return head('Haberler / Blog','Haberler / Blog','hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap"><div class="tools"><div class="filters"><a class="on" href="#">Tümü</a><a href="#">Haberler</a><a href="#">Fuarlar</a><a href="#">Rehber</a><a href="#">Sektör</a></div><div class="search" style="max-width:320px;margin-left:auto">{ic('search')}<input placeholder="Yazılarda ara…" aria-label="Ara"></div></div>
<a class="card feat fu" href="blog-detay.html" style="margin-bottom:24px"><div class="ph" style="background:var(--tint);display:grid;place-items:center;color:var(--mute);font-weight:700">Kapak görseli — eklenecek</div><div class="bd"><div class="meta"><span class="tag">Haberler</span><span>TÜYAP · 2024</span></div><h3>SBC Boru olarak 46. Yapı Fuarı – Turkeybuild İstanbul’a katıldı</h3><p>KTSO ve Sanayi Dairesi katkısıyla Kıbrıs’tan katılan 5 sanayici firmadan biri olduk.</p><span class="link-arrow">Devamını oku {ic('arrow')}</span></div></a>
<div class="grid g3 keep1" style="grid-template-columns:repeat(3,1fr)">{po}</div></div></section>'''

def blog():
    return head('Blog yazısı','<a href="haberler.html">Haberler</a> <span>›</span> Yazı','hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap"><article class="article"><div class="meta"><span class="tag">Haberler</span><span>TÜYAP · 2024</span><span>3 dk okuma (yer tutucu)</span></div>
<h2>SBC Boru olarak 46. Yapı Fuarı – Turkeybuild İstanbul’a katıldı</h2>
<div class="card" style="aspect-ratio:16/9;display:grid;place-items:center;margin:32px 0;color:var(--mute);font-weight:700;background:var(--tint)">Kapak görseli — eklenecek</div>
<p class="lead">SBC Boru, TÜYAP’ta 2024 yılında düzenlenen 46. Yapı Fuarı – Turkeybuild İstanbul’a katıldı.</p>
<p>KTSO ve Sanayi Dairesi katkısıyla Kıbrıs’tan katılan 5 sanayici firmadan biri olarak, ürün gruplarımızı sektör profesyonellerine tanıttık.</p>
<h3>Alt başlık (yer tutucu)</h3><p>Yer tutucu içerik: yazının devamı onay sonrası eklenecektir.</p>
<div class="share" style="margin-top:32px"><b style="color:var(--ink)">Paylaş</b><a class="x-btn" href="#" aria-label="X">{ic('x','sm')}</a><a class="x-btn" href="#" aria-label="Facebook">{ic('facebook','sm')}</a><a class="x-btn" href="#" aria-label="LinkedIn">{ic('linkedin','sm')}</a></div></article></div></section>
<section class="sec tint"><div class="wrap">{sec_head('İlgili yazılar','Bunlar da ilginizi çekebilir')}<div class="grid g3 keep1" style="grid-template-columns:repeat(3,1fr)">{''.join(f'<a class="card post" href="blog-detay.html"><div class="ph">Görsel eklenecek</div><div class="bd"><div class="meta"><span class="tag">Rehber</span></div><h4>{t}</h4></div></a>' for t in ['PPRC boru nedir, nerelerde kullanılır?','Tarımsal sulamada damla sulama borusu seçimi','PVC atık su borusu ölçü ve basınç sınıfları rehberi'])}</div></div></section>'''

def iletisim():
    cards = ''.join(f'<div class="card info fu"><div class="ic-box">{ic(i)}</div><div><b>{t}</b>{v}</div></div>' for i, t, v in [
        ('pin','Adres',ADDR),('phone','Telefon',f'<a href="tel:+905338417880">{PHONE}</a>'),('whatsapp','WhatsApp',f'<a href="{WA}">{PHONE}</a>'),('mail','E-posta',f'<a href="mailto:{MAIL}">{MAIL}</a>'),('clock','Çalışma saatleri','Eklenecek (yer tutucu)')])
    return head('İletişim','İletişim','bina.jpg' if False else 'hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap"><div class="contact-grid"><div style="display:grid;gap:16px;align-content:start">{cards}</div>
<div class="card card-pad fu"><h3 style="margin-bottom:8px">Bizimle İletişime Geçin</h3><p style="margin-bottom:24px">Herhangi bir sorunuz var mı? İletişim formumuzdan bize ulaşın, kısa süre içinde size geri döneceğiz.</p>{contact_form()}</div></div></div></section>
<section style="padding:0 0 var(--sec)"><div class="wrap"><div class="mapcard" style="min-height:420px;margin:0"><div class="grid-bg"></div><div class="road" style="left:-5%;top:58%;width:110%;height:16px;transform:rotate(-8deg)"></div><div class="road" style="left:34%;top:-5%;width:12px;height:110%;transform:rotate(14deg)"></div>
<div class="pinwrap">{ic('pin')}<span class="lbl">Gazimağusa Büyük Sanayi Bölgesi</span></div><a class="btn btn-primary" href="{MAPS}">{ic('pin')}Yol Tarifi Al</a></div></div></section>'''

def hizmetler():
    svcs = [('warehouse','Toptan Tedarik','Yapı market, hırdavat ve inşaat firmalarına geniş stoktan toptan boru ve tesisat tedariği.'),
            ('factory','Yerinde Üretim','Kendi üretim tesisimizde PVC, HDPE-LDPE, U-PVC ve PPRC ürünleri üretiyoruz.'),
            ('target','Proje ve Keşif Desteği','Ürün seçimi ve ihtiyaç planlaması için teknik yönlendirme.'),
            ('drip','Tarımsal Sulama Çözümleri','Damla sulama hatları ve aksamlarıyla verimli sulama sistemleri.'),
            ('sprinkler','Peyzaj ve Otomatik Sulama','Bahçe ve peyzaj alanları için yağmurlama ve otomatik sulama ürünleri.'),
            ('truck','Lojistik ve Dağıtım','KKTC geneline planlı sevkiyat ve dağıtım hizmeti.')]
    sv = ''.join(f'<div class="card svc fu"><div class="ic-box">{ic(i)}</div><h4>{t}</h4><p>{d}</p></div>' for i, t, d in svcs)
    return head('Hizmetlerimiz','Hizmetler','alt-yapi.jpg') + f'''
<section class="sec"><div class="wrap">{sec_head('Hizmetlerimiz','Ürünün ötesinde, çözüm ortağınız','Metinler taslaktır; onay sonrası güncellenecek.')}<div class="grid g3 keep1">{sv}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="cta fu">{flow(grad='fw')}<div><h3 style="font-size:36px;line-height:44px">İhtiyacınız için teklif alın</h3><p>Ürünleri seçin, teklif listenizi oluşturun.</p></div><a class="btn btn-white" href="urunler.html">Ürünleri İncele {ic('arrow')}</a></div></div></section>
{contact_section()}'''

def err404():
    return f'''<section class="err404 sec"><div class="blueprint"></div><div class="wrap"><div class="big">404</div><h2>Aradığınız sayfa bulunamadı</h2><p style="margin:14px 0 28px">Sayfa taşınmış veya kaldırılmış olabilir.</p><a class="btn btn-primary" href="index.html">Ana Sayfaya Dön {ic('arrow')}</a></div></section>'''

def ok():
    return f'''<section class="err404 sec"><div class="blueprint"></div><div class="wrap"><div class="okmark">{ic('check')}</div><h2>Mesajınız gönderildi</h2><p style="margin:14px 0 28px">Teşekkür ederiz, kısa süre içinde size geri döneceğiz.</p><a class="btn btn-primary" href="index.html">Ana Sayfaya Dön {ic('arrow')}</a></div></section>'''

def stil():
    cols = [('Marka mavisi','#0096D4','Birincil, link, ikon vurgusu'),('Mavi koyu','#007BB0','Hover / pressed'),('Mavi derin','#0B4F7A','Hero overlay, CTA bitişi'),('Lacivert-gri','#343F52','Başlıklar'),
            ('Gövde metni','#60697B','Paragraf'),('Soluk metin','#959CA9','Yardımcı'),('Açık mavi zemin','#EDF2FC','Alternatif bölüm'),('Sayfa zemini','#FEFEFE','Ana zemin'),
            ('Çizgi','#E3E8F0','Kenarlık'),('Footer','#21262C','Footer / koyu bant'),('Başarı','#198754','Form'),('Hata','#DC3545','Form')]
    sw = ''.join(f'<div><i style="background:{h}"></i><span>{n}<small>{h} · {u}</small></span></div>' for n, h, u in cols)
    ics = ''.join(f'<div>{ic(k)}{k}</div>' for k in ICONS)
    ty = [('H1 64/72 · 700','h1','Suyun Aktığı Her Yerdeyiz'),('H2 44/52 · 700','h2','Güvenilir altyapının üreticisi'),('H3 28/36 · 700','h3','Yenilikçi üretim tesisi'),('H4 20/28 · 700','h4','Ürün grupları'),('Gövde 17/28 · 400','p','Uzun ömürlü ürünler üretiyor, KKTC’nin dört bir yanına ulaştırıyoruz.'),('Etiket 13/16 · 700','e','Ürün Grupları')]
    tr = ''.join(f'<div class="type-row"><code>{l}</code><{"span class=eyebrow style=margin:0" if t=="e" else t}>{x}</{"span" if t=="e" else t}></div>' for l, t, x in ty)
    return head('Stil Kılavuzu','Stil Kılavuzu','hero-tesis.jpg') + f'''
<section class="sec"><div class="wrap">{sec_head('Renkler','Renk sistemi','Yalnızca mavi + koyu lacivert-gri + beyaz. Gradient: hero fotoğraf overlay’i ve CTA bandı.')}<div class="sw">{sw}</div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Tipografi','Manrope')}<div class="card card-pad">{tr}</div></div></section>
<section class="sec"><div class="wrap">{sec_head('İkon seti','Özel ikon ailesi','1.75 px çizgi · 32 px grid · düz çizgi + tek mavi vurgu · yuvarlatılmış uç.')}<div class="icons">{ics}</div></div></section>
<section class="sec tint"><div class="wrap">{sec_head('Bileşenler','Buton, form, kart')}
<div class="gs-row"><a class="btn btn-primary" href="#">Birincil {ic('arrow')}</a><a class="btn btn-secondary" href="#">İkincil</a><span style="background:var(--dark);padding:12px;border-radius:12px;display:inline-flex"><a class="btn btn-ghost" href="#">Hayalet</a></span><a class="btn btn-primary sm" href="#">Küçük</a><a class="link-arrow" href="#">Bağlantı {ic('arrow')}</a></div>
<div class="grid g3 keep1" style="grid-template-columns:repeat(3,1fr);margin-top:32px"><div class="card card-pad"><h4>Kart</h4><p class="small" style="margin-top:8px">16 px köşe, 1 px kenar, hover’da üst 3 px mavi çizgi + gölge.</p></div>
<div class="card pg"><div class="ph"><img src="{IMG}pprc.jpg" alt=""><span class="badge">{ic('coupling')}</span></div><div class="bd"><span>PPRC GRUBU</span><span class="go">{ic('arrow')}</span></div></div>
<div class="card card-pad"><div class="fld"><label for="g1">Form alanı</label><input id="g1" placeholder="56 px · 10 radius"></div><div class="fld err" style="margin-top:14px"><label for="g2">Hata durumu</label><input id="g2" value="x"><div class="em">Bu alan zorunludur.</div></div></div></div></div></section>
<section class="sec"><div class="blueprint"></div><div class="wrap">{sec_head('İmza öğe','Akış çizgisi ve eş merkezli halka','Logo kavisinden türeyen 1.5 px akış çizgisi, boru kesitini anlatan halka ve %4 blueprint ızgarası.')}
<div class="card card-pad" style="position:relative;height:220px;overflow:hidden">{flow(grad='fg')}<div class="rings" style="width:200px;height:200px;right:60px;top:10px"></div></div>
<div class="grid" style="grid-template-columns:repeat(4,1fr);margin-top:24px"><div class="card card-pad"><b>Ölçüler</b><p class="small">1440 / içerik 1240 / 12 kolon / 24 boşluk · mobil 390 / kenar 20 · bölüm 120 (mobil 72)</p></div><div class="card card-pad"><b>Köşe</b><p class="small">kart 16 · buton 10 · input 10 · görsel 20</p></div><div class="card card-pad"><b>Gölge</b><p class="small">0 12 32 rgba(52,63,82,.08)</p></div><div class="card card-pad"><b>Hareket</b><p class="small">16 px fade-up 400 ms, sayaç, yavaş marquee, hafif paralaks.</p></div></div></div></section>'''

# ------------------------------------------------------------------ ÜRET
if __name__ == '__main__':
    page('index.html', 'Ana Sayfa', home(), 'home', True, 'Suyun Aktığı Her Yerdeyiz… SBC Boru — KKTC’nin en büyük boru üreticisi ve tedarikçisi.')
    page('hakkimizda.html', 'Hakkımızda', hakkimizda(), 'kurumsal')
    page('yonetim-kurulu.html', 'Yönetim Kurulu', yonetim(), 'kurumsal')
    page('markalarimiz.html', 'Markalarımız', markalar(), 'kurumsal')
    page('bizi-taniyin.html', 'Bizi Tanıyın', tanitim(), 'kurumsal')
    page('urunler.html', 'Ürünler', urunler(), 'urunler')
    page('urun-detay.html', 'Ürün Detayı', urun_detay(), 'urunler')
    page('teklif-listesi.html', 'Teklif Listesi', teklif(), '')
    page('katalog.html', 'Katalog', katalog(), '')
    page('referanslar.html', 'Referanslar', referanslar(), 'kurumsal')
    page('belgelerimiz.html', 'Belgelerimiz', belgeler(), 'kurumsal')
    page('insan-kaynaklari.html', 'İnsan Kaynakları', ik(), 'ik')
    page('haberler.html', 'Haberler / Blog', haberler(), 'haberler')
    page('blog-detay.html', 'Blog Yazısı', blog(), 'haberler')
    page('iletisim.html', 'İletişim', iletisim(), 'iletisim')
    page('hizmetler.html', 'Hizmetler', hizmetler(), 'hizmetler')
    page('404.html', '404', err404(), '')
    page('tesekkurler.html', 'Form gönderildi', ok(), '')
    page('stil-kilavuzu.html', 'Stil Kılavuzu', stil(), '')
    print('ok')
