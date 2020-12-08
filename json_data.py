import json


#people_string='''
#{
#    "people":[
#        {
#            "name":"Likhitha",
#            "phone":"999999999",
#            "emails":["likithapichika@gmail.com","likhithasrinivas90@gmail.com"],
#            "has_license":true
#        },
#        {
#            "name":"sravani",
#            "phone":"88888888",
#            "emails":null,
#            "has_license":false
#        }
#    ]
#}
#'''
#data = json.loads(people_string)
#print(data)
#print(type(data['people']))
#for person in data['people']:
    #print(person)
    #print(person['name'])
#    del person['phone']
#new_str=json.dumps(data,indent=4,sort_keys=True)
#print(new_str)    

with open('states.json') as f:
    data=json.load(f)
for state in data['states']:
    #print(state['name'],state['abbreviation']) 
    del state['area_codes']
with open('new_states.json','w') as f:
    json.dump(data,f,indent=2,sort_keys=True)        