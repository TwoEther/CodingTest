package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj16234 {
    /*
        1. 국경을 열어야 하는 나라 탐색
        2. 해당 나라를 대상으로 인구수 변경
     */
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int n;
    static int l;
    static int r;
    static int[][] country;


    public static class Pointer {
        private int x;
        private int y;

        public int sum() {
            return this.x + this.y;
        }

        public Pointer(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "Pointer{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }
    public static boolean is_range(int x, int y) {
        return (0 <= x && x < n) && (0 <= y && y < n);
    }

    public static int findOpenBoundaryCountry() {
        boolean[][] visited = new boolean[n][n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    List<Pointer> list = new ArrayList<>();
                    Queue<Pointer> queue = new ArrayDeque<>();

                    queue.add(new Pointer(i, j));
                    list.add(new Pointer(i, j));

                    while (!queue.isEmpty()) {
                        Pointer poll = queue.poll();
                        int x = poll.x;
                        int y = poll.y;
                        visited[y][x] = true;

                        for (int k = 0; k < 4; k++) {
                            int cx = x + dx[k];
                            int cy = y + dy[k];

                            if(!is_range(cx, cy)){continue;}
                            int diff = Math.abs(country[y][x] - country[cy][cx]);
                            if (l <= diff && diff <= r && !visited[cy][cx]) {
                                queue.add(new Pointer(cx, cy));
                                list.add(new Pointer(cx, cy));
                            }

                        }
                    }

                    if(list.size() == 1){continue;}
                    int sum = list.stream().mapToInt(Pointer::sum).sum();
                    for (Pointer pointer : list) {
                        int x = pointer.x;
                        int y = pointer.y;

                        country[y][x] = sum / list.size();
                    }
                    for (Pointer pointer : list) {
                        System.out.println("pointer.toString() = " + pointer.toString());
                    }
                    System.out.println("----------------");
                    answer += 1;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        country = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                country[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(findOpenBoundaryCountry());

        br.close();
    }
}
