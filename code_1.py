#Given a non-negative number represented as an array of digits, add 1 to the number
#( increment the number represented by the digits ).
#The digits are stored such that the most significant digit is at the head of the list.
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
