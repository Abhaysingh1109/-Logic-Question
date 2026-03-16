n = int(input("Enter the number:"))

number = []

for i in range(1,n+1):
    iter = int(input(f"Enter the number{i}:"))   
    
    number.append(iter)

k = int(input("Enter the value of k:"))
kth = []
for i in number:
    
    if i > k:
       kth.append(i)
print(kth)
    