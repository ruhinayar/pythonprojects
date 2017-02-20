x = raw_input('How many numbers?')
Last_num = 0
Last_last_num = 1

x=int(x)

while len(Fibonacci_Series) < x:
    New_num = Last_num + Last_last_num
    Last_last_num = Last_num
    Last_num = New_num
    Fibonacci_Series.append(New_num)
    
print Fibonacci_Series
