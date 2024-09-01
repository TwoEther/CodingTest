package org.bfs;

import java.util.*;
import java.util.stream.IntStream;

public class Boj5014 {
    public static class Point{
        int stair;
        int depth;

        public Point(int stair, int depth) {
            this.stair = stair;
            this.depth = depth;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Point> queue = new ArrayDeque<>();
        int[] cost = new int[1000001];
        Arrays.fill(cost, 100000000);

        int f = Integer.parseInt(sc.next());
        int s = Integer.parseInt(sc.next());
        int g = Integer.parseInt(sc.next());
        int u = Integer.parseInt(sc.next());
        int d = Integer.parseInt(sc.next());
        int answer = 0;

        if(s == g){System.out.println(0);}
        else {
            queue.add(new Point(s, 0));
            while (!queue.isEmpty()) {
                Point poll = queue.poll();
                int upStair = poll.stair + u;
                int downStair = poll.stair - d;
                int depth = poll.depth;

                if (upStair == g || downStair == g) {
                    answer = depth + 1;
                    break;
                }

                if (upStair <= f && cost[upStair] > depth) {
                    cost[upStair] = depth;
                    queue.add(new Point(upStair, depth + 1));
                }
                if (downStair >= 1 && cost[downStair] > depth) {
                    cost[downStair] = depth;
                    queue.add(new Point(downStair, depth + 1));
                }
            }
            if (answer != 0) {
                System.out.println(answer);
            } else {
                System.out.println("use the stairs");
            }
        }
        sc.close();

    }



}
