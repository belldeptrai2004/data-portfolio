\# U.S. Medical Insurance Cost Analysis  

\### Exploratory Data Analysis (Python)



\## 1. Project Overview

This project explores key factors influencing \*\*medical insurance charges in the United States\*\* using \*\*exploratory data analysis (EDA) in Python\*\*.



The objective is to identify which variables are most strongly associated with insurance costs, understand how these relationships differ across population segments, and translate statistical patterns into clear analytical insights.



This project is designed as a \*\*portfolio-grade EDA\*\* for a \*\*fresher / junior data analyst\*\*, emphasizing analytical thinking, data interpretation, and structured insight communication rather than predictive modeling.



---



\## 2. Business Questions

The analysis addresses the following questions:



\- How does \*\*smoking status\*\* affect medical insurance charges?

\- What is the relationship between \*\*BMI and insurance costs\*\*, and does it change by smoking status?

\- How do insurance charges vary with \*\*age\*\*, and are age effects consistent across smokers and non-smokers?

\- Does the \*\*number of children\*\* meaningfully influence insurance costs?



---



\## 3. Dataset Description

The dataset contains individual-level U.S. medical insurance records with the following variables:



| Column     | Description |

|-----------|-------------|

| `age`     | Age of the individual |

| `sex`     | Gender |

| `bmi`     | Body Mass Index |

| `children`| Number of dependents |

| `smoker`  | Smoking status (yes / no) |

| `region`  | Residential region in the U.S. |

| `charges` | Medical insurance cost |



Each row represents a single individual insurance record.



---



\## 4. Tools \& Environment

\- \*\*Python\*\*

\- \*\*Pandas\*\*

\- \*\*NumPy\*\*

\- \*\*Matplotlib\*\*

\- Jupyter Notebook



---



\## 5. Analytical Approach

The project follows a structured EDA workflow:



\### 5.1 Data Sanity Checks

\- Data type validation

\- Missing value checks

\- Duplicate detection and removal

\- Cardinality assessment for categorical variables



\### 5.2 Univariate Analysis

\- Distribution, skewness, and outlier assessment for numerical variables

\- Frequency and proportion analysis for categorical variables

\- Identification of variables with strong skewness and extreme values



\### 5.3 Bivariate Analysis

\- Comparison of insurance charges across key categorical segments

\- Analysis of relationships between numerical variables and charges

\- Stratified analysis to uncover \*\*interaction effects\*\* (e.g., BMI × smoking)



\### 5.4 Synthesis

\- Ranking variables by explanatory strength

\- Translating statistical patterns into analytical insights

\- Identifying implications for downstream analysis



---



\## 6. Key Findings

\- \*\*Smoking status\*\* is the dominant driver of insurance charges, creating a strong and consistent separation between smokers and non-smokers.

\- \*\*Age\*\* shows a clear positive relationship with insurance costs, particularly among non-smokers.

\- \*\*BMI\*\* has a weak overall association with charges, but becomes highly informative when analyzed jointly with smoking status, indicating a strong interaction effect.

\- \*\*Number of children\*\* shows limited explanatory power and should be treated as a secondary or control variable rather than a primary cost driver.

\- Aggregate relationships often mask important subgroup dynamics; \*\*segmentation is critical\*\* for accurate interpretation.



---



\## 7. Implications

\- Median-based comparisons are more appropriate than mean-based summaries due to strong right skewness and extreme outliers.

\- Smoking status should be treated as a \*\*core segmentation variable\*\* in any downstream modeling or pricing analysis.

\- Interaction effects (e.g., smoking × BMI, smoking × age) are likely to be important in predictive or explanatory models.



---



\## 8. Project Scope \& Limitations

\- This project focuses on \*\*exploratory analysis only\*\*; no predictive modeling is performed.

\- The dataset is observational, so findings reflect \*\*associations rather than causality\*\*.

\- Results may not generalize beyond the population represented in the dataset.



---



\## 9. Next Steps

Potential extensions of this project include:

\- Statistical testing of group differences

\- Regression modeling with interaction terms

\- Log-transformation or robust modeling approaches to handle skewness



---



\## 10. Author Note

This project was completed as part of a personal portfolio to demonstrate \*\*data analysis thinking, EDA structure, and insight communication\*\* using Python.



