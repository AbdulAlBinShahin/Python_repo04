def c_vowel(s):
    vowel="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowel:
            count+=1
    return count
string=input("enter string: ")
vowel_count = c_vowel(string)
print(f"The number of vowels in the given string is : {vowel_count}")
