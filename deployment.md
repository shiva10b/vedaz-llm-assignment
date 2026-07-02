# Hosting Qwen Model on VPS using vLLM

## Overview

After fine-tuning the Qwen2.5 model, it needs to be deployed on a Virtual Private Server (VPS) so users can interact with it through an API.

In this project, vLLM is used because it provides fast and memory-efficient inference for Large Language Models.

---

## Step 1: Create a VPS

Choose a cloud provider such as:

- AWS EC2
- Google Cloud Platform (GCP)
- Azure
- DigitalOcean
- RunPod

Recommended OS:

Ubuntu 22.04 LTS

---

## Step 2: Update the Server

```bash
sudo apt update
sudo apt upgrade -y
```

---

## Step 3: Install Python

```bash
sudo apt install python3 python3-pip -y
```

---

## Step 4: Install CUDA Drivers

Verify GPU installation:

```bash
nvidia-smi
```

The GPU information should be displayed successfully.

---

## Step 5: Install vLLM

```bash
pip install vllm
```

---

## Step 6: Download the Fine-tuned Model

Place the trained model folder on the VPS.

Example:

```
trained_model/
```

---

## Step 7: Start the vLLM Server

```bash
python -m vllm.entrypoints.openai.api_server \
    --model ./trained_model \
    --host 0.0.0.0 \
    --port 8000
```

This command starts an OpenAI-compatible API server.

---

## Step 8: Test the API

Example request:

```bash
curl http://localhost:8000/v1/models
```

If the model is running correctly, the server will return the available model information.

---

## Step 9: Production Deployment

For production use:

- Configure Nginx as a reverse proxy.
- Enable HTTPS using SSL certificates.
- Run the server as a systemd service.
- Monitor logs and GPU usage.

---

## Conclusion

Using vLLM allows efficient deployment of the fine-tuned Qwen model with low latency and high throughput. The deployed model can then be integrated into web applications, mobile apps, or chatbot services.