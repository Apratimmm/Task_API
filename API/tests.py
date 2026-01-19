
import requests

data1= {
    'username':'Lord Apratim',
    'password':'apratim'
    }

data2= {
    'username':'Apratim',
    'password':'Apratim'
    }

token1 = '9eb1689c676b569818bd2475337da2c21521a0a5'

token2 = '177e84a7f8ff919451192b22e290ff4b95be1e42'

# response = requests.post(
#     "http://127.0.0.1:8000/auth/login/?next=/", data = data1)
# print(response.cookies.get('sessionid'))

# response = requests.post(
#     'http://127.0.0.1:8000/token/', data=data2
# )
# print(response.json())
# token2 =  "177e84a7f8ff919451192b22e290ff4b95be1e42"
# response = requests.get('http://127.0.0.1:8000/users/',headers={'Content-Type':'application/json','Authorization':f'Bearer {token2}'})
# print(response.json())

# response  = requests.post('http://127.0.0.1:8000/access_token/',data=data2)
# print(response.json())
#
# {
#   'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2Nzk2MTQ3OSwiaWF0IjoxNzY3ODc1MDc5LCJqdGkiOiI0ZWRkNWEyOTdlODQ0MjQ5ODFjZGVmN2QwOWI2NjZkMCIsInVzZXJfaWQiOiIxIn0.p9-n7F1mZby6OK4m7Q6v3GIJAUFnySKp6oCvFsUxGyI',
#   'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY3ODc1MTI5LCJpYXQiOjE3Njc4NzUwNzksImp0aSI6IjBlYzQ3MWQzYTQxNzRhNDY5NTdlNWZiMWI0ZTQyY2ZhIiwidXNlcl9pZCI6IjEifQ.QO5RZlmjxXCZKiek9-5uM_W-AX4TFOlctgpQZXioPL8'
# }

# response = requests.post(
#     "http://127.0.0.1:8000/refresh_token/", data = {'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2Nzk2MTQ3OSwiaWF0IjoxNzY3ODc1MDc5LCJqdGkiOiI0ZWRkNWEyOTdlODQ0MjQ5ODFjZGVmN2QwOWI2NjZkMCIsInVzZXJfaWQiOiIxIn0.p9-n7F1mZby6OK4m7Q6v3GIJAUFnySKp6oCvFsUxGyI'})
# print(response.json())

# response = requests.get('http://127.0.0.1:8000/users/', headers={'Authorization': 'Bearer {}'.format("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY3ODc2MTc1LCJpYXQiOjE3Njc4NzU4NzUsImp0aSI6ImQ0MWUyZDg2MWFiYzRiY2Y5ZmU4ODg0ZTBmNGRjZTQ2IiwidXNlcl9pZCI6IjEifQ.m2fhROrtH68kSepFs23hsx5ACL3w7XX8V2lW1Tzo12s")})
# print(response.json())