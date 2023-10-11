import math
a = float(input("Masukkan koefisien a: "))
b = float(input("Masukkan koefisien b: "))
c = float(input("Masukkan koefisien c: "))

discriminant = b**2 - 4*a*c
if a !=0:
    print(f"Persamaan kuadrat {a}x² + {b}x + {c}")
    print("Determinannya =", discriminant)
    if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print("Memiliki akar berbeda")
            print("Akar x1 =", x1)
            print("Akar x2 =", x2)
            x1, x2
    elif discriminant == 0:
            x1 = -b / (2*a)
            print("Merupakan akar kembar")
            print("Akar =", x1)
            x1
    else:
            print("Merupakan akar imaginer")
            print(f"Akar x1 = {b} + √{discriminant} / 2*{a}")
            print(f"Akar x2 = {b} - √{discriminant} / 2*{a}")
            
else:
    print("Bukan merupakan persamaan kuadrat, karena nilai A = 0")

        
        
        







