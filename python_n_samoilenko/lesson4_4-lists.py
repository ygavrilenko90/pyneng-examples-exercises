##########################################
###### Методы списков - продолжение ######
##########################################

a = print(10) #10
print(a) #None - сама по себе функция print() ничего не возвращвет


#count() - возвращает количество вхождений элементов в списке
# Одни методы возращают значения:
vlans = [1, 10, 100, 1000]
a = print(vlans.count(10)) # count() возвращает значение, значит его можно присвоить переменной и вывести:
print(a) #1

#Другие методы НЕ возвращают значения:
print(vlans.append(22)) #None - метод append() поменял список на месте
print(vlans) #[1, 10, 100, 1000, 22]

print(vlans.sort()) #None
print(vlans)        #[1, 10, 22, 100, 1000]

#join() - из списка получить строку - метод join():
access = [
 'switchport mode access',
 'switchport access vlan 10',
 'switchport nonegotiate',
 'spanning-tree portfast']

print("\n".join(access))
# switchport mode access
# switchport access vlan 10
# switchport nonegotiate
# spanning-tree portfast

#split() - из строки получить список

data = "\n".join(access)
print(data.split("\n")) #['switchport mode access', 'switchport access vlan 10', 'switchport nonegotiate', 'spanning-tree portfast']

# pop() - удаление одного элемента по индексу - по умолчанию [-1]
# pop()  меняет список на месте и возвращает удаленный элемент
vlans = [1, 10, 100, 1000]
vlans.pop()
print(vlans) #[1, 10, 100]
vlans.pop(0)
print(vlans) #[10, 100]

# remove() - удаление первого доступного элемента по значению, метод ничего не возвращает
vlans = [1, 10, 100, 1000, 10]
vlans.remove(10)
print(vlans) #[1, 100, 1000, 10]

# ip_address = "10.217.31.81/28"
# print(ip_address.split("/")) #['10.217.31.81', '28']
# print(" ".join(ip_address.split("/"))) # 10.217.31.81 28

# vlans_test = "10, 20, 30"
# print(" ".join(vlans_test.split(","))) #10  20  30

config = [
"ip vpn-instance CISZ_OSIP_15",
"route-distinguisher 6.15.2.15:40818",
"apply-label per-instance",
"vpn-target 6697:4081863599 export",
"vpn-target 6697:4081863501 import",
]
print(" \n".join(config))
# str1 = (", ".join(config))
# print(str1.split(","))


# index() - возвращает индекс по переданному элементу списка
vlans = [10, 100, 101, 200, 10]
print(vlans.index(100)) #1

# copy() - создает копию текущего списка - новый объект
vlans_copy  = vlans.copy()
print(vlans_copy) #[10, 100, 101, 200, 10]
print(id(vlans), id(vlans_copy)) #138207301518192 138207305893200 - это реально разные объекты

#Аналогично для создания копии списка можно использовать создание среза:
vlans = [10, 100, 101, 200, 10]
vlans_c = vlans[:]
print(vlans, id(vlans), vlans_c, id(vlans_c)) #[10, 100, 101, 200, 10] 137559830244240 [10, 100, 101, 200, 10] 137559830213648

#Лирическое отступление: в python имя переменной - это ссылка на объект в памяти
#  например, a = 5 - в памяти создан объект класса int и на него ссылается переменная "a"
# поэтому когда присваиваем vlans2 = vlans1    "vlans2" - ссылается ровно на тот же объект что и vlans1
vlans1 = [1, 2, 3]
vlans2 = vlans1
print(vlans1) #[1, 2, 3]
print(vlans2) #[1, 2, 3]
# теперь если поменять vlans1 например, то поменяется и vlans2
vlans1.append(100)
print("-"*20)
print(vlans1) #[1, 2, 3, 100]
print(vlans2) #[1, 2, 3, 100]
print(id(vlans1), id(vlans2)) #128878303324912 128878303324912

# числа - неизменяемые объекты, поэтому при явном присваивании  b = a и смене "a", b не меняется
a = 5
b = a
a = 6
print(a, b) #6 5
# У переменных ссылающихся на числа  0-256 будут одинаковые id - эти числа заранее находятся в памяти python

a, b  = 17, 17; print(id(a), id(b)) #8934688 8934688 - id одинаковые

c, d = 257,257; print(id(c), id(d)) #131732213594064 131732213594096 -id уже разные

a = b = 1000
print(id(a), id(b)) # id одинаковые 130958917199568 130958917199568, т.к a=b и переменные ссылаются на один объект