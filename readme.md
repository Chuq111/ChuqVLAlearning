# ChuqVLAlearning (Project Name)
> 记录我的VLA入门之路



---


## 🚀 快速上手 (Quick Start)
### 环境要求
PyTorch 2.2.0，torchvision 0.17.0，transformers 4.40.1，tokenizers 0.19.1，timm 0.9.10，以及flash-attn 2.5.5

### 安装步骤
\`\`\`bash
# Create and activate conda environment
conda create -n openvla python=3.10 -y
conda activate openvla
git clone https://github.com/openvla/openvla.git
cd openvla
pip install -e . -i https://pypi.tuna.tsinghua.edu.cn/simple
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia -y 
# Install Flash Attention 2 for training (https://github.com/Dao-AILab/flash-attention)
#   =>> If you run into difficulty, try `pip cache remove flash_attn` first
pip install packaging ninja
ninja --version; echo $?  # Verify Ninja --> should return exit code "0"
pip install "flash-attn==2.5.5" --no-build-isolation
\`\`\`

## 🛠️ 使用说明 (Usage)
提供最基础的运行示例代码或命令。
\`\`\`bash
python scripts/generate.py --model_path ./checkpoints
\`\`\`

## 📁 目录结构 (Project Structure)
简要说明代码组织方式。
* `openvla/`: 核心模型代码
* `scripts/`: 训练与推理脚本
* `data/`: 数据预处理工具

