## 📊 Mathematical Framework
- The Impactlytics platform is grounded in **experimental design**, **causal inference**, and **machine learning**. The objective is to estimate the **causal effect** of video-level treatment conditions on TikTok engagement outcomes using anonymized, real-world data.
---
## 1. Notation and Setup
Let:
- $i \in \{1, 2, ..., N\}$: Index over TikTok videos or content units
- $X_i \in \mathbb{R}^d$: Covariate vector for the user or content metadata
- $T_i \in \{0, 1\}$: Binary treatment indicator (e.g., caption with sentiment vs. neutral)
- $Y_i \in \mathbb{R}$: Observed engagement outcome (e.g., number of views, likes, shares)
- $Y_i(1), Y_i(0)$: Potential outcomes under treatment and control
- We assume the **Rubin Causal Model** (Potential Outcomes Framework), where each unit has two potential outcomes but only one is observed.
---
## 2. Causal Estimation Objectives
### 2.1 Average Treatment Effect (ATE)
$$
\text{ATE} = \mathbb{E}[Y(1) - Y(0)]
$$

- Estimated by comparing average outcomes between treatment and control groups, adjusting for confounders.
---
### 2.2 Conditional Average Treatment Effect (CATE)
$$
\text{CATE}(x) = \mathbb{E}[Y(1) - Y(0) \mid X = x]
$$

Estimated using methods such as:
- T-Learner / S-Learner / X-Learner
- Causal forests
- Doubly Robust Estimators
---
## 3. Propensity Score Estimation
We estimate the **propensity score** $e(X_i)$ as:
$$
e(X_i) = \mathbb{P}(T_i = 1 \mid X_i)
$$

Used for:
- Inverse Propensity Weighting (IPW)
- Covariate balancing
- Matching and stratification
---
## 4. Experimental Design
Treatments are randomly assigned through TikTok Content Posting API with constraints to maintain ethical limits.
Each content experiment is represented as a tuple:
$$
(u_i, v_i, T_i, t_i)
$$

Where:
- $u_i$: user account (anonymized)
- $v_i$: content variant
- $T_i$: treatment indicator
- $t_i$: posting time

We ensure **covariate balance** using standardized mean differences (SMD):
$$
\text{SMD}_j = \frac{|\mu_T(X_j) - \mu_C(X_j)|}{\sqrt{ \frac{1}{2} (\sigma_T^2(X_j) + \sigma_C^2(X_j)) }} < 0.1
$$
---
## 5. Outcome Modeling
We model $Y_i$ using supervised learning (when necessary) for outcome prediction, using:
- Linear/Logistic regression
- XGBoost
- Random Forests
- Neural networks (for multi-modal signals)
- These models are used within meta-learning architectures (e.g., X-Learner) or for predictive diagnostics.
---
## 6. Uplift Modeling (Optional)
We may use **uplift models** to estimate treatment effect heterogeneity:
$$
U(x) = f_1(x) - f_0(x)
$$

Where:
- $f_1(x)$: predicted outcome under treatment
- $f_0(x)$: predicted outcome under control

Used for identifying segments where treatment (e.g., sentiment change) has the greatest marginal effect.

---
## 7. Evaluation Metrics
- **Treatment effect quality**:
  - Precision in Estimation of Heterogeneous Effects (PEHE)
  - ATE bias
  - SMD diagnostics
- **Model performance**:
  - RMSE, MAE for regression
  - AUC-ROC, Precision-Recall for classification
- **Causal graph diagnostics** (optional): if using DoWhy + DAG structure
---
## 8. Tools and Libraries
- `DoWhy`: Causal graph modeling and estimators  
- `EconML`: Meta-learners, doubly robust methods  
- `scikit-learn`, `xgboost`: Machine learning models  
- `pandas`, `numpy`, `statsmodels`: Data manipulation and inference  
- `TikTok API`: Content deployment and metric acquisition