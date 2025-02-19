import os
import shutil
import sys
from datetime import datetime

def get_home_directory():
    """Retourne le répertoire personnel de l'utilisateur en fonction de l'OS."""
    return os.path.expanduser("~")


def get_backup_filename(base_name):
    """Génère un nom de fichier unique basé sur le dossier spécifié."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_backup_{timestamp}.tar.gz"


def create_backup(user_input, temp_directory, output_directory):
    """Crée une archive compressée contenant le dossier spécifié et son contenu, sans inclure ses parents."""
    home_dir = get_home_directory()
    target_path = os.path.join(home_dir, user_input)  # Chemin du dossier spécifié
    base_name = os.path.basename(target_path)  # Nom du dossier final sans les parents
    backup_filename = get_backup_filename(base_name)
    temp_dir = os.path.join(temp_directory, "temp_backup")  # Dossier dédié pour temporaire
    backup_path = os.path.join(output_directory, backup_filename.replace(".tar.gz", ""))

    # Vérifie que le dossier existe
    if not os.path.exists(target_path) or not os.path.isdir(target_path):
        raise FileNotFoundError(f"Le dossier spécifié '{target_path}' n'existe pas ou n'est pas un dossier valide.")

    # Création des dossiers temporaires et de sortie si nécessaire
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(output_directory, exist_ok=True)

    temp_backup_dir = os.path.join(temp_dir, base_name)

    # Assurer que le dossier temporaire est bien supprimé avant de continuer
    if os.path.exists(temp_backup_dir):
        shutil.rmtree(temp_backup_dir, ignore_errors=True)

    try:
        shutil.copytree(target_path, temp_backup_dir)
    except PermissionError:
        raise PermissionError(
            f"Impossible de copier '{target_path}' dans '{temp_backup_dir}'. Vérifiez les permissions.")

    # Compression du dossier temporaire
    shutil.make_archive(backup_path, 'gztar', root_dir=temp_dir, base_dir=base_name)

    # Suppression du dossier temporaire après compression
    try:
        shutil.rmtree(temp_backup_dir)
    except PermissionError:
        print(
            f"Avertissement : Impossible de supprimer le dossier temporaire '{temp_backup_dir}', supprimez-le manuellement.")

    return backup_path + ".tar.gz"


def main():

    user_input = input("Entrez le chemin du dossier à sauvegarder (depuis votre répertoire personnel) : ")
    temp_directory = input("Entrez le chemin où stocker le répertoire temporaire : ")
    output_directory = input("Entrez le chemin où stocker le fichier compressé : ")

    backup_file = create_backup(user_input, temp_directory, output_directory)
    print(f"Backup créé : {backup_file}")


if __name__ == "__main__":
    main()
