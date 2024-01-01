from collections import Counter

def solution(str1, str2):
    str1=str1.upper()
    str2=str2.upper()

    list1=[]
    list2=[]

    # make list1 & list2
    for idx,val in enumerate(str1):
        if idx==len(str1)-1:
            break
        if val.isalpha() and str1[idx+1].isalpha():
            list1.append(val+str1[idx+1])
        
  
    for idx,val in enumerate(str2):
        if idx==len(str2)-1:
            break
        if val.isalpha() and str2[idx+1].isalpha():
            list2.append(val+str2[idx+1])

    list1_counter= Counter(list1)
    list2_counter= Counter(list2)


    union = list((list1_counter|list2_counter).elements())
    intersection= list((list1_counter&list2_counter).elements())

    if len(union)==0:
        if len(intersection)==0:
            return 65536
        else:
            return 0
    
    answer = 65536*(len(intersection)/len(union))
    return answer//1
