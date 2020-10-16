from typing import Dict, List

'''Create a fibonnaci dictionary.
Keys are the positions and values are fibonnaci lists through that position.

'''

def fibonacci_dict(n: int) -> Dict[int, List[int]]:
    if n <= 0:
        raise IndexError
    # Creates fibonacci list
    fibonacci_list = [0, 1]
    for i in range(0, n):
      fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i + 1])
    # Creates dictionary from list slices
    return {i: fibonacci_list[2:i + 2] for i in range(1, n + 1)}


fibonacci = fibonacci_dict(5)
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 5], 5: [1, 2, 3, 5, 8]}

for i, fib_list in fibonacci.items():
  print('{0}: {1}'.format(i, fib_list))

print(fibonacci[5])
# [1, 2, 3, 5, 8]
