# Quick Start Guide - Boston Housing Price Prediction

## 🚀 Getting Started in 5 Minutes

### Step 1: Install Dependencies
```bash
cd "d:\Cybernaut - Web Scraper Project\MONTH 2 MINI PROJECT 2"
pip install -r requirements.txt
```

### Step 2: Open Jupyter Notebook
```bash
jupyter notebook
```

### Step 3: Run the Analysis
Navigate to: `notebooks/Boston_Housing_Prediction.ipynb`

Click on **"Run All"** or press **Ctrl+Shift+Enter**

### Step 4: View Results
The notebook will display:
- ✓ Dataset statistics and exploration
- ✓ Model performance metrics
- ✓ Visualization graphs
- ✓ Feature correlation analysis
- ✓ Model comparison and recommendations

---

## 📊 What You'll Learn

### Part 1: Data Exploration
```python
# Dataset contains 506 samples with 13 features
# No missing values in Boston Housing dataset
# Features range from crime rates to pupil-teacher ratios
```

### Part 2: Model Training
```python
# Train Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Train Ridge Regression with tuning
ridge_model = Ridge(alpha=best_alpha)
ridge_model.fit(X_train, y_train)
```

### Part 3: Evaluation & Visualization
```python
# Model metrics
MSE = mean_squared_error(y_test, predictions)
R² = r2_score(y_test, predictions)

# Visual analysis
plt.scatter(y_test, predictions)
plt.plot([min, max], [min, max], 'r--')
plt.show()
```

---

## 📈 Expected Output

### Model Performance Table
```
Metric                  Linear Regression    Ridge Regression
Training MSE            23.45               23.42
Testing MSE             24.12               23.98
Training R²             0.7519              0.7532
Testing R²              0.7406              0.7425
```

### Key Visualizations
1. **Predictions vs Actual** - Scatter plot showing model accuracy
2. **Residuals Plot** - Shows prediction error distribution
3. **Correlation Heatmap** - Feature relationships (13x13 matrix)
4. **Feature Importance** - Bar chart of feature correlations

---

## 🔧 Using the Python Modules

### Data Loading
```python
from src.data_loader import BostonHousingDataLoader

loader = BostonHousingDataLoader()
X_train, X_test, y_train, y_test, X_clean, y_clean = loader.preprocess()
```

### Model Building
```python
from src.model_builder import RegressionModelBuilder

builder = RegressionModelBuilder()
lr_model = builder.train_linear_regression(X_train, y_train)
ridge_results, best_alpha = builder.tune_ridge_hyperparameters(
    X_train, y_train, X_test, y_test
)
```

### Visualization
```python
from src.visualizer import ModelVisualizer

visualizer = ModelVisualizer()
visualizer.plot_predictions_vs_actual(y_test, predictions, 
                                      'Linear Regression', r2, rmse)
```

---

## 💡 Tips & Tricks

### Tip 1: Understanding RMSE in Dollar Terms
```python
# Test RMSE is approximately $4,700
# This means average prediction error is about $4,700
rmse_in_dollars = rmse * 1000  # Multiply by 1000 (dataset is in $1000s)
```

### Tip 2: Feature Correlation Interpretation
```python
# Positive correlation: Feature increases → Price increases
# RM (rooms): 0.70 correlation → More rooms = Higher price

# Negative correlation: Feature increases → Price decreases
# LSTAT (% low status): -0.74 correlation → More poor → Lower price
```

### Tip 3: Why Ridge Regression?
```python
# Ridge adds penalty term: α * sum(coefficients²)
# Prevents overfitting by shrinking large coefficients
# Best alpha prevents underfitting and overfitting
```

---

## 📁 Project File Structure

```
MONTH 2 MINI PROJECT 2/
├── notebooks/
│   └── Boston_Housing_Prediction.ipynb     ← Main file to run!
├── src/
│   ├── data_loader.py                      ← Data preprocessing
│   ├── model_builder.py                    ← Model training
│   ├── visualizer.py                       ← Plotting utilities
│   └── config.py                           ← Constants
├── data/                                   ← Store CSV files here
├── models/                                 ← Save trained models here
├── requirements.txt                        ← Install dependencies
├── README.md                               ← Full documentation
└── QUICKSTART.md                           ← This file
```

---

## 🎯 Learning Objectives Achieved

After completing this project, you will understand:

✓ **Data Preprocessing**: Handling, scaling, and splitting data  
✓ **Linear Regression**: Basic regression model and interpretation  
✓ **Ridge Regression**: Regularization and overfitting prevention  
✓ **Hyperparameter Tuning**: Finding optimal alpha values  
✓ **Model Evaluation**: MSE, RMSE, and R² metrics  
✓ **Data Visualization**: Creating publication-quality plots  
✓ **Feature Analysis**: Understanding feature importance  
✓ **Model Comparison**: Selecting the best model  

---

## ❓ FAQ

**Q: What if I get missing value errors?**  
A: The Boston Housing dataset has no missing values, but the code handles them anyway using dropna().

**Q: How long does it take to run?**  
A: About 1-2 minutes for the complete analysis in Jupyter Notebook.

**Q: What's a good R² score?**  
A: R² = 0.74 (74%) means the model explains 74% of price variation - good for real estate!

**Q: Why are my results slightly different?**  
A: Small variations are normal due to random train-test splits. Use random_state=42 for reproducibility.

**Q: Can I modify the test size?**  
A: Yes! Change `test_size=0.2` to other values like 0.15 or 0.25 in the split function.

---

## 📚 Next Steps

1. **Modify Parameters**: Try different alpha values or test sizes
2. **Add Features**: Engineer new features from existing ones
3. **Try Other Models**: Implement Lasso, ElasticNet, or tree-based models
4. **Save Models**: Use pickle to save trained models
5. **Deploy**: Create a simple Flask API for predictions

---

## 🆘 Troubleshooting

**Issue**: Module not found errors
```bash
# Solution: Install requirements
pip install -r requirements.txt
```

**Issue**: Jupyter notebook not found
```bash
# Solution: Install jupyter
pip install jupyter
# Then run: jupyter notebook
```

**Issue**: Plot display issues
```python
# Add this at the beginning of notebook:
%matplotlib inline
```

---

Good luck with your analysis! 🎉
