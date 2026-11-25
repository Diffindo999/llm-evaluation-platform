# LLM Evaluation Platform
LLM 多维度评测平台｜自动评测 + 人工复核

## 项目介绍
轻量化大模型评测工作台，Python + Streamlit 实现。
支持自定义打分标尺、批量样本评测、指标可视化大盘、人工复核面板，适用于 SFT 数据质检、大模型输出效果验证。

> ✅ 本仓库为**离线演示版本**：内置 mock 打分逻辑，无需配置腾讯云 SecretId、SecretKey，不需要调用外部大模型 API 即可完整运行演示。

## 技术栈
- Python 3.10+
- Streamlit：Web 可视化面板
- Pandas：指标统计
- Matplotlib：图表绘制
- JSON：评测标尺、结果存储

## 目录结构
```
val_platform/
├── main_eval.py          # 批量评测主脚本（mock 打分）
├── streamlit_demo.py     # 可视化大盘 + 人工复核页面
├── rubric.json           # 五维评分规则：事实正确性、指令遵循、内容安全、简洁度、格式合规
├── test_samples.json     # 测试样例
├── outputs/
│   └── eval_result.json  # 评测输出结果
└── README.md


## 快速运行
1. 创建虚拟环境
```bash
python -m venv .venv
```
激活（Windows PowerShell）
.venv\Scripts\Activate.ps1
```
2. 安装依赖

```
pip install streamlit pandas matplotlib tqdm
```

3. 执行批量评测（生成结果）

```
python main_eval.py
```

4. 启动可视化页面

```
streamlit run streamlit_demo.py
```

## 功能说明

1. 按 rubric 自定义规则批量打分，自动标记 BadCase
2. 汇总大盘：样本总量、BadCase 数量、全局平均分
3. 多维度平均分柱状图可视化
4. 折叠面板逐条查看 Query、模型输出、标准答案、打分理由，支持人工复核勾选

## 项目局限

- 离线版使用模拟打分逻辑，不是真实 LLM judge 打分
- 复核勾选状态仅页面临时生效，刷新丢失，未持久化保存
- 不支持在线编辑打分标尺

## 扩展方向

- 接入 LLM API（混元 / OpenAI 等）替换 mock 打分，此时才需要配置密钥
- 持久化保存人工复核记录
- 支持多批次模型 A/B 对比评测
