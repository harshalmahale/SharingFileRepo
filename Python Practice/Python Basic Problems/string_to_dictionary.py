a = 'a/1/b/2/c/3'

d = dict()

ab = a.split('/')
print(ab)
for i in range(len(ab)):
    print(i)
    if(i%2==0):
        d[ab[i]]=ab[i+1]

print(d)