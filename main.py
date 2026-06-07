def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0 ga bo'lish mumkin emas"
    return a / b

while True:
    print("\n1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")
    print("5. Chiqish")

    choice = input("Tanlang: ")

    if choice == "5":
        break

    a = float(input("1-son: "))
    b = float(input("2-son: "))

    if choice == "1":
        print(add(a, b))
    elif choice == "2":
        print(subtract(a, b))
    elif choice == "3":
        print(multiply(a, b))
    elif choice == "4":
        print(divide(a, b))
