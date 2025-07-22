# перевод из десятичной в двоичную
a = 255
print(bin(a)) # 0b11111111

# перевод из двоичной в десятичную
b = '1111'
print(int(b, 2)) # 15

# перевод из шестнадцатеричной в десятичную
c = "ff"
print(int(c, 16)) #255

# перевод из  десятичной в шестнадцатеричную
print(hex(252)) #0xfc

int_from_hex = int(c, 16)
bin_from_int = bin(int_from_hex)
print(bin_from_int) #0b11111111

# перевод из шестнадцатеричной в десятичную
print(int("0x11",16))  #17

# можно так вывести версию python, которая используется в системе(venv-e)
import sys
print(sys.version_info) #sys.version_info(major=3, minor=11, micro=2, releaselevel='final', serial=0)

####### строки в python########

tunnel_template = '''
    interface Tunnel0
    ip address 10.1.1.1 255.255.255.0
    ip mtu 1416
    ip ospf hello-interval 5

'''

print(tunnel_template)

# Конкатенация строк встроенная в python
a = "one " "two"
print(a) #one two

# тогда tunnel_template можно записать так:
tunnel_template = (
    "interface Tunnel0\n"
    "ip address 10.1.1.1 255.255.255.0\n"
    "ip mtu 1416\n"
    "ip ospf hello-interval 5\n"
)
print(tunnel_template)

#### индексы / срезы строк ######
#######012345678910...
cmd = 'interface Gi0/0'
print(cmd[0]) #i
print(cmd[-1]) #0
print(cmd[0:]) #interface Gi0/0
print(cmd[1:5])  #nter

index = 2
count = 5
print(cmd[index: index + count]) #terfa
print(cmd[:7]) # interfa

s = '0123456789'
print(s[::2]) #02468 - сначала до конца с шагом 2

#из десятичного получить двоичное и срезать '0b' с начале такой строки
num = 255
bin_num = bin(num) #"0b11111111"
print(bin_num[2:]) #   11111111

print(len(cmd)) #15  - все символы с пробелом

print(len("\nabc")) #4 - длина \n - выступает за один символ - whitespace

#строковые методы #####
print(cmd.upper()) #INTERFACE GI0/0

print(cmd.lower()) #interface gi0/0
