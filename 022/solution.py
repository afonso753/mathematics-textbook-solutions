import ast

def letter_score(c: str):
  alf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  letters = list(c)
  res = 0
  for i in range(len(letters)):
    res = res + alf.index(letters[i])+1
  return res

with open("names.txt", "r") as file:
  names = ast.literal_eval(file.read())

names = list(names)
names.sort()

def total_scores():
  score = 0
  for i in range (len(names)):
    score += letter_score(names[i])*(i+1)
  return score

print(total_scores())