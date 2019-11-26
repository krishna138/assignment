import abc
from fpdf import FPDF

class MyInterface(abc.ABC):
    def __init__(self,name,mobile,age,city):
        self.name  = name
        self.age = age
        self.mobile = mobile
        self.city = city
    @abc.abstractclassmethod
    def writetofile(self,filename,userformat):
        """User must implement this function and provide first parameter as file name \
        second parameter of the format of the file"""
        pass
   
class MyClass(MyInterface):
    def __init__(self,name,mobile,age,city):
        super().__init__(name,mobile,age,city)
       
    def writetofile(self,filename,userformat):
       
        data = "Name " + self.name + ", " +\
                "Mobile No." + str(self.mobile) + ", " +\
                "Age " + str(self.age) + ", " +\
                "City " + self.city
        if userformat == 'txt':
            with open(filename+".txt",'a+') as f:
                f.write(data)
        elif userformat == 'pdf':
           
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=str(data), align="C")
            pdf.output(filename+'.pdf')
           

name = input("Enter your name ")
mobile = int(input("Enter your mobile number (10 digits only ) "))
age = int(input("Enter your age (int only )"))
city = input("Enter your city ")
filename = input("Enter the file name ")
userformat = input("Enter the formte of file {txt,pdf,etc.} ")
obj = MyClass(name,mobile,age,city)
obj.writetofile(filename,userformat)
