# Repeated Substring
def f(s):  
    z=""
    for ch in s:
        z +=ch
        c = s.count(z)
        t = len(z)
        if t*c == len(s):
            return (z, c)  
#Simple String Matching
def solve(a,b):
    l = a.find('*') 
    return ("*" in a and len(a)-1<=len(b) and a[:l] == b[:l] or a == b )
# Is it a palindrome
def is_palindrome(x):
    x=str(x) 
    x = x.replace(" ","")
    return x == x[::-1]
#find_nth_occurrence
def find_nth_occurrence(substring,string,occurrence=1):
    x,n,c=0,0,0
    for i in range(len(string)):
        if string.startswith(substring,i):c +=1
    if c>=occurrence:
        while x<occurrence :
            IN = string.find(substring, n)
            n=IN+1
            x +=1
        return(IN)
    else:return(-1)