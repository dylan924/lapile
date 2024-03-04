class MyOutOfSizeException(Exception):
    pass

class MyEmptyStackException(Exception):
    pass

class MyStackNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class MyStack:
    def __init__(self, taille_max):
        self.taille_max = taille_max
        self.top = None
        self.size = 0

    def add_to_stack(self, element):
        if self.is_full():
            raise MyOutOfSizeException("La pile est pleine.")
        
        new_node = MyStackNode(element, self.top)
        self.top = new_node
        self.size += 1

    def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException("La pile est vide.")
        
        popped_value = self.top.value
        self.top = self.top.next_node
        self.size -= 1
        return popped_value

    def is_full(self):
        return self.size == self.taille_max

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
   myStack = MyStack(3)
   myStack.add_to_stack('hello')
   myStack.add_to_stack('hello')
   print(myStack.is_full()) # False
   myStack.add_to_stack('hello')
   print(myStack.is_full()) # True
   myStack.add_to_stack('hello') # MyOutOfSizeException
   print(myStack.pop_from_stack()) # hello
   print(myStack.is_empty()) # False
   print(myStack.pop_from_stack()) # hello
   print(myStack.is_empty()) # False
   print(myStack.pop_from_stack()) # hello
   print(myStack.is_empty()) # True
   print(myStack.pop_from_stack()) #→ MyEmptyStackException
        

