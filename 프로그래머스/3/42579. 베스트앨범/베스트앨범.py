from collections import defaultdict
def solution(genres, plays):
    answer = []
    genres_dict=defaultdict(int)

    length=len(genres)
    for i in range(length):
        genres_dict[genres[i]]+=plays[i]
    
    while(True):
        first_genre=max(genres_dict, key=genres_dict.get)
        first_plays, second_plays=[], []
        for i in range(length):
            if genres[i]==first_genre: first_plays.append((plays[i], i))
        
        first_plays.sort(key=lambda x: (-x[0]))
        answer.append(first_plays[0][1])
        if len(first_plays)>=2 :answer.append(first_plays[1][1])

        genres_dict.pop(first_genre)
        
        if len(genres_dict)==0:
            return answer