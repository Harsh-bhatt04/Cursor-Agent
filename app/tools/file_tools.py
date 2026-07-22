from pathlib import Path

from langchain_core.tools import tool


@tool
def read_file(file_path: str) -> str:
    """Read the contents of a file."""

    return Path(file_path).read_text()



@tool
def list_files(directory: str) -> str:
    """List all files and directories in a directory."""

    path = Path(directory)

    directories = []
    files = []

    for item in sorted(path.iterdir()):
        if item.is_dir():
            directories.append(f"📁 {item.name}")
        else:
            files.append(f"📄 {item.name}")

    return (
        f"Directory: {path.resolve()}\n\n"
        f"Folders:\n" + ("\n".join(directories) or "None") +
        f"\n\nFiles:\n" + ("\n".join(files) or "None")
    )