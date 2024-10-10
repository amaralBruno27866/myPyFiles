def fun(val, num):
  # part 1
  if num == 0: # 1 operation
    return 1 # 1 operation
  elif num == 1: # 1 operation
    print(val)
    return val # 1 operation
  else:
    half = num // 2 # 2 operations
    res = fun(val, half) # 2 operations

    # part 2
    if num % 2 == 0: # 2 operations
      return res * res # 2 operations
    else:
      return res * res * val # 3 operations

fun(1, 100)