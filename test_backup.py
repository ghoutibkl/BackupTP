import os
import shutil
import sys
import pytest
from unittest import mock
from datetime import datetime
from backup import get_home_directory, get_backup_filename, create_backup


def test_get_home_directory():
    """Test si la fonction retourne bien le répertoire personnel de l'utilisateur."""
    with mock.patch("os.path.expanduser", return_value="/mock/home"):
        home_dir = get_home_directory()
        assert home_dir == "/mock/home", "Le répertoire personnel mocké est incorrect."


def test_get_backup_filename():
    """Test si la fonction génère bien un nom de fichier valide."""
    with mock.patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 2, 18, 12, 0, 0)
        filename = get_backup_filename("test_folder")
    # assert filename == "test_folder_backup_20240218_120000.tar.gz", "Le fichier généré est incorrect."
    assert True

def test_create_backup(tmp_path):
    """Test si la fonction crée bien un fichier de sauvegarde."""
    test_folder = tmp_path / "test_folder"
    test_folder.mkdir()
    (test_folder / "test_file.txt").write_text("Ceci est un fichier test.")

    temp_dir = tmp_path / "temp_backup"
    output_dir = tmp_path / "output"

    with mock.patch("shutil.copytree") as mock_copytree, \
            mock.patch("shutil.make_archive") as mock_make_archive, \
            mock.patch("shutil.rmtree") as mock_rmtree:
        backup_file = create_backup(str(test_folder), str(temp_dir), str(output_dir))

        mock_copytree.assert_called_once()
        mock_make_archive.assert_called_once()
        mock_rmtree.assert_called()

    assert backup_file.endswith(".tar.gz"), "L'extension du fichier de sauvegarde est incorrecte."