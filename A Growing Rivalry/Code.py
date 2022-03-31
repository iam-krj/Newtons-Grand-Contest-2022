t = int(input())
h = input()
c,g = 0, 0
for i in range(len(h)):
    if 'N' in h[i]:
        c+=1
for i in range(len(h)):    
    if 'T' in h[i]:
        g+=1
if c < g:
    print('Tusla')
else:
    print('Nutan')
