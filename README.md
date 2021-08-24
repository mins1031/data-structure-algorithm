# data-structure-algorithm
## 1. 순차자료구조 vs 연결자료구조
* 순차자료구조는 메모리상에서 일렬로 나열된 데이터형이다
* 연결자료규조는 메모리 상에서는 분산되어 있지만 하나의 노드가 다음으로 이어지는 포인터를 가지고 있어 연속적으로 접근이 가능한 데이터형이다.
* 데이터 삽입 : 순차자료구조의 마지막에 데이터를 삽입하는 경우는 빠르지만 처음과 중간에 삽입하는 경우에는 자리교환으로 인한 오버헤드가 발생하여 느리다. 연결 자료구조는 데이터를 어디에 삽입하던 해당 위치까지 엑세스하는 시간만 소요되지만 자료 추가시 링크만 교체하면 되므로 빠르다.
* 데이터 읽기 : 연결자료구조는 위치를 알던 모르던 관계없이 해더부터 찾으려는 위치까지 탐색해야 하므로 느리다. 순차 자료구조는 탐색하려는 위치를 알고 있다면 즉시 엑세스 할 수 있으므로 빠르며 탐색하려는 위치를 모른다고 하더라도 메모리 상에서 근접한 데이터의 접근이 더 빠르므로 연결 자료구조보다 빠르다.
## 배열(Array)
* 데이터를 나열하고 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
  * 배열의 필요성
    * 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
    * 같은 종류의 데이터를 순차적으로 저장
    * 장점 : 빠른 접근이 가능하다 
    * 단점 : 데이터 추가 삭제가 어렵다
## 2. 큐
### 큐의 구조
  * 줄을 서는 행위와 유사하다
  * 가장 먼저 넣은 데이터를 가장 먼저 꺼낼수 있는 구조(FIFO=First-in,First-out)
  * 택시승강장을 생각해보면 된다. 먼저온 택시가 먼저 손님을 태우고 나간다.
  <img src="https://user-images.githubusercontent.com/72924060/129683395-77044ed8-2180-4043-acae-4938d2922552.png">
  * 큐의 가장 첫 원소를 front, 끝 원소를 rear이라고 한다
  * 큐는 데이터가 들어올떄 rear로 들어오지만 나올떄는 front부터 빠지는 특성을 가진다. 접근방법은 가장 첫 원소와 끝 원소로만 가능하다. 
  * 큐의 활용 예시
    * 컴퓨터 내부의 프로세스 구조의 함수 동작 방식?
    * 우선 순위가 같은 작업 예약(프린터의 인쇄 대기열) 

## 3. 스택
* 데이터를 제한적으로 접근 할 수 있는 구조
  * 한쪽 끝에서만 자료를 넣거나 뺄수 있는 구조이다.
* 가장 나중에 쌓은 데이터를 가장 먼저 뺴낼수 있는 데이터 구조(LIFO정책 Last-in, First-out)
### 스택 구조
  * 스택은 LIFO 혹은 FILO(First-in,Last-out) 데이터 관리 방식을 따름
  * 대표적 스택의 활용
    * 웹 브라우저 방문기록(뒤로가기)
    * 실행 취소
    * 역순 문자열 만들기 : 가장 나중에 입력된 문자부터 출력
### 스택의 장단점
  * 장점
    * 구조가 단순해 구현이 쉽다
    * 데이터 저장/읽기 속도가 빠르다
  * 단점 
    * 데이터 최대 갯수를 미리 정해야 한다.
    * 저장 공간의 낭비가 발생 가능.  

## 4. 링크드 리스트
### 1) 링크드 리스트 구조
* 연결리스트 라고도 함
* 배열은 순차적으로 연결된 공간에 데이터를 나열하는 구조
* 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로(주소기억) 연결해서 관리하는 데이터 구조 이다.
* 결국 링크드 리스트는 배열처럼 값만 들어가는 것이 아닌 값이 들어가고 다음값의 주소값을 가지고 있는(혹은 전의 데이터 주소까지) 2~3개의 데이터가 합쳐져 있는 형태라고 생각하면 된다.
* 노드 : 데이터의 저장단위(데이터값, 주소값)로 구성 즉 해당 메모리 데이터값과 다음 데이터의 주소값이 있는 형태가 노드라고 표현된다.
* 포인터 : 각 노드안에서 다음이나 이전 노드의 연결정보를 가지고 있는 공간
 <img src="https://en.wikipedia.org/wiki/Linked_list"/>
 
 ### 2. 간단한 링크드 리스트
 ```
 class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 ```
 * 위처럼 하나의 노드를 하나의 클래스로 구현하는 건이 가장 간단한 방법이다.
 
 ### 3. 링크드 리스트 장단점
 * 장점
   * 미리 데이터 공간을 할당하지 않아도 된다(배열은 미리 해야함-> 큐..스택..)
 * 단점
   * 연결을 위한 별도 데이터 공간이 필요 하므로 저장공간 효율이 높지 않음
   * 연결 정보를 찾는 시간이 필요하므로 접근속도가 느림
   * 중간 데이터 삭제시 앞뒤데이터의 연결을 재구성해야 하는 부가적인작업 필요   

## 5. 해쉬
### 1) 해쉬 구조
* 해쉬 테이블 : 키(key)에 데이터(value)를 저장하는 데이터 구조
  * key를 통해 바로 데이터를 받아올 수 있으므로 속도가 획기적으로 빨라짐 
  * 보통 배열로 미리 해쉬테이블 사이즈만큼 생성후에 사용

### 2) 알아둘 용어
* 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
* 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
* 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
* 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
* 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
<img src="https://www.fun-coding.org/00_Images/hash.png" width=400 />

### 3) 해쉬 테이블의 장단점과 주요 용도
* 장점
  * 데이터 저장/일기 속도가 빠르다(검색속도가 빠르다)
  * 해쉬는 키에대한 데이터가 있는지(중복)확인이 쉽다
* 단점
  * 일반적으로 저장공간이 좀더 많이 필요하다
  * 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요하다   
* 주요 용도
  * 검색이 많이 필요한 경우
  * 저장, 삭제, 읽기가 빈번한 경우
  * 캐쉬 구현시(중복 확인이 쉽기 때문에) 
### 4) 간단 구현
* 다양한 해쉬함수 기법이 존재하지만 가장 간단한 나누기를 동한 방식을 구현했다.
```
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data) // 해시함수를 통해 해당 데이터의 키값을 추출

def hash_function(key):
    return key % 8  // 테이블의 크기가 8개기에 8개중 어디에 저장할지 정해준다.

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
    
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
read_data('Dave')

print(hash_table) => ['0102030200', 0, 0, 0, 0, 0, 0, '01033232200']
```
### 5) 충돌 해결 알고리즘
> 해쉬 테이블의 가장 큰 문제는 여러데이터의 키값이 충돌하는 상황이다.이 문제를 충돌(Collision) 또는 해쉬충돌(Hash Collision) 이라고 한다

1) Chaining 기법
  * 개방 해슁 또는 Open Hashing 기법중 하나이다. 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
  * 충돌이 일어나면 충돌이 일어난 데이터들을 링크드 리스트를 사용해 데이터를 추가로 뒤에 연결시켜서 저장하는 기법
2) Linear Probing 기법
  * 폐쇄 해슁 또는 Close Hashing 기법중 하나이다. 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
  * 충돌이 일어나면 해당 해쉬 주소의 다음 주소 부터 맨 처음 나오는 빈공간에 저장하는 기법
    * 저장 공간 활용도를 높이기 위한 기법
### 6) 시간 복잡도
* 일반적인 경우(충돌이 없는 경우) O(1)
* 최악의 경우(충돌이 모두 발생하는 경우) O(n)
* 16개의 배열에 데이터를 저장후 검색시 -> O(n)
* 16개의 데이터 저장공간을 가진 해쉬 테이블에 데이터를 저장후 검색시 -> O(1) : 데이터마다 키값을 만들고 저장하기에 데이터 검색시 해당데이터의 키값만 테이블에서 찾아주면 되기 때문이다.
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcmb93t%2FbtqITt7eR8A%2FmGgrbmF8XUo38BG1SiYLi1%2Fimg.png"/> 
