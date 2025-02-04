from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
import logging

logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("torch").setLevel(logging.ERROR)

def load_model(model_id):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        torch_dtype=torch.bfloat16
    )
    return tokenizer, model
    
def answer(message, tokenizer, model):
    
    date_string = datetime.today().strftime('%Y-%m-%d')

    prompt = tokenizer.apply_chat_template(
        message,
        tokenize=False,
        add_generation_prompt=True,
        date_string=date_string
    )

    inputs = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
    outputs = model.generate(input_ids=inputs.to(model.device), max_new_tokens=200)

    return tokenizer.decode(outputs[0], skip_special_tokens=True).split('assistant')[-1:][0][1:]
