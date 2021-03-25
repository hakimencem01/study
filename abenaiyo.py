print("Student Grade Checker");
mark = int(input("Marks : "));
grade = "";
if((mark>=80) and (mark<=100) ):
    grade = "A";
if((mark>=60) and (mark<=79) ):
    grade = "B";
    
if((mark>=40) and (mark<=59) ):
    grade = "C";
    
if((mark>=0) and (mark<=39) ):
    grade = "Failed";
    
if(mark>=101):
    grade = "You have input the invalid marks";

print(grade);