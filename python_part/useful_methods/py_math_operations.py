"""
14 // 3 == 4 -> 最大的整數商 ([記] 14 / 3 == 4.66; 14 // 3 == 4 -> 多一刀把小數點切掉)
14 % 3  == 2 -> 看餘數 ([記] 「魚」 %%% -> 「餘」數)
"""

from functools import reduce
lst = [2, 3, 4]
ans = reduce(lambda x, y: x*y, lst)  # [python multiply elements in list](https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python)
print(f'ans: {ans}')


# https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
        # print(f'(x, y): {(x, y)}')
    return x


gcd(40, 16)


print('---------------------------------------------------------------------------------------------\n')

print('二進位和十進位: (Binary to Decimal) and (Decimal to Decimal)')
print(f"int('11101', 2): {int('11101', 2)}")  # Binary to Decimal Conversion and value addition
print(f"int('11101', 10): {int('11101', 10)}")  # Decimal to Decimal Conversion and value addition
