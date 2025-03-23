def abbreviate_words(n, words):
    result = []
    for word in words:
        if len(word) > 10:
            abbreviated = f"{word[0]}{len(word) - 2}{word[-1]}"
            result.append(abbreviated)
        else:
            result.append(word)
    return result

# Input
n = int(input())
words = [input().strip() for _ in range(n)]

# Process and Output
result = abbreviate_words(n, words)
for res in result:
    print(res)
