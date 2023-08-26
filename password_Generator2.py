import random
import string
def generate_pas(min_length, numbers=True, special_characters=True):
    
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    character = letters
    if numbers:
        character += digits
    if special_characters:
        character +=special
    
    password=""
    while len(password)<=min_length:
         new_char = random.choice(character)
         password+=new_char
    return password
min_length= int(input("Enter the number"))
has_num= input("do you want the number in pass word (y/n)? ").lower()== "y"
has_sp= input("do you want the special in pass word (y/n)? ").lower()== "y"

password = generate_pas(min_length,has_num,has_sp)
print(password)
        
    

