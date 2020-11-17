exp = input()
s = ''
l = []
for i in range(0,len(exp)):
    if exp[i].isdigit():
        s = s+exp[i]
    else:
        l.append(s)
        s = ''
        s =s+exp[i]
        l.append(s)
        s = ''
    if i == len(exp)-1:
        l.append(s)
        s = ''

for i in range(0, len(l)):
    if l[i].isdigit():
        l[i] = int(l[i])
    else:
        pass
cal = l[0]

for i in range(1, len(l)):
    if l[i] == '+':
        cal = cal + l[i+1]
    elif l[i] == '-':
        cal = cal - l[i+1]
    elif l[i] == '/':
        cal = cal / l[i+1]
    elif l[i] == '*':
        cal = cal * l[i+1]
    else:
        pass
print(exp+' = '+str(cal))
