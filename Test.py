words = ["a","aba","ababa","aa"]
ans = 0
for s in range(len(words)):
    i = len(words[s])
    for c in range(s+1,len(words)):
        print(words[c][:i])
        print(words[c][-i:])
        if words[s]==words[c][:i] and words[s]==words[c][-i:]:
            ans+=1
print(ans)