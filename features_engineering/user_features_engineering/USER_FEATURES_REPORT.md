
# 用户侧特征提取与加权评论特征生成报告  
*User-Side Feature Extraction & Weighted Review Feature Construction Report*

## 📌 项目背景 | Background

本阶段工作旨在从 Yelp 数据集中提取用户层级的统计与行为特征，识别高质量用户，并据此对商家评论信息进行加权处理，以提升后续模型识别宝藏商家的准确性。

This phase focuses on extracting user-level features from the Yelp dataset, identifying high-quality users, and leveraging this to compute weighted business review features—enhancing the downstream ability to discover underrated businesses.



## 🧠 用户特征提取 | User Feature Extraction

📁 源代码文件: `user_feature.ipynb`  
🔢 输出文件: `businesses_user_Indianapolis_features.csv`

我们从原始的 `users_df` 与 `reviews_df` 数据中，聚合用户特征到商家维度，形成以下字段：

| 特征名 | 含义 |
|--------|------|
| avg_user_review_count | 平均发评数 |
| avg_user_useful / funny / cool | 用户被标记的互动质量 |
| avg_user_avg_stars | 用户整体评分倾向 |
| elite_user_ratio | 留言用户中 elite 用户比例 |
| avg_user_fans | 社交影响力指标 |
| avg_user_compliments | 用户被点赞总数 |
| avg_user_account_age_days | 平均账号年龄 |

并使用 `log1p + Z-score 标准化` 方式对偏态列进行处理，确保后续输入模型时特征具有可比性。关于标准化前后的对比，参照源文件里的可视化结果，这里不展示。



## 🏅 高质量用户识别 | High-Quality User Scoring

📁 源代码文件: `user_quality.ipynb`

为了提升评价的可信度，我们在用户原始特征基础上构建了用户质量评分 `user_quality_score`。得分标准包括：

- 评论活跃度（review_count）
- 内容互动质量（useful、compliment_sum）
- 社交影响力（fans）
- elite 标记（elite_flag）
- 账号资历（account_age_days）

我们采用 `log1p 转换 + Z-score 标准化` 处理上述变量，并通过线性加权公式生成质量评分。为避免极端分值干扰，最终采用了“Top 10% 高质量用户加权放大”的策略：

```python
users_quality_df['user_quality_weight'] = users_quality_df['user_quality_score'].apply(
    lambda x: 1.5 if x >= score_90th_percentile else 1.0
)
```



## 🧮 评论加权计算 | Weighted Review Aggregation

📁 输出文件: `business_review_Indianapolis_features_weighted.csv`  
（在 `business_review_Indianapolis_features.csv` 基础上新增字段）

基于用户评分权重，我们对每个商家在以下维度进行了加权汇总：

| 加权字段名 | 含义 |
|------------|------|
| weighted_stars | 高质量用户视角下的平均星级 |
| weighted_useful / funny / cool | 高质量用户行为权重加总后的互动性指标 |
| weighted_sentiment_score_scaled | 基于标签映射（-2 ~ +2）的情感加权均值（标准化后） |
| weighted_interact_score_scaled | 加权计算的互动综合分 |
| std_weighted_stars_scaled | 加权星级的标准差，衡量评分一致性 |

这些指标更能反映出“高质量用户对商家的真实看法”，对后续识别“被埋没的宝藏商家”具有重要参考价值。



## ✅ 输出结构 | Final Outputs

- `businesses_user_Indianapolis_features.csv`  
  商家维度聚合的用户侧特征（标准化后）

- `business_review_Indianapolis_features_weighted.csv`  
  原始评论特征 + 高质量用户加权生成的评论特征



## 📌 后续工作建议 | Next Steps

- 合并商家、评论、用户三类特征，构建完整的 `business_features_full.csv`
- 进行无监督聚类（如 KMeans）或监督分类模型训练
- 可视化比较 weighted 与 unweighted 的差异，识别潜在宝藏商家

