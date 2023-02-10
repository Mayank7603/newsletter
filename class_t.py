str="            THIS IS THE CASE"
print(str)
x=str.center(60)
print(x)


# list 
# len
# in 
# not in 
# * (replication )
# + (conccatenation )

l=[1,2,3]
print(l)
l+='2'          # list +=int is not allowed 
l+=[5]
print(l)

# list is mutable 
# in place value updation is allowed in list 

l[2]='R'    #in place
print(l)

# slicing [start:stop:step]
print(l[1:5:2])

a=[1,2,3]
b=a
a[1]=[34]       # will be updated in both the list
print(a)
print(b)

c=list(a)       # will not be updated in bothe the lists
a[1]=[3]        # alternate is dest_list=src_list_name.copy()
print(a)
print(c)


# list.append()

u=c.append(56)      #apeend fucntion does not return anything 
print(u)
print(c)

# list.extend () append fucntion adds one element to a list while extend can add multiple elements toa list 

u=c.extend([9])
print(c)
print(u)

#insert fucntion        insert(indexx,item)

c.insert(0,456)
print(c)

#pop fucntion        pass index otherwise last element 

print(c.pop(2))
print(c)

# remove  takes the values as arg ,, if not present then values error

c.remove(9)
print(c)


# del  delete the var , any list value or a part of list 

del c[2:]
print(c)

arr=[]
arr.append(1)
arr.append([7]+[2,3])
print(arr)

r=[1,2,4,6,7]
if(r.reverse()==r[::-1]):
    print("t")
else:
    print("f")
# false because r.reverse does not retuen anything
print(r.reverse())
print(r[::-1])

# clear - remove all the items from the list , but list exists as as empty list 
#r.clear()
print(r)

# count - count the frequency
print(r.count(7))
print(r.count("7"))

# sort -  used of sorting   doesn't return anything
r.sort()    #asc
r.sort(reverse=True)    # des
print(r)

#sorted() - same arg as sort , returns a list sort does not return but it does return 

# min , max , sum - there should be similar type of data elements in the list 

print(max('quix2cdodez'))
print(min('quiAx2cdodez'))
print(sum([1,2,4,6]))

# neseted list 

l1=[1,2,4]
lFinal=[l1,[23,44,2],[[23,45,1],[88,4]],6]
print(lFinal[0])
print(lFinal[1][1])
print(lFinal[2][0][0])
# print(lFinal[3])

#ragged list - a list that has list with different shapes aka irregualar 2D list 