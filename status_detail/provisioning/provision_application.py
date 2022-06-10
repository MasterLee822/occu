from status_detail.models import Employee
from django.core.exceptions import ValidationError

employees = [
        {
            "id": "1",
            "name": "Tiger Nixon",
            "position": "System Architect",
            "salary": "$320,800",
            "start_date": "2011-04-25",
            "status": "warn",
            "extn": "5421"
        },
        {
            "id": "2",
            "name": "Garrett Winters",
            "position": "Accountant",
            "salary": "$170,750",
            "start_date": "2011-07-25",
            "status": "fail",
            "extn": "8422"
        },
        {
            "id": "3",
            "name": "Ashton Cox",
            "position": "Junior Technical Author",
            "salary": "$86,000",
            "start_date": "2009-01-12",
            "status": "pass",
            "extn": "1562"
        },
        {
            "id": "4",
            "name": "Cedric Kelly",
            "position": "Senior Javascript Developer",
            "salary": "$433,060",
            "start_date": "2012-03-29",
            "status": "pass",
            "extn": "6224"
        },
        {
            "id": "5",
            "name": "Airi Satou",
            "position": "Accountant",
            "salary": "$162,700",
            "start_date": "2008-11-28",
            "status": "warn",
            "extn": "5407"
        },
        {
            "id": "6",
            "name": "Brielle Williamson",
            "position": "Integration Specialist",
            "salary": "$372,000",
            "start_date": "2012-12-02",
            "status": "fail",
            "extn": "4804"
        },
        {
            "id": "7",
            "name": "Christopher Lee",
            "position": "Principal Engineer",
            "salary": "$175,000",
            "start_date": "2022-07-11",
            "status": "pass",
            "extn": "9916"
        },
        {
            "id": "8",
            "name": "Rhona Davidson",
            "position": "Integration Specialist",
            "salary": "$327,900",
            "start_date": "2010-10-14",
            "status": "pass",
            "extn": "6200"
        },
        {
            "id": "9",
            "name": "Colleen Hurst",
            "position": "Javascript Developer",
            "salary": "$205,500",
            "start_date": "2009-09-15",
            "status": "pass",
            "extn": "2360"
        },
        {
            "id": "10",
            "name": "Sonya Frost",
            "position": "Software Engineer",
            "salary": "$103,600",
            "start_date": "2008-12-13",
            "status": "pass",
            "extn": "1667"
        },
        {
            "id": "11",
            "name": "Jena Gaines",
            "position": "Office Manager",
            "salary": "$90,560",
            "start_date": "2008-12-19",
            "status": "pass",
            "extn": "3814"
        },
        {
            "id": "12",
            "name": "Quinn Flynn",
            "position": "Support Lead",
            "salary": "$342,000",
            "start_date": "2013-03-03",
            "status": "pass",
            "extn": "9497"
        },
        {
            "id": "13",
            "name": "Charde Marshall",
            "position": "Regional Director",
            "salary": "$470,600",
            "start_date": "2008-10-16",
            "status": "pass",
            "extn": "6741"
        },
        {
            "id": "14",
            "name": "Haley Kennedy",
            "position": "Senior Marketing Designer",
            "salary": "$313,500",
            "start_date": "2012-12-18",
            "status": "pass",
            "extn": "3597"
        },
        {
            "id": "15",
            "name": "Tatyana Fitzpatrick",
            "position": "Regional Director",
            "salary": "$385,750",
            "start_date": "2010-03-17",
            "status": "pass",
            "extn": "1965"
        },
        {
            "id": "16",
            "name": "Michael Silva",
            "position": "Marketing Designer",
            "salary": "$198,500",
            "start_date": "2012-11-27",
            "status": "pass",
            "extn": "1581"
        },
        {
            "id": "17",
            "name": "Paul Byrd",
            "position": "Chief Financial Officer (CFO)",
            "salary": "$725,000",
            "start_date": "2010-06-09",
            "status": "pass",
            "extn": "3059"
        },
        {
            "id": "18",
            "name": "Gloria Little",
            "position": "Systems Administrator",
            "salary": "$237,500",
            "start_date": "2009-04-10",
            "status": "fail",
            "extn": "1721"
        },
        {
            "id": "19",
            "name": "Bradley Greer",
            "position": "Software Engineer",
            "salary": "$132,000",
            "start_date": "2012-10-13",
            "status": "pass",
            "extn": "2558"
        },
        {
            "id": "20",
            "name": "Dai Rios",
            "position": "Personnel Lead",
            "salary": "$217,500",
            "start_date": "2012-09-26",
            "status": "pass",
            "extn": "2290"
        },
        {
            "id": "21",
            "name": "Jenette Caldwell",
            "position": "Development Lead",
            "salary": "$345,000",
            "start_date": "2011-09-03",
            "status": "pass",
            "extn": "1937"
        },
        {
            "id": "22",
            "name": "Yuri Berry",
            "position": "Chief Marketing Officer (CMO)",
            "salary": "$675,000",
            "start_date": "2009-06-25",
            "status": "pass",
            "extn": "6154"
        },
        {
            "id": "23",
            "name": "Caesar Vance",
            "position": "Pre-Sales Support",
            "salary": "$106,450",
            "start_date": "2011-12-12",
            "status": "pass",
            "extn": "8330"
        },
        {
            "id": "24",
            "name": "Doris Wilder",
            "position": "Sales Assistant",
            "salary": "$85,600",
            "start_date": "2010-09-20",
            "status": "pass",
            "extn": "3023"
        },
        {
            "id": "25",
            "name": "Angelica Ramos",
            "position": "Chief Executive Officer (CEO)",
            "salary": "$1,200,000",
            "start_date": "2009-10-09",
            "status": "pass",
            "extn": "5797"
        },
        {
            "id": "26",
            "name": "Gavin Joyce",
            "position": "Developer",
            "salary": "$92,575",
            "start_date": "2010-12-22",
            "status": "pass",
            "extn": "8822"
        },
        {
            "id": "27",
            "name": "Jennifer Chang",
            "position": "Regional Director",
            "salary": "$357,650",
            "start_date": "2010-11-14",
            "status": "pass",
            "extn": "9239"
        },
        {
            "id": "28",
            "name": "Brenden Wagner",
            "position": "Software Engineer",
            "salary": "$206,850",
            "start_date": "2011-06-07",
            "status": "pass",
            "extn": "1314"
        },
        {
            "id": "29",
            "name": "Fiona Green",
            "position": "Chief Operating Officer (COO)",
            "salary": "$850,000",
            "start_date": "2010-03-11",
            "status": "pass",
            "extn": "2947"
        },
        {
            "id": "30",
            "name": "Shou Itou",
            "position": "Regional Marketing",
            "salary": "$163,000",
            "start_date": "2011-08-14",
            "status": "pass",
            "extn": "8899"
        },
        {
            "id": "31",
            "name": "Michelle House",
            "position": "Integration Specialist",
            "salary": "$95,400",
            "start_date": "2011-06-02",
            "status": "fail",
            "extn": "2769"
        },
        {
            "id": "32",
            "name": "Suki Burks",
            "position": "Developer",
            "salary": "$114,500",
            "start_date": "2009-10-22",
            "status": "pass",
            "extn": "6832"
        },
        {
            "id": "33",
            "name": "Prescott Bartlett",
            "position": "Technical Author",
            "salary": "$145,000",
            "start_date": "2011-05-07",
            "status": "pass",
            "extn": "3606"
        },
        {
            "id": "34",
            "name": "Gavin Cortez",
            "position": "Team Leader",
            "salary": "$235,500",
            "start_date": "2008-10-26",
            "status": "pass",
            "extn": "2860"
        },
        {
            "id": "35",
            "name": "Martena Mccray",
            "position": "Post-Sales support",
            "salary": "$324,050",
            "start_date": "2011-03-09",
            "status": "pass",
            "extn": "8240"
        },
        {
            "id": "36",
            "name": "Unity Butler",
            "position": "Marketing Designer",
            "salary": "$85,675",
            "start_date": "2009-12-09",
            "status": "fail",
            "extn": "5384"
        },
        {
            "id": "37",
            "name": "Howard Hatfield",
            "position": "Office Manager",
            "salary": "$164,500",
            "start_date": "2008-12-16",
            "status": "pass",
            "extn": "7031"
        }
    ]


def add_employee_to_db(employee_record: dict) -> bool:
    try:
        employee = Employee(name=employee_record['name'],
                            status=employee_record['status'],
                            position=employee_record['position'],
                            salary=employee_record['salary'],
                            start_date=employee_record['start_date'],
                            extension=employee_record['extn'])
        employee.save()
    except ValidationError:
        return False
    return True
