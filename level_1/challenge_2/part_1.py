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


name=input("enter your name: ")
surname=input('enter your surname: ')

print(reverse_name(name))
print(intersperse_name(name,surname))
print(format_name(name,surname))
