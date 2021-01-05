def recursive_fibo(number):
   if number <= 1:
       return number
   else:
       return(recursive_fibo(number-1) + recursive_fibo(number-2))


number = int(input("Enter the number: "))
if number <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci series:")
   for ele in range(number):
       print(recursive_fibo(ele))