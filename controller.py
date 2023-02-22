import view
import model

def start():
    while True:
        button = view.menu()
        match button:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                pb = model.get()
                view.show_contact(pb)
            case 4:
                new = view.input_new_contact()
                model.add(new)
            case 5:
                pb = model.get()
                view.show_contact(pb)
                ind = view.get_ind()
                contact = view.input_new_contact()
                name = model.get_name(ind)
                if view.confirm('изменить', name):
                    model.change_contact(ind, contact)
            case 6:
                find_option = view.find_contact()
                result = model.find(find_option)
                view.show_contact(result)
            case 7:
                pb = model.get()
                view.show_contact(pb)
                ind = view.get_ind()
                name = model.get_name(ind)
                if view.confirm('удалить', name):
                    model.delete(ind)
            case 8:
                if model.check_changes():
                    if view.confirm_changes():
                        model.save_file()
                print('До свидания!')
                break