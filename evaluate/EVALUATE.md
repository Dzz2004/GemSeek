# Hidden Gem Identification Project: Model Validation, Scoring Rule Optimization, and Regression Generalization

## 一、项目目标

本项目旨在于利用评论数据和特征抽取把握商户评价的内在结构，定量化地评估并定位那些“评分高、露面率低”的优质商户，即我们所称的 hidden gems (宝藏商户)。

---

## 二、后验数据的建立与分析

为验证原打分算法 gem_score 的有效性，我们成立了两套统计后验数据：

- `evaluate/cluster1_now_sorted.csv`
  - 记录了 cluster1 的 860 个商户在 2025 年 4 月的当前信息 (stars_now, review_count_now)，以及过去数据对应值 (stars, review_count)，并计算了增量、增长率等关键指标
- `evaluate/gem_businesses_info_now.csv`
  - 记录了初始规则筛选出的 82 个 gem 商户的基础信息和后验增长数据

### 后验分析结果

- 随机抽样的355名商户:
  - 平均增长评分: **-0.013**
  - 平均评论增量: **+19.47**
  - 平均评论增长率: **0.54**

- 原始 gem_score 筛选出的82名 gem 商户:
  - 平均增长评分: **-0.028**
  - 平均评论增量: **+6.66**
  - 平均评论增长率: **1.18**

- 各自增长率分布显示：
  - cluster1 流行区间: **(0.329, 0.506]**
  - gem82 流行区间: **(-0.2, 0.368]**

> 结论：我们初步证明原则选择的 gem 商户实际评论增长率的确明高于全体汇统，其中一部分商户实现了爆发式增长。

---

## 三、打分规则优化过程

### 问题评价

- 旧规则存在过于保守、分布均值的问题
- 爆发性指标 (burst, recent, sentiment) 加分效应较弱
- 评分分类太精细，导致展现分布失真

### 分析工作

- 参考 `evaluate/cluster1_now.ipynb`，分析了 review_count 分布和 Top100 高增长率商户的分布点点图
- 生成热力图，分析“评分 × 评论量” 结构与增长率关系

### 新打分规则

- 基础分分类应用分位数分类，具备跨城市转移能力
- 爆发性指标作为主要分别条件，重点抽积 recent_ratio, review_burst_score, sentiment_score 等特征

---

## 四、新 gem_score 命中效果

| 指标 | cluster1 | Top100 (gem_score) |
|---------|------------|----------------------|
| avg_increase_stars | -0.054 | **-0.148** |
| avg_increase_review_count | 14.51 | **20.17** |
| avg_growth_rate_review_count | 0.57 | **1.79** |
| median_growth_rate_review_count | 0.273 | **0.536** |
| max bin 分布 | (0.19, 0.732] | (-0.226, 0.328] |

### 实际验证：“进一步分析实际宝藏商户实现率”

- 全体 cluster1 中高于平均增长率的商户: 198/860 、满足率 23.0%
- gem_score Top100 中满足该条件的商户: 50/100 、满足率 50.0%

> 证明打分规则对高增长商户的装载效率是随机抽样的 **2.17 倍**，具备较好的预判力和数据位置能力。

---

## 五、gem_score 进行 XGBoost 回归学习

- 特征同前，总共 26 项
- 结果：MSE = **0.031**, R^2 = **0.724**
  - 表明模型对原打分规则抽象力强，具备应用于新城市和新库的强跨域能力

---

## 六、特征重要性分析 + SHAP 分析

- 最重要特征：
  - `sentiment_score_mean_scaled`
  - `std_review_stars_scaled`
  - `review_timespan_days_scaled`
  - `review_burst_score_scaled`
  - `avg_user_avg_stars`

### SHAP 分析结果：
- 依赖时间性、情感、爆发性三大正向指标
- 对于 `review_timespan_days_scaled`，SHAP 结果显示：评论距离时间迅长但评论量不高的商户，并不是真正的 gem，因此模型对该特征出现负向应策

---

## 七、回归预测的 Top100 验证效果

| 指标 | Top100 (regression model) |
|--------|-------------------------------|
| avg_increase_stars | -0.154 |
| avg_increase_review_count | 22.82 |
| avg_growth_rate_review_count | 1.99 |
| median_growth_rate_review_count | 0.488 |
| 主分布区间 | (-0.0736, 0.463] |

> 推进证明：模型培育后进行排名，可以较好地实现“选择出更有成长力的 gem ”，表现略佳于手工打分

## 八、显著性分析
为进一步验证 gem_score 的预测能力，我们使用了三种统计检验方法：

- Pearson 相关系数显示 gem_score 与评论增长率之间具有显著正相关（r = 0.529，p < 1e-7）；

- Spearman 秩相关系数为 0.475（p < 1e-6），说明两者在排序上的一致性也具有统计显著性；

- Mann–Whitney U 检验对 gem_score Top100 与其他商户的增长率分布进行对比，结果显示两组差异显著（p = 4.77e-05）。

综上所述，gem_score 不仅在平均水平上具备较强的区分能力，也在排名和分布层面展示出良好的稳定性与一致性，为后续建模与推荐提供了理论支持。

---

## 结论

- 原则 gem_score 具有不错的挖掘效果，特别是对时间性和情感评价数据效应明显
- 基于 gem_score 进行回归学习可以实现支撑跨城市和平台跨期的通用性打分
- SHAP 分析与后验数据分析反映了模型学习到了一些超越手工规则的规律，倾向新型 gem (新店爆发型)的挖掘能力

