"""
Vedaz AI Engineer Assessment
Fine-tuning Qwen2.5-3B-Instruct using LoRA

Author: Snehil Shukla
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig

# --------------------------------------------------
# Model Configuration
# --------------------------------------------------

MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading model...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto"
)

print("Model Loaded Successfully!")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

print("Loading Dataset...")

dataset = load_dataset(
    "json",
    data_files="dataset/astrology_dataset.json"
)

print(dataset)

# --------------------------------------------------
# LoRA Configuration
# --------------------------------------------------

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

# --------------------------------------------------
# Training Configuration
# --------------------------------------------------

training_args = SFTConfig(
    output_dir="./trained_model",
    num_train_epochs=1,
    per_device_train_batch_size=1,
    learning_rate=2e-4,
    logging_steps=10,
    save_strategy="epoch",
)

# --------------------------------------------------
# Trainer
# --------------------------------------------------

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    args=training_args,
    peft_config=lora_config,
)

# --------------------------------------------------
# Train
# --------------------------------------------------

print("Starting Training...")

# trainer.train()

print("Training Complete!")

# --------------------------------------------------
# Save Model
# --------------------------------------------------

# trainer.save_model("./trained_model")

print("Model Saved!")