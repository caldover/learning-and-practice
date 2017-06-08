def string_comp(string):
  
  if len(string) <= 2:
    return string
  
  result = ""
  char_count = 1
  
  for i in range(1, len(string)):
    
    # All characters in string besides last character
    if i < len(string) - 1:
      # Increase count if next two characters are equal
      if string[i-1] == string[i]:
        char_count += 1
      # Otherwise append the left character followed by the count and reset the count to 1
      else:
        result += string[i-1] + str(char_count)
        char_count = 1
    
    # Last character only
    else:
      #  If last two chars are equal, increase the count of that character by 1, append the character, then append the count
      if string[i-1] == string[i]:
        char_count += 1
        result += string[i] + str(char_count)
      # Otherwise append left char and its count then the right char and 1
      else:
        result += string[i - 1] + str(char_count) + string[i] +'1'
  
  # Return the smaller string of the original vs. the result
  if len(result) < len(string): return result
  else: return string

print(1 if string_comp("") == "" else 0)
print(1 if string_comp("a") == "a" else 0)
print(1 if string_comp("Aa") == "Aa" else 0)
print(1 if string_comp("AAa") == "AAa" else 0)
print(1 if string_comp("AAA") == "A3" else 0)
print(1 if string_comp("AAaa") == "AAaa" else 0)
print(1 if string_comp("AAAaaa") == "A3a3" else 0)
print(1 if string_comp("abcd") == "abcd" else 0)
print(1 if string_comp("aabcccccaaa") == "a2b1c5a3" else 0)
