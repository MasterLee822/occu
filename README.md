# **Local Traffic**

## ********Digitally Assisted Communications System********

### **Introduction**
This system was built to provide a digital assistant into the communications experience  
between customers and enterprises. This platform allows enterprises to build infinite types of experience
for their customers and staff to communications. 

### **Installation**
1. [Install Docker](https://www.docker.com/get-started/)
2. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3. Clone repository

### **System Provisioning**
1. `manage.py migrate` This will create the blank database tables.
2. `createsuperuser`. Follow prompts to create user credentials.
3. Open browser and navigate to [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin) 
4. `manage.py provision` This will pre-populate the database with records.


### **Digital Assistant Provisioning**
1. Log into Django Admin
2. Navigate to Store(s). Click "ADD STORE +" button.  Add Store attributes.
3. Navigate to Store(s) Departments. Select the department associated with the newly created store.
   1. Add Phone number that will receive the call
   2. Add Twilio phone number (From Twilio)
4. Run `docker-compose run web python manage.py template_type STORE_ID_NUMBER`. 
   Replace STORE_ID_NUMBER with the store ID added in step 2.  This will take a moment to 
   build. Current `template_type` available for use are:
   1. build_financial_services
   2. build_franchisee
   3. build_retail
   4. build_social
5. Log into Twilio and build assistants:
      1. ID_staff_assistant
      2. ID_customer_faq_assistant
      3. ID_customer_assistant  
      4. Add Twilio Phone number to StoreDepartment
6. Navigate to DepartmentStaff and click on "Add Department Staff +"
   1. Select Store Department
   2. Add Staff Member Name
   3. Add full phone number with country code (+18085557777)

### Conclusion
Depending on the chosen `template_type` above, the application will behave in different ways.  
Most applications will send a text message to the newly created staff member.  


# LocalTraffic
