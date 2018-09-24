from sys import stdin

def recorridos(matriz):
	cont = 0
	t =2
	for i in range(10):
		temp = False
		if i <=5:
			cont = i
		else:
			cont = i - t
			t = t+2
			temp = True

		for j in range(10):
			matriz[i][j] = cont
			if cont == 0 :
				temp = True
			if cont == 5:
				temp = False

			if temp:
				cont = cont +1
			else:
				cont = cont - 1

	return matriz

def valorDistancia(A,B,distancia):
	return distancia[int(A[0])][int(B[0])]+distancia[int(A[1])][int(B[1])]+distancia[int(A[2])][int(B[2])]+distancia[int(A[3])][int(B[3])]


def solve(cantidad, arreglo,distancia):
	ans = float("INF")
	dist = [float("INF") for j in range(cantidad)]
	distanciaTotal = [[0 for j in range(cantidad)] for k in range(cantidad)]
	visit = [False for j in range(cantidad)]
	dist[0] = 0
	inicio = [0,0,0,0]
	menor = 0
	parcial = 0 #o actual

	#hallo las distancias que hay entre cada nodo:
	for j in range(cantidad):
		for k in range(cantidad):
			temp = valorDistancia(arreglo[k],arreglo[j],distancia)
			distanciaTotal[j][k] = temp
			distanciaTotal[k][j] = temp


	#el mas cercano para poder empezar la busqueda desde ese
	for j in range(cantidad):
		ans = min(ans,valorDistancia(inicio,arreglo[j],distancia))

	for j in range(cantidad):
		menor = float("INF")
		for k in range(cantidad):
			if visit[k] == False and dist[k] < menor:
				menor = dist[k]
				parcial = k

		dist[parcial] = 0
		visit[parcial] = True

		for k in range(cantidad):
			if visit[k] == False and distanciaTotal[parcial][k] < dist[k]:
				dist[k] = distanciaTotal[parcial][k]

		ans = ans + menor

	return ans



def main():
	cantidad = int(stdin.readline())
	matriz = [[0 for i in range(10)] for j in range(10)]
	matriz = recorridos(matriz)
	for i in range(cantidad):
		line = stdin.readline().split()
		numberKey = int(line[0])
		arreglo = line[1:]
		print(solve(numberKey,arreglo,matriz))

main()