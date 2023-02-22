from copy import deepcopy

phone_book = []
confirm_book = []
path = 'sem8/phone_book.txt'

def open_file():
    global phone_book
    global confirm_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_dict = {}
            new_dict['name'] = new[0]
            new_dict['phone'] = new[1]
            new_dict['comment'] = new[2]
            phone_book.append(new_dict)
    confirm_book = deepcopy(phone_book)

def get():
    global phone_book
    return phone_book

def add(new_dict: dict):
    global phone_book
    phone_book.append(new_dict)

def save_file():
    global phone_book
    global path
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def find(find_option: str):
    global phone_book
    all_find = []
    for contact in phone_book:
        for element in contact.values():
            if find_option.lower() in element.lower():
                all_find.append(contact)
    return all_find

def change_contact(ind: int, contact: dict):
    global phone_book
    phone_book.pop(ind-1)
    phone_book.insert(ind-1, contact)

def delete(ind: int):
    global phone_book
    phone_book.pop(ind-1)

def get_name(ind: int):
    global phone_book
    return phone_book[ind-1].get('name')

def check_changes():
    global phone_book
    global confirm_book
    if phone_book != confirm_book:
        return True
    return False