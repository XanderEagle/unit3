import math


def triangle(a, b, c):
   return (a + b + c) / 2


def main():
    a = 6
    b = 8
    c = 10
    s = triangle(a, b, c)
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(A)

main()
