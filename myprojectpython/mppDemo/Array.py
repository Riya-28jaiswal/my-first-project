# first program
# import array
# lst=[12,23,45,"john"];
# lst1=[23,45,67,89];
#
# arr=array.array('d',[12,45,34,89,56,78,90]);
# # print(type(arr));
# arr.append(76)
# arr.insert(2,100);
# print(arr)
# program no. 2
import array as ar
arr=ar.array('i',[]);
n=int(input("how many elements you want ?"));
for i in range(n):
    x=int(input("enter elements:"));
    arr.append(x);
print(arr);
