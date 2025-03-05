public class Proyecto1 {
    // Proyecto 1 DALGO

    public int Proyecto1Principal(int n, int j, int m, int[] pesos) {

        // Construir el árbol de segmentos para manejar mínimos
        // TODO EL SEGMENT TREE NO LO PEGUE
        SegmentTree st = new SegmentTree(arr);
        
        // Para cada posicion en los primeros j
        for(int pos = 0; pos < j; pos++){
            if(m <= 0) break; // si ya no hay swaps, no podemos mover más
            
            // Limite = la posición más lejana que podemos "jalar" (pos + mSwaps)
            int limit = Math.min(pos + m, n - 1);
            
            // Consultamos al árbol de segmentos el índice del mínimo en [pos, limit]
            int minIdx = st.queryMinIndex(pos, limit);
            
            // si minIdx == pos, no hay que mover nada
            if(minIdx == pos) continue;
            
            // Cantidad de swaps necesarios para llevar arr[minIdx] a arr[pos]
            int needed = minIdx - pos;
            if(needed > m) needed = m; // (en teoría no pasa por el limit anterior)
            
            // "Bubble-up" del elemento desde minIdx hasta pos
            // Actualizamos el arreglo arr y el segment tree con cada swap adyacente
            while(minIdx > pos && m > 0) {
                // Intercambiar arr[minIdx] y arr[minIdx - 1]
                int temp = arr[minIdx - 1];
                arr[minIdx - 1] = arr[minIdx];
                arr[minIdx] = temp;
                
                // Actualizar en el árbol de segmentos las posiciones minIdx y minIdx-1
                st.update(minIdx,     arr[minIdx]);
                st.update(minIdx - 1, arr[minIdx - 1]);
                
                minIdx--;
                m--;
                return suma;
            }
        }
        
        // Calcular la suma de los primeros j
        int suma = 0;
        for(int i = 0; i < j; i++){
            suma += arr[i];
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
                
                int[] pesos = new int[n];
                for (int k = 0; k < n; k++) {
                    pesos[k] = Integer.parseInt(parts[3 + k]);
                }
                
                int resultado = instancia.Proyecto1Principal(n, j, m, pesos);
                
                System.out.println(resultado);
            }
        }
    }
}