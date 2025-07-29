
s  = 'switchport trunk allowed vlan 1,23,998,999,1001'
lst_split = s.split()
print(lst_split)
a = lst_split[-1]
print(a, type(a))
lst = (lst_split[-1].split(","))
for i in lst:
    print(i)

test_str = "one/two/three/four/five"
mod_str = test_str.split("/")
print(" | ".join(mod_str))

