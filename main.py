import math

def getTypeTreeagle(a, b, c):
    if type(a) == str or type(b) == str or type(c) == str:
        return None
    if a <= 0 or b <= 0 or c <= 0:
        return None
    if ((a + b) < c) or ((b + c) < a):
        return None
    p = (a + b + c) / 2
    S = math.floor(math.sqrt((p * (p - a) * (p - b) * (p - c))))
    if S == 0:
        return None
    if a == b and b == c:
        return f"Треугольник с сторонами {a}, {b}, {c} - Равносторонний"
    elif (a == b and (a == b) != c) or (b == c and (b == c) != a):
        return f"Треугольник с сторонами {a}, {b}, {c} - Равнобедренный"
    else:
        return f"Треугольник с сторонами {a}, {b}, {c} - Разносторонний"
