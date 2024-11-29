def rev(n):
    s=str(n)
    s=s[::-1]
    return int(s)
num = int(input("Enter number"))
rev_num=rev(num)
print(f"reverse num is {rev_num}")
