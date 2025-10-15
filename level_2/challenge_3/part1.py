dict_1={'First name':'Jane', 'Last name': 'Doe', 'Age':42, 'Employed': 'Yes'}
dict_2={'First name':'Tom', 'Last name': 'Smith', 'Age':18, 'Employed': 'Yes'}
dict_3={'First name':'Mariam', 'Last name': 'Coulter', 'Age':66, 'Employed': 'No'}
dict_4={'First name':'Gregory', 'Last name': 'Tims', 'Age':8, 'Employed': 'No'}
people=[]
for groups in (dict_1,dict_2,dict_3,dict_4): people.append(groups)

def printing_(dictionary):
  for info in dictionary:
    for keys,values in info.items():
      print(f'{keys}: {values}')

def get_user_action():
  while True:
    action=input('Would you like to add or remove a person from your records: ')
    if action.lower() in ['add', 'remove']:
      return action
    else:
      print('Please enter either add or remove')

def new_details(dictionary):
  print('please enter the details of the person you would like to add to the record')
  First_name=input('First name: ')
  Last_name=input('Last name: ')
  Age=int(input('Age: '))
  Employed=input('Employed (enter Yes or No): ')
  new_person={'First name':First_name, 'Last name': Last_name, 'Age':Age, 'Employed': Employed}
  dictionary.append(new_person)
  return dictionary

def user_remove(dictionary):
  while True:
    person_to_remove=input('What is the name of the person you would like to remove? ')
    matching = [person for person in dictionary if person['First name'].lower() == person_to_remove.lower()]
    if matching:
      for person in matching:
        dictionary.remove(person)
        print(f"{person_to_remove} has been removed.")
        return dictionary
    else:
      print('sorry this person is not in your records, try writing just their first name')
      continue

def updating_records(HR_records):
  print('this is a programme to help you update your HR records')
  print('you can specify whether you would like to exit or continue after each update')
  _continue=True
  while _continue:
    action=get_user_action()
    if action.lower()=='add':
      HR_records=new_details(HR_records)
      printing_(HR_records)
    else:
      HR_records=user_remove(HR_records)
      printing_(HR_records)
    

  
    quit_=input('Would you like to exit the programme(Y/N): ')
    if quit_ in ['Y','N']:
      if quit_=='Y':
        _continue=False
      else:
        _continue=True
    
  
updating_records(people)
