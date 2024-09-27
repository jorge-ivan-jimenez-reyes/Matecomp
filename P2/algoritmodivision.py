def division(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser 0")
    
    if a == 0:
        cociente = 0
        residuo = 0
    else:
        r = abs(a)  # valor absoluto de a
        q = 0
        
        while r >= b:
            r -= b
            q += 1
        
        if a > 0:
            cociente = q
            residuo = r
        elif a == 0:
            cociente = -q
            residuo = 0
        else:
            cociente = -q - 1
            residuo = b - r
    
    return cociente, residuo

# Ejemplo de uso
a = 10
b = 3
cociente, residuo = division(a, b)
print(f"Cociente: {cociente}, Residuo: {residuo}")
