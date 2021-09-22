## Phoneketmon
* 개선된 코드에 대한 고찰
```
 public int solution(int[] nums) {
        return Arrays.stream(nums)
            .boxed()
            .collect(Collectors.collectingAndThen(Collectors.toSet(),
              phonekemons -> Integer.min(phonekemons.size(), nums.length / 2)));
 }
 //가시성을 위한 줄이동
```

* collectingAndThen()은 첫 인자로 Collecting을 진행한후 하나의 메서드 동작을 더하게 하는 메서드라고 한다.
  1) 배열을 입력받는다
  2) 스트림API를 이용해 바로 리턴해준다.
  3) boxed()는 해당 스트림을 박싱해준다. 주로 기본 타입과 사용된다
  4) collectingAndThen() 메서드를 통해 nums를 Set으로 Collecting 해준다
  5) 또 나머지 인자는 포켓몬의 종류(4의 결과 phonekemons)와 기존 nums에서 / 2한 몫중 작은 값을 Integer로 반환한다
  6) 바로 Integer를 리턴해준다
  + 폰켓몬은 총 폰켓몬중 반절의 수만 대려갈수 있다.
  + 따라서 폰켓몬의 종류가 반절의 수보다 적다면 종류를, 많다면 반절의 수가 최대 종류값이 된다.
* 결국 스트림을 사용해 set으로 변환하는 작업, 가장 작은 것을 골라내는 작업 두개를 하나의 스트림안에서 모두 해결했다.ㄷㄷ
