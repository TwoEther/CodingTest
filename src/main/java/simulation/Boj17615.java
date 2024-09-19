package simulation;

import java.util.Scanner;

public class Boj17615 {
    public static void main(String[] args) {
        // 맨 끝 색상에 따른 2가지의 경우의 수 존재
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        char[] colors = s.toCharArray();
        int answer = 500001;

        // 맨 끝의 값이 R
        if (colors[colors.length - 1] == 'R') {
            // R을 움직이는 경우
            // R로 이루어진 배열은 움직일 필요가 없음
            int idx = colors.length;
            int result = 0;
            
            while(--idx >= 0 && colors[idx] == 'R'){}

            for (int i = 0; i < idx; i++) {
                if(colors[i] == 'R'){result += 1;}
            }
            answer = Math.min(answer, result);
            result = 0;

            // B를 움직이는 경우
            for (int i = colors.length-1; i >= 0; i--) {
                if(colors[i] == 'B'){result += 1;}
            }
            answer = Math.min(answer, result);


        }else{
            int idx = colors.length;
            int result = 0;

            while(--idx >= 0 && colors[idx] == 'B'){}

            for (int i = 0; i < idx; i++) {
                if(colors[i] == 'B'){result += 1;}
            }
            answer = Math.min(answer, result);
            result = 0;
            // R을 움직이는 경우
            for (int i = colors.length-1; i >= 0; i--) {
                if(colors[i] == 'R'){result += 1;}
            }
            answer = Math.min(answer, result);
        }
        System.out.println(answer);
        
        sc.close();

    }
}
