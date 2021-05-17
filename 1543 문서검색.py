b = input()
a = input()


def search(data,target):
    index = 0
    result = 0
    #인덱스를 전역변수로 하나 두고 계속 값 증가시키는 구조로 while조건문 구현
    while len(data) - index >= len(target):
        if data[index:index+len(target)] == target:
#여기가 생각도 못함. 그냥 문자열로 리스트 처리가 가능함. 해서
#문자열도 슬라이싱해 target의 길이만큼 슬라이싱 해서 해당 값과 target이 맞는지
#비교후 맞으면 결과 +1, 인덱스 target길이만큼 증가, 아닌경우 인덱스 1 증가.
            result += 1
            index += len(target)
        else :
            index += 1

    return result

r = search(b,a)
print(r)

"""
내가 왜 어려웠는가? => 우선 해당값들 비교와 맞는 경우 target크기 만큼 반복문을
뛰어 넘어야했기에 리스트로 처리해야하는 문자열로 처리해야 하는지 부터 괴리가 오기
시작함. 결국 시작도 못했음.... 생각보다 까다로움
"""
        
    
    
