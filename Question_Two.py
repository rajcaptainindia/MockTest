#jai Ganesha

def list_to_num(sub_list):
    res=""
    for i in sub_list:
        res+=str(i)
    #print(res)
    return res
    
def solution(list1):
    res=[]
    for i in range(len(list1)):
        for j in range(len(list1)):
            for k in range(len(list1)):
                if(i!=j and j!=k and k!=i):
                    sub_list=[list1[i],list1[j],list1[k]]
                    res.append(list_to_num(sub_list))
    unique_res_list=list(set(res))
    print(max(unique_res_list),len(unique_res_list),sep=",")
    
# INPUT     
list1=[1,2,1,4]
solution(list1)


