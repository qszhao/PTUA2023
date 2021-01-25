```python
#Exercise 1

#testing the legal
#ensuring whether 42 = n is legal or not

42 = n

#it appears that 42 = n is not legal
```


      File "<ipython-input-80-de39b3827347>", line 6
        42 = n
        ^
    SyntaxError: cannot assign to literal




```python
#testing x = y = 1

x = y = 1

#it appears the statement is legal
```


```python
#testing semi-colon at the end of statement
x = "hi"
y = "old"
z = "friend"
print(x); print(y); print(z)

#it appears that it result the same as with not semi-colon
```

    hi
    old
    friend



```python
#testing period at the end of statement

```


```python
#testing math notation

x = 10
y = 20
z = x*y

print(z)

#it appears the result will be emerged
```

    200



```python
#Exercise 2

#measuring volume of a sphere

pi = 3.1415926535897932
r = 5

volume = 4/3 * pi * r**3
print("Volume is:", volume)
```

    Volume is: 523.5987755982989



```python
#calcultating the wholesale cost

cover_price = 24.95
discount = 40/100

final_price = cover_price - cover_price*discount
print("Final Price is:", final_price)

st_shipping_cost = 3
st_price = st_shipping_cost + final_price
print("1st Price is:", st_price)

additional_cost = 0.75
rest_price = (additional_cost + final_price)*59
print("Rest Price:",rest_price)

total_price = st_price + rest_price
print("Total Price:", total_price)
```

    Final Price is: 14.969999999999999
    1st Price is: 17.97
    Rest Price: 927.4799999999999
    Total Price: 945.4499999999999



