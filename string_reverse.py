
import stack

string = "have a great day"
reverse_string = ""
s = stack.Stack()


for char in string:
    s.push(char)

while not s.is_empty():
    reverse_string += s.pop()

print(reverse_string)