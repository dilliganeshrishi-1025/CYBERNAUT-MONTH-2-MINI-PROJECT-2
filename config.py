"""
Configuration and Constants for Boston Housing Price Prediction Project
"""

# Data Configuration
TRAIN_TEST_SPLIT_RATIO = 0.2
RANDOM_STATE = 42

# Ridge Regression Configuration
RIDGE_ALPHA_VALUES = [0.001, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000]
DEFAULT_RIDGE_ALPHA = 1.0

# Visualization Configuration
FIGURE_SIZE_STANDARD = (12, 6)
FIGURE_SIZE_LARGE = (14, 10)
FIGURE_SIZE_HEATMAP = (12, 10)

# Color Configuration
COLOR_LINEAR = 'blue'
COLOR_RIDGE = 'green'
COLOR_POSITIVE = 'green'
COLOR_NEGATIVE = 'red'

# Feature Names (for reference)
BOSTON_FEATURES = [
    'CRIM',    # per capita crime rate by town
    'ZN',      # proportion of residential land zoned for lots over 25,000 sq.ft
    'INDUS',   # proportion of non-retail business acres per town
    'CHAS',    # Charles River dummy variable
    'NOX',     # nitric oxides concentration
    'RM',      # average number of rooms per dwelling
    'AGE',     # proportion of owner-occupied units built prior to 1940
    'DIS',     # weighted distances to five Boston employment centres
    'RAD',     # index of accessibility to radial highways
    'TAX',     # full-value property-tax rate per $10,000
    'PTRATIO', # pupil-teacher ratio by town
    'B',       # 1000(Bk - 0.63)^2 where Bk is the proportion of blacks
    'LSTAT'    # % lower status of the population
]

# Performance Metrics Names
METRICS = {
    'MSE': 'Mean Squared Error',
    'RMSE': 'Root Mean Squared Error',
    'R2': 'R-squared Score'
}

# Model Names
MODELS = {
    'LINEAR': 'Linear Regression',
    'RIDGE': 'Ridge Regression'
}
