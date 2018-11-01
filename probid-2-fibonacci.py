#!/usr/local/bin/python

a=1
b=2
i=0
sum=2

while i < 4000000:
	i=a+b
	if i%2 == 0:
		sum=sum+i
	a=b
	b=i

print sum
