import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
# начальные данные для создания, изменения и удаления пета

pet_id=55555

input_pet = {
    "id": pet_id,
    "category": {
        "id": 22,
        "name": "Bobik"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 12,
            "name": "Dog"
        }
    ],
    "status": "pending"
}
input_pet_to_update = {
    "id": pet_id,
    "category": {
        "id": 22,
        "name": "Bobik_Tobik"
    },
    "name": "doggie_moggy",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 12,
            "name": "Dog"
        }
    ],
    "status": "available"
}
# заголовки передаваемые в запросе
header = {'accept': 'application/json', 'Content-Type': 'application/json'}

# делаем post запрос
res = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
print('post запрос создаем пета ')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера :', res.json(), '\n')

# post запрос по статусу 'pending'
status = 'pending'
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
print('поиск по статутсу ')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера :', res.json(), '\n')
# делаем get запрос
res = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
print('поиск по ID ')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера :', res.json(), '\n')

# делаем put запрос
res = requests.put(url='https://petstore.swagger.io/v2/pet/',data=json.dumps(input_pet_to_update), headers=header)
print('обновление информации ')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера :', res.json(), '\n')

# загрузка фото по ID
image = 'cat.jpg'
files = MultipartEncoder(fields = {'file': (image, open(image, 'rb'), 'image/jpeg')})
header = {'accept': 'application/json', 'Content-Type': files.content_type}
res = requests.post(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}', headers=header, data=files)
print('загрузка фото по ID ')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# Post обновление питомца по ID
header={'accept': 'application/json','Content-Type': 'application/x-www-form-urlencoded'}
upd_pet ={"id": pet_id,"name": "Vasia","status": "available"}

res = requests.post(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}', headers=header, data=json.dumps(upd_pet))

print('Post обновление питомца по ID')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# делаем delete запрос
res = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
print('delete запрос ')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера :', res.json(), '\n')




