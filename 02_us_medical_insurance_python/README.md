# U.S. Medical Insurance Costs — Exploratory Data Analysis (Python)

**Project type:** Exploratory Data Analysis (EDA)  
**Domain:** Health Insurance / Pricing & Risk Analysis  
**Tools:** Python (Pandas, NumPy, Matplotlib)  

---

## Overview

This project analyzes individual-level U.S. medical insurance data to identify **which factors are most strongly associated with variation in insurance charges**, and **how these relationships differ across key population segments**, with particular focus on **smoking status**.

Rather than building predictive models, the analysis emphasizes **distributional understanding, group-level separation, and interaction patterns**, providing a **modeling-ready analytical foundation** for downstream pricing, risk segmentation, or actuarial analysis.

---

## Analytical Objective

The primary objectives of this analysis are to:

- Identify the **dominant cost drivers** of medical insurance charges  
- Examine how cost relationships vary across **key demographic and behavioral segments**  
- Detect **interaction effects** that may be obscured in aggregate analysis  
- Establish an evidence-based foundation for future modeling or pricing analysis  

---

## Dataset

The dataset contains individual-level U.S. medical insurance records, where each row represents a single insured individual.

| Variable     | Description |
|--------------|-------------|
| `age`        | Age of the individual |
| `sex`        | Gender |
| `bmi`        | Body Mass Index |
| `children`   | Number of dependents |
| `smoker`     | Smoking status |
| `region`     | Residential region in the U.S. |
| `charges`    | Medical insurance cost |

---

## Analytical Workflow

The analysis follows a structured EDA workflow designed to move from data validation to insight synthesis:

1. **Data loading and structural overview**
2. **Data quality checks**
   - Missing values
   - Duplicate records
   - Categorical cardinality
3. **Univariate analysis**
   - Distribution shape
   - Skewness and outliers
4. **Bivariate and segmented analysis**
   - Group-level comparisons
   - Interaction patterns
5. **Synthesis and analytical implications**

---

## Data Quality Summary

- No missing values were detected across all variables  
- Categorical variables show reasonable and expected cardinality  
- One fully duplicated record was identified and removed to prevent double-counting  

All subsequent analyses are conducted on the deduplicated dataset.

---

## Key Findings

### 1. Smoking Status — Dominant Cost Driver

- Smoking status creates a **clear and strong separation** in insurance charges  
- Smokers incur **substantially higher costs** than non-smokers  
- Median charges for smokers are multiple times higher than those of non-smokers  
- Cost distributions among smokers exhibit a **heavy right tail** with extreme high-cost cases  

**Implication:** Smoking status should be treated as a **primary segmentation variable** in pricing and risk analysis.

---

### 2. Age — Strong Structural Driver

- Insurance charges generally increase with age  
- Among **non-smokers**, age shows a **strong and steady upward relationship** with charges  
- Among **smokers**, elevated baseline costs reduce the relative marginal effect of age  

**Implication:** Age is an important continuous predictor, but its effect differs by smoking status.

---

### 3. BMI — Conditional (Interaction-Dependent) Driver

- Overall, BMI shows only a **weak aggregate association** with insurance charges  
- When stratified by smoking status:
  - BMI has minimal impact among non-smokers  
  - BMI is **strongly associated with higher charges among smokers**  

**Implication:** BMI should not be interpreted independently; **BMI × smoking** interaction effects are critical.

---

### 4. Number of Children — Weak Explanatory Variable

- Insurance charges do not increase monotonically with the number of children  
- Median costs remain relatively stable across most family sizes  
- Substantial overlap exists across all groups  

**Implication:** Number of children functions primarily as a **control variable**, rather than a primary cost driver.

---

## Synthesis of Variable Importance

Based on strength, consistency, and interpretability of observed relationships:

1. **Smoking status** — dominant cost driver  
2. **Age** — strong structural factor  
3. **BMI** — conditional driver (interaction-dependent)  
4. **Number of children** — weak explanatory variable  

Key patterns observed:

- Aggregate analysis masks important subgroup dynamics  
- High insurance charges are disproportionately concentrated among **smokers with higher BMI and older age**  
- Mean-based summaries are sensitive to extreme values; **median-based comparisons are more robust**

---

## Methodological Notes

- This analysis is **exploratory and observational**; no causal claims are made  
- Skewed cost distributions are treated as **real-world variability**, not removed by default  
- Interaction patterns are assessed via **segmentation and distributional comparison**, not formal modeling  

---

## Output & Next Steps

This analysis provides a **modeling-ready perspective** on insurance cost drivers and interaction structure.

Potential extensions include:

- Regression or GLM modeling with interaction terms (e.g. smoking × BMI, smoking × age)  
- Log-transformation of charges to address skewness and heteroskedasticity  
- Segmented modeling for smokers vs non-smokers to improve interpretability  

---

## Repository Contents

- `analysis.ipynb` — Full exploratory analysis notebook  
- `README.md` — Project overview and analytical summary  

📓 **View full notebook (mobile-friendly):**  
https://nbviewer.org/github/minhkhoi-data/data-portfolio/blob/main/02_us_medical_insurance_python/analysis.ipynb
