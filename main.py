#Palindrome Maker
def flipper(word):
  assist = []
  newword= ""
  for letter in word:
    assist.insert(0,letter)
  for letter in assist:
    newword += letter
  return newword

def maker(word, flipword):
  """CANNOT GO OVER 1/2 of flipword"""
  maximum = 1/2 * len(flipword)
  assist = []
  scroll = 0
  for letter in flipword:
    assist.append(letter)
  if int(maximum) != maximum:
    maximum = int(maximum) + 1
  while scroll != maximum:
    if word[scroll].upper() == flipword[scroll].upper():
      scroll += 1
    else:
      assist[scroll] = word[scroll]
      scroll += 1
  flipword = ""
  for letter in assist:
      flipword += letter
  return flipword
def decider(word):
  message = ""
  flipword = flipper(word)
  if flipword.upper() == word.upper():
    message += word
    message += " is a palindrome \n"
    return message
  else:
    flipword = maker(word, flipword)
    message += word
    message += " was turned into a palindrome, "
    message += flipword.lower()
    message += "\n"
    return message

print(decider("Racecar"))
print(decider("Noom"))