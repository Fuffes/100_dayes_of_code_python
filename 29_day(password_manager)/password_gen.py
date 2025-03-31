#Password Generator Project
from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




def get_rand_password():
  password_list = []
  [password_list.append(choice(letters)) for _ in range(randint(2,3 ))]
  [password_list.append(choice(symbols)) for _ in range(randint(2, 3))]
  [password_list.append(choice(numbers)) for _ in range(randint(2, 3))]
  shuffle(password_list)
  return "".join(password_list)