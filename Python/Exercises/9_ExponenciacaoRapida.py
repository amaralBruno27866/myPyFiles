def fast_exponentiation(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half = fast_exponentiation(base, exp // 2)
        return half * half
    else:
        return base * fast_exponentiation(base, exp - 1)

print(fast_exponentiation(2, 10))  # 1024