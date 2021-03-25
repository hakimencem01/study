total = 0;
expense = [];
expense_count = int(input("Enter # of expense : "));
for i in range(expense_count):
    expense.append(float(input("Enter an expense : RM ")));

total = sum(expense);
formula = "";
for each in expense:
    formula +=" + RM "+str(each);
length = len(formula);
print("\nYou spend ("+formula[2:length]+") = RM "+str(total));