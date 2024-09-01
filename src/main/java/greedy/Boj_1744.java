package greedy;

import java.util.*;

public class Boj_1744 {
    public static int findSumMaxArray(List<Integer> numbers) {
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        for (Integer number : numbers) {
            if(stack.isEmpty()){
                stack.add(number);
            }else{
                int peek = stack.peek();
                if ((peek < 0 && number <= 0) || (peek > 1 && number > 1)) {
                    answer += peek * number;
                }else if(peek == 1 || number == 1){
                    answer += peek + number;
                }
                else{
                    if(peek < 0) answer += peek + number;
                    else if(peek == 0) answer += number;
                    else answer += peek * number;
                }
                stack.clear();
            }
        }
        if(!stack.isEmpty()) answer += stack.peek();
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>();
        
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            numbers.add(x);
        }
        
        Collections.sort(numbers);
        int n1 = findSumMaxArray(numbers);
        Collections.sort(numbers, Comparator.reverseOrder());
        int n2 = findSumMaxArray(numbers);

        System.out.println(Math.max(n1, n2));

    }
}
