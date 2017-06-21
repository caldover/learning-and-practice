class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
  def __str__(self):
    return str(self.data)
    
class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
  
  def addNode(self, data):
    temp = Node(data)
    if self.head == None:
      self.head = temp
      self.tail = temp
    else:
      self.tail.next = temp
      self.tail = temp
    
  def removeNode(self,data):
    # If deleting first node, update head
    if self.head.data == data:
      self.head = self.head.next
    else:
      current = self.head
      while current.next != None:
        if current.next.data == data:
          # If deleting the last node, update tail
          if current.next.next == None:
            self.tail = current
          current.next = current.next.next
          break
        else:
          current = current.next 
  
  def printList(self):
    current = self.head
    while current != None:
      print(current)
      current = current.next

  # With Dictionary - O(n) Time, O(n) Space
  def removeDups(self):
    hash = {}
    current = self.head
    while current != None:
      if current.data not in hash:
        hash[current.data] = 0
      hash[current.data] += 1
      current = current.next
      
    for key in hash:
      while hash[key] > 1:
        hash[key] -= 1
        self.removeNode(key)
  
  # Without Temporary Buffer - O(n^2) Time - O(1) Space
  def removeDups2(self):
    i = self.head
    j = self.head
    
    while i != None:
      while j.next != None:
        if i.data == j.next.data:
          j.next = j.next.next
        else:
          j = j.next
      i = i.next
      j = i
          
      
test1 = LinkedList()
test1.addNode(1)
test1.addNode(1)
test1.addNode(2)
test1.addNode(2)
test1.addNode(3)
test1.addNode(3)
test1.removeDups2()
test1.printList()
        
      
      
      
      
      
      
      
      
      
