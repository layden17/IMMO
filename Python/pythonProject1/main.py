
tab = [0,1,2,4]
tab2 = [5,6,7,1,2,5]


def fonction(tab,nb):
    if nb in tab:
        return True
    else:
        return False

def fonction2(tab,tab2):
    tab3 =[]
    for nb in tab :
        tab3.append(nb)
    for nb2 in tab2 :
        if not nb2 in tab3 :
            tab3.append(nb2)
    return tab3

print(fonction(tab,0))
tab4 = fonction2(tab,tab2)
for nb in tab4 :
    print(nb)