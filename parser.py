import json
import os 

wd=''

with open("message_1.json", 'r') as f:
    data=json.load(f)


recipiants=data.get('participants',None)

# print(recipiants[0]['name'])
# exit()
def get_messages(data):
    
    messages=[]

    for i in data['messages']:
        x=i.get('content',None)
        if x:
            if x.find('@')>=0:
                x=x.replace('@everyone','').strip().replace('  ',' ')
                x=x.replace('@Meta Ai','').strip().replace('  ',' ')
                for rec in recipiants:
                    x=x.replace(f"@{rec['name']}",'').strip().replace('  ',' ')

            if x.endswith('to your message '): 
                print('valid')
                continue

            if x != '': messages.append(x)
    return messages

res= get_messages(data)
print(res)
print(len(res))
# print(data['messages'][1]['content'])

# @ + recipienets names  exclustion  from emssages
# links and special characters exclusion


