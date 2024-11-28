import string
import random

def passwordGen():
    s1 = string.ascii_uppercase
    
    s2 = string.ascii_lowercase
    
    s3 = string.digits #digits fro 0-9
    
    s4 = string.punctuation # special characters
   
    passLen = int(input("Enter password length: "))
    s = []
    s.extend(list(s1))  #The extend() method adds the specified list elements (or any iterable) to the end of the current list.
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s) 
    pas = ("".join(s[0:passLen]))
    print(pas)

passwordGen()