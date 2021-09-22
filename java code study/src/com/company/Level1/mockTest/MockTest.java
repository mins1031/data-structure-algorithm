package com.company.Level1.mockTest;

import java.util.ArrayList;
import java.util.List;

public class MockTest {

    public int[] solution(int[] answers) {
        int [] first = {1,2,3,4,5};
        int [] second = {2,1,2,3,2,4,2,5};
        int [] third = {3,3,1,1,2,2,4,4,5,5};

        int firstCnt = 0;
        int secondCnt = 0;
        int thirdCnt = 0;

        int [] result = new int[3];

        for (int i = 0; i< answers.length; i++){
            if (answers[i] == first[firstCnt]){
                result[0]++;
            }
            if (answers[i] == second[secondCnt]){
                result[1]++;
            }
            if (answers[i] == third[thirdCnt]){
                result[2]++;
            }

            if (firstCnt < first.length -1)
                firstCnt++;
            else
                firstCnt = 0;
            if (secondCnt < second.length -1)
                secondCnt++;
            else
                secondCnt = 0;
            if (thirdCnt < third.length -1)
                thirdCnt++;
            else
                thirdCnt = 0;
        }

        int maxCnt = result[0];

        for (int i = 1; i < 3 ; i++){
            if (result[i] > maxCnt)
                maxCnt = result[i];
        }

        List<Integer> list = new ArrayList<>();

        if (result[0] == maxCnt)
            list.add(1);
        if (result[1] == maxCnt)
            list.add(2);
        if (result[2] == maxCnt)
            list.add(3);

        list.stream().sorted();

        int [] answer = new int[list.size()];

        for (int i=0;i<list.size();i++){
            answer[i] = list.get(i);
        }

        list.stream().mapToInt(i->i.intValue()).toArray();

        return answer;
    }

    public static void main(String[] args) {
        // write your code here
        int [] answers = {1,2,3,4,5};
        int [] answer = new MockTest().solution(answers);
        for (int result: answer) {
            System.out.println(result);
        }

    }

    /**
     * 1. 1번,2번,3번 수포자가 찍는 방식이 다르다
     * 2. 각자의 방식은 규칙을 띈다
     * 3. 해당 규칙을 따라 answers배열의 내용에 맞고 다름을 봐준다
     * 규칙 = 배열, 정답 = 배열 다만 문제의 수만큼 반복문이 돌아가야 한다.
     * 그럼 하나의 반복문에서 3개의 규칙을 모두 검수하는게 낫겠다
     *  각 규칙마다의 배엺의 수가 있으므로 각각의 카운트 값을 가지고 카운트가 만족되면 카운트를 줄여준다
     * 4. 이후 맞는 카운트에 따라 누가 제일 큰지 판별해 줄력한다.
     *
     * */
}
