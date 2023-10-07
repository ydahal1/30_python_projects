import os
import shutil

if a := "age":
    print("Hello age")

def create_folder(path: str, extension:str) -> str:
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path

def sort_files(src_path: str):
    for root_dir, sub_dir, file_names in os.walk(src_path):
        for file_name in file_names:
            file_path: str = os.path.join(root_dir, file_name)
            extension: str = os.path.splitext(file_name)[1]

            if extension:
                target_folder: str = create_folder(src_path, extension)
                target_path: str = os.path.join(target_folder, file_name)

                shutil.move(file_path, target_path)


def remove_empty_folders(src_path: str) -> None:
    """ This func removes all empty folders """
    for root_dir, sub_dir, file_name in os.walk(src_path, topdown=False):
        for current_dir in sub_dir:
            folder_path = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):
                os.removedirs(folder_path)


def main() -> None:
    user_input = input("Please enter a path to sort: ")
    if os.path.exists(path= user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)
    else:
        print("Invalid path entered !!")

if __name__ == "__main__":
    main()