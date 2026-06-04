def create_txt_file(name):
    with open(f"{name}.txt", "w") as f:
        f.write("")
    print(f"{name}.txt fayli yaratildi!")


create_txt_file(input("Fayl nomini kiriting: "))
