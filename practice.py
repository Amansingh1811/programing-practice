class array:
    def even(self, ):  
        self.num = num
        if num > 1 :
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    print(i, "times" , num//i, "is" , num)
                    break
                else:
                    print(num, "is a prime number")

        else:
            print(num, "is not a prime number")            
                
num = int(input("enter the value"))
N = array()
print(N.even())