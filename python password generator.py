import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't' , 'u', 'v', 'w', 'x', 'y', 'z'
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L',  'M',  'N', 'O',  'P',  'Q',  'R', 'S',  'T','U', 'X','Y','Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')' ,'*', '+']
print ("WELCOME TO THE PASSWORD GENARATOR")
n_Letters=int(input("How Many Letters You Want In Your Password?\n"))
n_Symbols=int(input("How Many Symbol You Want In Your Password?\n"))
n_Numbers=int(input("How Many Numbers You Want In Your Password?\n"))
Password_list = []
for i in range(1, n_Letters+1):
    char = random.choice(Letters)
    Password_list +=char
for i in range(1, n_Symbols+1):
    char = random.choice(Symbols)
    Password_list +=char
for i in range(1, n_Numbers+1):
    char = random.choice(Numbers)
    Password_list +=char
print(Password_list)
random.shuffle(Password_list)
print(Password_list)
Password=""
for char in Password_list:
    Password +=char
print(Password)
