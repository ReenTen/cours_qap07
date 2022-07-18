import xml.etree.ElementTree as ET    # Импорт модуля элемента дерева


def searching_by_author(author_name):
    tree = ET.parse('library.xml')    # Открываем XML файл
    root = tree.getroot()    # Получаем root-tag дерева
    for book in root:    # Итерация по child-tag (book) в root
        for author in book:    # Итерация по child-tag (author) в book
            if author.tag == 'author':    # Если тэг итерируемого эл-та = author, то переходим в цикл
                if not f'{author_name}' in author.text:    # Если в тэгах нет текста, то
                    text = "None"
                else:    # Если в тэгах есть текст, то
                    text = author.text    # Извлекаем текст
                    print(f'{book.tag}{book.attrib} => Author: {text}')
            else:    # Если тэг итерируемого эл-та != author, то пропускаем его без вывода информации
                continue


def searching_by_title(book_title):
    tree = ET.parse('library.xml')
    root = tree.getroot()
    for book in root:
        for title in book:
            if title.tag == 'title':
                if not f'{book_title}' in title.text:
                    text = "None"
                else:
                    text = title.text
                    print(f'{book.tag}{book.attrib} => Title: {text}')
            else:
                continue



def searching_by_price(book_price):
    tree = ET.parse('library.xml')
    root = tree.getroot()
    for book in root:
        for price in book:
            if price.tag == 'price':
                if not f'{book_price}' in price.text:
                    text = "None"
                else:
                    text = price.text
                    print(f'{book.tag}{book.attrib} => Price: {text}')
            else:
                continue


def searching_by_description(book_description):
    tree = ET.parse('library.xml')
    root = tree.getroot()
    for book in root:
        for description in book:
            if description.tag == 'description':
                if not f'{book_description}' in description.text:
                    text = "None"
                else:
                    text = description.text
                    print(f'{book.tag}{book.attrib} => Description: {text}')
            else:
                continue


if __name__ == '__main__':
    searching_by_author('Gambardella')
    searching_by_title('XML')
    searching_by_price('36')
    searching_by_description('A Very Simple')
