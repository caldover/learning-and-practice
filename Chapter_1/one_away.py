def one_away(string1, string2):
  
  # One away
  if abs(len(string1) - len(string2)) == 1:
    small_length = min(len(string1), len(string2))
    i = 0
    diff_char = False
    while i < small_length:
      if string1[i] != string2[i]:
        if diff_char == True:
          return False
        diff_char = False
      i += 1

  # Zero away
  if len(string1) - len(string2) == 0:
    diff_char = False
    for i in range(len(string1)):
      if string1[i] != string2[i]:
        if diff_char == True:
          return False
        diff_char = True
  
  return True
  
  
# Test Cases
print(1 if one_away("","") == True else 0)
print(1 if one_away("a","") == True else 0)
print(1 if one_away("","a") == True else 0)
print(1 if one_away("a","a") == True else 0)
print(1 if one_away("ab","a") == True else 0)
print(1 if one_away("ab","cb") == True else 0)
print(1 if one_away("pale","ple") == True else 0)
print(1 if one_away("pales","pale") == True else 0)
print(1 if one_away("pale","bale") == True else 0)
print(1 if one_away("pale","bake") == False else 0)
