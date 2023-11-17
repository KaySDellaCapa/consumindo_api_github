import requests

print("GitHub Users")

username = input("Qual o nome do usúario: ")

print(username)

url = f"https://api.github.com/users/{username}"

response = requests.get(url)
data = response.json() 

if response.status_code == 200:
    #print(data)
    print(f"Nome completo: {data['name']}")
    print(f"Bio: {data['bio']}")
    print(f"Localização: {data['location']}")
    print(f"Seguindo: {data['following']}")
    
else:
    print("Nenhum usuario encontrado")