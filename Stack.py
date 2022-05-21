class Stack:
  """ Creating the Stack object """
    def __init__(self):
      """Initialization of the object in a list-like structure"""
      self.items=[]
        
    def add(self, element):
      """add whatever element on top of the stack"""
        self.items.append(element)
        
    def pop(self):
      """pop the last element of the stack and return it"""
        return self.items.pop()
        
