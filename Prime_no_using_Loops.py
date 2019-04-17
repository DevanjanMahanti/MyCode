print ("This for Prime no printing prog with loop")

for i in range(1,30):
    counter = 0
    j = 2

    while j<i :
        if i%j==0 :
            counter = 1
            j=j+1

        else :

            j=j+1
            
    if counter== 0:
        print (str(i) + "This is a prime number")
		
		/* I love INDIA */

    else :
        counter = 0
