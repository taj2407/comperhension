#list comperhension.
#adding the numbers into list.
l=[j for j in range(1,11)]
print(l)
#from the given tuple add only even numbers into the list.
t=(11,22,33,44,55,66,77,88,99)
even=[i for i in t if i%2==0]
print(even)
#from the given tuple add only odd numbers which are greater than 50 into the list.
t=(11,15,60,55,99)
n=[i for i in t if i%2==1 and i>50]
print(n)
#add all the odd numbers and as well as even numbers which are greater than 100 which is present in given tuple into list.
t=(11,20,15,150,500,400,90)
l=[i for i in t if i%2==1 or i>100]
print(l)
#output form will like this [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]] by using list comperhension.
#method1
l=[[i,j,k] for i in range(1,6) for j in range(1,6) for k in range(1,6) if i==k==j]
print(l)
#method2
l=[[i]*3 for i in range(1,6)]
print(l)
#set comperhension
#add all the odd numbers and as well as even numbers which are greater than 100 which is present in given tuple into list.
t=(11,20,15,150,500,400,90)
l={i for i in t if i%2==1 or i>100}
print(l)
#from the given tuple add only odd numbers which are greater than 50 into the list.
t=(11,15,60,55,99)
n={i for i in t if i%2==1 and i>50}
print(n)
#dictionary comperhension
#add elements of given tuple and its square into the dictionary.
#method1
elements={i:i**2 for i in range(1,11)}
print(elements)
#method2
t=11,22,33,44,55
d={i:i**2 for i in t}
print(d)


















