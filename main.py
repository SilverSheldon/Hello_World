choice = input("Вы входите в пещеру. Направо или налево? ")
if choice == "направо":
    print("Вы пришли к сокровищу!")
else:
    print("Вы встретили дракона")
    choice2 = input("Вступить в битву? (да/нет) ")
    if choice2 == "да":
        print("Вы победили!")
    else:
        print("Вы с позором убегаете...")