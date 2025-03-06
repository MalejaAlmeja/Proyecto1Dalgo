import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ProblemaCHAT {

    // Método que, dado n, j, m y el arreglo de pesos,
    // retorna la mínima suma de los primeros j tras a lo sumo m swaps adyacentes.
    public int resolverProblema(int n, int j, int m, int[] arr) {
        int mSwaps = m;

        // Para cada posición en [0.. j-1]
        for (int pos = 0; pos < j; pos++) {
            // Hasta dónde podemos buscar
            int limite = Math.min(pos + mSwaps, n - 1);

            // Buscar índice del valor mínimo en arr[pos..limite]
            int minIdx = pos;
            int minVal = arr[pos];
            for (int i = pos + 1; i <= limite; i++) {
                if (arr[i] < minVal) {
                    minVal = arr[i];
                    minIdx = i;
                }
            }

            // Burbujeo adyacente y actualización de mSwaps
            while (minIdx > pos && mSwaps > 0) {
                // Intercambiar
                int temp = arr[minIdx];
                arr[minIdx] = arr[minIdx - 1];
                arr[minIdx - 1] = temp;

                minIdx--;
                mSwaps--;
            }
        }

        // Sumar los primeros j
        int suma = 0;
        for (int i = 0; i < j; i++) {
            suma += arr[i];
        }
        return suma;
    }

    public static void main(String[] args) throws IOException {
        ProblemaCHAT instancia = new ProblemaCHAT();

        try (InputStreamReader is = new InputStreamReader(System.in);
             BufferedReader br = new BufferedReader(is)) {

            // Leer la cantidad de casos de prueba
            int casos = Integer.parseInt(br.readLine());

            for (int i = 0; i < casos; i++) {
                String line = br.readLine();
                if (line == null || line.isEmpty()) {
                    continue;
                }

                // Leer n, j, m y los n valores
                String[] parts = line.trim().split("\\s+");
                int n = Integer.parseInt(parts[0]);
                int j = Integer.parseInt(parts[1]);
                int m = Integer.parseInt(parts[2]);

                int[] arr = new int[n];
                for (int k = 0; k < n; k++) {
                    arr[k] = Integer.parseInt(parts[3 + k]);
                }

                // Llamar el método que resuelve el problema
                int resultado = instancia.resolverProblema(n, j, m, arr);

                // Imprimir la respuesta
                System.out.println(resultado);
            }
        }
    }
}
