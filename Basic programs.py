#1.reversed a string by using functions and built in methods
#using built in method
#method1
s='hello'
rev_string=s[ : :-1]
print(rev_string)
#method2
string = "hello"
reversed_string = ''.join(reversed(string))
print(reversed_string)
#using functions
s=input()
def rev_string(s):
    rev=''
    for i in s:
        rev=i+rev
    return rev
#s='hello'
print(rev_string(s))







