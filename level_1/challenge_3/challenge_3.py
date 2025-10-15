
def sum_to_n():
  #This function sums all numbers from 1 to n
  
  n=ask_user_for_number()
  sum=0
  for i in range(1,int(n)+1):
    sum+=i
  print(f'the sum of all numbers 1 to {n} is {sum}')
  return sum

      
  

def sum_to_n_35():
  #This function sums all numbers from 1 to n, 
  #if the numbers are multiples of 3 or 5

  n=ask_user_for_number()
  sum=0
  for i in range(1,int(n)+1):
    if i%3==0:
      sum+=i
    elif i%5==0:
      sum+=i
    else:
      sum+=0
  print(f'the sum of all multiples of 3 and 5 between 1 and {n} is {sum}')
  return sum

   

def product_to_n():
  #this function compuetes the product for all numbers 1 to n
  n=ask_user_for_number()
  product=1
  for i in range(1,int(n)+1):
    product=product*i
  print(f'the product of all numbers 1 to {n} is {product}')
  return product

  
  

def product_or_sum():

  print("please choose between the following options")
  options=['1. return the sum of all numbers between one and my number','2. return the product of all numbers between one and my number']
  for option in options:
    print(option)
  while True:
    opt=input('please enter the number corresponding to your chosen option: ')
    if opt in ['1','2']:
      if opt=='1':
        return sum_to_n()
        
      else:
        return product_to_n()
        
    else:
      print("Error please select the number 1 or 2 corresponding to the given options")
      continue
  
def ask_user_for_number():
  while True:
    number=input('please enter a number in digits: ')
    if number.isdigit():
      return number
    else:
      print('Error: you need to enter a number that uses the digits 0123456789')
      continue

print(product_or_sum())
