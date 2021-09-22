package com.company.Level1.phoneketmon;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Stream;

public class Phonketmon {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> dupDel = new HashSet<>();
        for (int num : nums) {
            dupDel.add(num);
        }

        if (dupDel.size() >= nums.length / 2){
            return nums.length / 2;
        }
        return dupDel.size();
    }

    public static void main(String[] args) {
        int [] num = {3,1,2,3};

        int solution = new Phonketmon().solution(num);
        System.out.println(solution);
    }
}
