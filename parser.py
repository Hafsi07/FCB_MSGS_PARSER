import json
import os


def get_messages(data,participants_to_exclude=[]):
        
    recipiants=data.get('participants',None)
    messages=[]

    for i in data['messages']:
        sender=i.get('sender_name',None)
        if sender in participants_to_exclude:
            continue
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
            if x.strip().endswith('from the group.'): 
                print('kick')
                continue
            if x.strip().endswith('left the group.'): 
                print('leave')
                continue
            if x.startswith('https://') or x.startswith('http://'):
                print('link')
                continue
            
            if x != '': messages.append(x)
    return messages


def file_loader(wd=os.getcwd()):
    text=[]
    for filename in os.listdir(wd):
        fp = os.path.join(wd, filename)
        if os.path.isfile(fp) and fp.endswith('.json'):
            with open(fp,'r') as f :
                data=json.load(f)
            text=text+['------']+get_messages(data,['Participants to remove'])
        else: continue
    return text
cc=file_loader()
print(cc)
print(len(cc))