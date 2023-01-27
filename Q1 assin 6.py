n = int(input("Enter the number: "))
sum =0

for i in range(1,n):
    if n%i==0 :
       sum = sum + i 
       print([i],end="")
if sum == n:
        print("**it is a prefect number**")
else:
    print("**it is not a  prefect number**")
        