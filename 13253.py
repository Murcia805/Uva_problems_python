from sys import stdin

#Danny Julian Murcia Gomez


#Se encarga de buscar las monedas que estan a un lado de la moneda padre
#Es una busqueda de solo un lado donde primero me muevo al lado contrario, despues me muevo al lado que debo
def busqueda_bin(P,Q,Cantidad,a,b,V):
    if Cantidad != 0:
        indiceA = P + a
        indiceB = Q + b
        tempA = P
        tempB = Q
        V.append((indiceA,indiceB))
        Cantidad = Cantidad - 1
        while Cantidad!=0:
            indiceA = indiceA + tempA
            indiceB = indiceB + tempB
            V.append((indiceA,indiceB)) #Asigno los valores a la respuesta
            Cantidad = Cantidad - 1

#Busqueda binaria el cual busca encontrar en donde se encuentra P/Q en el arbol.
def solve(P,Q,N):
    # inicializacion
    a, b = 1, 2
    encontro = False
    mid = False
    impar = False

    #Donde se almacenan las respuestas, se guardan como parejas
    ans = list()

    # Guarda el anterior izquierda si se mueve a la derecha
    IzqA = 0
    IzqB = 1

    # Guarda el anterior derecha si se mueve a la izquierda
    DerA = 1
    DerB = 1

    #Contador
    lleno = N

    if P == 0 and Q == 1: #Si empieza en M(0/1)
        # Agrego a las respuestas las monedas mas grandes que la que tengo
        if lleno != 0: #Asigna el valor de la izquierda
            lleno = lleno - 1
            ans.append((1, 1))
        if lleno != 0: #Asigna el valor de la derecha
            lleno = lleno - 1
            ans.append((1, 2))

        if lleno != 0:
            #Busco las monedas mas pequeñas
            busqueda_bin(P, Q, lleno, 1, 2, ans)

    elif P == 1 and Q == 1:#Si empieza en M(1/1)
        #Agrego a las respuestas las monedas mas grandes que la que tengo
        if lleno != 0: #Asigna el valor de la izquierda
            lleno = lleno - 1
            ans.append((0, 1))
        if lleno != 0: #Asigna el valor de la derecha
            lleno = lleno - 1
            ans.append((1, 2))

        if lleno != 0:
            #Busco las monedas mas pequeñas
            busqueda_bin(P, Q, lleno, 1, 2, ans)

    else:
        while encontro == False:
            if a == P and b == Q:
                if a == 1 and b == 2:
                    #Si M(1/2)
                    # Agrego a las respuestas las monedas mas grandes que la que tengo
                    mid = True
                    if lleno != 0:
                        lleno = lleno - 1
                        ans.append((IzqA, IzqB))
                    if lleno != 0:
                        lleno = lleno - 1
                        ans.append((DerA, DerB))
                    if lleno != 0:
                        # Busco las monedas mas pequeñas
                        if lleno%2 != 0:
                            #si N es impar
                            lleno = lleno // 2
                            busqueda_bin(P, Q, lleno+1, IzqA, IzqB, ans) #Derecha
                            busqueda_bin(P, Q, lleno, DerA, DerB, ans)  # izquierda

                        else:
                            # si N es par tiene la misma cantidad a ambos lados
                            lleno = lleno//2
                            busqueda_bin(P, Q, lleno, IzqA, IzqB, ans)#Derecha
                            busqueda_bin(P, Q, lleno, DerA, DerB, ans)  # izquierda

                else:
                    # Agrego a las respuestas las monedas mas grandes que la que tengo
                    if lleno != 0:
                        lleno = lleno - 1
                        ans.append((IzqA, IzqB))
                    if lleno != 0:
                        lleno = lleno - 1
                        ans.append((DerA, DerB))
                    if lleno != 0:
                        if lleno%2 != 0:#impar
                            # si N es impar las monedas que estan al lado Derecho tiene radio mas grande
                            # por lo tanto tiene prioridad
                            impar = True
                            lleno = lleno // 2
                            busqueda_bin(P, Q, lleno+1, DerA, DerB, ans)  # Derecha
                            busqueda_bin(P, Q, lleno+1, IzqA, IzqB, ans)  # izquierda
                        else:
                            # si N es par tiene la misma cantidad a ambos lados
                            lleno = lleno//2
                            busqueda_bin(P,Q,lleno,DerA,DerB,ans)#Derecha
                            busqueda_bin(P,Q,lleno,IzqA,IzqB,ans)#izquierda

                encontro = True

            elif a / b > P / Q:
                #Movimiento a la izquierda
                DerA = a
                DerB = b
                a = a + IzqA
                b = b + IzqB
            else:
                #Movimiento a la Derecha
                IzqA = a
                IzqB = b
                a = a + DerA
                b = b + DerB

    #Cuando acaba el algoritmo, sencillamente le asigno a un string las respuestas para
    #poderlas imprimir en una sola linea
    if mid:
        ans.sort()
    else:
        ans.sort(key=lambda x: x[1])
        if impar:
            ans.pop()

    imprimir = ''
    for i, j in ans:
        imprimir = imprimir + "M(" + str(i) + "/" + str(j) + ") "

    return imprimir.rstrip()

def main():
    line = stdin.readline() #Se lee la entrada
    while line: #Mientras exista algo que leer
        p,q,n = map(int,line.split()) #Asigna las entradas a sus respectivas variables
        print(solve(p,q,n)) #Resuelve el problema
        line = stdin.readline()#Se lee la siguiente entrada

#Llamo la funcion padre
main()