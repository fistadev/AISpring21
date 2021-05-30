try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(f'Your age is {age}')
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value!")