def palindrome_perm(string):
  
  # Check for empty string input
  if len(string) == 0:
    return False
  
  hash = {}
  string = str.lower(string)
  
  # Count the occurances of each character in the string (not counting spaces)
  for letter in string:
    if letter != ' ':  
      if letter not in hash:
        hash[letter] = 0
      hash[letter] += 1
    
  # Check if a character with an odd count exists
  odd_ind = False
  for key in hash:
    if hash[key] % 2 == 1:
      if odd_ind == True:
        return False
      odd_ind = True
  
  return True
      
  

# Test Cases - Assume case insensitive and ignore spaces  
print(1 if palindrome_perm("") == False else 0)
print(1 if palindrome_perm(" ") == True else 0)
print(1 if palindrome_perm("a") == True else 0)
print(1 if palindrome_perm("aa") == True else 0)
print(1 if palindrome_perm("aaa") == True else 0)
print(1 if palindrome_perm("aabb") == True else 0)
print(1 if palindrome_perm("aab") == True else 0)
print(1 if palindrome_perm("Aa") == True else 0)  
print(1 if palindrome_perm("Tact Coa") == True else 0)
print(1 if palindrome_perm("abc") == False else 0)
print(1 if palindrome_perm("aabbc") == True else 0)
print(1 if palindrome_perm("aabc") == False else 0)
