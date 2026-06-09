num=int(input("Enter a number: "))
original_num=num
sum_factorial=0
while num>0:
    digit=num%10
    factorial=1
    for i in range(1, digit + 1):
        factorial*=i
        sum_factorial+=factorial
        num//=10
        if sum_factorial ==original_num:
            print("its is a strong number")
        
else:
    print("Not a Strong Number")

        
                   

    
        


