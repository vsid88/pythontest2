from collections import defaultdict
employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]


values = [i['job'] for i in employees]
values2 = [i['name'] for i in employees]
values3 = [i["address"]["city"] for i in employees]
print(values)
print(values2)
print(values3)
print(employees[1]['address']['city'])