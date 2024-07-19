class Students: 
   def __init__(self, name, math, science, english, sst): 
      self.name = name 
      self.math = math 
      self.science = science 
      self.english = english 
      self.sst = sst
   
   def ave(self): 
      self.average = (self.math + self.science + self.english + self.sst) / 4

   def division(self):
      m1=Students.grade(self.math)
      s1=Students.grade(self.science)
      e1=Students.grade(self.english)
      st1=Students.grade(self.sst)
      div_total=int(m1[-1])+int(s1[-1])+int(e1[-1])+int(st1[-1])

      if div_total <=12: 
         print("Aggregate:", div_total,"Divion: 1")
      elif div_total <=23:
         print("Aggregate:", div_total,"Divion: 2")
      elif div_total <=29:
         print("Aggregate:", div_total,"Divion: 3")
      else:
         print("Aggregate:", div_total,"Divion: 4")    
   

   def grade(mark):
      if 0 <= mark <=100:
         if mark >=85:
            return "D1" 
         elif mark >=80:
            return "D2"
         elif mark >=70:
            return "C3"
         elif mark >=65:
            return "C4"
         elif mark >=60:
            return "C5"
         elif mark >=55:
            return "C6"
         elif mark >=50:
            return "P7"
         elif mark >=45:
            return "P8"
         else:
            return "F9"
      else:
         return "The value is out of range."

   def show(self): 
      print()
      print("ST. BARNABAS PRIMARY SCHOOL") 
      print("PLE MOCK GRADING SYSTEM USING CLASSES")
      print("Student Name: ", self.name)
      
      # printing Aligned Header 
      print(f"{'Subject' : ^10}{'Marks' : <10}{'Grade' : <10}")
      print(f"{'Math' : ^10}{self.math : <10}{Students.grade(self.math): <10}")
      print(f"{'Science' : ^10}{self.science : <10}{Students.grade(self.science): <10}")
      print(f"{'English' : ^10}{self.english : <10}{Students.grade(self.english): <10}")
      print(f"{'SST' : ^10}{self.sst : <10}{Students.grade(self.sst): <10}")
      print()
      print(Students.division(self))
   
      self.ave()
      if self.average >= 50: 
         self.status = "You are promoted to the next class." 
         print("Average Grade: {}".format(round(self.average,0)))
         print("Remark: ",self.status)
      else: 
         self.status = "You are advised to repeat the class." 
         print("Average Grade: {}".format(round(self.average,0))) 
         print("Remark:",self.status)
         print()

#ENTRIES FOR THE DISPLAY SCREEN
print()
Name = str(input("Enter Name: ")) 
Math = float(input("Enter Math: ")) 
Science = float(input("Enter Science: ")) 
English = float(input("Enter English: ")) 
SST = float(input("Enter SST:"))
print()
stud = Students(Name, Math, Science, English, SST) 
stud.show()
print()
print()


print("PART TWO OF THE PROJECT:")
# lambda that accepts one argument
weekend_wish = lambda name : print('Happy weekend,', name)

# lambda call
print()
weekend_wish(Name)
print()
class_list = ["Maria", "Rosa"]
print(f'Current Class List is: {class_list}')
class_list.append(Name)
print(f'Updated Class List is: {class_list}')

mark_list = [40, 68 ]
print(f'Current Number List is: {mark_list}')
mark_list.insert(0,Math)
print(f'Updated Number List is: {mark_list}')


# printing values of variables in Aligned manner 
print()
print(f"{'Name' : <10}{'Marks' : <10}")

for i in range(0, 3): 
    print(f"{class_list[i] : <10}{mark_list[i] : <10}") 
   
   
   # # Appending to file
   # file = open("myfile.txt", 'a')
   # file.write("yawe")
   # file.close()
 


       
                





        