# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import uuid
import codecs

from bs4 import BeautifulSoup


def parse():


    walk_dir = '/Users/cody/Downloads/files'

    for root, directories, filenames in os.walk(walk_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                print(file_path)
                #f = open(file_path)
                #with open(file_path, encoding='utf-8') as f:
                with codecs.open(file_path, 'r', encoding='utf-8',
                                 errors='ignore') as f:
                    soup = BeautifulSoup(f, features="html.parser")

                f.close()

                print(soup.prettify())


def main():
    # Use a breakpoint in the code line below to debug your script.
    parse()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
