# json is short for js object 

# this is to data  change 
# this is use to web application 
# now json is one of the best moudles for web application
import json

person={"namme":"Ayman Sajid","age":20,"city":"Dhaka","Wife":"false","title":"Programmer,engneer"}
#print(person)
person_json = json.dumps(person, indent=4,sort_keys=True)   # when we use to indent  to print to any system 
print(person_json)

# json file handling

with open('person.json','w') as file:
    json.dump(person, file)