package com.company.Level1.phoneketmon;

import java.util.Arrays;
import java.util.stream.Collectors;

public class GoodPhonketmon {
    public int solution(int[] nums) {
        return Arrays.stream(nums)
                .boxed()
                .collect(Collectors.collectingAndThen(Collectors.toSet(),
                        phonekemons -> Integer.min(phonekemons.size(), nums.length / 2)));
        //collectingAndThen()은 첫 인자로 Collecting을 진행한후 하나의 메서드 동작을 더하게 하는 메서드라고 한다.
        /**
         * 1. 입력받은 배열을
         * 2. 박싱해서 Integer로 만들고
         * 3. 컬렉션으로 만드는데 이걸 Set으로 만들어 중복을 없애고
         * 4. 폰켓몬 종류와 총 길이/2를 비교해 작을쪽을 리턴한다.
         * 5. 결국 4에 의해 Integer가 리턴된다.
         * */
    }
}
