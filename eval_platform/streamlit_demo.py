import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# 解决matplotlib中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

st.set_page_config(page_title="LLM评测工作台", layout="wide")
st.title("LLM多维度评测平台｜自动评测+人工复核")

# 加载并展开 judge_score
with open("outputs/eval_result.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

for item in raw_data:
    # 把打分字典摊开
    score_dict = item.pop("judge_score")
    item.update(score_dict)

df = pd.DataFrame(raw_data)

# 顶部指标
total_cnt = len(df)
bad_cnt = int(df["is_badcase"].sum())
avg_score = df["total"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("样本总量", total_cnt)
col2.metric("BadCase数量", bad_cnt)
col3.metric("全局平均分", round(avg_score, 2))

# 维度列表，和mock脚本保持一致
score_cols = ["事实正确性", "指令遵循", "内容安全", "简洁度", "格式合规"]
mean_scores = df[score_cols].mean()

fig, ax = plt.subplots(figsize=(7, 3.5))
mean_scores.plot(kind="bar", ax=ax)
ax.set_title("各维度平均分")
plt.tight_layout()
st.pyplot(fig)

# 样本复核列表
st.subheader("样本列表（支持人工复核）")
for idx, row in df.iterrows():
    with st.expander(f"样本 {idx+1} ｜总分：{row['total']}"):
        st.markdown(f"**Query：** {row['query']}")
        st.markdown(f"**模型输出：** {row['model_response']}")
        st.markdown(f"**标准答案：** {row['golden']}")
        st.markdown(f"**理由：** {row['reason']}")
        st.checkbox("标记复核", key=f"check_{idx}")
