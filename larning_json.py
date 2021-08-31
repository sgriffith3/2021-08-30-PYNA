import json
import yaml

with open("astros.json", "r") as spacey:
    txt = spacey.read()
    #print(txt)

    data = json.loads(txt)
    #print(data)
    #print(type(data))
    #print(data["people"])



pets = ["animals", {"dogs": 3, "cats": 2, "fish": None, "likes to play": True}]
#print(pets)
#print(type(pets))
fluffers = json.dumps(pets)
print(fluffers)
print(type(fluffers))

with open("pets.jso", "w") as f:
    json.dump(pets, f)
    
with open("pets.yml", "w") as fi:
    yaml.dump(pets, fi)
