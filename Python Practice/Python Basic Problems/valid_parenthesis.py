str = '[]'

stack = []
open_backets = '{(['

for char in str:
    if char in open_backets:
        stack.append(char)
        
    else:
        if char == ')' and stack[-1] == '(':
            stack.pop()       
        elif char == '}' and stack[-1] == '{':
            stack.pop()            
        elif char == ']' and stack[-1] == '[':
            stack.pop()        
        else:
            print("Invalid Parenthesis")
            break
       
if(len(stack) == 0):
    print("Valid Parenthesis")
    