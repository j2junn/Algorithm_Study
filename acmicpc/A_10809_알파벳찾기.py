alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabets_cnt = [-1 for _ in range(26)]

S = input()

for i, s in enumerate(S):
    if s in alphabets:
        if alphabets_cnt[alphabets.index(s)] == -1:
            alphabets_cnt[alphabets.index(s)] = i

print(" ".join(map(str, alphabets_cnt)))

# find를 쓰면 훨씬 더 빠르다
# for ascii in range(97, 123):
#     print(S.find(chr(ascii)), end=' ')