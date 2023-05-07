def print_red(word):
  print('\033[31m !!!!!!!!!!!!!!!! \033[0m')
  print('\033[31m', word, '\033[0m')

def user_object_to_dict(users_object):
  users_dict = []
  for user_object in users_object:
    user_dict = {
      'name' : user_object.name,
      'score': user_object.score
    }
    users_dict.append(user_dict)
  return users_dict

