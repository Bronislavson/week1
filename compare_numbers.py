try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if num1 > num2:
        print(f"Первое число ({num1}) больше второго ({num2})")
    elif num1 < num2:
        print(f"Первое число ({num1}) меньше второго ({num2})")
    else:
        print(f"Оба числа равны ({num1})")

except ValueError:
    print("Пожалуйста, вводите только числа.")
