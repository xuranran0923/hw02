# deepseek_demo1.py
import os
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="c552e229-e813-41a5-8a64-1861942f3c91",  # 你的API Key
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

# 设置问题
question = "脑电检测仪的作用是什么？"

# 发送请求
response = client.chat.completions.create(
    model="ep-20260318094713-5rh82",  # 已修复引号
    messages=[
        {"role": "user", "content": question}
    ]
)

# DeepSeek模型特有功能: 输出推理过程
if hasattr(response.choices[0].message, 'reasoning_content'):
    print(response.choices[0].message.reasoning_content)

# 打印最终答案
print(response.choices[0].message.content)

