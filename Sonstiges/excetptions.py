try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("ERROR")
except ValueError:
    print("ERROR")
