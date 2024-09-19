package union;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Boj1822 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> result = new ArrayList<>();
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int[] nA = new int[a];
        int[] nB = new int[b];
        int idx = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < a; i++) {
            nA[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < b; i++) {
            nB[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nA);
        Arrays.sort(nB);

//        System.out.println(Arrays.asList(nA).removeAll(Arrays.asList(nB)).toString());
        br.close();
    }
}
