import requests

response = requests.get(
    url='https://fakerestapi.azurewebsites.net/api/v1/Authors')  # Получаем список всех авторов по ссылке
print(f'Status code = {response.status_code}')
assert response.status_code == 200, 'Error! Something wong!'

response2 = requests.get(
    url='https://fakerestapi.azurewebsites.net/api/v1/Authors/27')  # Получаем автора по конкретному id
print(f'Status code = {response2.status_code}')
assert response2.status_code == 200, 'Error! Something wong!'

new_book = {
    "id": 1000,
    "title": "Book 1000",
    "description": "Description\n",
    "pageCount": 1000,
    "excerpt": "Text\n",
    "publishDate": "2022-07-18T15:30:00.6863427+00:00"
}
# Добавляем новую книгу. json=new_book добавляет данные из new_book сразу в json формате.
response3 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Books', json=new_book)
print(f'Status code = {response3.status_code}')
assert response3.status_code == 200

new_user = {
    "id": 1000,
    "userName": "User 1000",
    "password": "Password1000"
}
# Добавляем нового пользователя. json=new_user добавляет из new_user данные сразу в json формате.
response4 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Users', json=new_user)
print(f'Status code = {response4.status_code}')
assert response4.status_code == 200

book_10 = {
    "id": 10,
    "title": "Book 10",
    "description": "Description\n",
    "pageCount": 800,
    "excerpt": "Text\n",
    "publishDate": "2022-07-18T15:45:00.6863427+00:00"
}
# Обновляем данные книги с id=10. json=book_10 добавляет данные из book_10 сразу в json формате.
response5 = requests.put(url='https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=book_10)
print(f'Status code = {response5.status_code}')
assert response5.status_code == 200

response6 = requests.delete(url='https://fakerestapi.azurewebsites.net/api/v1/Users/4')
print(f'Status code = {response6.status_code}')
assert response6.status_code == 200, 'Error! Something wong!'