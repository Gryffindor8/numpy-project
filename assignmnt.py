"""
Python Programming: Coursework
------------------------------

The instructions are listed in the attached Word document. Please do not change the
structure of this file. Add your solutions within the functions where it says "Your
code follows below: replace `None` with your code". Do not remove any of the code.

"""

# Add your import statements here...

import math
import os
from collections import Counter
from datetime import datetime

import pandas as pd

# Change working directory: add the correct path
# os.chdir('C:/python_projects/PythonProgramming/Coursework')
print('Current working dir:', os.getcwd())

# Replace your student ID
student_id = 'YOURSTUDENTID'


def q0(num_1, num_2):
    # Your code follows below: replace `None` with your code
    sum_of_the_two = num_1 + num_2

    # Do not change the code below
    return sum_of_the_two


"""
Task 1: Python fundamentals
"""


def q1():
    # Your code follows below: replace `None` with your code
    """
    we declare
    list with []
    tuple with ()
    and dic with {key: value}
    """
    example_list = ["apple", "banana", "cherry"]
    # tuple
    example_tuple = ("apple", "banana", "cherry")
    # dictionary
    example_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    # Do not change the code below
    return example_list, example_tuple, example_dict


def q2(lower_limit=11, upper_limit=23):
    # Your code follows below: replace `None` with your code
    """
    Here we used the list comprehension using for loop.
    In this we used math.sqrt function as expression to find the squrate root
    of x between specific ranges and return it.
    """
    square_roots = [math.sqrt(x) for x in range(lower_limit, upper_limit)]

    # Do not change the code below
    return square_roots


def q3(num_rows=15, num_cols=100):
    # Your code follows below: add your code and assign the created DataFrame to `df`
    """
    In this function first we declared two lists than looping through it with the specific
    range of numbers given in parameters and append the values in these lists.At the end we
    created a dataframe using Dataframe function of pandas library and return it.
    """
    rows = []
    colums = []
    for k in range(num_rows):
        rows.append("Portfolio" + str(k))
    for k in range(num_cols):
        colums.append("Company" + str(k))
    df = pd.DataFrame(0, rows, colums)
    # Do not change the code below
    return df


def q4(companies=('Apple', 'Amazon', 'Alphabet', 'Microsoft', 'Visa')):
    # Your code follows below; assign the new list to `companies_new`
    # List comprehension with if-else statement using for loop
    companies_new = [x.upper() if 'p' in x else x.lower() for x in companies]

    # Do not change the code below
    return companies_new


def q5(companies=('Microsoft', 'Berkshire Hathaway', 'Apple')):
    # Your code follows below
    """
    Looping through the companies set and created a text file
    with the name of each company set item
    """
    for k in companies:
        open("./data-task1/" + k + ".txt", "x")
    # Do not change the code below
    return True


def q6(input_dir='./data-task1/q6/'):
    # Your code follows below: add your code (find all .txt files in `input_dir` and
    # assign the corresponding list to `extracted_contents`
    """
    This function read all text files in the subfolders of ./data-task1/q6/
    and add the file content to a list.
    """
    fles = []
    for path, subdirs, files in os.walk(input_dir):
        for name in files:
            fles.append(os.path.join(path, name))

    extracted_contents = []
    # get the only txt files
    for k in fles:
        if k.endswith(".txt"):
            with open(k, "r") as rd:
                extracted_contents.append(rd.readline())

    # Do not change the code below
    return extracted_contents


"""
Task 2: pandas
"""


def q10():
    # Pandas to read the csv file
    """
    This function load two CSV files using pandas function read_csv and
    and assign them to the corresponding variables and return them
    """
    comp_info = pd.read_csv("./data-task2/company-info.csv")
    comp_data = pd.read_csv("./data-task2/compensation-data.csv")

    # Do not change the code below
    return comp_info, comp_data


def q11():
    # Run this code to load the data set (necessary for next steps)
    """
    Created new list called female.Looping through gender list,
    By using if else statement, check if it equals to Female append 1 to female
    list otherwise append 1 to it.
    """
    _, df_data = q10()
    gender = list(df_data["gender"])
    female = []
    """get the data if teh coulm contains the Female CEO"""
    for k in gender:
        if k == "FEMALE":
            female.append(1)
        else:
            # if not female append 0
            female.append(0)

    df_data['female'] = female
    # convert to csv
    df_data.to_csv('compensation-data.csv', index=False)

    return df_data


def q12():
    # Run this code to load the data set (necessary for next steps)
    """ get the data for of both csvs and then extract the related info """
    df_info, _ = q10()
    df_data = q11()
    """ getting the data from csvs and convert the df into list"""

    coname = list(df_info["coname"])
    dfinfo_gvkey = list(df_info["gvkey"])
    gvkey = list(df_data["gvkey"])
    gender = list(df_data["gender"])
    year = list(df_data["year"])
    exec_counts = []
    for i in range(len(year)):
        """ split the data on the basis of year and female"""
        if str(year[i]) == "2017" and gender[i] == "FEMALE":
            k = gvkey[i]
            exec_counts.append(coname[dfinfo_gvkey.index(k)])

    # getting all words
    """ get the company name with most Female executives"""
    word_counts = Counter(exec_counts)
    # Step 5: What is the name of the company with the highest percentage of female executives?
    company_name = word_counts.most_common(1)
    company_name = (company_name[0][0])
    # Do not change the code below
    return company_name


def q13():
    # Run this code to load the data set (necessary for next steps)
    """ in this section 1st we will get the cs data from the q12 function
        then we will get age,year and ceo colum from the dataset. after that implementing neceesary algo to
        get the average we will return the averae
    """
    _, df_data = q10()
    age = list(df_data["age"])
    year = list(df_data["year"])
    ceo = list(df_data["ceoann"])
    avge = []
    # filter the data according to requirements
    for i in range(len(age)):
        if year[i] == 2016 and ceo[i] == "CEO":
            avge.append(age[i])
    average_age_per_company = (sum(avge) / len(avge))
    # Do not change the code below
    return average_age_per_company


def q14():
    # Run this code to load the data set (necessary for next steps)
    df_info, df_data = q10()

    # Your code follows below: add your code and assign the new DataFrame to `ceo_tenure`. As
    # before, we work in smaller steps.
    age = list(df_data["age"])
    # Step 1: We need the company name.
    coname = list(df_info["coname"])
    dfinfo_gvkey = list(df_info["gvkey"])
    year = list(df_data["year"])
    ceo = list(df_data["ceoann"])
    gvkey = list(df_data["gvkey"])
    gender = list(df_data["gender"])
    # Step 2: Format the date columns `becameceo` and `leftofc` as a date
    becomeceo = list(df_data["becameceo"])
    leftceo = list(df_data["leftofc"])
    salary = list(df_data["salary"])
    exec_full = list(df_data["exec_fullname"])
    # create list to store the data for new dataframe
    age1, ceo_tenure, year1, ceo1, gvkey1, gender1, becomeceo1, leftceo1, salary1, exec_full1, coname1 = [], [], [], \
                                                                                                         [], \
                                                                                                         [], [], [], \
                                                                                                         [], \
                                                                                                         [], [], []

    for i in range(len(age)):
        if ceo[i] == "CEO":
            key = gvkey[1]
            coname1.append(coname[dfinfo_gvkey.index(key)])
            age1.append(age[i]), ceo1.append(ceo[i]), year1.append(year[i]), gvkey1.append(gvkey), gender1.append(
                gender)
            salary1.append(salary[i]), exec_full1.append(exec_full[i])
            if str(becomeceo[i]) == "nan" or str(becomeceo[i]) == "":
                becomeceo1.append("NaN")
                leftceo1.append(leftceo[i])
                ceo_tenure.append("NaN")
            # Step 3: If the CEO was appointed in the past but there is no end date, set the
            # end date to '2020-12-31' (as a proxy for "still in office")
            elif str(leftceo[i]) == "nan" or str(leftceo[i]) == "":
                leftceo1.append(leftceo[i])
                becomeceo1.append(becomeceo[i])
                # calculate the tensure date by differniating between joiing and left date
                date_format = "%Y/%m/%d"
                a = datetime.strptime(str(becomeceo[i]), date_format)
                b = datetime.strptime("2020/12/31", date_format)
                delta = b - a
                y = ("%.2f" % (delta.days / 365))
                ceo_tenure.append(y)
                ceo_tenure.append(y)
            else:
                date_format = "%Y/%m/%d"
                a = datetime.strptime(str(becomeceo[i]), date_format)
                b = datetime.strptime(str(leftceo[i]), date_format)
                delta = b - a
                y = ("%.2f" % (delta.days / 365))
                # Step 4: Create a new column with the tenure, i.e., difference of end and start date

                ceo_tenure.append(y)
                becomeceo1.append(becomeceo[i])
                leftceo1.append(leftceo[i])
    # creating the data for the new dataframe

    data = [age1, ceo_tenure, year1, ceo1, gvkey1, gender1, becomeceo1, leftceo1, salary1, exec_full1, coname1]
    # insert data into dataframe to convert into pickle file
    filtered_ceo_tenure = pd.DataFrame(data,
                                       index=["age1", "duration_tenure", "year1", "ceo1", "gvkey1", "gender1",
                                              "becomeceo1", "leftceo1",
                                              "salary1", "exec_full1", "company_name"])
    filtered_ceo_tenure = filtered_ceo_tenure.T
    # Step 5: Export the DataFrame `filtered_ceo_tenure` as a Pickle file
    filtered_ceo_tenure.to_pickle("./data-task2/ceo_data.pkl")

    # Do not change the code below
    return filtered_ceo_tenure


"""
Task 3: Matplotlib
"""


def q21():
    """ using pandas to read pickle file """
    # Your code follows below: replace `None` with your code
    df = pd.read_pickle("./data-task3/daily-returns.pkl")
    # Do not change the code below
    return df


def q22():
    """"
    read the data from the return csv file. create two list of for the both companies
    calcualte the monthly commulative for both companies
    store the new data into data frame
    """
    # Run this code to load the data set
    returns_data = q21()
    microsoft = list(returns_data["Microsoft"])
    bp = list(returns_data["BP"])
    count, id1 = 0, 0
    microsoft_cumulative = 1
    bp_cumulative = 1
    micro = []
    bp1, m = [], []
    for i in range(len(microsoft)):
        # calcualte teh monthly camulative for both companies
        microsoft_cumulative = ((1 + microsoft[i]) * microsoft_cumulative) - 1
        bp_cumulative = ((1 + bp[i]) * bp_cumulative) - 1
        if count == 28:
            micro.append(microsoft_cumulative)
            bp1.append(bp_cumulative)
            microsoft_cumulative = 1
            count = 7
            m.append(id1)
            id1 += 1
            bp_cumulative = 1
        count += 1
    # create a new data frame for both company
    data = [m, micro, bp1]
    # create the datarame
    monthly_data = pd.DataFrame(data, index=["month", "microsoft", "BP"])
    monthly_data = monthly_data.T
    # Do not change the code below
    return monthly_data


def q23():
    """
    This function use the data of above function named q22() and plot it using matplotlib
    """
    global student_id

    # Run this code to load the data set
    monthly_data = q22()

    # Your code follows below: add your code and assign the plot to a variable `plot`
    # using the monthly data percentage to show the graph
    plot = monthly_data.cumsum()

    plot.plot(kind='line', x='BP', y='month')
    plot.plot(kind='line', x='microsoft', y='month', color='red')

    plot.show()

    # Run this to show your plot
    plot.figure.show()

    # Do not change the code below
    plot.figure.savefig(str(student_id) + '.png')
    return plot
