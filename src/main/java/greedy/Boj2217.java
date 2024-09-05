package greedy;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Boj2217 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] numbers = new int[n];
        int maxWeight = 0;
        int totalWeight = 0;

        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }

        Arrays.sort(numbers);

        for (int i = n-1; i >= 0; i--) {
            maxWeight = Math.max(maxWeight, numbers[i] * (n-i));
        }

        System.out.println(maxWeight);
        sc.close();

    }

}
