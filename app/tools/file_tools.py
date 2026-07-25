import os
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


@tool
def search_text(directory: str, text: str) -> list[str]:
    """
    Search for text recursively in all project files.
    """

    matches = []

    for root, _, files in os.walk(directory):
        for file in files:
            path = Path(root) / file

            try:
                content = path.read_text()

                if text in content:
                    matches.append(str(path))

            except Exception:
                continue

    return matches


@tool
def edit_file(file_path: str, old_text: str, new_text: str) -> str:
    """
    Replace old_text with new_text inside a file.
    """

    path = Path(file_path)

    if not path.exists():
        return f"{file_path} does not exist."

    content = path.read_text(encoding="utf-8")

    if old_text not in content:
        return f'"{old_text}" was not found in {file_path}.'

    updated_content = content.replace(old_text, new_text)

    path.write_text(updated_content, encoding="utf-8")

    return f"Successfully updated {file_path}"