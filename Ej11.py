import time
import math 

def primeFactors(n):  
    print("Empezamos")   
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print (2)
        n = n / 2       
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2):   
        #print(i)  
        # while i divides n , print i ad divide n 
        if ((time.time() - start_time)%100==0):
            print("---Vas por %s segundos ---" % (time.time() - start_time))
        while n % i== 0: 
            print (i) 
            n = n / i              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print (n)   
    


start_time = time.time()
hex64 = "c9df896360979d1d"
hex128="be0d02633305f3d5c3c6044d17149baf"
n = int(hex128, 16)
#print(dec64)
  
primeFactors(n) 


print("--- %s seconds ---" % (time.time() - start_time))
#print("--- %s minuts ---" % ((time.time() - start_time)/60))


# A function to print all prime factors of  
# a given number n 

# Driver Program to test above function 