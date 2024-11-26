import requests
import pandas as pd

# # response = requests.get('https://fakestoreapi.com/products') # chama a api
# # data = response.json()
# # print(data)

# data = {
#     "title": "teste",
#     "price": 100.95,
#     "description": "teste",
#     "category": "men's test",
#     "image": "https"
# }
# response = requests.post
def get_api_data():
    response = requests.get(url)
    return response.json()

api_url = 'https://fakestoreapi.com/products'
data = get_api_data(api_url)
df = pd.DataFrame(data)
df.to.csv('dados_api.csv', index=False)
df.head()