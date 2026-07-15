# Supervised Learning in R: Regression and Classification

## Project Overview

This project applies a complete supervised-learning workflow in R to two predictive modelling problems:

1. **Regression** — predict residential building heating load from design characteristics.
2. **Classification** — predict whether an online learner will complete a course from early engagement, performance, subscription, and device information.

The project moves from data inspection and cleaning through exploratory analysis, model fitting, diagnostics, cross-validation, threshold tuning, and stakeholder-oriented interpretation.

The analysis was completed in R Markdown and uses a personalised random seed to make all random procedures reproducible.

---

## Project Objectives

The project addresses two different response-variable types and demonstrates why they require different modelling and evaluation strategies.

### Regression

Predict:

```text
heating_load
```

from residential building design variables.

Main questions:

- Which building characteristics are most strongly related to heating demand?
- Is a single predictor sufficient?
- Does a nonlinear relationship improve the fit?
- Does an interaction between wall area and glazing area improve the model?
- Which regression model performs better under 10-fold cross-validation?

### Classification

Predict:

```text
completed = yes / no
```

for online learners.

Main questions:

- Which early engagement and performance variables are associated with course completion?
- How accurately can a logistic regression model classify unseen learners?
- How do sensitivity and specificity change when the classification threshold changes?
- Is the single 80/20 test result consistent with 10-fold cross-validation?

---

## Tools

### R

The entire analysis is completed in R.

Main techniques:

- data inspection
- missing-value handling
- scatterplot matrices
- correlation analysis
- simple linear regression
- polynomial regression
- multiple regression
- interaction terms
- regression diagnostics
- 10-fold cross-validation
- stratified train-test splitting
- logistic regression
- odds-ratio interpretation
- confusion matrices
- sensitivity and specificity
- ROC analysis
- AUC
- classification-threshold tuning

### R Packages

```r
boot
pROC
```

Package roles:

- `boot` — 10-fold cross-validation using `cv.glm()`
- `pROC` — ROC curve construction and AUC calculation

The recorded analysis environment used:

```text
R 4.6.0
boot 1.3-32
pROC 1.19.0.1
```

### R Markdown

The report combines:

```text
R code
+ model output
+ plots
+ interpretation
```

in one analytical document.

---

## Recommended Project Name

```text
07_supervised_learning_regression_classification_r
```

This name is more accurate than `07_learner_retention_analytics_r` because the project contains **two separate supervised-learning problems**:

- building heating-load regression
- learner-completion classification

Learner retention represents only the second half of the project.

---

## Recommended Project Structure

```text
07_supervised_learning_regression_classification_r/
│
├── data/
│   ├── energy_homes.csv
│   └── learners.csv
│
├── report/
│   └── supervised_learning_regression_classification_report.pdf
│
├── supervised_learning_regression_classification.Rmd
│
└── README.md
```

Suggested file renaming:

```text
Assignment 2.Rmd
    ↓
supervised_learning_regression_classification.Rmd
```

```text
Assignment-2.pdf
    ↓
supervised_learning_regression_classification_report.pdf
```

---

## Data

The project uses two datasets.

### 1. `energy_homes.csv`

Purpose:

```text
Regression
```

Response variable:

```text
heating_load
```

Dataset size:

```text
768 rows
12 columns
```

Each row represents a simulated residential building.

Variables include:

| Variable | Meaning |
|---|---|
| `home_id` | Building identifier |
| `relative_compactness` | Volume-to-surface-area compactness ratio |
| `surface_area` | External surface area |
| `wall_area` | Wall area |
| `roof_area` | Roof area |
| `overall_height` | Building height |
| `orientation` | Facing direction |
| `glazing_area` | Fraction of facade covered by glass |
| `glazing_distribution` | Glazing distribution code |
| `wall_insul_rating` | Wall insulation quality |
| `window_age` | Window age |
| `heating_load` | Annual heating demand |

The dataset contains no missing values.

---

### 2. `learners.csv`

Purpose:

```text
Binary Classification
```

Response variable:

```text
completed
```

Classes:

```text
no
yes
```

Dataset size:

```text
2,000 rows
18 columns
```

The dataset contains learner background, engagement, performance, subscription, and device information.

Predictor groups include:

```text
Background
- age
- prior_score
- prior_courses

Engagement
- weekly_hours
- videos_watched
- assignments_done
- forum_posts
- logins_per_week
- support_tickets

Performance
- quiz_avg

Account and timing
- days_since_signup
- signup_hour
- email_verified

Categorical context
- plan
- device
- region
```

Initial missing values:

```text
quiz_avg:          12
logins_per_week:    8
device:             5
----------------------
Total:             25
```

Numeric predictor missing values are replaced with the median.

Categorical predictor missing values are replaced with the most frequent category.

After cleaning:

```text
Missing values: 0
Rows retained:  2,000
```

---

## Reproducibility

The personalised seed is:

```r
D <- 599
set.seed(D)
```

`599` is derived from the last three digits of the student ID used for the original analysis.

The seed affects:

### Regression

- 10-fold cross-validation for Model A
- 10-fold cross-validation for Model B
- 10-fold cross-validation for polynomial orders 1 to 5
- bonus cross-validation experiment

### Classification

- stratified 80/20 train-test split
- training and test row allocation
- fitted training-set logistic model
- test-set confusion matrix
- accuracy
- sensitivity
- specificity
- ROC and AUC results
- threshold comparison
- 10-fold classification cross-validation

A different seed may produce slightly different validation and test results.

Deterministic outputs such as dataset dimensions, missing-value counts, correlations, and regression models fitted on the complete energy dataset remain unchanged.

### Path Note

The archived assignment source uses absolute local file paths from the original development environment.

After moving or renaming the project, update the two data paths in the R Markdown file before rerunning:

```r
energy_file <- "data/energy_homes.csv"
learners_file <- "data/learners.csv"
```

The knitted PDF preserves the original outputs produced from the completed analysis.

---

# Part 1 — Heating Load Regression

## Exploratory Analysis

The regression analysis begins with:

- dataset dimensions
- structure inspection
- missing-value validation
- scatterplot matrix
- correlation matrix

The strongest linear relationships with `heating_load` include:

| Predictor | Correlation with Heating Load |
|---|---:|
| `overall_height` | 0.647 |
| `relative_compactness` | -0.520 |
| `surface_area` | 0.328 |
| `wall_insul_rating` | -0.222 |

Weak relationships include:

```text
orientation: 0.009
window_age:  0.033
```

The exploratory results suggest that a one-predictor model would have relatively low variance but high bias because several building characteristics contribute to heating demand.

---

## Simple Linear Regression

A baseline model predicts `heating_load` from `relative_compactness`.

Estimated equation:

```text
Predicted heating_load
=
130.871
-
55.906 × relative_compactness
```

The slope is statistically significant:

```text
p-value ≈ 1.96e-54
```

Slope interpretation:

```text
A 0.1 increase in relative compactness
is associated with an estimated
5.591 kWh/m² decrease in annual heating demand.
```

Model performance:

```text
R²:                       0.270
Adjusted R²:              0.269
Residual Standard Error:  9.428 kWh/m²
```

The model explains approximately 27% of the variation in heating load.

It is useful as a baseline but is not strong enough for detailed building-design decisions.

---

## Regression Diagnostics

The baseline model is checked using:

- Residuals vs Fitted
- Normal Q-Q
- Scale-Location

Main interpretation:

```text
Linearity:
Not fully satisfied

Residual normality:
Broadly acceptable with tail departures

Constant variance:
Not fully satisfied
```

The diagnostic results support using the simple model as a baseline rather than a final predictive model.

---

## Polynomial Regression

Polynomial regressions of `heating_load` on `glazing_area` are compared for orders 1 to 5.

Training-fit comparison:

| Order | Adjusted R² | AIC |
|---:|---:|---:|
| 1 | 0.0207 | 5854.801 |
| 2 | 0.0579 | 5826.055 |
| 3 | 0.0567 | 5828.034 |
| 4 | 0.0567 | 5828.034 |
| 5 | 0.0567 | 5828.034 |

The order-2 polynomial is preferred because it improves model fit without adding unnecessary higher-order terms.

10-fold cross-validation confirms the same choice:

| Order | CV MSE |
|---:|---:|
| 1 | 119.4469 |
| 2 | **114.9313** |
| 3 | 115.2163 |
| 4 | 115.2163 |
| 5 | 115.2163 |

The quadratic model achieves the lowest cross-validated MSE.

---

## Multiple Regression

A full multiple regression model is fitted using all ten building-design predictors.

Predictors identified as statistically insignificant at the 5% level are:

```text
glazing_distribution
window_age
```

These variables are removed to create **Model A**.

Model A retains:

```text
relative_compactness
surface_area
wall_area
roof_area
overall_height
orientation
glazing_area
wall_insul_rating
```

---

## Interaction Model

**Model B** extends Model A by adding:

```text
wall_area : glazing_area
```

The interaction is statistically significant:

```text
Interaction coefficient: 0.050985
p-value:                 0.0035
```

Interpretation:

The estimated effect of glazing area on heating load changes depending on wall area.

The positive interaction coefficient indicates that the relationship between additional glazing and heating demand becomes stronger as wall area increases.

---

## Model A vs Model B

Training-fit comparison:

| Model | Adjusted R² | Residual Standard Error | AIC |
|---|---:|---:|---:|
| Model A | 0.912114 | 3.270040 | 4010.293 |
| Model B | **0.912983** | **3.253837** | **4003.650** |

10-fold cross-validation:

| Model | CV MSE |
|---|---:|
| Model A | 10.84055 |
| Model B | **10.75440** |

Model B is recommended.

The improvement is small, but Model B:

- has higher adjusted R²
- has lower residual standard error
- has lower AIC
- has lower cross-validated MSE
- captures a meaningful wall-area and glazing-area interaction

---

# Part 2 — Learner Completion Classification

## Data Cleaning and Class Balance

The original learner dataset contains:

```text
2,000 rows
18 columns
```

After median and mode imputation:

```text
Missing values: 0
Rows retained:  2,000
```

Completion distribution:

```text
No:  1,143 learners — 57.2%
Yes:   857 learners — 42.8%
```

The classes are reasonably balanced.

Accuracy is therefore informative, although sensitivity, specificity, and AUC are also used to evaluate class-specific and threshold-independent performance.

---

## Stratified Train-Test Split

A personalised stratified 80/20 split is created using:

```r
set.seed(599)
```

Split size:

```text
Training set: 1,599 learners
Test set:       401 learners
```

Training class counts:

```text
No:  914
Yes: 685
```

The stratified split preserves the original class distribution.

---

## Logistic Regression

A full logistic regression model is initially fitted using all available predictors except the learner identifier.

Predictors with stronger statistical evidence include:

```text
prior_score
prior_courses
weekly_hours
videos_watched
assignments_done
quiz_avg
logins_per_week
plan
device
```

Predictors with weaker statistical evidence are removed from the refined model.

The final logistic model uses:

```text
prior_score
prior_courses
weekly_hours
videos_watched
assignments_done
quiz_avg
logins_per_week
plan
device
```

---

## Odds-Ratio Interpretation

### Assignments Completed

Odds ratio:

```text
1.323
```

Holding the other model variables constant:

```text
Each additional completed assignment
is associated with approximately 32.3% higher odds
of course completion.
```

### Mobile Device

Odds ratio:

```text
0.765
```

Desktop is the reference device category.

Holding other predictors constant:

```text
Mobile-device learners have approximately 23.5% lower odds
of course completion than desktop-device learners.
```

These values describe changes in **odds**, not direct probability ratios.

---

## Test-Set Evaluation at a 0.50 Threshold

Confusion matrix:

| Actual | Predicted No | Predicted Yes |
|---|---:|---:|
| No | 184 | 45 |
| Yes | 61 | 111 |

Performance:

```text
Accuracy:     0.736
Sensitivity:  0.645
Specificity:  0.803
```

The model correctly classifies approximately 73.6% of test learners.

Sensitivity shows that approximately 64.5% of actual completers are correctly identified.

Specificity shows that approximately 80.3% of actual non-completers are correctly identified.

---

## ROC and AUC

The final logistic model achieves:

```text
AUC = 0.813
```

The ROC curve evaluates the model across probability thresholds rather than at only the default 0.50 cutoff.

An AUC of 0.813 indicates useful discrimination between learners who complete and do not complete the course.

---

## Classification Threshold Tuning

The business goal is to identify learners at risk of non-completion so that support can be prioritised.

The default threshold is:

```text
0.50
```

An alternative threshold of:

```text
0.60
```

is evaluated.

Comparison:

| Threshold | Sensitivity | Specificity |
|---:|---:|---:|
| 0.50 | 0.645 | 0.803 |
| 0.60 | 0.535 | 0.878 |

Increasing the completion threshold to 0.60:

- improves specificity
- identifies a larger proportion of actual non-completers as `no`
- reduces sensitivity
- incorrectly flags more actual completers as potential non-completers

The threshold should therefore be selected according to the operational cost of false alarms versus missed at-risk learners.

---

## 10-Fold Cross-Validated Classification Performance

The final logistic model is evaluated using 10-fold cross-validation.

Results:

```text
Cross-validated misclassification rate: 0.282
Cross-validated accuracy:               0.718
```

Single 80/20 test split:

```text
Misclassification rate: 0.264
Accuracy:               0.736
```

The two evaluations are reasonably similar.

The single split is slightly more optimistic, but the difference is not large enough to suggest an extremely lucky or unrepresentative test set.

---

# Bonus — Least Useful Predictor Experiment

The bonus experiment evaluates:

```text
window_age
```

The variable is selected because it has:

```text
Correlation with heating_load: 0.033
Regression coefficient:       -0.0024
p-value:                       0.858
```

Training comparison:

| Model | Training MSE | R² | Adjusted R² | AIC |
|---|---:|---:|---:|---:|
| Without `window_age` | 10.54253 | 0.9132390 | 0.9122089 | 4010.450 |
| With `window_age` | 10.54208 | 0.9132427 | 0.9120967 | 4012.418 |

10-fold cross-validation:

| Model | CV MSE |
|---|---:|
| Without `window_age` | **10.82843** |
| With `window_age` | 10.85146 |

Adding `window_age` slightly improves the training MSE and ordinary R².

However:

- adjusted R² becomes slightly worse
- AIC becomes worse
- cross-validated MSE becomes worse

The experiment demonstrates why a variable can slightly improve training fit without improving out-of-sample prediction.

The simpler model without `window_age` is preferred.

---

## Main Findings

### Heating Load

The strongest observed linear relationships with heating load are:

```text
overall_height:         0.647
relative_compactness:  -0.520
```

A simple compactness model explains only:

```text
27.0% of heating-load variation
```

The multiple regression interaction model performs substantially better:

```text
Adjusted R²: 0.913
CV MSE:      10.754
```

The significant wall-area and glazing-area interaction suggests that the effect of glazing depends on building wall area.

### Learner Completion

Course completion can be predicted with useful but imperfect discrimination.

Final test performance:

```text
Accuracy: 0.736
AUC:      0.813
```

One additional completed assignment is associated with:

```text
32.3% higher odds of completion
```

The model also demonstrates a clear threshold trade-off:

```text
Higher threshold
    ↓
Higher specificity
    ↓
More non-completers identified

but

Lower sensitivity
    ↓
More completers incorrectly flagged
```

The model is suitable for prioritising learner support but should not be the only basis for intervention decisions.

---

## Regression vs Classification

The two analyses use different evaluation metrics because their response variables are different.

### Regression

Response:

```text
Continuous numeric value
```

Example:

```text
heating_load = 85.4 kWh/m²
```

Appropriate metrics:

- MSE
- residual standard error
- R²
- adjusted R²
- AIC

These metrics evaluate numeric prediction error and explained variation.

### Classification

Response:

```text
Category
```

Example:

```text
completed = yes / no
```

Appropriate metrics:

- confusion matrix
- accuracy
- sensitivity
- specificity
- ROC
- AUC
- misclassification rate

These metrics evaluate class assignment and discrimination.

---

## Analytical Workflow

The project follows a practical data-science workflow:

```text
Obtain
   ↓
Load the energy and learner datasets

Scrub
   ↓
Inspect missing values
Impute learner predictors
Convert categorical variables to factors

Explore
   ↓
Scatterplot matrix
Correlation analysis
Class-balance analysis

Model
   ↓
Linear regression
Polynomial regression
Multiple regression
Interaction modelling
Logistic regression

Validate
   ↓
Regression diagnostics
80/20 stratified test split
10-fold cross-validation
ROC and AUC
Threshold comparison

Interpret
   ↓
Explain coefficients
Interpret odds ratios
Compare out-of-sample performance
Translate findings for stakeholders
```

---

## Analytical Limitations

### Heating-Load Regression

The building dataset contains simulated residential observations.

The regression diagnostic plots indicate that model assumptions are broadly acceptable but not perfect.

Some residual structure and variation in residual spread remain.

The selected model is predictive and associative; coefficients should not automatically be interpreted as causal building-design effects.

### Learner Completion Classification

The final logistic model provides useful but imperfect predictive discrimination.

At the 0.50 threshold:

```text
Accuracy:     73.6%
Sensitivity:  64.5%
Specificity:  80.3%
```

The model does not correctly classify every learner.

Threshold selection changes the balance between sensitivity and specificity.

Median and mode imputation are simple approaches and may not capture more complex missing-data mechanisms.

The model should support learner-intervention prioritisation rather than automatically determine who receives or does not receive support.

---

## Potential Extensions

Future analysis could explore:

### Regression

- regularised regression
- Ridge regression
- LASSO
- nonlinear models
- tree-based regression
- random forests
- gradient boosting
- more extensive interaction selection

### Classification

- regularised logistic regression
- decision trees
- random forests
- gradient boosting
- probability calibration
- cost-sensitive classification
- threshold optimisation using intervention cost
- precision-recall analysis
- repeated cross-validation

### Workflow

- project-relative file paths
- automated model comparison tables
- reusable evaluation functions
- parameterised R Markdown reports

---

## Author

**Phạm Minh Khôi**  
Student ID: **22145599**

COMP2025 — Introduction to Data Science  
Supervised Learning Project in R

