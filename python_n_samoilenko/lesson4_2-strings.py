######### lesson 4_2 - Методы строк, форматирование строк #########
###################################################################

st = 'interface Gi0/0'
print(st.upper()) #INTERFACE GI0/0
print(st.lower())  #interface gi0/0

print(st.startswith("int")) #True
print(st.startswith("Interface")) #False

print(st.endswith("0/0")) #True
print(st.endswith("0/1")) #False

print(st.startswith("nterface", 1)) #True

s = " switchport mode access"
print(s.startswith("switchport")) #False - потому как исходная строка начинается с пробела
# поэтому чтобы было True нужно переписать так:
print(s.startswith("switchport", 1))#True
#Данному методу можно передать кортеж

print(s.startswith(("router"," switch"))) #True

# метод count() - возвращает количество вхождений подстроки в строке

let = "o"
print(s.count(let)) #2

ip = "10.1.1.1"
print(ip.count(".")) #3

print(ip.count(".") == 3) #True

####print()  - в питоне строки вывести можно через запятую
a = "hello"
b = "world"
print(a,b) #hello  - здесть пробел м/у a  и b ставится из-за print()

# или всегда работает способ через суммирование строк:
print(a + " " + b) #hello world

# метод find() - возвращает индекс первого вхождения подстроки в строке, иначе -1
s = " switchport mode access"
print(s.find("w")) # 2
print(s.find("R")) # -1

# метод replace() - замена одной подстроки второй подстрокой
intf  = "interface Gi0/0"
print(intf.replace("Gi", "Fa")) #interface Fa0/0 - полученная строка является новой
print(intf) #interface Gi0/0

# 3-й параметр - количество замен слева направо
print(intf.replace("i", "TEST", 1)) #TESTnterface Gi0/0

#replace() можно применять паровозиком - т.к replace возвращает строку
print(intf.replace("i", "I", 1).replace("0", " ")) #Interface Gi /

#метод strip() - удаление всех whitespaces символов
cmd = "\n\tinterface Gi0/0\n\n\t"
print(cmd) # вывод с табуляцией и переносом строк
print(cmd.strip()) # подрезает все переносы - выводя с начала новой строки

str1 = "[]werw2ewr]" 
print(str1.strip('[]')) #werw2ewr - удаление всех '[' ']' только в начале и конце строки

# если для strip() указаны символы удаления и они не начальные/конечные, то они не удаляются:

str2 = "fdsf[]werewr[]"
print(str2.strip('[]')) #fdsf[]werewr

#метод rstrip()
cmd = "\n\tinterface Gi0/0\n\n\t"
print(cmd.rstrip()) # удалит все отступы справа в строке (\n\n\t)


#метод lstrip()
cmd = "\n\tinterface Gi0/0\n\n\t"
print(cmd.lstrip()) # удалит все отступы слева в строке (\n\t)

# метод split()  -разбивает строку на коллекцию строк - список
cmd = 'switchport trunk allowed vlan 1,2,3,4,5\n'

print(cmd.split()) #['switchport', 'trunk', 'allowed', 'vlan', '1,2,3,4,5']
new_cmd = cmd.split()
print(new_cmd[-1]) #1,2,3,4,5

vlans = "1,2,3,4,5"
print(vlans.split(",")) #['1', '2', '3', '4', '5']

ip = "10.1.1.1"
print(ip.split(".")) #['10', '1', '1', '1']

### форматирование строк ###
### метод format()  - используется для написания шаблонов#####

iface = '''
interface Eth-Trunk126.{iface}
 vlan-type dot1q {vlan}
 description {vpn_name}
 ip binding vpn-instance {vpn_name}
 ip address {ip_addr}
 statistic enable
 qos car cir {speed} cbs 486200 green pass red discard inbound
 qos car cir {speed} cbs 486200 green pass red discard outbound

'''
print(iface.format(iface=2752, vlan=2752, vpn_name="CISZ_BELY_02",  ip_addr="10.217.15.49 255.255.255.240", speed=2600))

# interface Eth-Trunk126.2752
#  vlan-type dot1q 2752
#  description CISZ_BELY_02
#  ip binding vpn-instance CISZ_BELY_02
#  ip address 10.217.15.49 255.255.255.240
#  statistic enable
#  qos car cir 2600 cbs 486200 green pass red discard inbound
#  qos car cir 2600 cbs 486200 green pass red discard outbound

###  В format() можно передавать список - например из 4-х элементов:
ip_template = "{} {} {} {}"
print(ip_template.format("192", "168", "100", "1")) # получим: 192 168 100 1

output = "{} {} {}"
print(output.format("Fa0/1", "10.1.1.1", "255.255.255.0"))
print(output.format("Fa0/15", "10.1.1.1", "255.255.255.0"))
# Fa0/1 10.1.1.1 255.255.255.0
# Fa0/15 10.1.1.1 255.255.255.0 <-- при format() по умолчанию выравнивание для чисел по пр краю, для строк - по левому

print("#"*20)
output2 = "{} {} {}\n"*2
print(output2.format("Fa0/1", "10.1.1.1", "255.255.255.0","Fa0/15", "192.168.100.1", "255.255.255.0" ))

# получили сдвинутые столбцы, а хочется ровно табличкой
# Fa0/1 10.1.1.1 255.255.255.0
# Fa0/15 192.168.100.1 255.255.255.0
# для этого в {} указывается {:число - ширина столбца}

output3 = "{:10} {:20} {:20}\n"*2
print(output3.format("Fa0/1", "10.1.1.1", "255.255.255.0","Fa0/15", "192.168.100.1", "255.255.255.0" ))

#теперь выводит с выравниванием красиво:
# Fa0/1      10.1.1.1             255.255.255.0       
# Fa0/15     192.168.100.1        255.255.255.0    