package sumsum;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj1806 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int[] numbers = new int[n];
        int[] ssum = new int[n+1];
        ssum[0] = 0;
        int start = 0;
        int end = 1;
        int result = 1000001;

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            int k = Integer.parseInt(st.nextToken());
            numbers[i-1] = k;
            ssum[i] = ssum[i - 1] + k;
        }

        while (start <= n && end <= n) {
            int target = ssum[end] - ssum[start];
            if(target < s){
                end += 1;
            }else if(target > s){
                result = Math.min(result, end - start);
                start += 1;
            }else{
                result = Math.min(result, end - start);
                end+=1;
            }
        }
        if(result == 1000001){
            System.out.println(0);
        }else{
            System.out.println(result);
        }

        br.close();
    }
}
