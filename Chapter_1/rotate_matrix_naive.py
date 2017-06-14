# Naive solution: O(n^2) time, O(n) space

def rotate_matrix(arr):
  width = len(arr)
  loop_count = 0
  remainder = 0
  
  while width > 1:
    
    # Initialize sub-arrays
    top = [0 for x in range(width+remainder)]
    right = [0 for x in range(width+remainder)]
    bottom = [0 for x in range(width+remainder)]
    left = [0 for x in range(width+remainder)]
    
    # Store current outtermost sides
    for i in range(width+remainder):
      top[i] = arr[0+loop_count][i+loop_count]
      right[i] = arr[i+loop_count][width-1+loop_count+remainder]
      bottom[i] = arr[width-1+loop_count+remainder][i+loop_count]
      left[i] = arr[i+loop_count][0+loop_count]
    
    # Rotate clockwise
    for i in range(width+remainder):      
      arr[i+loop_count][0+loop_count] = bottom[i]                                     # Bottom --> Left
      arr[i+loop_count][width-1+loop_count+remainder] = top[i]                        # Top    --> Right
      arr[0+loop_count][i+loop_count] = left[width-1-i+remainder]                     # Left   --> Top
      arr[width-1+loop_count+remainder][i+loop_count] = right[width-1-i+remainder]    # Right  --> Bottom
      
    # Move towards the center
    remainder = width % 2
    width //= 2
    loop_count += 1
  
  return arr

#test_arr = [[1,2,3],[4,5,6],[7,8,9]]    
#test_arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]    
test_arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(rotate_matrix(test_arr))
    
