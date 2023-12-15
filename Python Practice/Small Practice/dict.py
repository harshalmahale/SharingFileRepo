d = {'name' : 'Harshal', 'age' : '23'}
d['Id'] = '47144'
print(d)                        #print all dictionary                   
print(d['age'])                   #Access particular key

for key, value in d.items():
    print(f'Key is {key} and value is {value}')   #print key and value

for i in d:
    print(i)               #print all keys
    
for i in d.values():
    print(i)               #print all values
    
#Get method 
# to access a key and check existance
#print (d.get('name'))
# Q - why we use get 
# A - to get a rid of error

#Example
#print (d['names'])
print(d.get('names'))

#to delete item
# pop ---> take one agrument which is keyname

popped = d.pop('names')
print(popped)
print(d)

popped = d.popitem()
print(popped)
print(d)
