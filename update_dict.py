employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}
employee['job'] = 'software engineer'
employee.__delitem__('age')
for key, value in employee.items():
        print(key,':',value)

#print(employee)