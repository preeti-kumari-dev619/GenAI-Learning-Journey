gst = lambda price: price + (0.18 * price)

print(gst(100))    


final_price = lambda price, discount_percent=5: gst(price) - (gst(price) * discount_percent / 100)

print(final_price(100))     
print(final_price(100, 10))  