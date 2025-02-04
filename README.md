# Script to create your digital copy via your telegram activity 

## How to use:
Download your chat history from telegram in json format. Put result.json in app directory. Then in config.yaml change project_name, username and token. username and token are your HF user and token. then run main.py chose train model option and you'll get fine-tuned model on your HF account.

## Config:
base_model: HF link to base model
project_name: name of tour model
json_path: path to your telegram archive
username: HF_user
token: HF_token
push_to_hub: true for pushin' on HF
block_size: Size of the blocks for training, can be a single integer or a list of integers. 
model_max_length: Maximum length of the model input.
max_prompt_length: Maximum length of the prompt.
epochs: Number of training epochs
batch_size: Batch size for training
lr: Learning rate for training
peft: Whether to use Parameter-Efficient Fine-Tuning (PEFT).
quantization: Quantization method to use (e.g., ‘int4’, ‘int8’, or None).
target_modules: Target modules for quantization or fine-tuning.
padding: Side on which to pad sequences (left or right).
optimizer: Optimizer to use for training.
scheduler: Learning rate scheduler to use.
gradient_accumulation: Number of steps to accumulate gradients before updating.
mixed_precision: Type of mixed precision to use (e.g., ‘fp16’, ‘bf16’, or None).

