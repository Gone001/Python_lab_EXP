m=int(input("Enter the starting point"))
k=int(input("Enter the range :"))
for i in range (m,k+1):
    if (i%5==0):
        print(f"Table of {i}:\n")
        for j in range (1,11):
            print(f"{i} X {j}={i*j}")
        print()
else:print("done")