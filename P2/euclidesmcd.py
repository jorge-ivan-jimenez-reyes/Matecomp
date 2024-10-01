def mcd(a, b):
    c = abs(a)
    d = abs(b)
    print(f"Valores iniciales: c = {c}, d = {d}")
    
    while d != 0:
        r = c % d
        print(f"Residuo r = {c} % {d} = {r}")
        
        c = d
        d = r
        print(f"Nuevo valor de c = {c}, Nuevo valor de d = {d}")
    
    print(f"El MCD es: {abs(c)}")
    return abs(c)

a = 56
b = 42

print(f"El MCD de {a} y {b} es: {mcd(a, b)}")
