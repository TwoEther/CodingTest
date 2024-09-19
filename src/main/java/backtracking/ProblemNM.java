package backtracking;

import java.util.Scanner;

public class ProblemNM {
    static int n;
    static int m;
    static int[] numbers;
    static boolean[] visited;

    public static void bt(int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(numbers[i] + " ");
            }
            System.out.println();
        }else{
            for (int i = 1; i <= n; i++) {
                if (!visited[i - 1]) {
                    visited[i - 1] = true;
                    numbers[depth] = i;
                    bt(depth + 1);
                    visited[i - 1] = false;
                }

            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        numbers = new int[n];
        visited = new boolean[n];
        bt(0);
    }
}
