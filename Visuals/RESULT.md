# 🗺️ Yelp Hidden Gems 最终结果可视化报告  
**Final Visualization & Output Report for Hidden Gems on Yelp**

## 📁 文件说明 | Files Summary

| 文件名 | 内容说明 | Description |
|--------|-----------|-------------|
| `gem_businesses_info.csv` | 最终筛选出的 82 家宝藏商家的原始完整信息（名称、星级、评论数、分类等）<br> Final list of 82 selected gem businesses with name, stars, review count, categories, etc. |
| `results_visualizing.ipynb` | 可视化源代码（数据合并 + 图表 + 地图）<br> Jupyter Notebook for merging, visualization, and map generation |
| `gem_businesses_map.html` | 商家地图展示，支持交互查看<br> Interactive map of gem businesses with clickable markers |


## 📊 评论数分布分析 | Review Count Distribution Analysis

我们首先统计了全体 5,335 家商家的评论数分布，并按区间进行可视化：  
We analyzed review counts across all 5,335 businesses and visualized their distribution by range:

饼状图显示评论数分布如下 | Pie chart result:

- **0-10 条评论 / reviews**：35.8%
- **10-50 条评论**：43.4%
- **50-100 条评论**：10.0%
- **100-500 条评论**：10.0%
- **500+ 条评论**：0.8%

📌 **分析结论 / Conclusion**：**最终筛选出的宝藏商家评论数多数集中在 0-10 区间，说明模型有效识别了低曝光高质量商家。**  
The selected 82 gem businesses mostly fall in the 0-10 review range, indicating the model successfully captures low-exposure, high-quality targets.



## 🏷️ 宝藏商家信息整合 | Gem Business Information Enrichment

我们为最终结果补充了以下信息字段：  
We enriched the final gem list with additional business attributes:

- 商家名称 | `name`
- 星级评分 | `stars`
- 评论数 | `review_count`
- 属性 | `attributes`
- 分类 | `categories`
- 营业时间 | `hours`
- 经纬度 | `latitude`, `longitude`

📄 输出文件 / Output: `gem_businesses_info.csv`



## 🗺️ 地图展示 | Interactive Map Visualization

我们使用 folium 创建了交互地图，展示 82 家商家的地理位置。  
We created an interactive HTML map using `folium`, displaying the locations of the 82 gems.

📍 文件 / File: `gem_businesses_map.html`  
🖱️ 可浏览地图、点击查看商家名称和评分  
You can zoom and click to view business names and scores directly.



## ✅ 总结 | Summary

| 中文 | English |
|------|---------|
| 成功构建了从商家信息提取、得分排序、地图展示的完整可视化流程 | Successfully built a full visualization pipeline including extraction, ranking, and mapping |
| 所选商家平均评论数极低，但评分普遍较高，符合“低热度高质量”特征 | The selected gems have low review counts but high ratings — ideal "hidden gem" characteristics |
| 最终输出可用于城市推荐榜单、小红书地图种草、商家挖掘系统等 | Final results can power city recommendation lists, travel apps, or discovery engines |

