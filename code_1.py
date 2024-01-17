def add_one(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry:
        digits.insert(0, carry)

    return digits

# Example
input_array = [1, 2, 3]
output_array = add_one(input_array)
print(output_array)
