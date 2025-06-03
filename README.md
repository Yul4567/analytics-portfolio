# analytics-portfolio
**This repository contains small Python projects focused on data analysis and visualization.**

# Correlation Matrix Heatmaps for Psychological Data

This project visualizes correlation matrices for two groups of participants (with and without combat experience) based on the results of psychological testing.

## 🧠 Context

The analysis includes data from multiple psychological methods previously processed using SPSS. The variables reflect psychological traits or states relevant to individuals with military background and those without.

## 🔍 Purpose

To provide a comparative visual overview of:
- Inter-variable correlations within each group
- Differences in psychological patterning between the groups

## 🛠️ Tools & Libraries

- Python
- `pandas`
- `seaborn`
- `matplotlib`

## 📊 Output

The script generates two heatmaps:
1. One for the group **with combat experience**
2. One for the group **without combat experience**

These heatmaps help identify distinct psychological profiles and interrelations among traits for each group.

📝 Notes

- The color intensity and annotations reflect the strength and direction of Pearson correlation coefficients.
- This visual representation helps highlight unique patterns of inter-variable dynamics in each population.

> ⚠️ Note: The correlation values were obtained externally (in SPSS), and are manually included in the dataset.
