#task1
# a=input()
# big=0
# small=0
# for i in a:
#     if i.isalpha():
#         if i.isupper():
#             big+=1
#         if i.islower():
#             small+=1
# print(f'BIG={big}  SMALL={small}')


#task2
# text=' '
# tex=' '
# a=input()
# gl=('аеёиоуыэюя')
# for i in a:
#     if i in gl:
#         text+=i
#     else:
#         tex+=i
# print(tex)

#task3
# t=' '
# a=input()
# e=('е')
# u=('и')
# tex=' '
# for i in a:
#     if i in e:
#         i=u
#     tex+=i
# print(tex)

#task4
# a=input()
# cnt=0
# for i in a.split():
#     cnt+=1
# print(cnt)

#task5
# a=input()
# cnt=-999999
# for i in a.split():
#     if len(i)>cnt:
#        b=i
# print(b)

#task6
# a=input()
# b=('a')
# cnt=0
# for i in a:
#     if i in b:
#         cnt+=1
# print(cnt)

#task7
# a=input()
# sp=' '
# t=' '
# tx=''
# for i in a:
#     if i in sp:
#         t+=i
#     else:
#         tx+=i
# print(tx)
# a=input()
# t=a.replace(' ','')
# print(t)

#task8
# a=input()
# if a==a[::-1]:
#     print('palindrome')
# else:
#     print('Not palindrome')