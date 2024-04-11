def exercicio(n1, n2, n3):
    if n1 > n2 and n2 > n3:
        return(n1+n2)
    elif n1 > n2 and n3 > n2:
        return(n1+n3)
    elif n2 > n1 and n3 > n1:
        return(n2+n3)
    elif n2 > n1 and n1 > n3:
        return(n2+n1)
    elif n3 > n1 and n1 > n2:
        return(n3+n1)
    else:
        return(n3+n2)

assert 10 == exercicio(2, 4, 6), "n3: n2>n1 - total deveria ser 10 (6 + 4)"
assert 10 == exercicio(4, 2, 6), "n3: n1>n2 - total deveria ser 10 (6 + 4)"
assert 8 == exercicio(1, 5, 3), "n2: n3>n1 - total deveria ser 8 (5 + 3)"
assert 8 == exercicio(3, 5, 1), "n2: n1>n3 - total deveria ser 8 (5 + 3)"
assert 9 == exercicio(7, 1, 2), "n1: n3>n2 - total deveria ser 9 (7 + 2)"
assert 9 == exercicio(7, 2, 1), "n1: n2>n3 total deveria ser 9 (7 + 2)"
resultado = exercicio(-1, -1, -2)
assert -2 == resultado, "n1: n2>n3 total deveria ser -2 (-1-1), mas foi {res}".format(res=resultado)


# n1 = float(input("digite um número: "))
# n2 = float(input("digite outro: "))
# n3 = float(input("outro de novo: "))
# if n1 > n2 and n2 > n3:
#     print (n1 + n2)
# elif n1 > n2 and n3 > n2:
#     print (n1 + n3)
# elif n2 > n1 and n3 > n1:
#     print (n2 + n3)
# elif n2 > n1 and n1 > n3:
#     print (n2 + n1)
# elif n3 > n1 and n1 > n2:
#     print (n3 + n1)
# else:
#     print (n3 + n2)
