numbers = [8, 18, 14, 7, 13, 17]

def check_odd(num):
    return num%2 !=0

odd_no=list(filter(check_odd,numbers))

print(numbers)
print(odd_no)
