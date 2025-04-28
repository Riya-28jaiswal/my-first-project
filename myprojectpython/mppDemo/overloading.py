#method of method overloading
# def sum(a,b=None):
#     if b is not None:
#         print("addtion",(a+b));
#     else:
#          print("value of a",a);
# sum(10,10);
# sum(10);
#method of method overriding
class parent:
     def msg(self):
         print("this is base chlid");
class child(parent):
     def msg(self):
         print("this is chlid class");
d=child();
d.msg();