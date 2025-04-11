# 📊 Yelp Hidden Gems 项目工作报告 | Yelp Hidden Gems Project Report



## 🧾 项目目标 | Project Objective

识别 Yelp 中的“隐藏宝藏商家”（Hidden Gems），通过结构化特征构建评分体系，辅助后续建模与推荐任务。

> Identify highly-rated but less popular businesses on Yelp by engineering structured features and building a scoring system for further modeling and recommendation.



## 📁 源代码与输出 | Code & Outputs

- **源代码文件 / Source Code**: `business_feature.ipynb`
- **最终输出 / Final Output**:  
  `business_Indianapolis_features.csv`  
  包含字段：`business_id`, `stars`, `review_count`, `attr_score`, `cat_score`



## 🔄 数据处理流程 | Data Processing Pipeline

### 1. 原始字段清洗与结构化 | Raw Field Cleaning

#### ✅ 属性字段（attributes）
- 格式统一处理（修复嵌套引号、u'xx' 等格式错误）
- 嵌套字段展开为平铺键名：如 `BusinessParking.garage → businessparking_garage`
- 构建输出文件：`business_Indianapolis_cleaned.csv`（结构化格式）

#### ✅ 类别字段（categories）
- 多标签字段按逗号拆分处理
- 提取前 50 个高频类别作为候选特征



### 2. 高频特征提取 | Top Feature Extraction

- `business_Indianapolis_top_attributes.csv`：包含前 30 个高频属性字段及其取值
- `business_Indianapolis_categories.csv`：包含前 50 个高频类别标签及其出现频次



## 🧮 特征构建与打分体系 | Feature Engineering & Scoring System

### 🧱 属性得分（attr_score）

- 按属性取值打分，如下：
  - `'true'` → +1.0
  - `'false'` → -0.5
  - `'free'` → +1.0
  - `'casual'` → +1.0
  - `'none'` / 缺失 → 0
- 构造字段：`attr_score`

### 🏷️ 类别得分（cat_score）

- 使用 TF-IDF 模型对前 50 个类别进行加权建模
- 计算每个商家的类别信息密度得分
- 构造字段：`cat_score`



## 📊 可视化结果 | Visualization

- 输出图表文件：`business_scores_distribution.png`
- 内容包括：
  - `attr_score` 分布直方图 + KDE
  - `cat_score` 分布直方图 + KDE
  - 二维散点图：`cat_score` vs `attr_score`（辅助识别右上角宝藏商家）



## 📌 变量保留策略 | Variable Retention Strategy

- 保留 `attr_score` 和 `cat_score` 为两个独立变量
- 避免人为融合权重，便于后续建模或打分调优
- 支持未来引入：
  - 评论情感得分 `sentiment_score`
  - 用户影响力得分 `user_weighted_score`
  - 热度标准化指标 `popularity_score`



## 🗂️ 文件输出结构 | Output File Summary

| 文件名 | 说明 |
|--|--|
| `business_feature.ipynb` | 全部特征工程与评分代码 |
| `business_Indianapolis_cleaned.csv` | 清洗并标准化后的商家数据 |
| `business_Indianapolis_top_attributes.csv` | 高频属性字段及值统计 |
| `business_Indianapolis_categories.csv` | 高频类别标签及频次统计 |
| `business_Indianapolis_features.csv` | 最终包含评分的输出特征表 |
| `business_scores_distribution.png` | 评分分布与对比可视化图 |



📍 **作者备注：** 此报告为 Yelp 商家特征建模模块的重要阶段性成果，后续可用于推荐系统、评分模型或排行榜构建。

