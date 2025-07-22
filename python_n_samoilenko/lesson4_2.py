# 04 часть 2 Методы сторк, форматирование строк
# строки нельзя менять на месте

# как проверить что строка начинается с некоторого  слова

cmd = "interface Gi0/0"
print(cmd.upper()) # INTERFACE GI0/0
print(cmd.lower()) # interface gi0/0

print(cmd.startswith("interface")) #True


# при передаче кортежа можно искать совпадения и так: 
# если строка начинается либо с int либо c switch например
print(cmd.startswith(("int", "switch"))) #True

# метод count - сколько раз встречается символ/подстрока в строке
print(cmd.count("i")) # 2

ip = '10.1.1.1'
print(ip.count(".")) #3 - столько раз в ip адресе стоит точка


#####вывод строк print()
a = "Hello"
b = "world"
print(a,b) #Hello world - это работает только из-за специфики print()
print(a + " " + b) #Hello world  + работает со строками всегда!

# Метод find - выводит наименьший индекс, с которого нашлась подстрока в исходной строке
cmd = 'disp ip routing-table'
index  = cmd.find("ip")
print(index ) #5
print(cmd[index:]) #ip routing-table

conf = "switchport mode access"
find_word = "mode"
ind = conf.find("mode")
print(conf[ind:]) #mode access
print(conf[ind:ind + len(find_word)]) #mode

# Метод replace - заменяет все вхождения одной подстроки на другую,
#  можно указать сколько раз производить замену (это 3й параметр)
iface = "interface Gi0/0"
new_iface = iface.replace("Gi", "Fa")
print(new_iface) # interface Fa0/0
print(iface) #interface Gi0/0 - исходная строка не меняется
###
iface = iface.replace("Gi", "Fa")
print(iface) # interface Fa0/0

iface = 'interface Fa0/0'
print(iface.replace("a","TEST")) # interfTESTce FTEST0/0 - меняет все разы a на TEST
print(iface.replace("a","TEST",1)) #interfTESTce Fa0/0 - один раз меняет a на TEST

print("*" * 50)

str1 = 'bla-bla-bla'
str2 = str1.replace("a","b")
print(str1)
print(str2) # blb-blb-blb
str1 = str1.replace("a", "zz")
print(str1)
print(str2)

# Метод replace можно применять паровозиком, т.к 
# при каждом применении метода возвращается измененная, но строка
str = "interface Gi0/0"
print(str.replace("i","I").replace("face","leg")) #Interleg GI0/0

# метод strip - по умочанию удаляет все whitespace символы
stroka = "\n\n\tInterface fastEthernet1/1\n"
print(stroka)  # в таком случае выведет так:
# 2 перевода строка и отступ слева(таб)
#        
# 
#       Interface fastEthernet1/1
print(stroka.strip()) #Interface fastEthernet1/1 - удадяет все табы и переводы строк
# для strip  можно передать в кавычках подстроку которую нужно удалить в начале и в конце исходной строки
str_ex1 = "[proba]"
print(str_ex1.strip("[]")) # proba
str_ex2 = "[werfew]qewr[]"
print(str_ex2.strip("[]")) # werfew]qewr - удалил '[' и  ']' в начале и в конце строки, в середине не удалил

# lstrip, rstrip
stroka = "\n\n\tInterface fastEthernet1/1\n"
print(stroka.lstrip())

print(stroka.rstrip())

# ##########################about tuple () ##############
# # var_tuple = ("swderf", "234", "var234")
# # print(var_tuple)
# # var_tuple[4] = 45

# ex_tuple = ("a", "b", 1, 2)
# print(ex_tuple, type(ex_tuple)) # ('a', 'b', 1, 2) <class 'tuple'>