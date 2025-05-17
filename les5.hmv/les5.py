#task1
# def pl(a):
#     if(a==a[::-1]):
#         return "palindrome"
#     else:
#         return "not palindrome"

# print(pl("madam"))

#task2
# def slst(ls):
#     cnt=0
#     for i in ls:
#         cnt+=i
#     return cnt

# print(slst([1,2,3,4]))

#task3
# def greet(a):
#     if a=="":
#         return "Hello Guest"
#     else:
#         return (f"Hello {a}")
    
# print(greet('g'))

#task4
# def m(a,b,c):
#    if a>=b and a>=c:
#       return a
#    if b>=a and b>=c:
#       return b
#    else:
#       return c

# print(m(5,9,25))

#task5
# def gl(a):
#     glas=('aeiou')
#     cnt=0
#     for i in a:
#         if i in glas:
#             cnt+=1
#     return cnt
# print(gl('hello'))

#task6
st_dublicat=[1,2,2,3,1]
def func(lst_dublicat):
    lst1=[]
    for i in lst_dublicat:
        if i not in lst1:
            lst1.append(i)
    return lst1
print(func(st_dublicat))

#task7
# def ct(a):
#     for i in a:
#         if i%2==0:
#             print(i)

# ct([1,2,3,4,5,6])

#task8
# def sm(a):
#     cnt=0
#     i=a
#     while(i>0):
#         cnt+=i%10
#         i//=10
#     return cnt

# print(sm(124))

#task9
# str1 = ['hello', 'world', 'Python', 'code']
# def func(lst):
#     for i in lst:
#         if i[0].isupper():
#             return i
#     return 0


# print(func(str1))


