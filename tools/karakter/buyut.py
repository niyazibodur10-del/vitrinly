# portrait: crop -> Real-ESRGAN x4 (spandrel, local weights) -> RGB png
import sys, torch, numpy as np
from PIL import Image
import spandrel
src, out, box, w = sys.argv[1], sys.argv[2], tuple(int(v) for v in sys.argv[3].split(",")), sys.argv[4]
img = Image.open(src).convert("RGB").crop(box)
m = spandrel.ModelLoader().load_from_file(w).eval()
x = torch.from_numpy(np.asarray(img).astype(np.float32)/255).permute(2,0,1)[None]
with torch.no_grad(): y = m(x).clamp(0,1)[0].permute(1,2,0).numpy()
Image.fromarray((y*255).round().astype(np.uint8)).save(out); print(img.size, "->", y.shape)
