#python3 list
a = []
for i in range(0,5):
	i = int(input("Input number(5) : "))
	a.append(i)
for i in range(0,len(a)):
	print(a[i], end=" ")
print(end="\n")
print("List len : ", len(a))
print("List max : ", max(a))
print("List min : ", min(a))
print("List sum : ", sum(a))
a.pop()
for j in range(0,len(a)):
	print(a[j], end=" ")
print(end="\n")
a.insert(3,998)
for j in range(0,len(a)):
	print(a[j], end=" ")
print(end="\n")
a.append(53)
for j in range(0,len(a)):
	print(a[j], end=" ")
print(end="\n")
a.clear()
for j in range(0,len(a)):
	print(a[j], end=" ")
print(end="\n")
