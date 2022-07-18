import json
import yaml
from pprint import pprint

with open('order.yaml') as file:    # Открываем yaml-файл
    data = yaml.safe_load(file)

pprint(data)
print()

delivery_address = data['ship-to']['address']
for key, value in delivery_address.items():
    print(f'{key} => {value}')
print()

print(f'Invoice = {data["invoice"]}')
print()

for key in data['product']: # Перебираем  все ключи/аттрибуты  в data['product']
    # Вытаскиваем аттрибуты необходимых ключей
    print(f'Product: Description - {key["description"]}, Price - {key["price"]}, Quantity - {key["quantity"]}')

main_info = {
    "squadName": "Super hero squad",
    "homeTown": "Metro City",
    "secretBase": "Super tower",
}

heroes = [
    {
        "name": "Molecule Man",
        "age": 29,
        "secretIdentity": "Dan Jukes",
        "powers": [
            "Radiation resistance",
            "Turning tiny",
            "Radiation blast"
        ]
    },
    {
        "name": "Eternal Flame",
        "age": 1000000,
        "secretIdentity": "Unknown",
        "powers": [
            "Immortality",
            "Heat Immunity",
            "Inferno",
            "Teleportation",
            "Interdimensional travel"
        ]
    }
]

to_yaml = {'Main Info': main_info, 'Heroes': heroes}

# Записываем данные в yaml.
with open('superhero.yaml', 'w') as f:
    to_yaml = yaml.dump(to_yaml, f, default_flow_style=False)

# Считываем yaml-файл.
with open('superhero.yaml', 'r') as ym_file:
    to_json = yaml.safe_load(ym_file)

# Конвертируем yaml-файл в json.
with open('from_yaml_to_jsf.json', 'w') as js_file:
    json.dump(to_json, js_file, indent=4)
