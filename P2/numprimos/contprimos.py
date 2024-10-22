import math

def contar_primos(n):
    if n < 2:
        return 0

    # Crear un arreglo booleano para marcar los números primos
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # El 0 y el 1 no son primos

    # Criba de Eratóstenes
    for p in range(2, int(math.sqrt(n)) + 1):
        if es_primo[p]:
            for i in range(p * p, n + 1, p):
                es_primo[i] = False

    # Contar los números primos
    contador = 0
    for i in range(2, n + 1):
        if es_primo[i]:
            contador += 1

    return contador

# Ejemplo de uso
def main():
    n = int(input("Ingresa un número: "))
    print(f"El número de primos menores o iguales a {n} es: {contar_primos(n)}")

if __name__ == "__main__":
    main()
