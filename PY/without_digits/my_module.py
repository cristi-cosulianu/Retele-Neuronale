import sys
import os

def operations():
    if len(sys.argv) >=3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            print(a - b)
            print(a + b)
            print(a / b)
            print(a * b)
        except Exception as e:
            print(e)

def check_path():
    if len(sys.argv) >= 2:
        try:
            input_path = sys.argv[1]
            if os.path.isdir(input_path):
                print(os.listdir(input_path))
            elif os.path.isfile(input_path):
                file = open(input_path, "rt")
                print(file.read(4096))
            else:
                print("Invalid path!")
        except Exception as e:
            print("Invalid path!")
            print(e)

def write_info():
    if len(sys.argv) >= 2:
        try:
            file_path = sys.argv[1]
            if os.path.isfile(file_path):
                file = open(file_path, "wt")
                for item in os.environ.items():
                    file.write(item[0] + "\t\t" + item[1] + "\n")
        except Exception as e:
            print(e)
    else:
        print("Insert a file path!")

def recursiv_walk(path):
    try:
        if os.path.isdir(path):
            for entry in os.listdir(path):
                new_path = os.path.join(path, entry)
                print(new_path)
                if os.path.isdir(new_path):
                    recursiv_walk(new_path)
        else:
            print("Is not directory!")
    except Exception as e:
        print(e)

def function5():
    if len(sys.argv) >= 3:
        dir_path = sys.argv[1]
        file_name = sys.argv[2]
        paths = list()
        for (root, dirs, files) in os.walk(dir_path):
            for file in files:
                if file == file_name:
                    file_path = os.path.join(root, file)
                    file_desc = open(file_path, "wt")
                    for path in paths:
                        file_desc.write(path)
                else:
                    file_path = os.path.join(root, file)
                    paths.append(file_path + '\n')
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                paths.append(dir_path + '\n')

def move_file_content():
    if len(sys.argv) >= 4:
        file_path = sys.argv[1]
        dir_path = sys.argv[2]
        buffer_size = int(sys.argv[3])

        if os.path.isfile(file_path) and os.path.isdir(dir_path):
            file_name = os.path.basename(file_path)
            initial_file = open(file_path, "r")
            destination_path = os.path.join(dir_path, file_name)
            destination_file = open(destination_path, "a")

            content = initial_file.read(buffer_size)
            while content:
                destination_file.write(content)
                content = initial_file.read(buffer_size)