import os
from PIL import Image


def converter(argv):
    input_folder = argv[1]
    output_folder = argv[2]

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
        print(f'Directory \'{output_folder}\' was created')

    for file in os.listdir(input_folder):
        file_name = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]
        file_exists = os.path.exists(f'{output_folder}/{file}')
        if file_ext == '.jpg' and not file_exists:
            img = Image.open(f'{input_folder}/{file}')
            img.save(f'{output_folder}/{file_name}.png', 'png')

    print('All done!')
