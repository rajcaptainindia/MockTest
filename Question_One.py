#Jai Ganesha 

def reverse(num):
    strnum=str(num)
    rev=strnum[::-1]
    return(int(rev))
    
def is_palendrome(num):
    if(num == reverse(num)):
        return True
    return False

def solution(number):
    while(True):
        number=reverse(number)+number
        if(is_palendrome(number)):
            break
        else:
            continue
    print(number)
    
#NUMBER 
number=124
solution(number)
