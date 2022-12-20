#Друзья друзей

n = input()
d = dict()
while n != '':
    x = n.split()
    if x[0] not in d.keys(): # Первый человек их словаря
        d[x[0]] = {x[1]}
    else: 
        d[x[0]].add(x[1])
        
    if x[1] not in d.keys():     
        d[x[1]] = {x[0]}
    else: 
        d[x[1]].add(x[0])
        
        n = input()
        
d_res = {i: set() for i in d.keys()}
for i in d.keys():
    for j in d[i]:
        temp = d[j].copy()
        temp.discard(i)
        d_res[i] = d_res[i].union(temp) #объединение множеств - юнион
print(d_res)

sort_res = sorted(d_res.items(), key=lambda x: x[0])
print(sort_res)
for i in sorted(d_res):
    
print(f"{i}: {', '.join(sorted(list(d_res[i])))}")

#n = [1, 5, 9]
#a = n
#a.append(10)
#print(id(n))
#print(id(a))
#print(id(c))



   
