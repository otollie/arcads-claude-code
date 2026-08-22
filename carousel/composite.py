import sys, json
from PIL import Image, ImageDraw
import numpy as np

# usage: composite.py photo.png screen.png out.png "x0,y0 x1,y1 x2,y2 x3,y3" [debug]
# corners order: TL TR BR BL (of the white screen area in the photo)
photo_p, screen_p, out_p, corners_s = sys.argv[1:5]
debug = len(sys.argv) > 5 and sys.argv[5] == 'debug'
corners = [tuple(map(float, p.split(','))) for p in corners_s.split()]

photo = Image.open(photo_p).convert('RGBA')

if debug:
    d = ImageDraw.Draw(photo)
    d.polygon(corners, outline=(255, 0, 0, 255))
    for i, c in enumerate(corners):
        d.ellipse([c[0]-6, c[1]-6, c[0]+6, c[1]+6], fill=(255, 0, 0, 255))
    photo.convert('RGB').save(out_p)
    sys.exit()

screen = Image.open(screen_p).convert('RGBA')
sw, sh = screen.size
# solve homography mapping OUTPUT(photo) -> INPUT(screen) for PIL PERSPECTIVE
# we have src rect corners (screen) and dst quad (photo). PIL needs output->input,
# so compute transform from dst quad to src rect.
src = [(0, 0), (sw, 0), (sw, sh), (0, sh)]  # TL TR BR BL of screen
dst = corners
A = []
B = []
for (x, y), (u, v) in zip(dst, src):  # output (x,y) -> input (u,v)
    A.append([x, y, 1, 0, 0, 0, -u*x, -u*y]); B.append(u)
    A.append([0, 0, 0, x, y, 1, -v*x, -v*y]); B.append(v)
coeffs = np.linalg.solve(np.array(A), np.array(B))
warped = screen.transform(photo.size, Image.PERSPECTIVE, coeffs.tolist(), Image.BICUBIC)
# build a mask from the dst quad so we only paste inside the screen
mask = Image.new('L', photo.size, 0)
ImageDraw.Draw(mask).polygon(dst, fill=255)
# gentle screen glare for realism
glare = Image.new('RGBA', photo.size, (0, 0, 0, 0))
gd = ImageDraw.Draw(glare)
gx = [corners[0], corners[1], ((corners[1][0]+corners[2][0])/2, (corners[1][1]+corners[2][1])/2),
      ((corners[0][0]+corners[3][0])/2, (corners[0][1]+corners[3][1])/2)]
gd.polygon(gx, fill=(255, 255, 255, 26))
photo.paste(warped, (0, 0), mask)
photo = Image.alpha_composite(photo, Image.composite(glare, Image.new('RGBA', photo.size, (0,0,0,0)), mask))
photo.convert('RGB').save(out_p)
print('composited', out_p)
