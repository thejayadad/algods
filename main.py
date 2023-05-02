
#Writing the stack class
#last in first out
#add to the top use append
#retrieve item from top of stack pop


class Stack:
    #This is the constructor - creating objects called stack based on this template
    #Code that will be ran
    def __init__(self):
        self.items = []

    #Checking if the stack is empty
    def is_empty(self):
        return len(self.items) == 0    
    #push the item on to the stack
    def push(self, item):
        self.items.append(item)
    #remove item from stack
    def pop(self):
        return self.items.pop()
    #returns last item from stack
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    

if __name__ == "__main__":
    s = Stack()
    # print(s)
    # print(s.is_empty())
    # s.push(3)
    # s.push(5)
    # s.push(9)
    # print(s)
    # print(s.pop())
    # print(s)
    # print(s.peek())
    # print(s.size())
    

#How to reverse a string
# string = "have a great day"
# reverse_string = ""


# for char in string:
#     s.push(char)

# while not s.is_empty():
#     reverse_string += s.pop()

# print(reverse_string)

#linear search starts at beginning of list till reach target value
def linear_search(list, target):
    """
    #Returns index position of target if found else returns none

    
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        return None
    


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Targeet not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 3)
verify(result)