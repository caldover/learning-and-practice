def isUnique(string):
  hash = {}
  for letter in string:
    if letter not in hash:
      hash[letter] = 0
    hash[letter] += 1
    if hash[letter] > 1:
      return False
      
  return True
    
# Test Cases - Assuming case sensitive:
print(1 if isUnique("abc") == True else 0)
print(1 if isUnique("aaa") == False else 0)
print(1 if isUnique("a") == True else 0)
print(1 if isUnique("") == True else 0)
print(1 if isUnique("Aa") == True else 0)
print(1 if isUnique("AA") == False else 0)
