with open("cats_file.txt", "w") as fh:
    fh.write("""60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5""")


#print(license)    



def get_cats_info(path):
    cats_info_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            cat_data = line.strip().split(',')
            if len(cat_data) == 3:
                cat_info = {"id": cat_data[0], "name": cat_data[1], "age": int(cat_data[2])}
                cats_info_list.append(cat_info)

        return cats_info_list

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдений.")
    except Exception as e:
        print(f"Помилка: {e}")

# Приклад використання:
cats_info = get_cats_info("cats_file.txt")
if cats_info is not None:
    print(cats_info)
