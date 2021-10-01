# bounce.py
#
# Exercise 1.5


height = 100
bounce_back = 3/5

for bounce in range(1,11):
    height = height * (3/5)
    print(bounce," ",round(height, ndigits = 4))
