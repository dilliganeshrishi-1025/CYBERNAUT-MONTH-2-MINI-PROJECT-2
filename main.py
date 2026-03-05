#!/usr/bin/env python
"""
Main script for Boston Housing Price Prediction
Run this file to execute the complete analysis
"""

import pandas as pd
import numpy as np
from src.data_loader import BostonHousingDataLoader
from src.model_builder import RegressionModelBuilder, ModelComparator
from src.visualizer import ModelVisualizer
from src.config import RIDGE_ALPHA_VALUES


def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 80)
    print(title.center(80))
    print("=" * 80 + "\n")

# Set UTF-8 encoding for output
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    """Main execution function"""
    
    print_header("BOSTON HOUSING PRICE PREDICTION")
    print("Machine Learning Regression Analysis")
    
    # Step 1: Load and preprocess data
    print_header("Step 1: Data Loading and Preprocessing")
    loader = BostonHousingDataLoader()
    X_train, X_test, y_train, y_test, X_clean, y_clean = loader.preprocess()
    
    print(f"[OK] Dataset loaded successfully")
    print(f"  - Total samples: {len(X_clean)}")
    print(f"  - Number of features: {X_train.shape[1]}")
    print(f"  - Training set: {len(X_train)} samples (80%)")
    print(f"  - Testing set: {len(X_test)} samples (20%)")
    
    # Step 2: Train Linear Regression
    print_header("Step 2: Linear Regression Model")
    builder = RegressionModelBuilder()
    lr_model = builder.train_linear_regression(X_train, y_train)
    
    y_train_pred_lr = builder.predict(lr_model, X_train)
    y_test_pred_lr = builder.predict(lr_model, X_test)
    
    lr_train_metrics = builder.evaluate_model(y_train, y_train_pred_lr)
    lr_test_metrics = builder.evaluate_model(y_test, y_test_pred_lr)
    
    print(f"[OK] Linear Regression trained successfully")
    print(f"  Training Metrics:")
    print(f"    - R2 Score: {lr_train_metrics['r2']:.4f}")
    print(f"    - RMSE: {lr_train_metrics['rmse']:.4f}")
    print(f"  Testing Metrics:")
    print(f"    - R2 Score: {lr_test_metrics['r2']:.4f}")
    print(f"    - RMSE: {lr_test_metrics['rmse']:.4f}")
    
    # Step 3: Hyperparameter tuning for Ridge Regression
    print_header("Step 3: Ridge Regression - Hyperparameter Tuning")
    ridge_results, best_alpha = builder.tune_ridge_hyperparameters(
        X_train, y_train, X_test, y_test, alpha_values=RIDGE_ALPHA_VALUES
    )
    
    print(f"[OK] Hyperparameter tuning completed")
    print(f"  - Best Alpha: {best_alpha}")
    best_result = [r for r in ridge_results if r['alpha'] == best_alpha][0]
    print(f"  - Best Test R2: {best_result['r2']:.4f}")
    print(f"  - Best Test MSE: {best_result['mse']:.4f}")
    
    # Step 4: Train Ridge Regression with best alpha
    print_header("Step 4: Ridge Regression Model (Optimized)")
    ridge_model = builder.train_ridge_regression(X_train, y_train, alpha=best_alpha)
    
    y_train_pred_ridge = builder.predict(ridge_model, X_train)
    y_test_pred_ridge = builder.predict(ridge_model, X_test)
    
    ridge_train_metrics = builder.evaluate_model(y_train, y_train_pred_ridge)
    ridge_test_metrics = builder.evaluate_model(y_test, y_test_pred_ridge)
    
    print(f"[OK] Ridge Regression trained with a={best_alpha}")
    print(f"  Training Metrics:")
    print(f"    - R2 Score: {ridge_train_metrics['r2']:.4f}")
    print(f"    - RMSE: {ridge_train_metrics['rmse']:.4f}")
    print(f"  Testing Metrics:")
    print(f"    - R2 Score: {ridge_test_metrics['r2']:.4f}")
    print(f"    - RMSE: {ridge_test_metrics['rmse']:.4f}")
    
    # Step 5: Model comparison
    print_header("Step 5: Model Comparison")
    models_dict = {
        'Linear Regression': lr_model,
        'Ridge Regression': ridge_model
    }
    comparison_df = ModelComparator.compare_models(
        models_dict, X_train, X_test, y_train, y_test
    )
    
    
    print(comparison_df.to_string(index=False))
    
    best_model = ModelComparator.get_best_model(comparison_df, metric='Test_R2')
    print(f"\n[OK] Best Model: {best_model['Model']}")
    print(f"  - Test R2: {best_model['Test_R2']:.4f}")
    print(f"  - Test RMSE: {best_model['Test_RMSE']:.4f}")
    
    # Step 6: Feature analysis
    print_header("Step 6: Feature Importance Analysis")
    correlation_data = pd.concat([X_clean, y_clean], axis=1)
    target_correlation = correlation_data.corr()['PRICE'].sort_values(ascending=False)
    
    print("Top 5 Features (Positive Correlation):")
    for i, (feature, corr) in enumerate(target_correlation[1:6].items(), 1):
        print(f"  {i}. {feature:8} : {corr:+.4f}")
    
    print("\nTop 5 Features (Negative Correlation):")
    for i, (feature, corr) in enumerate(reversed(list(target_correlation[-5:].items())), 1):
        print(f"  {i}. {feature:8} : {corr:+.4f}")
    
    print_header("[OK] ANALYSIS COMPLETE!")
    print("All models have been trained and evaluated.")
    print("Check the notebook for visualizations and detailed analysis.")
    
    return {
        'loader': loader,
        'lr_model': lr_model,
        'ridge_model': ridge_model,
        'best_alpha': best_alpha,
        'comparison_df': comparison_df,
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'y_train_pred_lr': y_train_pred_lr,
        'y_test_pred_lr': y_test_pred_lr,
        'y_train_pred_ridge': y_train_pred_ridge,
        'y_test_pred_ridge': y_test_pred_ridge
    }


if __name__ == "__main__":
    results = main()
    print("\nYou can now access the results through the 'results' variable:")
    print("  - results['lr_model']: Trained Linear Regression model")
    print("  - results['ridge_model']: Trained Ridge Regression model")
    print("  - results['comparison_df']: Model comparison dataframe")
    print("  - results['X_test'], results['y_test']: Test data")
    print("  - results['y_test_pred_lr'], results['y_test_pred_ridge']: Predictions")
