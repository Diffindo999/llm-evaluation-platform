import json
import os

INPUT = "outputs/eval_result.json"
OUT_MD = "outputs/report.md"

def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        data = json.load(f)
    total_cnt = len(data)
    bad_cnt = sum(1 for x in data if x["is_badcase"])
    avg_total = sum(x["total"] for x in data) / total_cnt

    md = f"""# LLM模型版本评测报告
> 评测样本总数：{total_cnt}，BadCase数量：{bad_cnt}，整体平均分：{avg_total:.2f}

## 汇总指标
|指标|平均分|
| ---- | ---- |
"""
    dim_names = ["事实正确性","指令遵循","内容安全","简洁度","格式合规"]
    for dim in dim_names:
        s = sum(x["judge_score"][dim] for x in data) / total_cnt
        md += f"|{dim}|{s:.2f}|\n"

    md += "\n## 全部样本明细\n"
    for row in data:
        md += f"""
### Query：{row['query']}
- 模型回答：{row['model_response']}
- 总分：{row['total']}
- 打分详情：{row['judge_score']}
- 判定BadCase：{row['is_badcase']}
- 理由：{row['reason']}
"""
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✅ Markdown报告已生成：{OUT_MD}")

if __name__ == "__main__":
    main()
