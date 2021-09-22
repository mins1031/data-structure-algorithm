package com.company.Level1.notcompletion;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.LinkedTransferQueue;
import java.util.stream.Collectors;

public class NotCompletion {
    public String solution(String[] participant, String[] completion) {
        List<String> participantList = Arrays.stream(participant).collect(Collectors.toList());
        List<String> completionList = Arrays.stream(completion).collect(Collectors.toList());
        String answer = "";
        for (String s : participantList) {
            if (!completionList.contains(s)){
                System.out.println(s);
                answer = s;
            }
        }

        return answer;
    }
/**
 * 1. 시작자, 완주자 목록을 비교해 완주자에 없는 사람을 추출해야한다.
 * 2. 두 배열의 비교를 통해 추출하게 된다
 * 3. 허나 동명이인이 있다면 단순 String으로는 구별이 힘들다.
 * => 실패
 * */
    public static void main(String[] args) {
        String[] participant = {"janet","gang","tony","ju","tony"};
        String[] completion = {"tony","janet","gang","ju"};

        String solution = new NotCompletion().solution(participant, completion);
        System.out.println(solution);

    }
}
