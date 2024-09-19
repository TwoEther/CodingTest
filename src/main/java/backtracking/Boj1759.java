package backtracking;

import java.util.*;

public class Boj1759 {
    static int l;
    static int c;
    static String[] alpha;
    static String[] result;
    static StringBuilder answer;
    static boolean[] visited;

    public static void bt(int depth, int cons, int vow, int start) {
        StringBuilder sb = new StringBuilder();
        if (depth == l && cons >= 2 && vow >= 1) {
            for (int i = 0; i < l; i++) {
                answer.append(result[i]).append(" ");
            }
            answer.append("\n");
        }
        else{
            for (int i = start; i <= c; i++) {
                if (!visited[i - 1]) {
                    visited[i - 1] = true;
                    result[i-1] = alpha[depth];
                    boolean exp = alpha[depth].matches("[aeiou]");
                    if (exp) {
                        bt(depth + 1, cons, vow + 1, i+1);
                    }else {
                        bt(depth + 1, cons + 1, vow, i+1);
                    }
                    visited[i - 1] = false;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        l = sc.nextInt();
        c = sc.nextInt();
        alpha = new String[c];
        visited = new boolean[c];
        result = new String[c];
        answer = new StringBuilder();
        for (int i = 0; i < c; i++) {
            alpha[i] = sc.next();
        }
        Arrays.sort(alpha);
        bt(0, 0, 0, 1);
        System.out.println("answer.toString() = " + answer.toString());
    }
}
