test_list = ['apple', 'orange', 'baseball', 'tiger']
test_dict = {
  'a': 1,
  'b': 2,
  'c': 3
  }
list_1 = ["vanilla", "cherry"]
list_2 = ["cake", "ice_cream"]
list_1a = ["vanilla", "cherry", "pistachio"]

def list_sayer(test_list):
  index = 0
  output_str = None
  if test_list == []:
    print ('The list is empty.')
    return False
  else:
    for item in test_list:
      output_str = item
      print(f'Your list item is: {output_str} and it is at index: {index}')
      index += 1
    return True

print(list_sayer(test_list))
print(list_sayer([]))

def dict_sayer(test_dict):
  if test_dict == {}:
    print('Your dictionary is empty.')
    return False
  else:
    for keys, values in test_dict.items():
      print(f'Your key is: {keys}, and your value is: {values}.')
    return True

print(dict_sayer(test_dict))
print(dict_sayer({}))

def greatest(test_dict):
  for keys, values in test_dict.items():
    if values == max(test_dict.values()):
      return (keys, values)

print(greatest(test_dict))

def zipper(list_1, list_2):
  dict_a = {}
  list_a = [] 
  tuple_a = () 
  if len(list_1) == len(list_2):
    list_a = list(zip(list_1, list_2))
    dict_a.update(list_a)
    return dict_a   
  else:
    tuple_a = (list_1, len(list_1), list_2, len(list_2))
    return tuple_a

print(zipper(list_1, list_2))
print(zipper(list_1a, list_2))