class Student :
    clgName = "lit"
    def __init__(self):
        self.rollNo = int(input("Enter Student Roll_No :"))
        self.name = input("Enter Student Name :")
        self.gender = input("Enter Student Gender :")
        self.DeptName = input("Enter Student DeptName :")

    def GetMark(self) :
        self.sub1 = float(input("Enter sub1 mark :"))
        self.sub2 = float(input("Enter sub2 mark :"))
        self.sub3 = float(input("Enter sub3 mark :"))
        self.sub4 = float(input("Enter sub4 mark :"))
        self.sub5 = float(input("Enter sub5 mark :"))
        self.sub6 = float(input("Enter sub6 mark :"))

    def CalMark(self) :
        self.total = self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5 + self.sub6
        per = self.total *100/600
        self.Grade = None
        if per >= 60 :
            self.Grade = "1st Div"
        elif per >= 50 and per < 60 :
            self.Grade = '2nd Div'
        elif per >=35 and per <50 :
            self.Grade = '3rd Div'
        else :
            self.Grade = 'Fail'

    def Display(self): 
        print(f"Student ClgName : {Student.clgName}")
        print(f"Student Roll No : {self.rollNo}")
        print(f"Student Name : {self.name}")
        print(f"Student Gender : {self.gender}")
        print(f"Student DeptName : {self.DeptName}")
        print(f"Student Total secured marks ->{self.total}")
        print(f"Student Grade is : {self.Grade}")

no = int(input("Enter the number of students :"))
for i in range(1,no + 1):
    Sobj1 = Student()
    Sobj1.GetMark()
    Sobj1.CalMark()
    Sobj1.Display()