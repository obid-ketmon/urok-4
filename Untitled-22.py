#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def intersection_of_sets(set1, set2):
    # Преобразуем списки во множества, чтобы исключить повторяющиеся элементы
    set1 = set(set1)
    set2 = set(set2)
    # Находим пересечение множеств и сортируем его
    result = sorted(set1.intersection(set2))
    return result

def main():
    try:
        n = int(input("Введите количество элементов первого множества (n): "))
        m = int(input("Введите количество элементов второго множества (m): "))

        if n <= 0 or m <= 0:
            print("Количество элементов должно быть положительным.")
            return

        set1 = []
        set2 = []

        # Вводим элементы первого множества
        print("Введите элементы первого множества через пробел:")
        set1 = list(map(int, input().split()))

        # Вводим элементы второго множества
        print("Введите элементы второго множества через пробел:")
        set2 = list(map(int, input().split()))

        # Находим пересечение множеств и выводим результат
        result = intersection_of_sets(set1, set2)
        if result:
            print("Числа, которые встречаются в обоих множествах без повторений и в порядке возрастания:")
            print(*result)
        else:
            print("Пересечение множеств пусто.")
    
    except ValueError:
        print("Ошибка: Введите целые числа.")

if __name__ == "__main__":
    main() 

