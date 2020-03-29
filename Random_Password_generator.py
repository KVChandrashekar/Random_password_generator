#It's a PYTHON program that generates the password randomly using lettes, special symbols and numbers
#basically length of the password ranges from 9-13
#generated password changes everytime as it runs again and again


from random import*

print(('Password_Generator').center(50,'-'))

new_password=''

pos=0

s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','A','B','C','D','E','F','G','H','I','J',
   'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

r=randint(9,13)                         #here you can change the length of the password accordingly

while pos <(r):
    digit = randrange(10)
    new_password += choice(str(digit)+choice(s)+choice([letter.upper() for letter in s]))
    pos+=1

print(f"New Password: '{new_password}'\n Password Generated and its 100% safe")

