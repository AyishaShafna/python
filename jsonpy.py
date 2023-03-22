import json

with open ("sample.json") as f:
    python_dict = json.load(f)
    print (python_dict)
    for key,value in python_dict.items():
        print(key,"is",value)

    python_dict2 = {"name":"shana", "age":15, "class":9, "place":"calicut"}
    json_string = json.dumps(python_dict2)
    print(json_string)

    with open ("data.json","w") as f:
        json.dump(python_dict2,f)