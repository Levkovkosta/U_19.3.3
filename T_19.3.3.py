import requests
import json

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
    "status": "available"
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
res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
print(res_post.text)

# делаем get запрос
res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
print(res_get.text)

# делаем put запрос
res_put = requests.put(url='https://petstore.swagger.io/v2/pet/',data=json.dumps(input_pet_to_update), headers=header)
print(res_put.text)

# делаем delete запрос
res_delete = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
print(res_delete.text)

