def solution(numbers):
  if not all(isinstance(x, int) for x in numbers):
    raise ValueError("Input must be a list of integers")
  
  if len(numbers) < 3 or len(numbers) > 100:
    raise ValueError("Input must be a list of length 3 to 100")
  
  if not all(1 <= x <= 10**9 for x in numbers):
    raise ValueError("Input must be a list of integers between 1 and 10^9")
  
  def check_zigzag(i):
    if i >=len(numbers) - 2:
      return []
    
    a = numbers[i]
    b = numbers[i+1]
    c = numbers[i+2]

    is_zigzag = (a < b > c) or (a > b < c)
    result = 1 if is_zigzag else 0

    return[result] + check_zigzag(i+1)
  
  return check_zigzag(0)