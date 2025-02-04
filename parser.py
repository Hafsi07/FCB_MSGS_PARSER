import json
import os


def create_id(jizon):
    particips=jizon.get('participants',None)
    particips=[i['name'].strip() for i in particips]
    strng=''.join(particips)
    id=strng[:2]+str(hex(len(strng)))+strng[-3:]+strng[:3]+str(hex(2*len(strng)))+strng[-2:]
    return id

def get_messages(data,participants_to_exclude=[],participants_to_include=[]):
        
    recipiants=data.get('participants',None)
    recipiants=[i['name'].strip() for i in recipiants]
    if participants_to_include==[]: participants_to_include=recipiants
    participants_to_include=[i for i in participants_to_include if i not in participants_to_exclude]

    conversation_ID=create_id(data)

    messages=[]    
    for i in data['messages']:
        sender=i.get('sender_name',None)
        if sender in participants_to_exclude or sender not in participants_to_include:
            continue
            
        x=i.get('content',None)
        y=i.get('timestamp_ms',None)
        z=i.get('sender_name',None)
        w=i.get('reactions',None)
        if w:
            w=[str(i['reaction']) for i in w]
            print(w)
        else: w=[None]

        if x:
            if x.find('@')>=0:
                x=x.replace('@everyone','').strip().replace('  ',' ')
                x=x.replace('@Meta Ai','').strip().replace('  ',' ')
                for rec in recipiants:
                    x=x.replace(f"@{rec}",'').strip().replace('  ',' ')

            if x.strip().endswith('to your message'): 
                print('reaction')
                continue
            if x.strip().endswith('sent an attachment.'): 
                print('attachment')
                continue
            if x.strip().endswith('from the group.'): 
                print('kick')
                continue
            if x.strip().endswith('left the group.'): 
                print('leave')
                continue
            if x.startswith('https://') or x.startswith('http://'):
                print('link')
                continue
            
            if x != '': messages.append([conversation_ID,x,y,z,w])
    return messages


def file_loader(wd=os.getcwd(),participants_to_remove=[],participants_to_include=[]):
    text=[]
    if wd.endswith('.json'):
        with open(wd,'r') as f :
            data=json.load(f)
        return get_messages(data,participants_to_remove,participants_to_include)
    for filename in os.listdir(wd):
        fp = os.path.join(wd, filename)
        if os.path.isfile(fp) and fp.endswith('.json'):
            with open(fp,'r') as f :
                data=json.load(f)
            text=text+['------']+get_messages(data,participants_to_remove,participants_to_include)
        else: continue
    return text
cc=file_loader(participants_to_remove=['x1','x2'],participants_to_include=['x3','x5','x8','x2'])
print(cc[-3:])
print(len(cc))