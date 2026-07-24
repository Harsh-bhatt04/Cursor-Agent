import fnmatch
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


@tool
def write_file(file_path: str, content: str) -> str:
    """Write content to a file."""

    path = Path(file_path)
    path.write_text(content)

    return f"Successfully wrote to {file_path}"


@tool
def search_files(directory: str, pattern: str) -> list[str]:
    """
    Search for files recursively matching a pattern.

    Example patterns:
    *.py
    *.md
    *.json
    """

    matches = []

    for file in Path(directory).rglob("*"):
        if file.is_file() and fnmatch.fnmatch(file.name, pattern):
            matches.append(str(file))

    return matches