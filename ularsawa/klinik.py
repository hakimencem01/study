clinicname = "Klinik Awang";
print(clinicname+"\n");
temp = float(input("Your Temperature 'C : "));

if(temp>=(38.00)):
    print("Status : You known for sure to be infected by Covid-19 ");
else:
    print("\nStatus : You're fine, just a regular cold !");

print("\nThanks for coming to "+clinicname+" !");