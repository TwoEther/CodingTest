package twopointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] subSum = new int[n + 1];
        int start = 0;
        int end = 0;
        int answer = 0;

        subSum[0] = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int a = Integer.parseInt(st.nextToken());
            subSum[i + 1] = subSum[i] + a;
        }

        while (start <= n && end <= n) {
            int sum = subSum[end] - subSum[start];
            if(sum == m){
                answer += 1;
                start += 1;
            }else if(sum < m){end += 1;}
            else{start += 1;}
        }
        System.out.println(answer);
    }

}
