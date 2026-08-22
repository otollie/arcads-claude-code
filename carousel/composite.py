import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# composite.py photo screen out "TLx,TLy TRx,TRy BRx,BRy BLx,BLy" bright "r,g,b" [debug]
photo_p, screen_p, out_p, corners_s, bright_s, tint_s = sys.argv[1:7]
debug = len(sys.argv) > 7 and sys.argv[7] == 'debug'
corners = [tuple(map(float, p.split(','))) for p in corners_s.split()]

photo = Image.open(photo_p).convert('RGBA')
if debug:
    d = ImageDraw.Draw(photo)
    d.polygon(corners, outline=(255, 0, 0, 255))
    for c in corners:
        d.ellipse([c[0]-6, c[1]-6, c[0]+6, c[1]+6], fill=(255, 0, 0, 255))
    photo.convert('RGB').save(out_p); sys.exit()

bright = float(bright_s)
tint = [float(x) for x in tint_s.split(',')]
screen = Image.open(screen_p).convert('RGBA')
sw, sh = screen.size

# 1) match screen luminance + ambient color temperature to the scene
arr = np.array(ImageEnhance.Brightness(screen).enhance(bright)).astype(float)
for i in range(3):
    arr[..., i] *= tint[i]

yy, xx = np.mgrid[0:sh, 0:sw]
fx, fy = xx / sw, yy / sh

# 2) glass sheen: broad diagonal highlight + one soft streak (screen-local, warps with it)
sheen = np.clip((fx * 0.6 + (1 - fy) * 0.4 - 0.5) * 2.0, 0, 1) * 60
streak = np.exp(-((fx - (1 - fy) * 0.75 - 0.05) ** 2) / (2 * 0.015 ** 2)) * 42
glow = np.clip(sheen + streak, 0, 120)
for i in range(3):
    arr[..., i] = np.clip(arr[..., i] + glow, 0, 255)

# 3) subtle inner edge darkening under the bezel
edge = np.minimum.reduce([xx, sw - 1 - xx, yy, sh - 1 - yy]).astype(float)
vig = np.clip(edge / 20, 0, 1) * 0.10 + 0.90
for i in range(3):
    arr[..., i] *= vig

screen = Image.fromarray(np.clip(arr, 0, 255).astype('uint8'), 'RGBA')
# 4) match the photo's focus softness
screen = screen.filter(ImageFilter.GaussianBlur(0.7))

# perspective warp: output(photo) -> input(screen)
src = [(0, 0), (sw, 0), (sw, sh), (0, sh)]
A, B = [], []
for (x, y), (u, v) in zip(corners, src):
    A.append([x, y, 1, 0, 0, 0, -u*x, -u*y]); B.append(u)
    A.append([0, 0, 0, x, y, 1, -v*x, -v*y]); B.append(v)
coeffs = np.linalg.solve(np.array(A), np.array(B))
warped = screen.transform(photo.size, Image.PERSPECTIVE, coeffs.tolist(), Image.BICUBIC)

# 5) feathered mask so the edge isn't a hard cut
mask = Image.new('L', photo.size, 0)
ImageDraw.Draw(mask).polygon(corners, fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(1.6))
photo.paste(warped, (0, 0), mask)
photo.convert('RGB').save(out_p)
print('composited', out_p)
