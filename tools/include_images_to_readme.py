from pathlib import Path

readme_file = Path("README.md")
image_files = Path("docs/images").glob("*.png")
separator = "<!-- images -->"

images = [f"[{file.stem}]: {str(file)}" for file in image_files] + [""]

text = readme_file.read_text()
text, _ = text.split(separator)

readme_file.write_text("{}{}\n{}".format(text, separator, "\n".join(images)))
