def problema(arr, m, j):
    n=len(arr)
    temporal_menor = []
    valor_min=float("inf")
    arr=arr[0:m+j]
    arreglo_subarreglos= hacer_subarreglos_j(arr, j)
    for subarray in arreglo_subarreglos:
            if posible(arr, subarray) and sum(subarray)<valor_min:
                temporal_menor=subarray
                valor_min=sum(temporal_menor)

    return valor_min

def posible(arr, caso):
    posible = False
    #Terminar
    return posible

def hacer_subarreglos_j(arr, j):
    def backtrack(start, path):
        if len(path) == j:
            resultado.append(path[:])  # Copiamos la lista actual y la guardamos
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()  # Deshacemos la elección para probar otra combinación

    resultado = []
    backtrack(0, [])
    print(resultado)
    return resultado

print(problema([5,13,8,2,4],2,2))