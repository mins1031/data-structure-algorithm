# 선택테스트 - 모음찾기

def find_vowel(charactor):
    count = 0
    for i in range(len(charactor)):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            count += 1
    return count


s = "abracadabra"
print(find_vowel(s))
