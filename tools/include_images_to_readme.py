from pathlib import Path


readme_file = Path("README.md")
image_files = Path("docs/images").glob("*.png")
separator = "<!-- images -->"
images = [
    "[{}]: {}".format(file.stem, str(file).replace("\\", "/"))
    for file in image_files
]
text, _ = readme_file.read_text().split(separator)

readme_file.write_text(
    "{}{}\n\n{}\n".format(text, separator, "\n".join(images))
)
