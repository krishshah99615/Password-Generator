import keyboard
import random
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
   

if __name__ == '__main__':
    install('pyperclip')
import pyperclip as pc
import time

String_alfa="a b c d e f g h i j k l m n o p q r s t u v w x y z "
String_alfa_cap="A B C D E F G H I J K L M N O P Q R S T U V W Z Y Z"
String_dig="1 2 3 4 5 6 7 8 9 0 "
String_sp="~ ! @ # $ % ^ & * ( ) _ +"


l1=String_alfa.split()
l2=String_alfa_cap.split()
l3=String_dig.split()
l4=String_sp.split()

combi=[]

for i in range(1000):
   combi.append(random.choice(l2)+random.choice(l1)+random.choice(l3)+random.choice(l4)+random.choice(l2)+random.choice(l3)+random.choice(l4)+random.choice(l1)+random.choice(l3)+random.choice(l4)+random.choice(l1))


password=random.choice(combi)


pc.copy(password)  


import datetime
now = datetime.datetime.now()

f= open("PL.txt","a")
f.write("\n "+str(now)+" Password: "+ password)
f.close()
