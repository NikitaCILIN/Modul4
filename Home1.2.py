from salary_file import data

#with open("path", "w") as fh:
    #fh.write(("Alex Korp,3000/nNikita Borisenko,2000/nSitarama Raju,1000"))
#def total_salary(path):
    #try:
        #with open(path, 'r', encoding='utf-8') as file:  #Ми відкриваємо файл за допомогою менеджера контексту with, вказуючи кодування utf-8 для зчитування файлу.
            #lines = file.readlines()
            #salaries = [int(line.strip().split(',')[1]) for line in lines] #Читаємо рядки файлу та розділяємо їх за комами, витягуючи зарплати розробників.
            #total_sum = sum(salaries) #Обчислюємо загальну суму
            #average_salary = total_sum / len(salaries) # та середню заробітну плату
            #return (total_sum, average_salary)
    #except FileNotFoundError:
    #    return "Файл не знайдено"
    #except Exception as e:
    #    return "Виникла помилка: " + str(e) 
         
def total_salary(data):
    try:
        lines = data.strip().split('\n')

        total_salary = 0
        num_developers = 0

        for line in lines:
            name, salary_str = line.strip().split(',')
            salary = int(salary_str)
            total_salary += salary
            num_developers += 1

        if num_developers == 0:
            raise ValueError("Дані не містять інформації про заробітні плати розробників.")

        average_salary = total_salary / num_developers

        return total_salary, average_salary

    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Помилка: {e}")

    

total, average = total_salary(data)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
