#day1a
def freq():
    file1=open('input.txt').readlines()
    numbers=[]
    for number in file1:
        number=number.strip('\n')
        numbers.append(number)
    
    count=0
    for num in numbers:
        count+=eval(num)
   
    return count

#day1b
def rep():
    file1=open('input.txt').readlines()
    list1=[]
    for num in file1:
        list1.append(eval(num.strip('\n')))
    count=0
    counts=[0]
    while True:
        for number in list1:
            
            count+=number
            if count in counts:
                print(count)
                return count
            counts.append(count)
print(rep())