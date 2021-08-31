# def display(dicCustomer):
#     print("Total Customers:", len(dicCustomer))
#     total_customer = 0
#     total_amount = 0
#     for value in dicCustomer:
#         if dicCustomer[value] > 2000:
#             print(value, ":", dicCustomer[value])
#             total_customer += 1
#             total_amount += dicCustomer[value]
#     print("Total Customer with amount greater than 2000:", total_customer)
#     print("Total Amount with amount greater than 2000:", total_amount)
#
#
# mycustomers = {
#     "Alya": 1000,
#     "Noora": 2500,
#     "Salwa": 2000,
#     "Amna": 3500,
#     "Aysha": 1500,
#     "Fatima": 3000
# }
# display(mycustomers)

tp1 = ("H0023455", "Nabil", "CSF", 3.4)
tp2 = ("H0023456", "Ahmad", "CSF", 2.7)
tp3 = ("H0023457", "Hassan", "CSF", 3.1)
tp4 = ("H0023458", "Omer", "CSF", 2.6)
tp5 = ("H0023459", "Ali", "CSF", 3.8)
tp6 = ("H0023460", "Osman", "CSF", 2.4)
mystudent = []
gpa = []
mystudent.append(tp1)
mystudent.append(tp2)
mystudent.append(tp3)
mystudent.append(tp4)
mystudent.append(tp5)
mystudent.append(tp6)
for x in mystudent:
    if x[3] < 3.5:
        gpa.append(x[3])
print("Average GPA of student less than 3.5:", sum(gpa) / len(gpa))
