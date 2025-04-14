# 🌟 Yelp Hidden Gems 项目 | **Comprehensive Report on the Yelp Hidden Gems Project**

## 📌 项目简介 | **Project Introduction**

本项目名为 **GemSeek**，旨在从 Yelp 数据集中识别“隐藏宝藏商家”（Hidden Gems）——即评分高但曝光度低的优质商家。通过数据筛选、特征提取、聚类分析与建模打分，最终筛选出最具潜力的商家推荐名单。

> **GemSeek** is a data mining project aimed at identifying high-quality but underappreciated businesses on Yelp through feature engineering, clustering, and regression modeling.



## 📂 数据获取与预处理 | **Dataset Acquisition and Filtering**

### 🔽 数据下载 | Downloading the Yelp Dataset

- 数据来源于 Kaggle 的官方 Yelp 数据集，通过配置 kagglehub 下载脚本自动获取。
- Yelp 数据集文件巨大，尤其是 review.json (~5GB) 和 user.json (~3GB)，建议逐行读取以降低内存压力。

- The data originates from the official Yelp dataset on Kaggle and is automatically retrieved using a configured kagglehub download script.

- The Yelp dataset files are large—particularly review.json (~5GB) and user.json (~3GB)—so it is recommended to read them line by line to reduce memory overhead.

### 🏙️ 城市筛选与标准化 | City Filtering & Normalization

- 鉴于数据规模庞大，采用“城市粒度过滤”方法，仅选择 Indianapolis 作为分析对象，包含 7,547 家商家与 360,000 条评论。
- 使用向量嵌入和层次聚类标准化城市名，将 1,416 个原始城市统一为 983 个。


- Given the dataset's scale, a city-level filtering strategy was adopted, selecting only Indianapolis for analysis, which includes 7,547 businesses and 360,000 reviews.  
- City names were standardized using vector embeddings and hierarchical clustering, reducing 1,416 original entries to 983 unified city names.

## 🧠 情感分析 | **Sentiment Analysis on Reviews**

- 使用 `tabularisai/multilingual-sentiment-analysis` 模型对评论情感进行分类，支持多语言。
- 采用滑动窗口处理长文本，并结合批处理提升效率。
- 输出结果保存在 `reviews_Indianpolis_analyzed.csv`，包括情感标签和分布图。

- The `tabularisai/multilingual-sentiment-analysis` model was used for sentiment classification of reviews, supporting multiple languages.  
- A sliding window approach was applied to handle long texts, combined with batch processing to improve efficiency.  
- The results, including sentiment labels and distribution visualizations, were saved in `reviews_Indianpolis_analyzed.csv`.

## 🏗️ 特征工程 | **Feature Engineering**

### 🏪 商家特征 | Business Features

- 从原始属性（attributes）和分类（categories）字段中提取高频值，计算 `attr_score` 与 `cat_score`，用于表征商家的结构性特征。
- 所有中间文件与特征汇总在 `business_Indianapolis_features.csv`。

- High-frequency values were extracted from the original `attributes` and `categories` fields to compute `attr_score` and `cat_score`, representing structured characteristics of each business.  
- All intermediate files and aggregated features are compiled in `business_Indianapolis_features.csv`.

### 👤 用户特征 | User Features

- 提取用户平均行为指标（如 useful、fans、account age 等），聚合到商家维度。
- 构建用户质量评分并对高质量用户加权处理，为评论加权做准备。

- Average user behavior metrics (e.g., `useful`, `fans`, `account age`, etc.) were extracted and aggregated at the business level.  
- A user quality score was constructed, and high-quality users were assigned greater weights to prepare for weighted review aggregation.

### 💬 评论特征 | Review Features

- 多维度提取评论相关指标：评分均值与方差、情感占比、文本长度、互动性、活跃周期等。
- 并生成带有用户质量加权的版本（`weighted_stars`, `weighted_sentiment_score_scaled` 等）。

- Multi-dimensional review features were extracted, including average and variance of ratings, sentiment ratios, text length, interaction metrics, and activity span.  
- A user-quality-weighted version was also generated, featuring metrics such as `weighted_stars` and `weighted_sentiment_score_scaled`.

### 📦 综合特征融合 | Merged Features

- 所有特征合并至 `features.csv` 与 `features_weighted.csv`，作为后续聚类与建模输入。
- All features were merged into `features.csv` and `features_weighted.csv`, serving as input for subsequent clustering and modeling tasks.



## 🔍 聚类分析 | **Clustering for Hidden Gems Discovery**

- 初步基于评分与评论数用 KMeans 聚类，识别高评分低评论商家。
- 深度聚类则剔除评分与评论数，保留约 25 个行为特征，通过 PCA 可视化分析。
- 最终识别出聚类1（Cluster 1）为潜在宝藏商家集合，并打上 `gem_label`。

- Initial clustering was performed using KMeans based on star ratings and review counts to identify businesses with high ratings but few reviews.  
- Deep clustering excluded ratings and review counts, retaining around 25 behavioral features, and was visualized using PCA for exploratory analysis.  
- Cluster 1 was ultimately identified as a potential group of hidden gem businesses, and each member was labeled with `gem_label`.

## 🤖 建模与打分 | **Modeling and Gem Scoring**

### 🔢 阶段一：分类模型 | Phase 1: Classification

- 使用聚类1作为正类，训练 LR、RF、XGBoost 等模型，解决类别不平衡问题，取得良好效果（最高 F1 达 0.986）。

- Cluster 1 was used as the positive class to train models such as Logistic Regression, Random Forest, and XGBoost. Class imbalance was addressed using sampling and weighting techniques, achieving strong performance with a maximum F1 score of 0.986.

### 📈 阶段二：人工规则打分 + 回归建模 | Phase 2: Rule-Based Scoring + Regression

- 构建规则得分系统（如星级≥4.5 且评论少 → 得分高），作为监督信号训练 XGBoost 回归模型预测 `gem_score`。
- 输出包括：
  - `cluster1_scores_all.csv`：所有商家 gem_score 预测值
  - `gem_candidates_final.csv`：最终交集筛选的 82 家宝藏商家。


- A rule-based scoring system was developed (e.g., businesses with ≥4.5 stars and few reviews received higher scores) to serve as supervision for training an XGBoost regression model to predict `gem_score`.  
- Outputs include:  
  - `cluster1_scores_all.csv`: predicted `gem_score` values for all businesses  
  - `gem_candidates_final.csv`: the final set of 82 gem businesses selected through intersection-based filtering.


## 🗺️ 可视化与结果展示 | **Final Visualization & Outputs**

- 所有 5,335 家商家评论数分布图表明：最终入选的 82 家宝藏商家多为 **0-10 条评论的低曝光高评分商家**。
- 使用 folium 构建交互地图 `gem_businesses_map.html`，支持点击查看商家信息。
- 输出详细字段包括星级、分类、营业时间、经纬度等，保存于 `gem_businesses_info.csv`。

- The review count distribution of all 5,335 businesses revealed that the final 82 selected gem businesses are predominantly **low-exposure, high-rating businesses with 0–10 reviews**.  
- An interactive map was created using `folium` (`gem_businesses_map.html`), allowing users to click and view business details.  
- Detailed output fields—such as star rating, categories, business hours, and geographic coordinates—are stored in `gem_businesses_info.csv`.



## ✅ 项目亮点与总结 | **Highlights & Conclusion**

| 中文 | English |
|------|---------|
| 成功构建完整流程，从特征提取 → 聚类 → 打分 → 地图展示 | A full pipeline from feature extraction to scoring and visualization |
| 综合多种建模方法，回归打分比硬分类更具细粒度 | Combined classification & regression for nuanced gem_score modeling |
| 支持推荐系统、种草地图、城市引擎等多种应用场景 | Applicable to recommender systems, travel maps, discovery engines |




