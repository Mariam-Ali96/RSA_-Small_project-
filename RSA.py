import random
import math
import numpy as np
import simplejson

def rand_prime():
	while True:
		p = random.randrange(10001, 100000, 2)
		if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
			return p



p = rand_prime()
q = rand_prime()

n= p*q

m=(p-1)*(q-1)

def gcd(a, b):
	while b != 0:
 		a, b = b, a % b
	return a

E = np.arange(2.0,999)

for i in E: 
	a=gcd(i,m)
	if a==1:
		e=i
		break



Array=[]

with open("plain.txt") as f:
	for line in f:
		for ch in line:
			Array.append(ord(ch))




Cipher = []

def mod_exp(b,ex,mod):
	X = b
	E = ex
	Y = 1
	while E > 0:
		if E % 2 == 0:
			X = (X * X) % mod
			E = E/2
		else:
			Y = (X * Y) % mod
			E = E - 1
	return Y


for j in Array:
	c = mod_exp(j,e,n)
	Cipher.append(c)
print 'Cipher'
print Cipher

new_file = open('Cipher.txt','w')
simplejson.dump(Cipher, new_file)
new_file.close()


print 'Public key: '
print (e,n)

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n

	gcd = b

	return gcd,x,y

def MI(a, b):
	g, x, _ = egcd(a, b)
	return x % b
d = MI(e,m)


Decipher = []

for k in Cipher:
	M = mod_exp(k,d,n)
	Decipher.append(M)

print 'Decipher'
print Decipher

text=[]

for l in Decipher:
	qq= chr(l)
	text.append(qq)
print 'Private key: '
print (d,n)

print 'text'
print text


#Create a file of the encrypted text

new_file1 = open('New_plain.txt','w')

for i in text:
	new_file1.write(i)

new_file1.close()

