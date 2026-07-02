# Vedaz AI Engineer Assessment

## Project Overview

This project demonstrates the process of fine-tuning the Qwen2.5 language model using an astrology conversation dataset.

The objective is to train the model to behave like an AI astrologer that can:

- Respond politely and empathetically
- Analyze kundli-related questions
- Ask users for required birth details
- Avoid making harmful or guaranteed predictions
- Follow safe conversational practices

---

## Project Structure

```text
Vedaz-Assignment/
│
├── dataset/
│   └── astrology_dataset.json
│
├── fine_tune.py
├── deployment.md
├── conversations.md
├── requirements.txt
└── README.md
```

---

## Model

- Base Model: Qwen2.5-3B-Instruct
- Fine-tuning Method: LoRA
- Framework: Hugging Face Transformers
- Training Library: TRL

---

## Assignment Contents

- Fine-tuning pipeline
- VPS deployment guide using vLLM
- Five manually created astrology conversations