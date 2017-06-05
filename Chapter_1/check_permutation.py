def check_permutation(string1, string2):
  
  # Check if lengths are equal:
  if len(string1) != len(string2):
    return False
  
  hash = {}
  for letter in string1:
    if letter not in hash:
      hash[letter] = 0
    hash[letter] += 1
  
  for letter in string2:
    if letter not in hash:
      return False
    hash[letter] -= 1
    if hash[letter] < 0:
      return False
  
  return True

# Test Cases:
print(1 if check_permutation("", "") == True else 0)
print(1 if check_permutation("a", "b") == False else 0)
print(1 if check_permutation("ba", "ab") == True else 0)
print(1 if check_permutation("ca", "ab") == False else 0)
print(1 if check_permutation("abc", "ab") == False else 0)
print(1 if check_permutation("abc", "bac") == True else 0)
print(1 if check_permutation("Aa", "aa") == False else 0)
