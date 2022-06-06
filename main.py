#pyramid
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def left(self,data):
      if data<=self.data:
         self.l = Node(data)
      else: print("error")

   def right(self, data):
      if data <= self.data:
         self.r = Node(data)




fst = Node(8)
Node.left(fst,1)
Node.left(fst.l,1)

print(fst.l.l.data)
