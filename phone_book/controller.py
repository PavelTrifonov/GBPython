import model
import view

def start():
    user_choice=0
    while user_choice!=8:
        user_choice=view.main_menu()
        match user_choice:
            case 1:
                phone_book=model.get_phone_book()
                view.show_contakts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_book()
            case 3:
                model.save_phone_book()
                view.save_book()
            case 4:
                new=view.new_contakt()
                model.updata_book(new)
                view.add_contact(new)
            case 5:
                old_name=view.change_contakt()
                new_name=view.new_contakt()
                model.rename_contact(old_name,new_name)
            case 6:
                delete=view.delete_cont()
                model.delete_contact(delete)
                view.del_from_book(delete)
            case 7:
                search=view.find_contakt()
                result=model.search_contact(search)
                view.show_contakts(result)

            