n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter=1
listi=[0,0,1]
sum_of_numbers=1
while n>=counter:
    for each in listi:
        sum_of_numbers+=each
    print(listi[2])
    del listi[0]
    listi.append(sum_of_numbers)
    counter+=1
    sum_of_numbers=0
