"""
Nama  : Mohammad Abdul Hakim
Kelas : 4B
No Matrik : 20DDT19F1050
"""
for x in range(11):
    print("The square of "+str(x)+" is : "+str(x*x));

# 2,4,6,8,10

sum = 0;
start = 0;
stop = 10;
stopindex = 11;
for x in range(start,stopindex,2):
    sum+=x;

print("\n\nThe total of even numbers from "+str(start)+" to "+str(stop)+" is "+str(sum));




username = input("Please enter your username : ");
password = input("Please enter your password : ");
if((username.isalpha())!=True):
    print("Your username is not alphabetical");
if((password.isnumeric())!=True):
    print("Your password is not numerical");
else:
    if(len(password)<=4):
        print("Your password need to contain at least 5 character");




print("Monthly payment calculator");
downpayment = int(input("Please enter your downpayment : RM "));
loanyear = int(input("Please enter your loan period in years : "));

carprice = 103300;
loan_period_in_month = loanyear*12;
min_downpayment = 0.1; # 10%
car_ten_percent = carprice*min_downpayment;
if(downpayment>=car_ten_percent):

    loanamount = ((carprice - downpayment));
    interestrate =2.7;
    totalinterest = (interestrate/100) * loanamount*loanyear;
    monthly_installment = round(((loanamount+totalinterest)/loan_period_in_month),2);

    print("Monthly installment is RM "+str(monthly_installment));
else:
    print("You are not eligible for bank loan");