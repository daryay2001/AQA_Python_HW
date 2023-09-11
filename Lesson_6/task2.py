# 2- Написати програму, яка просканує кореневу папку вашого проєкту,
# збереже у файл files_size.txt назви та розмір файлів, і надрукує назву найбільшого файлу
# та його розмір.

import os

root_folder = './..'
files_size_list = []

try:
    for main_folder, sub_folders, files in os.walk(root_folder):
        for file in files:
            file_path = os.path.join(main_folder, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                files_size_list.append((file, file_size))

    with open("files_size.txt", "w") as f:
        for file, size in files_size_list:
            f.write(f"{file} -> {size} bytes\n")

    max_size_file = None
    largest_size = -1

    for filename, size in files_size_list:
        if size > largest_size:
            max_size_file = filename
            largest_size = size

    if max_size_file is not None:
        print(f"The biggest file is: {max_size_file}, size: {largest_size} bytes")
    else:
        print("There is no files at all")

except Exception as error:
    print(error)





