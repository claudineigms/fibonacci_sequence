def fib(n):
    return (n if n in [0,1] else fib(n-1) + fib(n-2))

def find_fib(number_find):
     fib_sequence = []
     fib_index = 0
     while fib(fib_index) <= number_find:
             fib_sequence.append(fib(fib_index))
             fib_index += 1
     if number_find in fib_sequence:
             return True
     return False
