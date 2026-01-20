# sum=0
# for i in range(1,101,5):
#     sum=sum+i
# # print(sum)
# for i in range(100,9,-1):
#     print(i)

# sum=0
# for i in range(100,9,-5):
#     sum=sum+i
# print(sum)
# fact=1
# for i in range(5,0,-1):
#     fact=fact*i
# print(fact)
# sum=0
# for i in range(2,21):
#        sum=sum+i*i
# # print(sum)
# for i in range(2,101):
#     if i%4==0:
#       print(i)
# for i in range(2,201):
#     if i%10==5 or i%10==0:
#         print(i)
# for i in range(2,201):
#     if i%5==0:
#         print(i)
# for i in range(1,101):
#     if i%7==0:
#         print(i)
# for i in range(7,101):
#     if i%8==0:
#         continue
#     print(i)
# for i in range(2,101):
#     if i%5==0 or i%7==0:
#         continue
#     print(i)
# for i in range(1,251):
#     if i%50==0:
#         continue
# #     print(i)
# count=0
# for i in range(10,101):
#     if i%5==0 or i%7==0:
#         count=count+1
# print('total count',count)
# for i in range(1,101):
#     if i**3>=2000:
#      break
    #  print(i)
     
#     print(f'cube is {i} X {i} X {i} is {i*i*i}')
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum/10)
# n=int(input('enter a num'))
# while n<=10:
#     print(n)
#     n=n+1
# n=int(input('enter a num'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# n=int(input('enter a num'))
# sum=0
# while n<=10:
#     sum=sum+n
#     n=n+1
# print(sum)
# n=int(input('enter a num'))
# i=1
# while i<=10:
#     print(f'table is {n} X {i} is {n*i}')
#     i=i+1
# n=int(input('enter by a num'))
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print(count)
# n=int(input('enter a num')) 
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print(count)   
# n=int(input('enter a num'))
# for i in range(0,n+1):
#     for j in range(n-i,0,-1):
#         print(j,end=' ')
#     print()
# for i in range(-10,0,1):
#     print(i)
# for i in range(5):
#     print(i)
# else:
# #     print('done')
# start=25
# end=50
# for n in range(start,end+1):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#         else:
#             print(n)
# a=int(input('enter a num'))
# b=int(input('enter a num'))
# for n in range(a,b+1):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#         else:
#             print(n)
# a=0
# b=1
# for i in range(10):
#     print(a)
#     a,b=b,a+b
# n=int(input('enter a num'))
# fact=1
# for i in range(n,0,-1):
#     fact=fact*i
#     i=i-1
# print(fact)
rev=0
n=input('enter a num')
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
