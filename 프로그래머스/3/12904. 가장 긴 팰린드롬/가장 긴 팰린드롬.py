def solution(s):
    for length in range(len(s),1,-1):
        middle=length//2
        for i in range(len(s)):
            if i+length>len(s): break
            _next=middle if length%2==0 else middle+1
            new_str=s[i:i+middle]
            reverse_str=new_str[::-1]
            if reverse_str==s[i+_next:i+length]:
                return length
    return 1