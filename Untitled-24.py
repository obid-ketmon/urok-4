
#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


def max_berries_harvest(a):
    n = len(a)
    left = [0] * n
    right = [0] * n

    # Вычисляем максимальное количество ягод на i-ом кусте и его левых соседях
    left[0] = a[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], a[i] + (left[i - 2] if i >= 2 else 0))

    # Вычисляем максимальное количество ягод на i-ом кусте и его правых соседях
    right[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], a[i] + (right[i + 2] if i <= n - 3 else 0))

    # Находим максимальное количество ягод, которое можно собрать на i-ом кусте и его соседях
    max_harvest = 0
    for i in range(n):
        max_harvest = max(max_harvest, max(left[i], right[i]))

    return max_harvest

def main():
    try:
        # Чтение входных данных
        n = int(input("Введите количество кустов черники: "))
        if n <= 0:
            print("Количество кустов должно быть положительным.")
            return

        print("Введите количество ягод на каждом кусте черники, разделяя числа пробелами:")
        a = list(map(int, input().split()))

        if len(a) != n:
            print("Количество чисел должно быть равно введенному количеству кустов.")
            return

        # Вызываем функцию для нахождения максимального количества ягод
        max_harvest = max_berries_harvest(a)

        print(f"Максимальное количество ягод, которое можно собрать за один заход собирающим модулем: {max_harvest}")

    except ValueError:
        print("Ошибка: Введите корректные целые числа.")

if __name__ == "__main__":
    main()
