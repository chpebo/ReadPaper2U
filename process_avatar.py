"""Process the HEIC photo of Banni: load, remove background, save as PNG.

Steps:
1. Read HEIC via pillow-heif
2. Apply EXIF rotation if any
3. Run rembg with the isnet-general-use model (better at fur/whisker edges than u2net)
4. Tight crop to the alpha bounding box with a small padding
5. Resize to a max dimension of 720 px to keep file size reasonable
6. Save as PNG (with alpha)
"""
import io
import os
from PIL import Image, ImageOps
import pillow_heif
from rembg import remove, new_session

pillow_heif.register_heif_opener()

SRC = "20260210_040814813_iOS.heic"
DST = "banni.png"
MAX_DIM = 720

print(f"[1/5] Loading {SRC}...")
img = Image.open(SRC)
img = ImageOps.exif_transpose(img)  # apply rotation from EXIF
img = img.convert("RGBA")
print(f"      original size: {img.size}")

print("[2/5] Running rembg (isnet-general-use)...")
# isnet-general-use is generally better than u2net for fur/whisker edges.
session = new_session("isnet-general-use")
cutout = remove(
    img,
    session=session,
    alpha_matting=True,
    alpha_matting_foreground_threshold=240,
    alpha_matting_background_threshold=10,
    alpha_matting_erode_size=10,
)

print("[3/5] Cropping to alpha bbox...")
alpha = cutout.split()[-1]
bbox = alpha.getbbox()
if bbox is None:
    raise RuntimeError("rembg returned an empty alpha channel — cat not found?")
# pad by 2% of the larger side
pad = max(8, int(0.02 * max(cutout.size)))
left, top, right, bottom = bbox
left = max(0, left - pad)
top = max(0, top - pad)
right = min(cutout.size[0], right + pad)
bottom = min(cutout.size[1], bottom + pad)
cropped = cutout.crop((left, top, right, bottom))
print(f"      cropped size: {cropped.size}")

print(f"[4/5] Resizing to max {MAX_DIM}px...")
w, h = cropped.size
scale = min(MAX_DIM / w, MAX_DIM / h, 1.0)
if scale < 1.0:
    new_size = (int(w * scale), int(h * scale))
    cropped = cropped.resize(new_size, Image.LANCZOS)
    print(f"      final size: {cropped.size}")
else:
    print("      no resize needed")

print(f"[5/5] Saving to {DST}...")
cropped.save(DST, "PNG", optimize=True)
size_kb = os.path.getsize(DST) / 1024
print(f"Done. {DST} ({size_kb:.1f} KB)")
