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

def dict_sayer(test_dict):
  if test_dict == {}:
    print('Your dictionary is empty.')
    return False
  else:
    for keys, values in test_dict.items():
      print(f'Your key is: {keys}, and your value is: {values}.')
    return True

def greatest(test_dict):
  for keys, values in test_dict.items():
    if value == max(test_dict.values()):
      return (keys, values)

def zipper(list_1, list_2):
  dict_a = {}
  list_a = []  
  if len(list_1) == len(list_2):
    list_a = list(zip(list_1, list_2))
    dict_a.update(list_a)
    print(dict_a)   