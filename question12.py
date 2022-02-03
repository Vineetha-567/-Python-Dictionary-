import abc
from typing import Awaitable, ContextManager


s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
l=list(s.values())
l.sort()
r=l.copy()
r.reverse()
d={}
for i in l:
    # print(i)
    for  j in s:
        if i==s[j]:
            d[j]=i
print("asseding order",d)
e={}
for i in r:
    for j in s:
        if i==s[j]:
            e[j]=i
print("desending order",e)

# print("asssending order",l)
# l.sort(reverse=True)

# print("desending order:",dict(l))