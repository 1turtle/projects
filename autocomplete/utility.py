def read_file():
    words_list = []

    file_path = 'words.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        words_list.append(line.strip())

    return words_list

def find_all(text, word_list):
    match_list = []

    for item in word_list:
        if item.lower().startswith(text):
            match_list.append(item)

    return match_list


if __name__ == '__main__':
    ...