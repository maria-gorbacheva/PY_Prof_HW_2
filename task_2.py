# Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
import hashlib
import os

def my_generator(file: str):
    file_path = os.path.join(os.getcwd(), file)
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            data = f.readline()
            if not data:
                break
            hash_line = hashlib.md5(data.encode())
            yield hash_line.hexdigest()

if __name__ == '__main__':
    for line in my_generator('wiki_links.txt'):
        print(line)