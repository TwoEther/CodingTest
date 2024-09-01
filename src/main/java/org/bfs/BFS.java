package org.bfs;

/*
    bfs는 큐를 사용
 */

import java.io.*;
import java.util.*;



public class BFS {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n, m, r;
        String[] line = br.readLine().split(" ");
        n = Integer.parseInt(line[0]);
        m = Integer.parseInt(line[1]);
        r = Integer.parseInt(line[2]);

        int[][] newGraph = new int[n+1][n+1];

        LinkedList<LinkedList<Integer>> graph = new LinkedList<>();
        Boolean[] visited = new Boolean[n + 1];
        Arrays.fill(visited, false);
        int[] position = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            graph.add(new LinkedList<Integer>());
        }
        for (int i = 0; i < m; i++) {
            line = br.readLine().split(" ");
            int u, v;
            u = Integer.parseInt(line[0]);
            v = Integer.parseInt(line[1]);
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(graph.get(i));
        }

        Queue<Integer> queue = new LinkedList<>();
        int start = r;
        int cnt = 1;
        queue.add(start);
        visited[start] = true;
        position[start] = cnt;
        
        while (!queue.isEmpty()) {
            int v = queue.poll();
            for (int i : graph.get(v)) {
                if (!visited[i]) {
                    visited[i] = true;
                    position[i] = ++cnt;
                    queue.offer(i);
                }
            }
        }

        for (int i = 1; i <= n; i++) {

            System.out.println(position[i]);
        }
        bw.flush();
        bw.close();
        br.close();
    }

}
