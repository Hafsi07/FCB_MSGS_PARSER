import json
import os 



with open("message_1.json", 'r', encoding='ascii') as f:
    data=json.load(f)


recipiants=data.get('participants',None)

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

            if x.strip().endswith('to your message'): 
                print('reaction')
                continue
            if x.strip().endswith('sent an attachment.'): 
                print('attachment')
                continue
            if x.startswith('https://') or x.startswith('http://'):
                print('link')
                continue
            
            if x != '': messages.append(x)
    return messages



# @ + recipienets names  exclustion  from emssages
# links and special characters exclusion
def file_loader(wd=os.getcwd()):
    text=[]
    for filename in os.listdir(wd):
        fp = os.path.join(wd, filename)
        if os.path.isfile(fp) and fp.endswith('.json'):
            with open(fp,'r') as f :
                data=json.load(f)
            text=text+['------']+get_messages(data)
        else: continue
    return text
cc=file_loader()
print(cc)
print(len(cc))