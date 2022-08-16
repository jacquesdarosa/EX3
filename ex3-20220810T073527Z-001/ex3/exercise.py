# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


# Task 1
n = int(input("enter a number for check even or odd="))
def check_odd_even(n):
 if n % 2 == 0:
   print("The given number is Even number")
 else: 
    print("The given number is Odd number")
        
num = 123

print(check_odd_even(n))

 # a = 32
a = int(input("enter 2nd number to check for even or odd="))

def check_odd_even(a): 
 if a % 2 ==0:
    print('The given number is Even number')
 else:
    print('The given number is Odd number')
print(check_odd_even(a))

b = int(input("enter 3rd number to check for even or odd="))
def check_odd_even(b):
  if b % 2 ==0:
     print123('The given number is Even number')
  else:
     print('The given number is Odd number')
# b = 121234
print(check_odd_even(b))


# Task 2

x = range (2, 8, 2)
for n in x:
  print(n)

# Task 3

num = int(input("Enter the number ="))
count = 0

for i in range(1, num + 1): 
    if num % i == 0:
       count += 1
       print(i, end="")
print ("\n")
print("Total", count)
    

# task 4
# Python program to check if a given number is prime or not
#num = 63 
# If given number is greater than 1

if num > 1:
   for i in range(2, int(num/2)+1):
       if (num % i) == 0:
          print(num,"is not a prime number")
          break     
   else:
         print(num,"is a prime number")
else:
    print(num, "is not a prime number")


# task 5
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
       print ("fizzbuzz")
       
    elif num % 3 == 0:
       print ("fizz")
       
    elif num % 5 == 0:
       print("buzz")
    else:
      print(num)
       

# task 6 
num = int(input("enter a new number="))

for num in range (1000, 2000+1):
   if num % 7 == 0 and num % 5!=0:
          print(num)
          

