def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    return_tuple = (0, -1)

    # якщо елемент пошуку > ніж максимальний елемент масиву, повертаємо (0, -1)
    if upper_bound < x:
        return return_tuple

    i = 0
    while low <= high:
        i += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return_tuple = (i, arr[mid])
            return return_tuple

    # якщо елемент не знайдений
    return_tuple = (i, upper_bound)
    return return_tuple


if __name__ == '__main__':
    arr = [3.5, 4.59, 11.341, 25.351, 33.4, 46.8, 51.55, 63.78, 77, 89.5, 98.2]
    x = 4.59

    result = binary_search(arr, x)

    if result != (0, -1):
        print("Кількість ітерацій пошуку =", result[0],
              " Верхня межа дорівнює ", result[1])
    else:
        print("Кількість ітерацій пошуку в масиві = 0.",
              "Елемент пошуку більший, ніж максимальна верхня межа масива.")