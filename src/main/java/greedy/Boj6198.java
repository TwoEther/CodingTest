package greedy;

import java.util.Scanner;
import java.util.Stack;

public class Boj6198 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> outputStack = new Stack<>();
        int answer = 0;
        int n = sc.nextInt();
        int[] numbers = new int[n];

        for (int i = 0; i < n; i++) {
            int k = sc.nextInt();
            stack.add(k);
        }

        for (int i = n - 1; i >= 0; i--) {
            int target = numbers[i];
            int visible = 0;
            if (stack.isEmpty()) {
                stack.add(target);
            } else {
                while (!stack.isEmpty() && stack.peek() > target) {
                    stack.pop();
                    answer += visible++;
                }
            }
        }

        System.out.println(answer);
        sc.close();

    }
}
