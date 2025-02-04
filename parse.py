import json
def parse(filepath="./results.json"):
    with open(filepath, 'r',encoding='utf-8') as file:
        data = json.load(file)
    with open('./data/train.jsonl', 'w', encoding='utf-8') as f:
        id = 0
        for i in data['chats']['list']:
            if 'name' in i.keys():
                line = []
                last_date = i['messages'][0]['date'].split('T')[0]
                for massage in i['messages']:
                    if isinstance(massage['text'], str):
                        if massage['date'].split('T')[0] == last_date:
                            if massage['text']!="":
                                if massage['from'] == i['name']:
                                    line.append({'content':massage['text'], 'role':'user'})
                                else:
                                    line.append({'content':massage['text'], 'role':'assistant'})
                        else:
                            if line!=[]:
                                line = {"id":id,"massage":line}
                                f.write(json.dumps(line, ensure_ascii=False) + '\n')
                                id+=1
                            if massage['text']!="":
                                if massage['from'] == i['name']:
                                    line = [{'content':massage['text'], 'role':'user'}]
                                else:
                                    line = [{'content':massage['text'], 'role':'assistant'}]
                            else:line=[]
                        last_date=massage['date'].split('T')[0]