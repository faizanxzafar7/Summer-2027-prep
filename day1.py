price= float(input("Medication price:"))
discount= float(input("Discount percentage:"))
price_cut= discount*price/100
final_price= price-price_cut
if final_price>50: print("Price is unaffordable:",final_price)
else:print("Price is affordable:",final_price)