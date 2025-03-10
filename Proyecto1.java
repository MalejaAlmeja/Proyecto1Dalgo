// Grupo de 3 conformado por:
// María Alejandra Carrillo: 202321854
// Juan David Uribe: 202322433
// Raúl Sebastián Ruiz: 202321332

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Proyecto1 {

    public float Proyecto1Principal(int n, int j, int m, int[] pesos) {
        float valor_min = Float.POSITIVE_INFINITY;

        for (List<Integer> caso: generarCombinaciones(pesos, j)){
            if (posible(caso, pesos, n,j,m)){
                int sum = 0;
                for(int numero: caso){
                    sum += numero;
                }
                if (sum<valor_min){
                    valor_min = sum;
                }
            }
        }
        return valor_min;
    }
/*
    public boolean posible(List<Integer> caso, int[] pesos, int m) {
        for (int i = 0; i < caso.size(); i++){
            int movimientos_necesarios;
            // Posicion del i del caso en el arreglo original
            int i_original = 0;
            for (int posicionIOriginal = 0; posicionIOriginal< pesos.length; posicionIOriginal++){
                if (pesos[posicionIOriginal] == caso.get(i)){
                    i_original = posicionIOriginal;
                    break;
                }
            }
            //if (i_original > caso.size()-1){
        
                movimientos_necesarios = i_original - i;
                m -= movimientos_necesarios;
            if (m<0){
                return false;
            }
        }
        if (m>=0){
            return true;
        } else {
            return false;
        }
    }
*/
public boolean posible(List<Integer> caso, int[] pesos,int n, int j, int m) {
        int[] copia = Arrays.copyOf(pesos, n);
        int swaps = 0;

        for (int i = 0; i < j; i++) {
            int indice_original = -1;
            for (int k = i; k < n; k++) {
                if (copia[k] == caso.get(i)) {
                    indice_original = k;
                    break;
                }
            }

            while (indice_original > i) {
                int tmp = copia[indice_original];
                copia[indice_original] = copia[indice_original - 1];
                copia[indice_original - 1] = tmp;
                indice_original--;
                swaps++;
            }
        }

        if (swaps <= m && swaps>0) {
            return true;
        }
        else{
            return false;
        }
}

    public static List<List<Integer>> generarCombinaciones(int[] arr, int j) {
        List<List<Integer>> resultado = new ArrayList<>();
        combinar(arr, j, 0, new ArrayList<>(), resultado);
        return resultado;
    }

    private static void combinar(int[] arr, int j, int inicio, List<Integer> actual, List<List<Integer>> resultado) {
        if (actual.size() == j) {
            resultado.add(new ArrayList<>(actual));
            return;
        }

        for (int i = inicio; i < arr.length; i++) {
            actual.add(arr[i]);
            combinar(arr, j, i + 1, actual, resultado);
            actual.remove(actual.size() - 1); 
        }
    }

    public static void main(String[] args) throws IOException {
        Proyecto1 instancia = new Proyecto1();
        // Leer la cantidad de casos de prueba
        try (InputStreamReader is = new InputStreamReader(System.in); BufferedReader br = new BufferedReader(is)) {
            int casos = Integer.parseInt(br.readLine());

            for (int i = 0; i < casos; i++) {
                String line = br.readLine();
                if (line == null || line.isEmpty()) continue;

                String[] parts = line.trim().split("\\s+");
        
                int n = Integer.parseInt(parts[0]);
                int j = Integer.parseInt(parts[1]);
                int m = Integer.parseInt(parts[2]);
                int limiteArreglo = j+m-1;
                int sizeReal;
                if (limiteArreglo>n){
                    sizeReal = n;
                } else {
                    sizeReal = limiteArreglo;
                }
                
                int[] pesos = new int[sizeReal];
                for (int k = 0; k < sizeReal; k++) {
                    pesos[k] = Integer.parseInt(parts[3 + k]);
                }
                
                float resultado = instancia.Proyecto1Principal(n, j, m, pesos);
                
                System.out.println(((int)resultado));
            }
        }
    }
}