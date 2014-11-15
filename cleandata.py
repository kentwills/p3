from unidecode import unidecode

def main():
    create_sanitized_file('Science.de')
    create_sanitized_file('Science.en')
    create_sanitized_file('Science.fr')
    create_sanitized_file('Science.te')
    create_sanitized_file('Science.tr')

def create_sanitized_file(file_name):
    data = unidecode(open_file(file_name).lower())
    writefile(file_name, data)

def writefile(file_name, data):
    with open(file_name+"-sanitized", "w") as text_file:
        text_file.write(data)

def open_file(file_name):
    with open(file_name, 'r') as f:
        read_data = f.read()
    return read_data

if __name__ == "__main__":
    main()