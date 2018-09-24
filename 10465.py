from sys import stdin

def ladoIzquierdo(m,n,t):
	cont1= 0
	cont2=0
	save1=0
	save2=0
	parcial=0
	mayor=0
	while True:
		parcial = m*cont1 + n*cont2
		if parcial < t:
			if mayor < parcial:
				mayor = parcial
				save1 = cont1
				save2 = cont2

			cont1 = cont1 +1

		elif parcial == t:
			return True, cont1, cont2
		else:
			#SI ES MAYOR
			if n*cont2 > t:
				return False, save1, save2

			cont1 = 0
			cont2 = cont2+1


def ladoDerecho(m,n,t):
	cont1= 0
	cont2=0
	save1=0
	save2=0
	parcial=0
	mayor=0
	while True:
		parcial = m*cont1 + n*cont2
		if parcial < t:
			if mayor < parcial:
				mayor = parcial
				save1 = cont1
				save2 = cont2

			cont2 = cont2 +1

		elif parcial == t:
			return True, cont1 ,cont2
		else:
			#SI ES MAYOR
			if m*cont1 > t:
				return False, save1 , save2

			cont1 = cont1+1
			cont2 = 0

def solve(m,n,t):
	notCompleteIzq = False
	notCompleteDer = False
	drink =0
	notCompleteIzq,resultado11,resultado12 = ladoIzquierdo(m,n,t)
	notCompleteDer,resultado21,resultado22 = ladoDerecho(m,n,t)
	if (resultado11+resultado12) < (resultado21 + resultado22):
		drink = t - (m*resultado11 + n*resultado12)
		if drink == 0:
			print(resultado21 + resultado22)
		else:
			print(str(resultado21 + resultado22) + " " + str(drink))
	else:
		drink = t - (m*resultado21 + n*resultado22)
		if drink == 0:
			print(resultado11 + resultado12)
		else:
			print(str(resultado11 + resultado12) + " " + str(drink))


def main():
	m,n,t = 1,1,1
	while m +n + t != 0:
		l = stdin.readline()
		if l != '\n' or l != "":
			m,n,t = map(int,l.split())
			l = None
			solve(m,n,t)
		else:
			pass


main()