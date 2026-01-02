from pathlib import Path
from zipfile import ZipFile

PACKAGE_NAME = "BowAndArrow"
ZIP_FILES = [
    Path("assets/minecraft"),
    Path("pack.png"),
    Path("pack.mcmeta"),
]


def check_required_files(files: list[Path]) -> None:
    for file in files:
        if not file.exists():
            raise FileNotFoundError(f"Required file: `{file.name}` not found.")


def create_zip_file(zip_name: str, zip_content: list[Path]) -> None:
    with ZipFile(zip_name, "w") as zip_file:
        for target in zip_content:
            if target.is_dir():
                [zip_file.write(file) for file in target.glob("**/*") if file.is_file()]
            else:
                zip_file.write(target)


if __name__ == "__main__":
    print("Create a new zip file", flush=False)
    check_required_files(ZIP_FILES)

    version = input("Version: ")
    zip_name = f"{PACKAGE_NAME}-{version}.zip"
    create_zip_file(zip_name, ZIP_FILES)
