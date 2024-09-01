package org.bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj2468 {
    public static class Point{
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int maxRain = 0;
        int answer = 0;
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        int[][] lake = new int[n][n];
        boolean[][] visited = new boolean[lake.length][lake[0].length];

        Queue<int[]> queue = new ArrayDeque<>();

        for (int y = 0; y < n; y++) {
            String s = br.readLine();
            StringTokenizer st = new StringTokenizer(s);
            for (int x = 0; x < n; x++) {
                lake[y][x] = Integer.parseInt(st.nextToken());
                maxRain = Math.max(maxRain, lake[y][x]);
            }
        }

        for (int safe = 0; safe <= maxRain+1; safe++) {
            int area = 0;

            for (int y = 0; y < n; y++) {
                for(int x=0; x < n; x++){
                    if(lake[y][x] <= safe){lake[y][x] = 0;}
                }
            }

            for (int y = 0; y < n; y++) {
                for(int x=0; x < n; x++){
                    if(lake[y][x] != 0 && visited[y][x]){
                        queue.add(new int[]{x, y});

                        while (!queue.isEmpty()) {
                            int[] point = queue.poll();
                            visited[point[1]][point[0]] = false;

                            for (int i = 0; i < 4; i++) {
                                int cx = point[0] + dx[i];
                                int cy = point[1] + dy[i];

                                if (!is_range(cx, cy, n)) {continue;}
                                if(!visited[cy][cx] || lake[cy][cx] == 0){continue;}
                                queue.add(new int[]{cx, cy});
                            }
                        }
                        area += 1;
                    }
                }
            }

            for (int y = 0; y < lake.length; y++) {
                for(int x=0; x< lake[0].length; x++){
                    visited[y][x] = true;
                }
            }

            answer = Math.max(answer, area);
        }
        System.out.println(answer);
        br.close();
    }


    public static boolean is_range(int x, int y, int n) {
        return (0 <= x && x < n) && (0 <= y && y < n); 
    }
}
