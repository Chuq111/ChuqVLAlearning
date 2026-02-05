import torch
from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image
import requests

# 1. 加载模型和处理器
model_id = "/home/user/cq/myvla/openvla/ckpts/openvla-7b"
print(f"正在加载模型 {model_id}，这可能需要一点时间...")

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
vla = AutoModelForVision2Seq.from_pretrained(
    model_id, 
    attn_implementation="flash_attention_2",  # 你的环境已装 flash-attn
    torch_dtype=torch.bfloat16, 
    low_cpu_mem_usage=True, 
    trust_remote_code=True
).to("cuda:0")

# 2. 准备输入：下载一张测试图片（或者用你本地的图片）
import numpy as np
print("正在准备模拟图片输入...")
# OpenVLA 默认通常处理 224x224 的图像
image = Image.open("robot_env.jpg")

# 3. 构造 Prompt (OpenVLA 的固定格式)
prompt = "In: What action should the robot take to pick up the corn?\nOut:"

# 4. 执行预测
print("正在预测动作...")
inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
action = vla.predict_action(**inputs, unnorm_key="bridge_orig", do_sample=False)

# 5. 查看输出
print("\n预测得到的 7 维动作向量 (Action Vector):")
print(action)
# 动作通常包含: [x, y, z, roll, pitch, yaw, gripper_open/close]