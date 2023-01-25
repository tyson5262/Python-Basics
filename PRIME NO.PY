def prime_finder(a):
    if(a>1): #if(a!=1 or a!=0):
        for x in range(2,a):
            if(a%x==0):
                print(a,' is a composite no.')
                break
        else:
            print(a,' is a prime no.')   
    else:
        print(a,'is niether prime nor composite')

y=int(input('enter the no.'))
for b in range(y+1):
    prime_finder(b)