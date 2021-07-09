import sys

words1 = sys.stdin.readline().strip()
words1_len = len(words1)
words2 = sys.stdin.readline().strip()
words2_len = len(words2)

# row : words1
# col : words2
graph = [[0 for _ in range(words2_len)] for _ in range(words1_len)]

answer = 0
for i in range(words1_len):
    for j in range(words2_len):
        if words1[i] == words2[j]:
            if i >= 1 and j >= 1:
                graph[i][j] += graph[i - 1][j - 1] + 1
            else:
                graph[i][j] += 1
                
            answer = max(answer, graph[i][j])

print(answer)