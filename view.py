
def menu():
    print('''\nГлавное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
    while True:
        try:
            button = int(input('Выберите действие: '))
            if 0<button<9:
                return button
            else:
                print('Введите число от 1 до 8')
        except:
            print('Вводи цифры!')

def show_contact(pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста или файл не открыт')
    else:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {phone:<15} {comment:<20}')

def input_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    new = {'name': name, 'phone': phone, 'comment': comment}
    return new

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def get_ind():
    ind = int(input('Введите индекс: '))
    return ind

def confirm(condition: str, name: str):
    answer = input(f'Вы действительно хотите {condition} контакт {name}? (y/n)')
    if answer == 'y':
        return True
    else:
        return False

def confirm_changes():
    answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n)')
    return True if answer == 'y' else False