emp2 = '/Example2.txt'
with open(emp2,'w') as writeline:
    writeline.write("Hello here we go\n")
    writeline.write("This is the line1\n")
    writeline.write("This is the line2\n")
    writeline.write("This is the line3\n")
    writeline.write("overwrite\n")
    
    
with open(emp2,'a') as writeline:
    writeline.write("This is line4\n")
    
with open(emp2, 'r') as readline:
    print(readline.read())
    
    