words = input()

d = {}

for word in words:
    d[word.upper()] = d.get(word.upper(), 0) + 1

answer = sorted(d.items(), key=lambda x: -x[1])
mx = answer[0][1]

if len(answer) > 1 and answer[1][1] == mx:
    print("?")
else:
    print(answer[0][0])