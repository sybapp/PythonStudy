"""
以下是使用re正则表达式操作
"""

import re


def count_word(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'[a-zA-z]+', text)
        count = len(words)
    return count


if __name__ == '__main__':
    print(count_word('text.txt'))


