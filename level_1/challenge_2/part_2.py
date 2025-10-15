def reverse_name(name):
  return name[::-1]


def intersperse_name(name,surname):
  name=reverse_name(name)
  result=''
  for a, b in zip(name,surname):
    result+=''.join(a+b)
  return result + name[len(surname):] + surname[len(name):]


def format_name(name,surname):
  string=intersperse_name(name,surname)
  username= string[:len(string)//2] + ' ' + string[len(string)//2:]
  return username.title()

import random
def rand_username():
  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  string = ''.join(random.choices(chars, k=10))
  username=string[:len(string)//2] + ' ' + string[len(string)//2:]
  return username.title()

def optional_username_gen():
  print('welcome to the username generator,below are options for generating a username: ')
  options = ['option 1: create username based on your name','option 2: generate a random username']
  for option in options:
    print(option)
  choice=input('please enter the number corresponding to your chosen option: ')
  if choice in ['1','2']:
    if choice=='1':
      name=input("enter your name: ")
      surname=input('enter your surname: ')
      username=format_name(name,surname)
    else:
      username=rand_username()
    print(f'your username is: {username}')
    return username
  else:
    print('ERROR: please enter either the number 1 or 2')
  
print(optional_username_gen())
