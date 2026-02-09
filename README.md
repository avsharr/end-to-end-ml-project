# End-to-End ML Project — Student Performance

Machine learning project for predicting student math scores based on demographic data and results in reading and writing.

## Description

The Students Performance dataset contains information about students:
- **Features:** gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading and writing scores
- **Target variable:** math score

## Project Structure

```
end-to-end-ml-project-1/
├── notebook/              # Jupyter notebooks
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb   # Exploratory data analysis
│   └── 2. MODEL TRAINING.ipynb               # Model training
├── src/
│   ├── components/
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py # Preprocessing (numerical + categorical)
│   │   └── model_trainer.py      # Model training
│   ├── pipeline/
│   │   ├── train_pipeline.py      # Full training pipeline
│   │   └── predict_pipeline.py   # Prediction pipeline
│   ├── utils.py                  # Utilities (save_object, load_object)
│   ├── logger.py
│   └── exceptions.py
├── artifacts/              # Processing outputs
│   ├── train_data.csv
│   ├── test_data.csv
│   ├── raw_data.csv
│   └── preprocessor.pkl
├── StudentsPerformance.csv # Raw data
├── requirements.txt
└── setup.py
```

## Installation

```bash
# Clone the repository and navigate to the project folder
cd end-to-end-ml-project-1

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or: .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

### 1. Data Ingestion — loading and splitting data

Reads `StudentsPerformance.csv`, splits into train/test (80/20), and saves to `artifacts/`:

```bash
python src/components/data_ingestion.py
```

### 2. Data Transformation — preprocessing

Applies numerical and categorical transformations, saves the preprocessor:

```bash
python src/components/data_transformation.py
```

> Make sure to run Data Ingestion first (`artifacts/train_data.csv` and `artifacts/test_data.csv` must exist).

## Technologies

- **Python 3**
- **pandas** — data manipulation
- **scikit-learn** — preprocessing, models, train_test_split
- **dill** — object serialization (preprocessor, models)
- **numpy** — arrays

## Contact

Author: Anastasiia  
Email: aasharovaa@gmail.com
