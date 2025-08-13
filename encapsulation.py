# ENCAPSULATION #
##SCHOOL REPORT CARD##
class ReportCard:
    def __init__(self,name):
        self.name=name
        self.__maths=0
        self.__english=0
        self.__science=0
        self.__socail=0
        self.__tamil=0
    def set_scorces(self,tamil,english,maths,science,socail):
        if 0 <= tamil <= 100:
            self.__tamil=tamil
        if 0 <= english <= 100:
            self.__english=english
        if 0 <= maths <= 100:
            self.__maths=maths
        if 0 <= science <= 100:
            self.__science=science
        if 0 <= socail <= 100:
            self.__socail=socail
    def __calculation_average(self):
        return(self.__tamil+self.__english+self.__maths+self.__science+self.__socail)/5
    def __get_scores(self):
        average=self.__calculation_average()
        if average>=90:
            print ('execellent(A)')
        elif average >=80:
            print("very good (B)")
        elif average>=70:
            print("good(C)")
        elif average>=60:
            print('average(D)')
        elif average>=35:
            print('imporove(E)')
        else :
            print('fail')
    def print(self):
        print("STUDENT NAME=",self.name)
        self.__get_scores()

student1=ReportCard("kavi")
student1.set_scorces(tamil=99,english=91,science=94,socail=90,maths=79)
student1.print()
print('----------------------')
student2=ReportCard("bala")
student2.set_scorces(tamil=23,english=34,science=21,socail=15,maths=2)
student2.print()