a,b=str(input()), str(input())
if a in ("красный", "синий", "желтый") and b in ("красный", "синий", "желтый"):
    if (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
        print("фиолетовый")
    elif (a == "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
        print("оранжевый")
    elif (a == "желтый" and b == "синий") or (a == "синий" and b == "желтый"):
        print("зеленый")
    elif a == b: 
        print(a)
else:
    print("ошибка цвета")
