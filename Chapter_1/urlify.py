def urlify(string, true_length):
  
  current_length = 0
  result = ""
  
  for letter in string:
    if letter == ' ' and current_length != true_length:
      result += "%20"
    else:
      result += letter
    current_length += 1
    if current_length == true_length:
      break
  
  return result

# Test Cases:
print(1 if urlify(" ", 1) == "%20" else 0)
print(1 if urlify("  ", 2) == "%20%20" else 0)
print(1 if urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith" else 0)
print(1 if urlify("Mr John Smith    ", 14) == "Mr%20John%20Smith%20" else 0)
print(1 if urlify(" Mr John Smith    ", 14) == "%20Mr%20John%20Smith" else 0)
print(1 if urlify("MrJohnSmith", 11) == "MrJohnSmith" else 0)
print(1 if urlify(" a", 2) == "%20a" else 0)
print(1 if urlify("a ", 2) == "a%20" else 0)
