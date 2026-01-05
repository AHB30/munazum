import os
from pathlib import Path
import pytest

from munazum.scanner import scan_folder, FileMetadata


def test_scan_folder_raises_if_not_exists(tmp_path: Path):
    missing = tmp_path / "does_not_exist"

    with pytest.raises(FileNotFoundError):
        scan_folder(missing)


def test_scan_folder_raises_if_not_directory(tmp_path: Path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("hello")

    with pytest.raises(NotADirectoryError):
        scan_folder(file_path)


def test_scan_folder_single_file(tmp_path: Path):
    file_path = tmp_path / "example.TXT"
    file_path.write_text("content")

    results = scan_folder(tmp_path)

    assert len(results) == 1
    meta = results[0]

    assert isinstance(meta, FileMetadata)
    assert meta.name == "example.TXT"
    assert meta.extension == ".txt"   # lowercased
    assert meta.size_bytes == len("content")
    assert meta.path.exists()


def test_scan_folder_recursive(tmp_path: Path):
    sub = tmp_path / "sub"
    sub.mkdir()

    (tmp_path / "a.txt").write_text("a")
    (sub / "b.txt").write_text("bb")

    results = scan_folder(tmp_path)

    names = {m.name for m in results}
    assert names == {"a.txt", "b.txt"}


def test_scan_folder_ignores_directories(tmp_path: Path):
    (tmp_path / "dir").mkdir()
    (tmp_path / "file.txt").write_text("x")

    results = scan_folder(tmp_path)

    assert len(results) == 1
    assert results[0].name == "file.txt"


def test_scan_folder_ignores_directories(tmp_path: Path):
    (tmp_path / "dir").mkdir()
    (tmp_path / "file.txt").write_text("x")

    results = scan_folder(tmp_path)

    assert len(results) == 1
    assert results[0].name == "file.txt"
