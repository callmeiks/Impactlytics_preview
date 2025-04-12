## Impactlytics Overview
**A Rigorous Causal Inference and Statistical Learning Framework for Quantifying Virality Dynamics in Short-Form Video Content**

**(This repository is a research preview and not intended for production use)**

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
