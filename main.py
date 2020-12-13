# http://trinary.su/projects/setunws/

import urllib
f = urllib.urlopen("http://web.ctf.msk.ru/ctn2020finalcvxbud/Ternary/TheNotesOfGenius")
f = str(f.read())
f = f.replace("-1", "-")
f = f.replace("1","+")
f = f.split(" ")
print f


def val(number_sequence, base):    
    return sum(int(n) * base ** p for p, n in enumerate(reversed(number_sequence)))

def balanced_ternary_value(number):
    return val([(-1 if c == '-' else (1 if c == '+' else 0))
                for c in str(number)], 3)



for i in f:
    print balanced_ternary_value(i)
    

