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

