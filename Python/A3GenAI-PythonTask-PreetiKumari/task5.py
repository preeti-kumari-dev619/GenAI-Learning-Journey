prices = [100, 250, 400, 1200, 50, 2000, 850]

above_500 = list(filter(lambda p: p > 500, prices))
upto_500  = list(filter(lambda p: p <= 500, prices))

print("Prices greater than 500      :", above_500)
print("Prices less than or equal 500:", upto_500)