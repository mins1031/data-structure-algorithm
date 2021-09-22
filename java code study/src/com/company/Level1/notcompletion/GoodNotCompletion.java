package com.company.Level1.notcompletion;

import java.util.HashMap;

public class GoodNotCompletion {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion) hm.put(player, hm.get(player) - 1);

        for (String key : hm.keySet()) {
            if (hm.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }

    /**
     * map자체를 생각못함.... 사용해본 적이 없어서 생각이 안난것 같다. 이 기회에 사용해보자
     * 1. 우선 문자열 key와 정수형 value를 가지는 해시맵을 생성한다.
     * 2. key로는 각 배열의 이름값과 value값은 1씩 넣어준다.
     * + put은 첫 인자의 키값이 map에 이미 존재하면 value를 덮어쓴다.
     * + getOfDefault메서드는 첫번쨰 인자가 Map에 존재하지 않는다면 두번쨰 인자 값을 넣고 존재한다면 해당 value값에 두번쨰 인자를 덮어쓴다
     * 3. 동명이인이 participant에 있다면 participant에 대한 for문이 다 돌고 나면 동명이인의 value값은 2일것이다(동명이인이 2명이라는 가정하)
     * 4. 이후 completion에 대한 for문을 돌리며 완료자 값을 맵에서 찾아서 value값을 다시 -1 시킨다
     * 5. 이렇게 되면 완주자 목록에 있는 key의 value는 다시 0이 될것이고 map에서 0이 아닌 key를 찾아주면 클리어한다.
     * */
}
