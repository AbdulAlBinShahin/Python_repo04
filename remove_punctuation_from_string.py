import string
def rev_punc(s):
    translator=s.maketrans('','',string.punctuation)
    return s.translate(translator)
 
s=input("enter: ")
wo_punc=rev_punc(s)
print(f"rev punc is {wo_punc}")
