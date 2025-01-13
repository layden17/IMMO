from random import randint

def polynome(n):
    tab = []
    for i in range(n+1):
        element = randint(-100, 100)
        tab.append(element)
    return tab

def affiche(tab):
    print("mon tableau : ")
    for i in tab:
        print(str(i)+" ")

def somme(p1,p2):
    tabSomme = []
    n = max(len(p1),len(p2))
    for i in range(n) :
        e1 = p1[i] if len(p1)>i else 0
        e2 = p2[i] if len(p2)> i else 0
        tabSomme.append(e1+e2)
    return tabSomme

def diffenrence(p1,p2):
    tabDiff = []
    n = max(len(p1),len(p2))
    for i in range(n) :
        e1 = p1[i] if len(p1)>i else 0
        e2 = p2[i] if len(p2)> i else 0
        tabDiff.append(e1-e2)
    return tabDiff


def decalage(p1,k):
    tabDecale = []
    for i in range(k):
        tabDecale.append(0)
    for element in p1:
        tabDecale.append(element)
    return tabDecale

def prodfac(p1,c,k):
    tabProd = decalage(p1,k)
    for i in range(len(tabProd)) :
        tabProd[i] = tabProd[i] * c
    return tabProd

def produit(p1,p2):
    tabProduit = []
    if len(p1)<len(p2):
        p = p1
    else:
        p = p2
    for i in range(len(p)):
        tab = prodfac(p1,p[i],i)
        tabProduit = somme(tabProduit,tab)
    return tabProduit


def karatsuba(A, B):
    # Si les longueurs de A et B sont différentes, complétez-les avec des zéros pour les rendre de même longueur
    if len(A) != len(B):
        max_len = max(len(A), len(B))
        A = [0] * (max_len - len(A)) + A
        B = [0] * (max_len - len(B)) + B

    # Si la longueur de A est égale à 1, effectuez une multiplication simple
    if len(A) == 1:
        return [int(A[0]) * int(B[0])]
    else:
        m = (len(A) + 1) // 2
        A0 = A[:m]
        A1 = A[m:]
        B0 = B[:m]
        B1 = B[m:]

        K2 = karatsuba(A1, B1)
        K0 = karatsuba(A0, B0)

        A0_A1_sum = [int(x) + int(y) for x, y in zip(A0, A1)]
        B0_B1_sum = [int(x) + int(y) for x, y in zip(B0, B1)]
        aux = karatsuba(A0_A1_sum, B0_B1_sum)
        K1 = [int(x) - int(y) - int(z) for x, y, z in zip(aux, K0, K2)]

        K1 = [0] *  m + K1
        K2 = [0] * m + K2

        res = K2 + K1 + K0
        return res


p1 = polynome(3)
p2 = polynome(1)

print("affiche p1 et p2")
affiche(p1)
affiche(p2)

print("produit")
prod = produit(p1,p2)
affiche(prod)

print("karatsuba")
kara = karatsuba(p1,p2)
affiche(kara)