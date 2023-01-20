#1) Write a python class to convert an integer into a roman numeral and viceversa
class int_to_roman:
    def convert(self,n):
        number = [1000, 900, 500, 400,100, 90, 50, 40, 10, 9, 5, 4,  1]
        roman = ["M", "CM", "D", "CD","C", "XC", "L", "XL", "X", "IX", "V", "IV","I"]
        if type(n) is int:
            pos=0
            value=n
            roman_value=''
            while value>0:
                if value - number[pos] >= 0:
                    roman_value=roman_value+roman[pos]
                    value=value-number[pos]
                else:
                    pos=pos+1
            return roman_value
        elif type(n) is str:#vi
             integer_value=number[roman.index(n[-1])]
             for i in range(len(n)-1):#CM
                 if number[roman.index(n[i])]<number[roman.index(n[i+1])]:
                     pos=roman.index(n[i])
                     integer_value-=number[pos]
                 else:
                     pos = roman.index(n[i])
                     integer_value+=number[pos]
        return integer_value
s=int_to_roman()
print(s.convert(1967))
print(s.convert('MCMLXVII'))

#2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].' \
#These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
class validity:
    def check(self,string):
        open=['[','{','(']
        close=[']','}','(']
        new=[]
        for i in string:
            if i in open:
                new.append(i)
            elif i in close:
                oitem=new[len(new)-1]
                pos=open.index(oitem)
                citem=close[pos]
                if i==citem:
                    new.remove(oitem)
                    continue
                else:
                    return 'Invalid'
        if len(new) >0:
            return 'Invalid'
        else:
            return 'Valid'
s=validity()
print(s.check('[{'))

#3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
class unique:
    def distinct(self,s):
        result=[[]]
        for i in s:
            result=result+[j+[i] for j in result ]
        return sorted(result)
value=unique()
print(value.distinct([4,5,6]))

#4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target
# number. Note: There will be one solution for each input and do not use the same element twice.
# Input: numbers= [10,20,10,40,50,60,70], target=50 Output: 2, 3
class Index:
    def sumation(self,li,target):
        for i in range(len(li)-1):
                if li[i]+li[i+1]==target:
                    print(i,i+1)
s=Index()
target=int(input("Enter the target"))
s.sumation([10,20,10,40,50,60,70],target)

#5) Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]
from itertools import combinations
class  group:
    def sum_2_zero(self,li):
        k=list(combinations(li,3))
        for i in k:
            if sum(i)==0:
                print(([i]),end=' ')
s=group()
li=[-25, -10, -7, -3, 2, 4, 8, 10]
s.sum_2_zero(li)

#6) Write a Python class to implement pow(x, n)
class Power:
    def pow(self,a,b):
        return a**b
s=Power()
print(s.pow(3,3))

#7) Write a Python class to reverse a string word by word.
#Input string : 'hello .py' Expected Output : '.py hello'
class reverse:
    def reversed(self,k):
        for i in range(len(k)-1,-1,-1):
            print(k[i],end=" ")
s=reverse()
k=input("Enter a string : ").split( )
s.reversed(k)

#8) Write a python class which has 2 methods get_string and print_string. get_string takes a string
# from the user and print_string prints the string in reverse order
class string:
    def __init__(self,str):
        self.str=str
    def get_string(self):
        self.str=input()
    def print_string(self):
        print(self.str[::-1])
s=string(str)
s.get_string()
s.print_string()

#9) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
from math import pi
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        value=pi*(self.r)**2
        return value
    def perimeter(self):
        peri=2*pi*self.r
        return peri
r=int(input("Enter the radius : "))
s=circle(r)
print("The are of circle is",round(s.area(),2))
print("the perimeter of circle is",round(s.perimeter(),2))

#10) Write a Python program to get the class name of an instance in Python.
class Student:
    def __init__(self):
       print(self.__class__.__name__)
s=Student()

#LAMBDA

#1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.Sample Output: 25 48
x=int(input("Enter value of X"))
y=int(input("Enter value of Y"))
addition=lambda x:x+15
product=lambda x,y:x*y
print(addition(x))
print(product(x,y))

#2) Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
li=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
li.sort(key=lambda li:li[0][1],reverse=True)
print(li)

#3)Write a Python program to sort a list of dictionaries using Lambda.
s=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
new_list=sorted(s, key=lambda s : s['color'])
print(new_list)

#4) Write a Python program to find if a given string starts with a given character using Lambda
s=input("enter a string : ")
k=lambda string:string[0]=='s' and 'True' or 'False'
print(k(s))

#5) Write a Python program to check whether a given string is number or not using Lambda.
s=input("Enter a string : ")
k=lambda x: x.isnumeric()
print(k(s))

#6)  Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
# Orginal list: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen: [19, 65, 57, 39, 152, 190]
li=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
value=list(filter(lambda x:x%19==0 or x%13==0,li))
print(value)

#7) Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
#Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
 #Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
#Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
from functools import reduce
li=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]#sorted(iterable, key=key, reverse=reverse)
k=sorted(li,key=lambda x:sum(x))
print(k)

#8) Write a Python program to check whether a given string contains a capital letter,
# a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string
s='PaceWisd0m'
li=[]
k=lambda s:any(x.isupper()for x in s)
li.append(k(s))
k= lambda s:any(x.islower()for x in s )
li.append(k(s))
k=lambda s:len(s)>1
li.append(k(s))
k=lambda li:all(x==True for x in li) and 'Valid string' or "Invalid string"
print(k(li))

#9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.
#Original list: ['red', 'black', 'white', 'green', 'orange']
#Substring to search: ack Elements of the said list that contain specific substring: ['black']
# Substring to search: abc Elements of the said list that contain specific substring: []
li=['red', 'black', 'white', 'green', 'orange']
s=input("enter a string")
search=list(filter(lambda x: s in x ,li))
print(s,"Elements of the said list that contain specific substring:",search)

#10) Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
#Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
#Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
li=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
li.sort(key=lambda i:(isinstance(i,str),i))
print(li)
