phone_book = []
start_phone_book = []
PATH = 'phone_book.txt'

def get_pb():
    global phone_book
    return phone_book



def load_file():
     global phone_book, start_phone_book  
     with open (PATH, 'r', encoding='utf-8') as file:
        date = file.readlines() 
     for contact in date:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0],
                           'phone':contact[1],
                           'comment':contact[2]})    
     start_phone_book = phone_book.copy()    

def save_file():
    global phone_book
    data = []   
    for contact in phone_book:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)    
    with open(PATH, "w", encoding='utf-8') as file:
        file.write(data)


def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)


def find_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact.values():
            print(field)
            if word in field:
                result.append(contact)
                break
    return result   

    
def exit_pb() -> bool:
    global phone_book, start_phone_book 
    if phone_book == start_phone_book:
        return False
    else:
        return True


def get_phone_book() -> list[dict]:
    return phone_book


def edit_contact(edited_contact: tuple[int, dict[str, str]]) -> None:
    index, contact = edited_contact
    original_contact = phone_book.pop(index - 1)
    contact = {'name': contact.get('name') if contact.get('name') else original_contact.get('name'),
               'phone': contact.get('phone') if contact.get('phone') else original_contact.get('phone'),
               'comment': contact.get('comment') if contact.get('comment') else original_contact.get('comment')}
    phone_book.insert(index - 1, contact)

def remove_contact(index: int) -> str:
    deleted_element = phone_book.pop(index - 1)
    return deleted_element.get('name')    