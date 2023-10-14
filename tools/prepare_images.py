from PIL import Image
from pathlib import Path
import shutil


image_paths = Path("assets").glob("**/*.png")
ignored_path_pattern = ["pulling", "entity"]
size = 256  # 32 is minimum
destination_path = Path(f"gallery/generated/{size}")

shutil.rmtree(str(destination_path), True)

for image_path in image_paths:
    if [
        True for pattern in ignored_path_pattern
        if pattern in str(image_path)
    ]:
        continue

    image = Image.open(image_path)
    resized_image = image.resize((size, size), Image.Resampling.NEAREST)

    if not destination_path.exists():
        destination_path.mkdir()

    resized_image.save(destination_path.joinpath(image_path.name))
