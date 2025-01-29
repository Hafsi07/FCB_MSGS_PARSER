import json
import os


def get_messages(data,participants_to_exclude=[],participants_to_include=[]):
        
    recipiants=data.get('participants',None)
    if participants_to_include==[]: participants_to_include=recipiants
    participants_to_include=[i for i in participants_to_include if i not in participants_to_exclude]

    messages=[]
    for i in data['messages']:
        sender=i.get('sender_name',None)
        if sender in participants_to_exclude or sender not in participants_to_include:continue
            
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


def file_loader(wd=os.getcwd(),participants_to_remove=[],participants_to_include=[]):
    text=[]
    for filename in os.listdir(wd):
        fp = os.path.join(wd, filename)
        if os.path.isfile(fp) and fp.endswith('.json'):
            with open(fp,'r') as f :
                data=json.load(f)
            text=text+['------']+get_messages(data,participants_to_remove,participants_to_include)
        else: continue
    return text
cc=file_loader(participants_to_include=['Hafsi Youssef'])
print(cc)
print(len(cc))


# add timestamp and conversation ID to the parsed data
# create a java application to give options to users to choose who to exclude and who to include and conversations from when to where 