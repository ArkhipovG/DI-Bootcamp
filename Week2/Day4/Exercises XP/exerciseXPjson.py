import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data_json = json.loads(sampleJson)


salary = data_json['company']['employee']['payable']['salary']
print("Salary:", salary)


data_json['company']['employee']['birth_date'] = "1990-01-01"


with open('data.json', 'w') as file:
    json.dump(data_json, file, indent=4)


