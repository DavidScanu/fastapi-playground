import requests
import json

def pretty_print_json(data):
  print(json.dumps(data, indent=2, sort_keys=True))

item = {
  "id": 231234,
  "name": "David Bowie",
  "age": 50,
  "secret_name": "String"
}
# req = requests.post("http://localhost/api/heroes", json=item).json()

# print("Adding an item:")
# print(req)
print()
pretty_print_json(requests.get("http://localhost/api/heroes").json())
print()

# print("Deleting an item:")
# print(requests.delete("http://localhost/api/heroes/1").json())
# print(requests.get("http://127.0.0.1:8000/").json())