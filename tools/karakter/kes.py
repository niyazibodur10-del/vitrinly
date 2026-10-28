# NOT: arka plan/ön plan bölgeleri pilot portresine (karakter-sayfasi-2d-v1, x4) özeldir; yeni görselde yeniden ayarlanır.
# GrabCut cutout of the bust (subject large, blurred office background)
import sys, cv2, numpy as np
img = cv2.imread(sys.argv[1]); h, w = img.shape[:2]
mask = np.full((h, w), cv2.GC_PR_BGD, np.uint8)
# sure-foreground: face/hair/shirt core; sure-background: top-right window area and left strip above shoulder
cv2.ellipse(mask, (int(w*0.50), int(h*0.40)), (int(w*0.25), int(h*0.30)), 0, 0, 360, cv2.GC_FGD, -1)
mask[int(h*0.82):, int(w*0.05):int(w*0.95)] = cv2.GC_FGD
mask[int(h*0.70):int(h*0.82), int(w*0.10):int(w*0.90)] = cv2.GC_PR_FGD
mask[:int(h*0.55), int(w*0.86):] = cv2.GC_BGD
mask[:int(h*0.50), :int(w*0.06)] = cv2.GC_BGD
mask[:int(h*0.02), :] = cv2.GC_BGD
cv2.fillPoly(mask, [np.array([[862,650],[905,650],[905,880],[828,880],[842,760]], np.int32)], cv2.GC_BGD)
cv2.fillPoly(mask, [np.array([[880,560],[w,560],[w,1030],[945,1110],[850,950]], np.int32)], cv2.GC_BGD)
bgd = np.zeros((1, 65), np.float64); fgd = np.zeros((1, 65), np.float64)
cv2.grabCut(img, mask, None, bgd, fgd, 8, cv2.GC_INIT_WITH_MASK)
a = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
a = cv2.morphologyEx(a, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(a)
keep = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); a = np.where(lab == keep, 255, 0).astype(np.uint8)
a = cv2.GaussianBlur(a, (5, 5), 0)
out = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA); out[:, :, 3] = a
cv2.imwrite(sys.argv[2], out)
prev = np.full_like(img, (60, 200, 60)); al = (a / 255.0)[..., None]
cv2.imwrite(sys.argv[3], (img * al + prev * (1 - al)).astype(np.uint8))
