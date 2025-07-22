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

text = "Congratulation! I'm daddy!"
print(text)

config = """
        interface gig10/0
 ip address 192.168.100.1 255.255.255.0
 no shutdown
 ip mtu 1500


"""
print(config) # все отступы которые есть у нас в тройных кавычках так и выводит print():

#         interface gig10/0
#  ip address 192.168.100.1 255.255.255.0
#  no shutdown
#  ip mtu 1500

# неочевидная конкатенация строк
a = "test" " " "hello"
print(a) #test hello

# при написании можно строку разбить на части используя ( ) 
config1 = (
  "str1"
  "str2"
  "str3"

)
print(config1) #конкатенация в итоге сработает тоже - результат будет  str1str2str3

# часто будет  возникать задача вывести многострочный конфиг чтобы отступы не попадали в вывод

config2 = ( "\n"
    "interface gig0/0\n"
    "ip address 192.168.100.5 255.255.255.0\n"
    "no shutdown\n"
    "ip mtu "
      "1500\n"

)
print(config2 ) #print каждый \n считывает и преобразует в перевод строки, вывод такой:
#
# interface gig0/0
# ip address 192.168.100.5 255.255.255.0
# no shutdown
# ip mtu 1500

cmd = "interface FastEthernet 0/1"
print(cmd[0]) # i
print(cmd[-1])  # 1 
print(cmd[2:5]) #ter

# в качестве индексов для среза можно использовать арифметич выражения:
index = 2
count = 5

print(cmd[index: index + count]) # terfa
print(cmd[:7]) #interfa 0:7
print(cmd[-7:]) #net 0/1 -7:end

s = "0123456789"
print(s[0:9]) #012345678

print(s[0:9:2]) #02468 - 3 параметр - шаг
print(s[::2]) #02468 с начала до конца с шагом 2

num = 255
bin_num = bin(num) #0b11111111
print(bin_num[2:]) #11111111

print(len(cmd)) #26

print(len("\nabc")) #4 \n - считается как один символ

# функция как правило работает с разными типами данных, например, print()
# метод работает с определенным типом данных - str.upper()
print(cmd.upper()) #INTERFACE FASTETHERNET 0/1
 
print("1" * 8)  #'11111111'
print('#' * 50) ##################################################