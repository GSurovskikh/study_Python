import pickle

rooms = {
    'W':[],
    'A':["B","C"],
    "C":["A"],
    "B":["A","Z","E"],
    "E":["B","Z"],
    "Z":["B","E"]
}

#Сохранение(Сериализация)
binary_data=pickle.dumps(rooms)
with open('data.bin','wb') as f:
    f.write(binary_data)


#Загрузка(десериализация)
with open("data.bin",'rb') as f:
    binary_data = f.read()
new_rooms = pickle.loads(binary_data)

print(new_rooms)