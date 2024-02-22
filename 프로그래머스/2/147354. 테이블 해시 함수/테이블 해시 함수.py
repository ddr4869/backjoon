def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0] ))
    sum, bitwise=0, []
    for row_idx in range(row_begin-1, row_end):
        sum=0
        for col in data[row_idx]:
            sum+= col%(row_idx+1)
        bitwise.append(sum)
    
    for i in range(len(bitwise)-1):
        bitwise[i+1] = bitwise[i] ^ bitwise[i+1]
    return bitwise[-1]