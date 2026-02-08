
import os


def entity_action(folder_full_path):
    list_of_dirs = os.scandir(folder_full_path)
    for entry in list_of_dirs:
        if entry.is_dir():
            print("folder: " + entry.name)
            entity_action(entry.path)
        if entry.is_file():
            print("   file: " + entry.name)
            with open(entry.path, 'r') as file:
                content = file.read()
                if len(content) == 0:
                    os.remove(entry.path)
                    print(f"файл видалено {entry.path}")

entity_action("chaotic_fs")