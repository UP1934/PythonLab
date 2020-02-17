
cover_price = 24.95
dis = 0.40
book_price = cover_price - dis


n = int(raw_input("Enter no. of copies: "))
if n > 1 :
	price = (3+book_price)+((n-1)*(0.75+book_price))
elif n == 1:
	price = 3 + book_price
else:
	price = 0

print("Total Price is ")
print(price)

OUTPUT ::

ace@ace-ThinkCentre-M70e:~$ cd Desktop
ace@ace-ThinkCentre-M70e:~/Desktop$ python Exp_4.py
Enter no. of copies: 60
Total Price is 
1520.25
ace@ace-ThinkCentre-M70e:~/Desktop$ python Exp_4.py
Enter no. of copies: 1
Total Price is 
27.55
ace@ace-ThinkCentre-M70e:~/Desktop$ 
