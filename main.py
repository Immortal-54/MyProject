import os
import shutil

def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')
    print(f"Файл {file_path} создан.")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл {file_path} удален.")
    else:
        print("Файл не существует.")

def move_file(source_path, destination_path):
    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Файл {source_path} перемещен в {destination_path}.")
    else:
        print("Файл не существует.")

def copy_file(source_path, destination_path):
    if os.path.exists(source_path):
        shutil.copy2(source_path, destination_path)
        print(f"Файл {source_path} скопирован в {destination_path}.")
    else:
        print("Файл не существует.")

def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)
    print(f"Папка {directory_path} создана.")

def delete_directory(directory_path):
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f"Папка {directory_path} удалена.")
    else:
        print("Папка не существует.")

def navigate_to_directory(directory_path):
    try:
        os.chdir(directory_path)
        print(f"Перешли в директорию: {directory_path}")
    except FileNotFoundError:
        print(f"Директории {directory_path} не существует.")

def list_files_in_directory(directory_path="."):
    files = os.listdir(directory_path)
    #print(f"Файлы в директории {directory_path}: {files}")
    for f in files:
        print('     ',f)

def help_command():
    print('COMMANDS LIST: ')
    print('     create_file ')
    print('     delete_file ')
    print('     move_file ')
    print('     copy_file ')
    print('     create_directory ')
    print('     delete_directory ')
    print('     navigate_to_directory ')
    print('     list_files ')

while True:
    current_directory = os.getcwd()
    command = input(f"{current_directory} $ ").split()

    if not command:
        continue

    if command[0] == 'exit':
        break
    elif command[0] == 'create_file':
        create_file(command[1])
    elif command[0] == 'delete_file':
        delete_file(command[1])
    elif command[0] == 'move_file':
        move_file(command[1], command[2])
    elif command[0] == 'copy_file':
        copy_file(command[1], command[2])
    elif command[0] == 'create_directory':
        create_directory(command[1])
    elif command[0] == 'delete_directory':
        delete_directory(command[1])
    elif command[0] == 'navigate_to_directory':
        navigate_to_directory(command[1])
    elif command[0] == 'list_files':
        list_files_in_directory(command[1] if len(command) > 1 else ".")
    elif command[0] == 'help':
        help_command()
    else:
        print("incorrect command")
