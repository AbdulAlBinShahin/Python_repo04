def number(n):
    unique_num=list(set(n))
    if len(unique_num)<2:
        return "There is no 2nd largest num"
    unique_num.sort(reverse=True)
    return unique_num[1]
 
num=list(map(int,input("enter a num").split()))
 
slar_num=number(num)
print(f"{slar_num}")
