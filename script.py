import json
from csv import DictReader


def read_books():
    with open('./data/books.csv', newline='') as library:
        csv_reader = DictReader(library)
        books = []
        for row in csv_reader:
            del row['Publisher']
            books.append(row)
        return books


def read_users():
    with open('./data/users.json', 'r') as people:
        people_json = json.load(people)
        return people_json


def parse(file):
    people_list = []
    for human in file:
        human_info = {'name': human["name"],
                      'gender': human["gender"],
                      'adress': human["address"],
                      'age': human["age"],
                      'books': []}
        people_list.append(human_info)
    return people_list


def add_book(users, books):
    checker = []
    lenght = len(books)
    while len(checker) < lenght:
        for user in users:
            for book in books:
                if book not in checker:
                    user['books'].append(book)
                    checker.append(book)
                    break

    with open('result.json', 'w') as result:
        json.dump(users, result, indent=4)


add_book(parse(read_users()), read_books())
