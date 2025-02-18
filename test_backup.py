# Tests unitaires
import os

from backup import get_home_directory, get_backup_filename, create_backup


def test_get_home_directory():
    """"Tester si le path existe"""
    home_dir = get_home_directory()
    assert os.path.exists(home_dir)


def test_get_backup_filename():
    """"Tester la création d'un réperstoire pour le backup"""
    filename = get_backup_filename()
    assert filename.startswith("backup_") and filename.endswith(".tar.gz")


# def test_create_backup():
#     backup_path = create_backup()
#     assert os.path.exists(backup_path)