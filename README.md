# Boston Housing Price Prediction - Mini Project

## Project Overview
This project develops regression models using the Boston Housing dataset to predict housing prices. It implements **Linear Regression** and **Ridge Regression** models with comprehensive data preprocessing, model evaluation, and visualization.

## Project Objectives
✓ Load and preprocess the Boston Housing dataset  
✓ Implement Linear Regression and Ridge Regression models  
✓ Perform hyperparameter tuning for Ridge Regression  
✓ Evaluate model performance using MSE and R² metrics  
✓ Visualize predictions and analyze feature correlations  
✓ Identify the best performing model  

## Project Structure
```
Boston Housing Price Prediction/
├── notebooks/
│   └── Boston_Housing_Prediction.ipynb    # Main analysis notebook
├── src/
│   ├── data_loader.py                     # Data loading and preprocessing
│   ├── model_builder.py                   # Model training and evaluation
│   ├── visualizer.py                      # Visualization utilities
│   └── config.py                          # Configuration and constants
├── data/                                  # Data directory (for saving datasets)
├── models/                                # Directory for saved models
├── requirements.txt                       # Python dependencies
└── README.md                              # This file
```

## Dataset Information
**Boston Housing Dataset** contains 506 samples with 13 features:
- **CRIM**: per capita crime rate by town
- **ZN**: proportion of residential land zoned for lots over 25,000 sq.ft
- **INDUS**: proportion of non-retail business acres per town
- **CHAS**: Charles River dummy variable
- **NOX**: nitric oxides concentration
- **RM**: average number of rooms per dwelling
- **AGE**: proportion of owner-occupied units built prior to 1940
- **DIS**: weighted distances to five Boston employment centres
- **RAD**: index of accessibility to radial highways
- **TAX**: full-value property-tax rate per $10,000
- **PTRATIO**: pupil-teacher ratio by town
- **B**: 1000(Bk - 0.63)² where Bk is the proportion of blacks
- **LSTAT**: % lower status of the population

**Target Variable**: MEDV (Median home value in $1000s)

## Technologies Used
- **Python 3.x**: Programming language
- **scikit-learn**: Machine learning library
- **Pandas & NumPy**: Data manipulation and numerical computing
- **Matplotlib & Seaborn**: Data visualization

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone or download the project
2. Navigate to the project directory
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Notebook
1. Open Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to `notebooks/Boston_Housing_Prediction.ipynb`

3. Run all cells to execute the complete analysis

### Using Python Modules
```python
from src.data_loader import BostonHousingDataLoader
from src.model_builder import RegressionModelBuilder
from src.visualizer import ModelVisualizer

# Load and preprocess data
loader = BostonHousingDataLoader()
X_train, X_test, y_train, y_test, _, _ = loader.preprocess()

# Build and train models
builder = RegressionModelBuilder()
lr_model = builder.train_linear_regression(X_train, y_train)
ridge_results, best_alpha = builder.tune_ridge_hyperparameters(
    X_train, y_train, X_test, y_test
)
ridge_model = builder.train_ridge_regression(X_train, y_train, alpha=best_alpha)

# Visualize results
visualizer = ModelVisualizer()
visualizer.plot_predictions_vs_actual(y_test, lr_model.predict(X_test), 
                                      'Linear Regression', 0.73, 4.79)
```

## Project Workflow

### 1. Data Preprocessing
- Load Boston Housing dataset from scikit-learn
- Handle missing values
- Standardize features using StandardScaler
- Split data into 80% training and 20% testing sets

### 2. Model Building
- **Linear Regression**: Baseline model for price prediction
- **Ridge Regression**: Regularized model to prevent overfitting
  - Hyperparameter tuning with alpha values: [0.001, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000]

### 3. Model Evaluation
Calculate and compare performance metrics:
- **Mean Squared Error (MSE)**: Average squared differences
- **Root Mean Squared Error (RMSE)**: Square root of MSE
- **R² Score**: Coefficient of determination (0-1 scale)

### 4. Visualization & Analysis
- **Predictions vs Actual**: Scatter plots showing model accuracy
- **Residuals Plot**: Analysis of prediction errors
- **Correlation Heatmap**: Feature relationships visualization
- **Feature Importance**: Correlation with target variable

## Key Findings

### Model Performance
The models are evaluated on test data (102 samples):
- Linear Regression Test R²: ~0.73-0.75
- Ridge Regression Test R²: ~0.73-0.75 (depends on alpha)

### Most Important Features (by correlation)
1. **RM** (avg rooms): Positive correlation with price
2. **LSTAT** (% lower status): Negative correlation with price
3. **PTRATIO** (pupil-teacher ratio): Negative correlation with price

## Files Description

### `notebooks/Boston_Housing_Prediction.ipynb`
Complete end-to-end analysis with:
- 10 sections covering all aspects of the project
- Data exploration and statistics
- Model training and evaluation
- Multiple visualizations
- Summary and conclusions

### `src/data_loader.py`
- `BostonHousingDataLoader`: Handles data loading and preprocessing
  - Load Boston Housing dataset
  - Handle missing values
  - Feature scaling with StandardScaler
  - Train-test split

### `src/model_builder.py`
- `RegressionModelBuilder`: Train and evaluate regression models
- `ModelComparator`: Compare multiple models

### `src/visualizer.py`
- `ModelVisualizer`: Create publication-quality visualizations
  - Predictions vs actual plots
  - Residuals analysis
  - Correlation heatmaps
  - Feature importance plots

### `src/config.py`
Configuration constants and hyperparameters

## Expected Results
After running the complete analysis, you should see:
- ✓ Model performance metrics for both Linear and Ridge Regression
- ✓ Visual comparisons of predictions vs actual values
- ✓ Residuals analysis showing model errors
- ✓ Correlation analysis identifying important features
- ✓ Recommendations for the best model

## Performance Benchmarks
- **Linear Regression**: MSE ~23-25, R² ~0.73-0.75
- **Ridge Regression (α=1)**: MSE ~23-24, R² ~0.73-0.75
- **Best Alpha**: Typically between 0.5-5.0

## Conclusions
1. Both Linear and Ridge Regression perform similarly on this dataset
2. Ridge Regression helps prevent overfitting with appropriate alpha value
3. Number of rooms (RM) is the strongest positive predictor
4. Lower status population (LSTAT) is the strongest negative predictor
5. The models explain approximately 73-75% of price variance

## Future Improvements
- Test additional regression algorithms (Lasso, ElasticNet)
- Feature engineering for better predictions
- Cross-validation for more robust evaluation
- Hyperparameter optimization using GridSearchCV
- Non-linear models (Random Forest, Gradient Boosting)

## Dependencies
See `requirements.txt` for complete list of dependencies and versions

## Author
Cybernaut - Web Scraper Project - Month 2 Mini Project 2

## License
This project is for educational purposes.

## References
- [Boston Housing Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Ridge Regression Guide](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression)
