import java.util.*;

public class JavaConsola {

    public static int algormarDP(int[] pesos, int n, int j, int m) {
        int INF = Integer.MAX_VALUE / 2; // Evitar overflow al sumar

        int[][][] dp = new int[n + 1][j + 1][m + 1];

        // Inicializar el DP con infinito
        for (int i = 0; i <= n; i++) {
            for (int k = 0; k <= j; k++) {
                Arrays.fill(dp[i][k], INF);
            }
        }

        // Caso base
        dp[0][0][0] = 0;

        for (int i = 0; i < n; i++) {
            for (int seleccionado = 0; seleccionado <= j; seleccionado++) {
                for (int swaps = 0; swaps <= m; swaps++) {
                    if (dp[i][seleccionado][swaps] == INF) continue;

                    // Opcion 1: No incluir jugador actual
                    dp[i + 1][seleccionado][swaps] = Math.min(dp[i + 1][seleccionado][swaps], dp[i][seleccionado][swaps]);

                    // Opcion 2: Incluir jugador actual
                    if (seleccionado < j) {
                        int costoMover = i - seleccionado;
                        int nuevoSwapTotal = swaps + costoMover;
                        if (nuevoSwapTotal <= m) {
                            dp[i + 1][seleccionado + 1][nuevoSwapTotal] = Math.min(
                                    dp[i + 1][seleccionado + 1][nuevoSwapTotal],
                                    dp[i][seleccionado][swaps] + pesos[i]
                            );
                        }
                    }
                }
            }
        }

        int resultado = INF;
        for (int s = 0; s <= m; s++) {
            resultado = Math.min(resultado, dp[n][j][s]);
        }
        return resultado;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int ncasos = Integer.parseInt(sc.nextLine());

        for (int t = 0; t < ncasos; t++) {
            String[] datos = sc.nextLine().trim().split(" ");
            int n = Integer.parseInt(datos[0]);
            int j = Integer.parseInt(datos[1]);
            int m = Integer.parseInt(datos[2]);

            int[] pesos = new int[n];
            for (int i = 0; i < n; i++) {
                pesos[i] = Integer.parseInt(datos[3 + i]);
            }

            int resultado = algormarDP(pesos, n, j, m);
            System.out.println(resultado);
        }

        sc.close();
    }
} 