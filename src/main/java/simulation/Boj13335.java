package simulation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Boj13335 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Queue<Integer> queue = new ArrayDeque<>();

        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int[] weights = new int[n];
        int time = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int weight = Integer.parseInt(st.nextToken());
            weights[i] = weight;
        }

        /*
            하나의 트럭이 도하를 시도할 때 현재 트럭 무게의 총합과 다리의 최대하중과 비교
         */
        int total_weight = 0;
        for (int weight : weights) {
            total_weight += weight;
            // 도하중인 트럭이 없다면
            if (queue.isEmpty() || total_weight <= l) {
                time += 1;
            }else{
                int current_truck_count = queue.size();
                while (total_weight > l && !queue.isEmpty()) {
                    int poll = queue.poll();
                    total_weight -= poll;
                    time += (w-current_truck_count) + 1;
                }
            }
            queue.add(weight);
        }

        if (!queue.isEmpty()) {
            time += w;
        }

        System.out.println(time);
        br.close();
    }
}
