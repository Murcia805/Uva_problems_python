from sys import stdin

MAX   = 50010
num   = [ None for i in range(MAX) ]
global cont

def respuesta2(n):
	cn = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (num[i] > num[j]):
				cn += 1

	return cn

def recursion(low, mid, hi):
	izquierda = num[low:mid]
	derecha = num[mid:hi]
	contador = 0
	der = 0
	izq = 0
	for i in range(low,hi):
		if der == len(derecha):
			num[i] = izquierda[izq]
			izq = izq + 1
			contador = contador + der
		elif izq == len(izquierda):
			num[i] = derecha[der]
			der = der + 1
		else:
			if izquierda[izq] <= derecha[der]:
				num[i] = izquierda[izq]
				izq = izq + 1
				contador = contador +der

			else:
				num[i]= derecha[der]
				der = der + 1
				#contador = contador +1

	return contador




def solve(low, hi):
	cont = 0
	if low+1 < hi:
		mitad = low+((hi-low) // 2)
		cont = solve(low, mitad) + solve(mitad, hi) + recursion(low, mitad, hi)

	#else:
	#	if num[low] > num[hi]:
	#		temp= num[low]
	#		num[low] = num[hi]
	#		num[hi] = temp
	#		return 1
	#	else:
	#		return 0

	return cont

def main():
	global num
	inp = stdin
	n = int(stdin.readline().strip())
	while n>0:
		for i in range(n):
			num[i] = int(stdin.readline())

		#print(respuesta2(n))
		print(solve(0,n))
		#print(num)
		n = int(stdin.readline().strip())

main()
