# 🤖 ChuqVLAlearning

> **记录我的 VLA (Vision-Language-Action) 入门之路**
>
> 本项目致力于探索大语言模型与机器人控制的结合，基于 OpenVLA 进行深度学习与实践。

---

## 🚀 快速上手 (Quick Start)

### 📋 环境要求
在开始之前，请确保你的系统环境满足以下版本要求：

* **核心框架**: `PyTorch 2.2.0`, `torchvision 0.17.0`
* **模型库**: `transformers 4.40.1`, `tokenizers 0.19.1`, `timm 0.9.10`
* **加速组件**: `flash-attn 2.5.5`

### 🔧 安装步骤
执行以下命令完成开发环境的初始化：

```bash
# 1. 创建并激活 conda 环境
conda create -n openvla python=3.10 -y
conda activate openvla

# 2. 克隆仓库与基础依赖安装
git clone [https://github.com/openvla/openvla.git](https://github.com/openvla/openvla.git)
cd openvla
pip install -e . -i [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)

# 3. 安装 PyTorch 核心组件 (推荐使用 CUDA 12.4)
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia -y 

# 4. 安装 Flash Attention 2 (训练必备)
# 💡 如果安装遇到困难，请先尝试运行: pip cache remove flash_attn
pip install packaging ninja
ninja --version; echo $?  # 验证 Ninja 是否安装成功，返回 0 即可
pip install "flash-attn==2.5.5" --no-build-isolation

# 5.数据集
# 💡由于OpenVLA-7B已经在包含BridgeData V2 数据集超集上进行了预训练，当我们再在该数据集上使用LoRA微调时能看到近乎100%的成功率。
# 💡因此我们后面会调整参数与预训练数据集做一些区分以达到微调效果
# Change directory to your base datasets folder
cd <PATH TO BASE DATASETS DIR>

# Download the full dataset (124 GB)
wget -r -nH --cut-dirs=4 --reject="index.html*" https://rail.eecs.berkeley.edu/datasets/bridge_release/data/tfds/bridge_dataset/

# Rename the dataset to `bridge_orig` (NOTE: Omitting this step may lead to runtime errors later)
mv bridge_dataset bridge_orig

**现在，启动训练脚本。如果你想使用不同数量的节点或GPU，可以在vla.py 中修改VLA训练配置，然后相应更改下面的和参数。--nnodes--nproc-per-node**
