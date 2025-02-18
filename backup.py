import os
import shutil
import platform
from datetime import datetime
import pytest


def get_home_directory():
    """Retourne le répertoire personnel de l'utilisateur en fonction de l'OS."""
    return os.path.expanduser("~")


def get_backup_filename():
    """Génère un nom de fichier unique pour la sauvegarde."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"backup_{timestamp}.tar.gz"


def create_backup():
    """Crée une archive compressée du répertoire personnel."""
    home_dir = get_home_directory()
    backup_filename = get_backup_filename()
    backup_path = os.path.join(os.getcwd(), backup_filename)

    shutil.make_archive(backup_filename.replace(".tar.gz", ""), 'gztar', home_dir)

    return backup_path


def main():
    backup_file = create_backup()
    print(f"Backup créé : {backup_file}")


if __name__ == "__main__":
    main()
