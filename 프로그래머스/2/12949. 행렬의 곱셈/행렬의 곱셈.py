def solution(arr1, arr2):
    arr1_y=len(arr1)
    arr1_x=len(arr1[0])
    arr2_y=len(arr2)
    arr2_x=len(arr2[0])
    answer=[[0 for _ in range(arr2_x)] for _ in range(arr1_y)]

    for y in range(arr1_y):
        for x in range(arr2_x):
            for i in range(arr1_x):
                answer[y][x] += arr1[y][i]*arr2[i][x]
    return answer