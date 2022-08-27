# **OCCU Employment DEMO**

## ********Status and Employee Management********

### **Introduction**
This system was built to provide a demonstration of work skills for Chris Lee. 

### **Installation**
1. [Install Python](https://www.python.org/)
2. [Install Django](https://www.djangoproject.com/download/)
3. Clone repository

### **System Provisioning**

1. Go to main project directory in terminal. 
2. Run `python manage.py runserver`. This will create the blank database tables.
3. Run `python manage.py createsuperuser`. Follow prompts to create user credentials to access the Django Admin.
4. Open browser and navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) 
5. Run `manage.py provision`. This will pre-populate the Employee database with records.

### **How to Use the system**
1. CRUD functionality can be done using the django admin at http://127.0.0.1:8000/admin.
2. http://127.0.0.1:8000/ can be the jumping off point for bullet point 1 of the assignment.
3. http://127.0.0.1:8000/details/ covers bullet point 2 of the assignment. CRUD functionality is available here too.


### Conclusion
Thanks for the opportunity.



 MVC exercise
Congratulations, you have been selected to move forward in the software developer interview process. The next step is to complete a simple website that outlines the information requested below. You pick the language(s) for your solution, but the solution must run on windows. You will return the exercise by posting your solution to GitHub – we will download, run, and evaluate your solution. Provide any setup instructions needed.
Note that the work submitted will only be used for the evaluation of your ability to meet the expectations of the role and as part of the interview process. All information provided is hypothetical. In general, we are unable to provide any details outside of what is provided here, and the use of outside resources is encouraged.
Requirement statements
• There are to be two sources of data, and each should be accessible:
o Asetof37statusvalues(fail,warn,pass)tobedisplayedinasinglepagealong
with a distinct id or tag. This webpage is meant to show the status values “at a
glance”.
o Asecondpage,noparticularrelationshiptothefirst,thatallowsforsearchplus
CRUD (create, read, update, delete) on a simple data set that has four text input fields and an update timestamp. One of the fields should be a name, which should be kept unique. Provide the following features:
 Read/index – show entire list before search – or what fits on a page. This should be the default view.
 Read/search – search on the contents of one of the fields, then show the list of data sets that match.
 Update/edit – provide a way to select an item for update, then provide a way to edit the fields for that item and save the changes.
 Delete – provide a way to create a new data set.
 Copy/edit – provide a way to copy an existing data set and then edit/save
the data set.
 Optional bonus feature: Provide a way to select two items from the list
and then compare the field contents with a visual clue when the same items from different sets have different values - You can ignore the name field and update timestamp in this case since they will generally be different anyway.
o Constraints:
 Solution must run on windows.
 Post your solution to GitHub – we will download, run, and evaluate your
solution.
 Provide any installation / setup instructions needed.
  
  The data doesn’t have to be in a database. It can be in a file, or memory, or database, etc. for this exercise.
 You can spend a little or a lot of time – the amount is up to you but should be completed within the specified timeframe.
Email a link to your completed exercise to HR@MyOCCU.org no later than Tuesday 6/14/2022 by 5 p.m.
