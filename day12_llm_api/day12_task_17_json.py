import json

with open("response_demo.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)

print(data["model"])
print(data["answer"])
print(data["tokens"])