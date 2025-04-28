#pattern1
# for i in range(5):#0,1
#     for j in range(5-i):#5-0=5,5-1=4
#         print("*",end=" ");
#     print();
#pattern 2
# for i in range(5):#5
#     for j in range(0+i):#
#         print("*",end=" ");
#     print();
#pattern3
# n=int(input("enter the value of n"));
# for i in range(n):
#     for j in range(i+0):
#         print( '%d'%i ,end=" ");
#     print();
#pattern 4
# number=1;
# n = int(input("enter the value of n:"));
# for i in range(n):
#     for j in range(i + 0):
#         print(number, end=" ");
#         number=number+1;
#     print();
#pattern 5

# n=int(input("enter the value of n"));
# for i in range(n):
#     for j in range(i+0):
#         print( '%d'%j ,end=" ");
#     print();
#pattern 6
number=1;
for i in range(5):
    for j in range(i+0):#0+0=0,1+0=1
        print(" ");#0
    for k in range(5-i):#5-0=5,5-1=4
        print(number,end=" ");number=number+1;
print();