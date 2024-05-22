try:
    with open('file_ not_exist.txt','r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found")