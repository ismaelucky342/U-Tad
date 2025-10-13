import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Ejemplo de API de prueba
data = {"title": "Prueba", "body": "Contenido", "userId": 1}

# GET
r_get = requests.get(url)
print("GET:", r_get.status_code)

# POST
r_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print("POST:", r_post.status_code, r_post.json())

# PUT
r_put = requests.put(url, json=data)
print("PUT:", r_put.status_code, r_put.json())

# DELETE
r_delete = requests.delete(url)
print("DELETE:", r_delete.status_code)

# HEAD
r_head = requests.head(url)
print("HEAD:", r_head.headers)

# OPTIONS
r_options = requests.options(url)
print("OPTIONS:", r_options.headers)

# PATCH
r_patch = requests.patch(url, json={"title": "Actualizado"})
print("PATCH:", r_patch.status_code, r_patch.json())