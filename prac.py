a=int(input("Enter no.of elements: "))
l=[]
for i in range(a):
    l.append(float(input()))
print(l)
print("\nTotal no.of elements: ",len(l))
b=int(input("\nEnter the element to be added: "))
l.appemd(b)
c=int(input("\nEnter the elemnt to check the frequency: "))
print("\nThe number of times the elemnt repeating is: ",l.count(c))