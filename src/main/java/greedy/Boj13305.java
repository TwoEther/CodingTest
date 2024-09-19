package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Boj13305 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] distances = new int[n - 1];
        int[] costs = new int[n];
        int[] sumSum = new int[n+1];
        int[] dp = new int[n + 1];
        
        sumSum[0] = sumSum[1] = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < distances.length; i++) {
            int v = Integer.parseInt(st.nextToken());            
            distances[i] = v;
            sumSum[i+2] += sumSum[i+1] + v;
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < costs.length; i++) {
            int v = Integer.parseInt(st.nextToken());
            costs[i] = v;
        }

        dp[0] = dp[1] = 0;
        dp[2] = costs[0] * distances[0];

        for (int i = 3; i <= n; i++) {
            dp[i] = costs[0] * sumSum[i];
            for (int j = 2; j < i; j++) {
                dp[i] = Math.min(dp[i], (dp[j] + costs[j - 1] * (sumSum[i] - sumSum[j])));
            }
        }
        System.out.println(dp[n]);

        br.close();
    }
}
