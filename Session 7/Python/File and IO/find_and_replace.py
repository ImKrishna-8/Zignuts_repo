with open("data.txt") as f:
    data = f.read()

data = data.replace("donkey","#####")
print(data)
with open("data.txt","w") as fl:
    fl.write(data)