import sys
import subprocess
import yaml

from parse import parse
from chat import answer, load_model

def execute_script(script_name):
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file)
    if script_name == "1":
        training(data['json_path'])
    elif script_name == "2":
        model_path = f"{data['hub']['username']}/{data['project_name']}"
        chatting(model_path=model_path)
    else:
        print("Unavaible option. Chose '1' or '2'.")

def training(data):
    parse(data)
    subprocess.run('autotrain --config config.yaml', shell=True)

def chatting(model_path, history=[]):
    user_input = 0
    tokenizer, model = load_model(model_path)
    while user_input != "exit":
        user_input = input()
        history.append({'role':'user','content':user_input})
        answ = answer(message=history, tokenizer=tokenizer, model=model)
        print(answ)
        history.append({'role':'assistant','content':answ})

if __name__ == "__main__":
    print("Type 1 to update mode, type 2 to start conversation.")
    user_input=input()
    while user_input not in ("1","2","exit"):
            print('Unknown input')
            user_input = input()
    else:
        if user_input != "exit":
            script_name = user_input
            execute_script(script_name)
