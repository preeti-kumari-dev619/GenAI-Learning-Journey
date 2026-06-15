#method 1
import math_utils
print(math_utils.add(10, 5))
print(math_utils.subtract(20, 10))
print(math_utils.square(10))


#method 2
from math_utils import square
print(square(4))

#task 2
import string_utils
text = "i am learning python modules"
print(f"Original Text: {text}")
print(f"Capitalize.text: {string_utils.capitalize_words(text)}")
print(f"Reverse Text: {string_utils.reverse_string(text)}")
print(f"word Count: {string_utils.word_count(text)}")


#task 3
from shop_package import (
    apply_discount,
    flat_discount,
    calculate_total,
    apply_tax
)

print(apply_discount(1000, 10))
print(flat_discount(1000))
print(calculate_total([100, 200, 300]))
print(apply_tax(600))



#task4

import shop_package.discount as disc

from shop_package.billing import calculate_total

print("Apply Discount:", disc.apply_discount(1000, 10))

print("Flat Discount:", disc.flat_discount(1000))
