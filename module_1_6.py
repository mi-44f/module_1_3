# Словари и множества
my_dict = {'masha': 2000, 'dasha': 2001, 'misha': 2002, 'dima': 2003, 'kolya': 2004}
print(my_dict)
print(my_dict['dima'])
print(my_dict.get('liza', 'а нету'))
del my_dict['kolya']
my_dict.update({'n111': 555, 'logika':False, 'cifra': 777})
print(my_dict)
print(type(my_dict))

my_set = {1,2,3,3,3,2,0,'bolt','vint',True,True,'vint','gaika'}
print(my_set)
my_set.add('new')
my_set.add(999)
print(my_set)
my_set.discard('les')
my_set.remove(3)
popik = my_dict.pop('misha')
print(popik)
print(my_set)
print(type(my_set))

# Дополнительное
grades = [[5,3,2,4,5,5,4], [1,5,2,4,3],[5,5,5,5,5,5],[4,5,4,5,4,5],[5,5,3,4,5,5,4,5]]
students = {'dima','misha','kolya','dasha','masha'}
print(type(grades))
print(type(students))
stud_list = list(students)
print(stud_list)
kol = len(stud_list)
print('dlina grada', kol)

obmen=100
while obmen>0:
    obmen=0
    for sind in range (0,kol-1):
        print(sind)
        if stud_list[sind] > stud_list[sind+1]:
            print('sind ', sind)
            print('stroki', stud_list[sind],' ',stud_list[sind+1])
            print('sravnim ', stud_list[sind] > stud_list[sind+1])
            helpp = stud_list[sind]
            stud_list[sind] = stud_list[sind+1]
            stud_list[sind+1] = helpp
            print(stud_list)
            obmen = obmen+1

print(stud_list)

itog = dict()

mesto = 0
for elt in grades:
    print('elt ', elt)
    sum_ocenok = 0
    for eltelt in elt:
        print('eltelt ', eltelt)
        sum_ocenok = sum_ocenok + eltelt
    sred_ocenka = sum_ocenok / len(elt)
    print('sred', sred_ocenka)
    itog[stud_list[mesto]] = sred_ocenka
    mesto = mesto + 1
    print(itog)