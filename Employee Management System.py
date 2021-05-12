employeeList = []
answer = 0
empSelect = True

def print_employee(x):
    print('------------------------  ' + employeeList[x][0] + '  -----------------------------')
    print('Employee SSN: ' + employeeList[x][1])
    print('Phone: ' + employeeList[x][2])
    print('E-Mail: ' + employeeList[x][3])
    print('Salary: ' + employeeList[x][4])
    print('-----------------------------------------------------------------------------')

while True:
    print('               ---------------------------- Employee Management System ----------------------------')
    print('                                    There are', len(employeeList), 'employees in the system                                ')
    print('               ------------------------------------------------------------------------------------')
    print('')
    print('1. Add new employee')
    print('2. View all employees')
    print('3. Search employee by SSN')
    print('4. Edit employee information')
    print('5. Export employees\' information into a text file')
    print('6. Import employees\' information from a text file')
    print('')
    print('               ------------------------------------------------------------------------------------')


    reqAction = input("Which option would you like to select? ")

    if reqAction == '1':
        addAnother = True
        while addAnother == True:
            employeeName = input("Please enter employee's name: ")
            employeeSSN = input("Please enter employee's Social Security Number: ")
            employeePhone = input("Please enter employee's Phone Number: ")
            employeeEmail = input("Please enter employee's E-Mail address: ")
            employeeSalary = "$" + input("Please enter employee's Salary: ")

            employeeInfo = (employeeName + ", " + employeeSSN + ", " + employeePhone + ", " + employeeEmail + ", " + employeeSalary)
            #employeeInfo.split(", ") would split this string but I used a list prior to seeing instruction to split strings
            employeeList.append([employeeName, employeeSSN, employeePhone, employeeEmail, employeeSalary])

            printAns = ''
            while printAns != "yes" and printAns != "no":
                printAns = input("Would you like to print new employee's information? ").lower()
                if printAns == "yes":
                    print_employee(-1)
                elif printAns == "no":
                    continue
                else:
                    print("Please enter Yes or No.")
            printAns = ''
            while printAns != "yes" and printAns != "no":
                printAns = input('Would you like to add another employee? ')
                if printAns == 'yes':
                    addAnother = True
                elif printAns == 'no':
                    addAnother = False
                else:
                    print('Please enter yes or no...')

    elif reqAction == '2':
        if len(employeeList) == 0:
            print("There are no employees in the database. Please add an employee before using this feature.")
        elif len(employeeList) > 0:
            for x in range(len(employeeList)):
                print_employee(x)  
            print("There are currently", len(employeeList), "employee in the database")

    elif reqAction == '3':
        empFound = False
        while empFound == False:
            empSearchSSN = input('Please enter employee\'s SSN: ')
            for x in range(len(employeeList)):
                if empSearchSSN == employeeList[x][1]:
                    print_employee(x)
                    empFound = True
            if empFound == False:
                print('The entered number ' + empSearchSSN + ' was not found in the employee database. Please try again')
            else:
                print('Please enter number of employee, view all or search...')
                checkAgain = True
            while checkAgain == True:
                answer = input("Would you like to view another employee? ").lower()

                if answer == "yes":
                    checkAgain = False
                    empFound = False
                elif answer == "no":
                    checkAgain = False
                else:
                    print("Please advise yes or no to continue")

    elif reqAction == '4':
        employee = input('Please enter the ssn of the employee you would like to edit: ')
        for x in range(len(employeeList)):
            if employee == employeeList[x][1]:            
                print('1. Name')
                print('2. SSN')
                print('3. Phone')
                print('4. Email')
                print('5. Salary')
                print('6. Remove Employee')

                finished = False
                while finished == False:
                    catSel = input('Please choose which category you would like to edit by selection above: ').lower()

                    if catSel == '1' or catSel == 'name':
                        name = input('Please enter full Name: ')
                        employeeList[x][0] = name
                        finished = True
                        print('Employee\'s name has successfully been changed.')
                        print_employee(x)
                    elif catSel == '2' or catSel == 'ssn':
                        ssn = input('Please enter Social Security Number: ')
                        employeeList[x][1] = ssn
                        finished = True
                        print('Employee\'s Social Security Number has successfully been changed.')
                        print_employee(x)
                    elif catSel == '3' or catSel == 'phone':
                        phone = input('Please enter phone number: ')
                        employeeList[x][2] = phone
                        finished = True
                        print('Employee\'s phone number has successfully been changed.')
                        print_employee(x)
                    elif catSel == '4' or catSel == 'email':
                        email = input('Please enter phone number: ')
                        employeeList[x][3] = email
                        finished = True
                        print('Employee\'s E-mail has successfully been changed.')
                        print_employee(x)
                    elif catSel == '5' or catSel == 'salary':
                        salary = input('Please enter annual salary: ')
                        employeeList[x][4] = '$' + salary
                        finished = True
                        print('Employee\'s salary has successfully been changed.')
                        print_employee(x)
                    elif catSel == '6' or catSel == 'remove' or catSel == 'remove employee':
                        print(employeeList[x][0], 'has been removed from the employee database')
                        employeeList.pop(x)
                        finished = True
                    else:
                        print('Invalid entry. Please enter one of the selections above.')
   
    elif reqAction == '5':
        exportedList = ''
        for list in employeeList:
            employees = list[0] + '/' + list[1] + '/' + list[2] + '/' + list[3] + '/' + list[4] + '\n'
            exportedList += employees
        print(exportedList)
        f = open('employees.txt', 'w')
        f.write(exportedList)
        f.close()
        print('The employee database has successfully been saved')

    elif reqAction == '6':
            f = open('employees.txt', 'r')
            importedList = f.readlines()
            f.close()
            line = 0
            for lines in importedList:
                employee = importedList[line].split('/')
                employee[4] = employee[4].rstrip('\n')
                employeeList.append(employee)
                line += 1
            print(len(employeeList), 'employees are now available in the employee database')

    elif reqAction == "exit":
        print("You are now exiting the program.")
        break
    else:
        print("Please select an option from above...")
            

