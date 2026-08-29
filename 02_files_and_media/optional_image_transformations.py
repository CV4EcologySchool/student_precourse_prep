"""Optional image transformations adapted from the previous assignment."""

from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image, ImageOps


PREP_DIR = Path(__file__).resolve().parents[1]
image_path = sorted((PREP_DIR / "shared_data" / "randalls_fish").glob("*.jpg"))[0]

with Image.open(image_path) as opened_image:
    original = opened_image.convert("RGB")

resized = original.resize((224, 224))
grayscale = ImageOps.grayscale(original)
flipped = ImageOps.mirror(original)

width, height = original.size
crop_size = min(width, height)
left = (width - crop_size) // 2
top = (height - crop_size) // 2
cropped = original.crop((left, top, left + crop_size, top + crop_size))

fig, axes = plt.subplots(1, 5, figsize=(16, 4))
examples = [original, resized, cropped, grayscale, flipped]
titles = ["Original", "Resized", "Center crop", "Grayscale", "Flipped"]

for ax, example, title in zip(axes, examples, titles):
    ax.imshow(example, cmap="gray" if title == "Grayscale" else None)
    ax.set_title(title)
    ax.axis("off")

fig.tight_layout()
plt.show()

# Optional questions:
# 1. Which transformations preserve your ecological label or measurement?
# 2. Which transformations could create an unrealistic observation?
# 3. Add one Pillow transformation and explain whether you would use it.

