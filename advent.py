#day1
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
print(freq())