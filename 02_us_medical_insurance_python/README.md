# U.S. Medical Insurance Cost Analysis

**Project type:** Exploratory Data Analysis (Python)  
**Focus:** Factors influencing medical insurance charges in the United States  

This project explores factors that influence **medical insurance charges in the United States**
using **exploratory data analysis (EDA) in Python**.  
The analysis focuses on understanding distributional characteristics, group-level differences,
and interaction patterns between key variables.

---

## 1. Project Scope

The goal of this project is to analyze U.S. medical insurance cost data to identify key factors
influencing insurance charges.

### Key questions explored:
- How does **smoking status** affect insurance costs?
- What is the relationship between **BMI** and insurance charges?
- How do insurance costs vary by **age**?
- Does the **number of children** meaningfully influence insurance charges?

---

## 2. Dataset

The dataset contains individual-level U.S. medical insurance records with the following variables:

| Variable   | Description |
|-----------|-------------|
| `age`     | Age of the individual |
| `sex`     | Gender |
| `bmi`     | Body Mass Index |
| `children`| Number of dependents |
| `smoker`  | Smoking status |
| `region`  | Residential region in the U.S. |
| `charges` | Medical insurance cost |

Each row represents a single individual insurance record.

---

## 3. Tools & Environment

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib  
- **Environment:** Jupyter Notebook  

---

## 4. Initial Data Overview

The analysis begins by loading the dataset and reviewing its basic structure to understand
available variables and data formats.

This includes:
- Inspecting the first few rows of the dataset
- Reviewing data types and summary statistics

---

## 5. Data Quality Checks

Before conducting deeper analysis, the dataset is assessed for potential data quality issues to
ensure observed patterns are not driven by structural errors.

The following checks are performed:
- Missing value detection
- Duplicate record identification
- Cardinality assessment of categorical variables

### Summary:
- No missing values were detected.
- Categorical variables show reasonable cardinality.
- One fully duplicated record was identified and removed to avoid double-counting and bias.

---

## 6. Univariate Analysis

Univariate analysis examines each variable individually to understand its distribution and basic
characteristics before exploring relationships between variables.

### Numerical variables analyzed:
- `age`
- `bmi`
- `children`
- `charges`

For each numerical variable, the analysis assesses:
- Central tendency (mean, median)
- Dispersion (range, interquartile range)
- Distribution shape and skewness
- Presence of potential outliers

Key observations include:
- Insurance charges exhibit strong right skewness with extreme high-cost outliers.
- BMI shows moderate right skewness.
- Number of children behaves as a discrete, right-skewed variable.
- These patterns suggest that median-based summaries may be more robust than means.

---

## 7. Categorical Variables Analysis

Categorical variables are examined to understand group composition and potential class
imbalances.

Variables analyzed:
- `sex`
- `smoker`
- `region`
- Discrete interpretation of `children`

Key observations include:
- Sex and region are relatively well balanced.
- Smoking status is notably imbalanced, with smokers representing a minority.
- Number of children is heavily concentrated in lower values (0–2), with sparse higher counts.

These distributions provide essential context for subsequent group-level comparisons.

---

## 8. Bivariate Analysis

Bivariate analysis examines relationships between variables, with a primary focus on how
different factors relate to insurance charges.

### Relationship 1: Insurance Charges by Smoking Status
- Smoking status creates a strong separation in insurance charges.
- Smokers incur substantially higher costs than non-smokers.
- Median-based comparisons are more appropriate due to skewness and extreme outliers.

### Relationship 2: Insurance Charges by BMI
- BMI shows a weak overall association with charges.
- Stratification by smoking status reveals a strong positive relationship between BMI and
  charges among smokers.
- High-cost outliers are concentrated among smokers with higher BMI.

### Relationship 3: Insurance Charges by Age
- Age shows a moderate positive relationship with insurance charges overall.
- Among non-smokers, insurance costs increase steadily with age.
- Among smokers, high baseline costs reduce the relative impact of age.

### Relationship 4: Insurance Charges by Number of Children
- Insurance charges do not increase monotonically with the number of children.
- Median costs remain relatively stable across most family sizes.
- Family size shows limited explanatory power compared to other variables.

---

## 9. Synthesis of Key Relationships

The exploratory analysis identifies clear differences in explanatory strength across variables:

### Relative importance of variables:
1. **Smoking status** — dominant cost driver  
2. **Age** — strong structural factor  
3. **BMI** — conditional factor dependent on smoking status  
4. **Number of children** — weak explanatory variable  

Key patterns:
- Aggregate relationships often mask important subgroup dynamics.
- High insurance charges are disproportionately concentrated among smokers, particularly
  those with higher BMI and older age.
- Mean-based summaries are sensitive to extreme values; medians provide more robust
  representations.

---

## 10. Conclusion

This exploratory analysis provides a clear, evidence-based understanding of how medical
insurance charges vary across individuals and population segments.

The findings establish a strong foundation for potential downstream modeling by identifying
dominant drivers, interaction effects, and appropriate summary metrics, while remaining strictly
within the scope of exploratory data analysis.
