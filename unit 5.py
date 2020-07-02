#1:wt is dictionary and explain¶
# dictionary:it is a collection of unordered,changeble,indexed
# it consists of keys and values in curly braces
d1={"chota":2,"bheem":4,"motu":6,"patlu":8}
print(d1)
{'chota': 2, 'bheem': 4, 'motu': 6, 'patlu': 8}


#2:sum of elements in a list
In [17]:
l1=[2,3,4,5]
t=sum(l1)
print(t)
14

#3:creating a list of empty directories
In [16]:
k=[{}for i in range(5)]
print(k)
[{}, {}, {}, {}, {}]

#4:accessing a key by taking index
In [22]:
d2={"chota":2,"bheem":4,"motu":6,"patlu":8}
print(list(d2)[2])
motu

#5:to iterate over key elemts using for loop
In [36]:
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for k in d:
    print(k,d[k])
1 10
2 20
3 30
4 40
5 50
6 60

#6:sum all elements in a dictionary
In [6]:
d2={"chota":2,"bheem":4,"motu":6,"patlu":8}
print(sum(d2.values()))
20

#7:merging
In [34]:
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d2.update(d3)
d1.update(d2)
print(d1)
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#8:checking dictionary is empty or not
In [12]:
d2={"chota":2,"bheem":4,"motu":6,"patlu":8}
if len(d2)==0:
    print("empty")
else:
    print("no")
no
In [ ]:
