import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# composite.py photo screen out "TL TR BR BL" bright [debug]
photo_p, screen_p, out_p, corners_s, bright_s = sys.argv[1:6]
debug = len(sys.argv) > 6 and sys.argv[6] == 'debug'
corners = [tuple(map(float, p.split(','))) for p in corners_s.split()]

photo = Image.open(photo_p).convert('RGB')
if debug:
    d = ImageDraw.Draw(photo); d.polygon(corners, outline=(255, 0, 0))
    for c in corners: d.ellipse([c[0]-6, c[1]-6, c[0]+6, c[1]+6], fill=(255, 0, 0))
    photo.save(out_p); sys.exit()

bright = float(bright_s)
screen = Image.open(screen_p).convert('RGB')
sw, sh = screen.size

# perspective warp: output(photo)->input(screen)
src = [(0, 0), (sw, 0), (sw, sh), (0, sh)]
A, B = [], []
for (x, y), (u, v) in zip(corners, src):
    A.append([x, y, 1, 0, 0, 0, -u*x, -u*y]); B.append(u)
    A.append([0, 0, 0, x, y, 1, -v*x, -v*y]); B.append(v)
coeffs = np.linalg.solve(np.array(A), np.array(B))
warped = screen.transform(photo.size, Image.PERSPECTIVE, coeffs.tolist(), Image.BICUBIC)
warped = warped.filter(ImageFilter.GaussianBlur(0.9))  # match photo softness

mask = Image.new('L', photo.size, 0)
ImageDraw.Draw(mask).polygon(corners, fill=255)
maskarr = np.array(mask) > 128
feather = np.array(mask.filter(ImageFilter.GaussianBlur(1.8))).astype(float) / 255.0

ph = np.array(photo).astype(float)
wp = np.array(warped).astype(float)

# --- KEY: transfer the REAL screen lighting from the photo onto the graphic ---
# the blank screen already carries the window reflection, glass sheen, brightness
# falloff and bezel shadow. Use its luminance, relative to the screen's mean, as a
# multiplicative light map so the graphic inherits the photo's actual light.
gray = (0.299*ph[..., 0] + 0.587*ph[..., 1] + 0.114*ph[..., 2])
m = gray[maskarr].mean()
lightmap = np.clip(gray / max(m, 1.0), 0.72, 1.18)
lightmap = np.array(Image.fromarray((lightmap*128).astype('uint8')).filter(
    ImageFilter.GaussianBlur(2.0))).astype(float) / 128.0

wp *= bright                      # sit below the scene's brightest point
wp *= lightmap[..., None]         # bake in the real reflection + shading
# tiny warm cast pulled from the screen's own color (keeps white matching ambient)
tint = ph[maskarr].mean(axis=0)
tint = tint / max(tint.mean(), 1.0)
wp *= (0.6 + 0.4*tint)[None, None, :]

# film/sensor grain to match the photograph
noise = np.random.normal(0, 2.4, wp.shape[:2])
wp += noise[..., None]
wp = np.clip(wp, 0, 255)

out = ph * (1 - feather[..., None]) + wp * feather[..., None]
Image.fromarray(np.clip(out, 0, 255).astype('uint8')).save(out_p)
print('composited', out_p)
