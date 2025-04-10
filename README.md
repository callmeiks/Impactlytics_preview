## Impactlytics Overview
**A Rigorous Causal Inference and Statistical Learning Framework for Quantifying Virality Dynamics in Short-Form Video Content**

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-research--preview-orange)

## Abstract

Impactlytics is an advanced computational framework developed to investigate the causal mechanisms and statistical patterns governing content performance on short-form video platforms. The methodology integrates experimental design principles, counterfactual inference techniques, and supervised learning algorithms to quantify the causal effects of specific content attributes on engagement metrics (views, likes, shares, completion rates).

This research addresses the methodological limitations present in current literature that predominantly relies on correlational analysis. By employing a formal causal framework and leveraging experimental data collected through official platform APIs, Impactlytics establishes a robust foundation for identifying true causal relationships between content features (linguistic characteristics, temporal factors, audiovisual elements) and performance outcomes. The framework thereby bridges the theoretical divide between behavioral science and empirical content optimization.

## Core Capabilities

- **Counterfactual Inference Framework**: Implementation of structural causal models via DoWhy and EconML for principled identification and estimation of treatment effects
- **Experimental Design & Execution**: Automated deployment of randomized controlled trials through content posting API to ensure internal validity
- **Heterogeneous Treatment Effect Estimation**: Measurement of conditional average treatment effects across dimensional subspaces (follower count, creator demographics, content categories)
- **Multimodal Feature Extraction**: Systematic extraction of linguistic sentiment vectors, temporal-contextual variables, and audiovisual characteristic embeddings
- **Ensemble Learning Architecture**: Implementation of gradient-boosted decision trees, regularized regression methods, and causal forest estimators for predictive and prescriptive analytics

## Installation Protocol

```bash
cd impactlytics

# Create isolated environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration Parameters

Create a `.env` file in the project root directory with the following authentication parameters:

```
TIKTOK_CLIENT_KEY=your_client_key
TIKTOK_CLIENT_SECRET=your_client_secret
```

## Implementation Procedures

### Authentication Protocol

```python
from impactlytics.auth.tiktok_auth import TikTokAuth
from impactlytics.api.tiktok_client import TikTokClient

# Initialize OAuth authentication process
auth = TikTokAuth()
auth.authorize()  # Initiates secure OAuth flow

# Establish API session with authorization context
client = TikTokClient(auth)
```

### Data Acquisition

```python
from impactlytics.data.collectors import TikTokDataCollector

# Instantiate data collection object
collector = TikTokDataCollector(client)

# Extract structured content data with specified cardinality constraint
videos_df = collector.collect_user_videos(limit=100)
```

### Feature Vector Construction

```python
from impactlytics.features.linguistic import LinguisticFeatureExtractor
from impactlytics.data.preprocessors import TikTokDataPreprocessor

# Initialize data transformation pipeline
preprocessor = TikTokDataPreprocessor()
clean_df = preprocessor.clean_video_data(videos_df)

# Extract linguistic feature embeddings
feature_extractor = LinguisticFeatureExtractor()
for index, row in clean_df.iterrows():
    # Calculate feature vector for textual content
    text_features = feature_extractor.extract_text_features(row['video_description'])
    # Augment dataset with derived features
    for feat_name, feat_value in text_features.items():
        clean_df.at[index, feat_name] = feat_value
```

### Experimental Protocol Implementation

```python
from impactlytics.experiments.design import ExperimentDesigner

# Define experimental parameters
designer = ExperimentDesigner(client)
exp_id = designer.create_experiment(
    name="Sentiment Polarity Analysis",
    treatment_variable="caption_sentiment",
    treatment_values=["high_positive", "neutral"],
    sample_size=20  # Minimum statistical power requirement
)

# Execute randomized controlled trial
designer.execute_experiment(exp_id)

# Collect empirical outcomes after predetermined temporal delay
results_df = collector.collect_experiment_results(
    experiment_id=exp_id,
    treatment_video_ids=designer.get_treatment_videos(exp_id),
    control_video_ids=designer.get_control_videos(exp_id),
    wait_hours=24  # Observation window
)
```

### Causal Effect Estimation

```python
from impactlytics.models.causal import CausalAnalyzer

# Initialize causal inference framework
analyzer = CausalAnalyzer()

# Prepare observational matrix with treatment and outcome variables
prepared_df = preprocessor.prepare_experiment_data(
    results_df,
    treatment_col="group",
    outcome_cols=["view_count", "like_count", "share_count"]
)

# Estimate average treatment effect with covariate adjustment
treatment_effects = analyzer.estimate_ate(
    data=prepared_df,
    treatment_col="treatment",
    outcome_col="like_count",
    covariates=["follower_count", "hour_of_day", "hashtag_count"]
)

print(f"Average Treatment Effect (ATE): {treatment_effects['ate']}")
print(f"Standard Error: {treatment_effects['std_error']}")
print(f"95% Confidence Interval: [{treatment_effects['ci_lower']}, {treatment_effects['ci_upper']}]")
```

### Predictive Modeling Framework

```python
from impactlytics.models.predictive import EngagementPredictor

# Initialize supervised learning architecture
predictor = EngagementPredictor()

# Fit parametric model to observed data
predictor.train(
    data=clean_df,
    target="engagement_rate",
    features=["sentiment_compound", "hashtag_count", "hour_of_day", "duration"],
    hyperparameters={
        "learning_rate": 0.01,
        "max_depth": 6,
        "reg_lambda": 1.0,
        "subsample": 0.8
    }
)

# Generate predictions on out-of-sample data
predictions = predictor.predict(new_data)
evaluation_metrics = predictor.evaluate(test_data)
```

## Methodological Framework

### 1. Feature Vector Representations

- **Linguistic Feature Space**: 
  - $\mathbf{L} = \{l_1, l_2, ..., l_k\}$ where components include:
    - Sentiment polarity vectors: $\vec{s} = (s_{pos}, s_{neg}, s_{neu})$
    - Emotional valence dimensions: $\vec{e} = (e_1, e_2, ..., e_m)$
    - Syntactic complexity metrics: Readability scores, n-gram distributions
  
- **Temporal-Contextual Features**:
  - $\mathbf{T} = \{t_1, t_2, ..., t_j\}$ encoding:
    - Cyclical time embeddings: $\sin(\frac{2\pi \cdot hour}{24}), \cos(\frac{2\pi \cdot hour}{24})$
    - Day-of-week indicator variables: $\mathbf{I}_{dow} \in \{0,1\}^7$
    - Posting frequency gradients: $\Delta f = \frac{df}{dt}$

- **Visual-Auditory Embeddings**:
  - $\mathbf{V} = \{v_1, v_2, ..., v_m\}$ derived from platform metadata

### 2. Experimental Design Formulation

Let $\mathcal{D}$ denote the set of experimental units with:
- Treatment assignment: $T_i \in \{0,1\}$ or $T_i \in \{t_1, t_2, ..., t_k\}$ for multi-level treatments
- Potential outcomes: $Y_i(0), Y_i(1)$ under Rubin causal model
- Covariates: $\mathbf{X}_i \in \mathbb{R}^d$

Treatment intervention protocols include:
- Sentiment modulation: $T^{sent} \in \{\text{high}, \text{neutral}\}$
- Information density variation: $T^{hashtag} \in \{0,1\}^k$ where $k$ is the hashtag count
- Temporal positioning: $T^{time} \in \{\text{morning}, \text{evening}\}$

### 3. Causal Inference Methodology

For a given treatment $T$, outcome $Y$, and covariates $\mathbf{X}$, we estimate:

- **Average Treatment Effect (ATE)**:
  $\tau_{ATE} = \mathbb{E}[Y(1) - Y(0)]$

- **Conditional Average Treatment Effect (CATE)**:
  $\tau_{CATE}(\mathbf{x}) = \mathbb{E}[Y(1) - Y(0) \mid \mathbf{X} = \mathbf{x}]$

- **Heterogeneous Treatment Effect (HTE)**:
  $\tau_{HTE}(g) = \mathbb{E}[Y(1) - Y(0) \mid G = g]$
  where $G$ represents group membership (e.g., micro vs. macro influencers)

Estimation techniques:
- Propensity score methodology: $e(\mathbf{x}) = P(T=1 \mid \mathbf{X}=\mathbf{x})$
- Inverse probability weighting:
  $\hat{\tau}_{IPW} = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{T_i Y_i}{e(\mathbf{X}_i)} - \frac{(1-T_i)Y_i}{1-e(\mathbf{X}_i)} \right)$
- Double/debiased machine learning:
  $\hat{\tau}_{DML} = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{T_i - \hat{e}(\mathbf{X}_i)}{\hat{e}(\mathbf{X}_i)(1-\hat{e}(\mathbf{X}_i))} (Y_i - \hat{m}(\mathbf{X}_i, T_i)) \right)$
  where $\hat{m}(\mathbf{X}, T)$ is the outcome model

### 4. Statistical Evaluation Framework

- **Regression Performance Metrics**:
  - Coefficient of determination: $R^2 = 1 - \frac{\sum_i (y_i - \hat{y}_i)^2}{\sum_i (y_i - \bar{y})^2}$
  - Root mean squared error: $RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$

- **Classification Evaluation**:
  - AUC-ROC curve: $AUC = \int_{0}^{1} TPR(FPR^{-1}(t)) dt$
  - Precision-recall analysis: $F_1 = 2 \cdot \frac{precision \cdot recall}{precision + recall}$

- **Causal Validation Procedures**:
  - Standardized mean difference for covariate balance:
    $SMD(X_j) = \frac{|\mu_T(X_j) - \mu_C(X_j)|}{\sqrt{\frac{\sigma^2_T(X_j)}{n_T} + \frac{\sigma^2_C(X_j)}{n_C}}}$
  - Sensitivity analysis using Rosenbaum bounds
  - Placebo tests with pseudo-treatments

## System Architecture

```
impactlytics/
├── __init__.py
├── main.py
├── config.py
├── auth/
│   ├── __init__.py
│   └── tiktok_auth.py
├── api/
│   ├── __init__.py
│   └── tiktok_client.py
├── data/
│   ├── __init__.py
│   ├── collectors.py
│   └── preprocessors.py
├── features/
│   ├── __init__.py
│   ├── linguistic.py
│   ├── temporal.py
│   └── visual_audio.py
├── models/
│   ├── __init__.py
│   ├── causal.py
│   └── predictive.py
├── experiments/
│   ├── __init__.py
│   ├── design.py
│   └── evaluation.py
└── visualization/
    ├── __init__.py
    └── plots.py
```

## Dependencies

The following computational libraries are required:

| Category | Dependencies |
|----------|-------------|
| **Core Data Science** | numpy ≥ 1.20.0, pandas ≥ 1.3.0, scipy ≥ 1.7.0 |
| **Machine Learning** | scikit-learn ≥ 1.0.0, xgboost ≥ 1.4.0 |
| **Causal Inference** | dowhy ≥ 0.8, econml ≥ 0.12.0 |
| **NLP Processing** | nltk ≥ 3.6.0, textblob ≥ 0.15.3, transformers ≥ 4.11.0 |
| **Visualization** | matplotlib ≥ 3.4.0, seaborn ≥ 0.11.0 |
| **Network & Auth** | requests ≥ 2.26.0, python-dotenv ≥ 0.19.0 |

## Research Context

This research was conducted under the auspices of:

**Institution**: University of Southern California  
**Department**: Marshall School of Business  
**Principal Investigator**: Professor Bowen Lou  
**Research Areas**: Causal Inference, Statistical Learning, Digital Media Analytics

## License

This software is distributed under the MIT License. See the accompanying LICENSE file for complete terms.

## Contributors

- Principal Developer: Lucy Qiu (lexuanqi@usc.edu)
- Faculty Advisor: Prof. Bowen Lou

## Acknowledgments

- TikTok Developer Platform for API access and technical documentation
- USC Marshall School of Business for research infrastructure and support
- The DoWhy and EconML development teams for their causal inference frameworks
