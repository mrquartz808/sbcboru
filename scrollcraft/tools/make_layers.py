#!/usr/bin/env python3
"""Tesis fotoğrafını 3 düzleme ayırır: base (temizlenmiş), sign (tabela+direk), fg (ön plan). Koordinatlar 2304x1296."""
import sys, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter
SRC, OUT = sys.argv[1], sys.argv[2]
im = Image.open(SRC).convert('RGB'); W, H = im.size
assert (W, H) == (2304, 1296), im.size
rgb = np.asarray(im)

def poly_mask(polys, feather=1.6, grow=0):
    m = Image.new('L', (W*2, H*2), 0); d = ImageDraw.Draw(m)
    for p in polys: d.polygon([(x*2, y*2) for x, y in p], fill=255)
    m = m.resize((W, H), Image.LANCZOS)
    if grow: m = m.filter(ImageFilter.MaxFilter(grow*2+1))
    if feather: m = m.filter(ImageFilter.GaussianBlur(feather))
    return np.asarray(m).astype(np.float32)/255.0

# --- tabela düzlemi: pano + iki lamba kolu + direk
sign_polys = [
  [(1285,443),(1733,443),(1733,729),(1285,729)],
  [(1344,424),(1362,424),(1362,446),(1344,446)],
  [(1653,424),(1670,424),(1670,446),(1653,446)],
  [(1474,729),(1523,729),(1523,1296),(1474,1296)],
]
sign_a = poly_mask(sign_polys, feather=1.2)
# --- ön plan düzlemi: kontrplak sundurma + rulolar + gri boru istifi
fg_poly = [(0,1165),(350,1150),(870,1105),(905,1105),(960,1140),(1015,1145),(1210,1140),(1325,1212),(1398,1296),(0,1296)]
fg_a = poly_mask([fg_poly], feather=2.0)

# --- base: tabelayı ve ön planı kaldır
base = rgb.copy()
# ön plan bölgesini asfalt dokusuyla doldur (örnek yama: sol-orta yarda asfaltı)
patch = rgb[860:980, 80:560].copy()
patch = np.concatenate([patch, patch[:, ::-1]], axis=1)          # aynalayıp genişlet
patch = np.concatenate([patch, patch[::-1]], axis=0)
tile = cv2.resize(patch, (1500, 260), interpolation=cv2.INTER_CUBIC)
fill = np.zeros_like(rgb); 
for y0 in range(1080, H, 260):
    h = min(260, H-y0); fill[y0:y0+h, 0:1500] = tile[:h, :1500]
fill = cv2.GaussianBlur(fill, (0,0), 1.2)
fg_big = poly_mask([fg_poly], feather=6.0, grow=6)[..., None]
base = (base*(1-fg_big) + fill*fg_big).astype(np.uint8)
# tabela bölgesi: Telea ile doldur
sign_big = (poly_mask(sign_polys, feather=0, grow=7) > 0.5).astype(np.uint8)*255
base = cv2.inpaint(cv2.cvtColor(base, cv2.COLOR_RGB2BGR), sign_big, 9, cv2.INPAINT_TELEA)
base = cv2.cvtColor(base, cv2.COLOR_BGR2RGB)
rng = np.random.default_rng(3)
base = np.clip(base.astype(np.float32) + rng.normal(0, 1.4, base.shape), 0, 255).astype(np.uint8)

Image.fromarray(base).save(f'{OUT}/plate-base.jpg', quality=84, optimize=True, progressive=True)
for name, a in (('sign', sign_a), ('fg', fg_a)):
    rgba = np.dstack([rgb, (a*255).astype(np.uint8)])
    Image.fromarray(rgba, 'RGBA').save(f'{OUT}/plate-{name}.webp', quality=86, method=6)
im.save(f'{OUT}/plate-full.jpg', quality=84, optimize=True, progressive=True)
# kontrol: 3 düzlemi 30px kaydırıp kompozit
def comp(dy_sign, dy_fg):
    c = Image.fromarray(base).convert('RGBA')
    for name, dy in (('sign', dy_sign), ('fg', dy_fg)):
        l = Image.open(f'{OUT}/plate-{name}.webp').convert('RGBA')
        c.alpha_composite(l, (0, -dy)) if dy>=0 else c.alpha_composite(l, (0, -dy))
    return c.convert('RGB')
comp(0,0).resize((1152,648)).save(sys.argv[3]+'/chk0.png')
comp(40,90).resize((1152,648)).save(sys.argv[3]+'/chk1.png')
print('ok')
