n = 0
words = []
min_len = float('inf')
max_len = float('-inf')
dynamic = dict()
result = 1
with open("wchain.in", "r") as f:
    n = int(f.readline())
    words = [[] for i in range(55)]

    for i in range(n):
        s = f.readline()
        words[len(s)].append(s)
        min_len = min(min_len, len(s))
        max_len = max(max_len, len(s))

for i in range(min_len, max_len + 1):
    if len(words[i-1]) == 0:
        for word in words[i]:
            dynamic[word] = 1
        continue

    for word in words[i]:
        curr_res = 1
        for k in range(i + 1):
            new_word = word[:k] + word[k+1:]
            if new_word in dynamic:
                curr_res = max(curr_res, dynamic[new_word] + 1)

            if (curr_res == i - min_len + 1):
                break

        dynamic[word] = curr_res
        result = max(result, curr_res)

with open("wchain.out", "w") as f:
    f.write(str(result))
