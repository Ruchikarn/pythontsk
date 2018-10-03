import os

BASE_DIR = r'/Users/bishnubhusal/Desktop/random'

file_types = {
    'photos': ['png', 'jpeg', 'jpg', 'gif'],
    'documents': ['key', 'ppt', 'pptx', 'xls', 'pdf', 'csv'],
    'movie': ['mp4', 'mkv', 'avi', 'mpeg', '3gp'],
    'text_file': ['txt'],
    'python': ['pyc', 'py']
}

# for creating for folders
for file_type in file_types:
    full_path = os.path.join(BASE_DIR, file_type)
    if not os.path.exists(full_path):
        os.mkdir(full_path)

# logic for moving files to folder
for file in os.listdir(BASE_DIR):
    extension = file.split('.')[-1]
    for key in file_types:
        # print(file, key, file_types[key])
        if extension in file_types[key]:
            print(extension, 'is a', key)
            path_src = os.path.join(BASE_DIR, file)
            path_dest = os.path.join(BASE_DIR, key, file)
            print(path_src, path_dest)
            os.rename(path_src, path_dest)
