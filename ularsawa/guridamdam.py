print("Body Mass Index calculator (BMI)");
weight = float(input("Weight (kg) : " ));
height = float(input("Height (m) :  " ));
bmi = round(weight / (height*height) );
status  = "";
if((bmi<18.5)):
    status = "Underweight";
if((bmi>=18.5) and (bmi<=24.9)):
    status = "Normal Weight";

if((bmi>=25.0) and (bmi<=29.9)):
    status = "Overweight";
if((bmi>=30.5) and (bmi<=34.9)):
    status = "Obesity Class I";

if((bmi>=35.5) and (bmi<=39.9)):
    status = "Obesity Class II";

if(bmi>40):
    status = "Obesity Class III";
print("Your BMI : "+str(bmi)+"\nYour status are "+status);