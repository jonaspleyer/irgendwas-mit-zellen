from pathlib import Path


def get_fresh_odir(odir: Path) -> Path:
    """Will give the next output folder in order which is not yet existing."""
    for i in range(9999):
        new_folder = odir / f"{i:04}"
        if not odir.exists():
            return new_folder
    else:
        raise ValueError("Could not find a folder in the given range")
