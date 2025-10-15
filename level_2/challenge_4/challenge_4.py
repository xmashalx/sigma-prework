animals=[
  {'name': 'Fluffy', 'type':'dog'},
  {'name': 'Parsley', 'type':'dog'},
  {'name': 'Ginger', 'type':'cat'},
  {'name': 'Biscuit', 'type':'cat'},
  {'name':'Poppet', 'type':'cow'}
]

def say_hello_to_pets(pets):
  for pet in pets:
    pet_name=pet['name']
    pet_type=pet['type']
    if pet_type=='dog':
      hello_message='Woof'
    elif pet_type=='cat':
      hello_message='Meow'
    else:
      raise Exception("Sorry we only greet cats and dogs")
    print(f"{hello_message}, {pet_name}!")

say_hello_to_pets(animals)
