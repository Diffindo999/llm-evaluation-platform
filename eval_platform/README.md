# LLM多维度评测平台
> AI产品方向项目｜用于大模型版本迭代自动评测、badcase归集、指标看板

## 项目简介
针对大模型迭代缺少标准化验收手段的痛点，搭建一套轻量化自动评测系统。
定义5大评测维度rubric，使用LLM作为Judge打分，支持批量评测、BadCase自动筛选、指标可视化、人工复核工作台、自动输出评测报告。
适合模型灰度发布、Prompt迭代、SFT后模型效果验证。

## 技术栈
Python / Pandas / JSON / 腾讯混元API / Streamlit / Matplotlib

## 快速启动
1. 安装依赖
pip install tencentcloud streamlit pandas matplotlib tqdm
2. 填入腾讯云 SecretId、SecretKey
3. 执行评测
python main_eval.py
4. 生成评测报告
python report.py
5. 启动可视化看板
streamlit run streamlit_demo.py
## 产出物

- rubric 打分规范文档
- 评测结果 json、badcase 数据集
- Markdown 汇总评测报告
- Streamlit 交互式评测看板