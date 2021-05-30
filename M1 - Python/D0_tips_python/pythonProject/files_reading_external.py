employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


# employee_file = open("employees.txt", "r")
#
# print(employee_file.readlines()[1])
#
# employee_file.close()





# employee_file = open("employees.txt", "r")
#
# print(employee_file.readable())
#
# employee_file.close()






# "r" => read
# "w" => write
# "a" => append
# "r+" => read & write
