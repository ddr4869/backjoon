def solution(n, words):
    words_list=[]
    previous=words[0]
    words_list.append(words[0])
    for i,word in enumerate(words):
        if i==0: continue
        if word[0]!=previous[-1] or word in words_list:
            break
        words_list.append(word)
        previous=word
    if previous==words[-1]:
        return [0,0]
    return [i%n+1, 1+i//n]