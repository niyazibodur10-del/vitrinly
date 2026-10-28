# NOT: arka plan/ön plan bölgeleri pilot portresine (karakter-sayfasi-2d-v1, x4) özeldir; yeni görselde yeniden ayarlanır.
# color-based alpha cleanup on the right edge band of the cutout (bg is light/grey/green, subject is skin/hair/black outline)
import sys, numpy as np, cv2
from PIL import Image
im = np.array(Image.open(sys.argv[1]))[:1110].copy()
x0, x1, y0, y1 = 760, 1000, 430, 1110
rgb = im[y0:y1, x0:x1, :3].astype(int); r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
mx = rgb.max(2)
dark = mx < 115
skin = (r > g) & (g > b) & (r - b > 55)
keep = (dark | skin).astype(np.uint8)
# only allow pixels connected to the main body (avoid isolated keeps in bg)
keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
a = im[y0:y1, x0:x1, 3].astype(np.uint8)
a = np.minimum(a, keep * 255)
a = cv2.GaussianBlur(a, (3, 3), 0)
im[y0:y1, x0:x1, 3] = a
orig = np.array(Image.open(sys.argv[1]))[:1110]
im[530:625, 760:845, 3] = orig[530:625, 760:845, 3]
Image.fromarray(im).save(sys.argv[2])
bg = np.zeros_like(im[..., :3]); bg[:] = (60, 200, 60); al = im[..., 3:4] / 255
Image.fromarray((im[..., :3] * al + bg * (1 - al)).astype('uint8')).crop((650, 450, 1050, 1000)).save(sys.argv[3])
