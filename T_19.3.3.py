import requests
import json

# data
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

header = {'accept': 'application/json', 'Content-Type': 'application/json'}
# post
res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
print(res_post.text)

# get
res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
print(res_get.text)

# put
res_put = requests.put(url='https://petstore.swagger.io/v2/pet/',data=json.dumps(input_pet_to_update), headers=header)
print(res_put.text)

# check put
# res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
# print(res_get.text)
# delete
res_delete = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

# check delete
# res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
# print(res_get.text)
