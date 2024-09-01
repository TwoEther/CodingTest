package org.example;

public class BackTracking {
    public static int[] bt(int[] array, int depth, int n){
        if(depth == n){
            return array;
        }
        return new int[]{};
    }

    public static void main(String[] args) {

    }
}
