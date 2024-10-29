def yigindi_hisobla(a, b):
    return a + b

try:
    a = int(input("a = "))
    b = int(input("b = "))
    
    natija = yigindi_hisobla(a, b)
    
    print(f"Yig'indi: {natija}")

except ValueError:
    print("Iltimos, son kiriting!")