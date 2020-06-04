#Números primo

def isPrime(num):
    count=0
    for x in range(1,num+1):
        residuo=num % x
        if residuo == 0:
            count+=1
        if count>2:
            return False
    if count==2:
        return True

for i in range(1, 20):
    if isPrime(i + 1)==True:
        print(i + 1, end=" ")
print()
