from datetime import datetime

import pandas as pd

csv_input = pd.read_csv("compensation-data.csv")
df_info = pd.read_csv("./data-task2/company-info.csv")
age = list(csv_input["age"])
coname = list(df_info["coname"])
dfinfo_gvkey = list(df_info["gvkey"])
print(coname[dfinfo_gvkey.index(5125)])
year = list(csv_input["year"])
ceo = list(csv_input["ceoann"])
gvkey = list(csv_input["gvkey"])
gender = list(csv_input["gender"])
becomeceo = list(csv_input["becameceo"])
leftceo = list(csv_input["leftofc"])
salary = list(csv_input["salary"])
exec_full = list(csv_input["exec_fullname"])
age1, duration_tenure, year1, ceo1, gvkey1, gender1, becomeceo1, leftceo1, salary1, exec_full1, coname1 = [], [], [], [], [], [], [], [], [], [], []

avge = []
for i in range(len(age)):
    if ceo[i] == "CEO":
        key = gvkey[1]
        coname1.append(coname[dfinfo_gvkey.index(key)]);age1.append(age[i]), ceo1.append(ceo[i])
        year1.append(year[i])
        gvkey1.append(gvkey)
        gender1.append(gender)
        salary1.append(salary[i])
        exec_full1.append(exec_full[i])
        if str(becomeceo[i]) == "nan" or str(becomeceo[i]) == "":
            becomeceo1.append("NaN")
            leftceo1.append(leftceo[i])
            duration_tenure.append("NaN")
        elif str(leftceo[i]) == "nan" or str(leftceo[i]) == "":
            leftceo1.append(leftceo[i])
            becomeceo1.append(becomeceo[i])
            duration_tenure.append("Oppointed")
        else:
            date_format = "%Y/%m/%d"
            a = datetime.strptime(str(becomeceo[i]), date_format)
            b = datetime.strptime(str(leftceo[i]), date_format)
            delta = b - a
            y = ("%.2f" % (delta.days / 365))
            duration_tenure.append(y)
            becomeceo1.append(becomeceo[i])
            leftceo1.append(leftceo[i])

data = [age1, duration_tenure, year1, ceo1, gvkey1, gender1, becomeceo1, leftceo1, salary1, exec_full1, coname1]
df1 = pd.DataFrame(data,
                   index=["age1", "duration_tenure", "year1", "ceo1", "gvkey1", "gender1", "becomeceo1", "leftceo1",
                          "salary1", "exec_full1", "company_name"])
df1 = df1.T
df1.to_pickle("./data-task2/ceo_data.pkl")

# date_format = "%m/%d/%Y"
# a = datetime.strptime('8/1/2004', date_format)
# b = datetime.strptime('9/26/2008', date_format)
# delta = b - a
# y = ("%.2f" % (delta.days / 365))

# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = (pd.read_pickle("./data-task3/daily-returns.pkl"))
# df_no_indices = df.to_string(index=False)
# microsoft = list(df["Microsoft"])
# bp = list(df["BP"])
# count = 0
# microsoft_cumulative = 1
# bp_cumulative = 1
# micro = []
# bp1 = []
# dt = []
# ind = 1
# for i in range(len(microsoft)):
#     microsoft_cumulative = ((1 + microsoft[i]) * microsoft_cumulative) + 1 / microsoft_cumulative
#     bp_cumulative = ((1 + bp[i]) * bp_cumulative) + 1 / bp_cumulative
#
#     if count == 28:
#         micro.append(microsoft_cumulative)
#         bp1.append(bp_cumulative)
#         microsoft_cumulative = 1
#         count = 7
#         dt.append(ind)
#         ind += 1
#         bp_cumulative = 1
#     count += 1
# data = [dt, micro, bp1]
# df1 = pd.DataFrame(data, index=["month", "microsoft", "BP"])
# df1 = df1.T.cumsum()
#
# # df3 = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"]).cumsum()
#
# ax = plt.gca()
#
# df1.plot(kind='line', x='BP', y='month')
# df1.plot(kind='line', x='microsoft', y='month', color='red')
#
# plt.show()
