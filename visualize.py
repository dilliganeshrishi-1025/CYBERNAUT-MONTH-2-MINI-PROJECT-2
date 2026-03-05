#!/usr/bin/env python
"""
Visualization Script for Boston Housing Price Prediction
Generates bar charts, graphs, and plots for model analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import BostonHousingDataLoader
from src.model_builder import RegressionModelBuilder, ModelComparator
from src.config import RIDGE_ALPHA_VALUES

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

def plot_feature_importance():
    """Create bar chart of feature importance (correlation with price)"""
    # Load data
    loader = BostonHousingDataLoader()
    X, y = loader.load_data()
    X_clean, y_clean = loader.handle_missing_data()
    
    # Calculate correlations
    data = pd.concat([X_clean, y_clean], axis=1)
    correlations = data.corr()['PRICE'].drop('PRICE').sort_values()
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(12, 7))
    colors = ['red' if x < 0 else 'green' for x in correlations.values]
    bars = ax.barh(correlations.index, correlations.values, color=colors, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Correlation with Price', fontsize=13, fontweight='bold')
    ax.set_title('Feature Importance - Correlation with Housing Prices', fontsize=15, fontweight='bold', pad=20)
    ax.axvline(x=0, color='black', linestyle='-', linewidth=1)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for i, (idx, val) in enumerate(correlations.items()):
        ax.text(val + 0.02 if val > 0 else val - 0.02, i, f'{val:.3f}', 
                va='center', ha='left' if val > 0 else 'right', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('feature_importance_chart.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved: feature_importance_chart.png")
    plt.show()


def plot_model_comparison():
    """Create comparison bar charts for models"""
    # Load and preprocess data
    loader = BostonHousingDataLoader()
    X_train, X_test, y_train, y_test, _, _ = loader.preprocess()
    
    # Train models
    builder = RegressionModelBuilder()
    lr_model = builder.train_linear_regression(X_train, y_train)
    ridge_results, best_alpha = builder.tune_ridge_hyperparameters(X_train, y_train, X_test, y_test)
    ridge_model = builder.train_ridge_regression(X_train, y_train, alpha=best_alpha)
    
    # Compare models
    models_dict = {'Linear Regression': lr_model, 'Ridge Regression': ridge_model}
    comparison_df = ModelComparator.compare_models(models_dict, X_train, X_test, y_train, y_test)
    
    # Create comparison charts
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Model Performance Comparison', fontsize=16, fontweight='bold', y=1.00)
    
    # 1. Training R2 Comparison
    ax = axes[0, 0]
    x = np.arange(len(comparison_df))
    width = 0.35
    bars1 = ax.bar(x - width/2, comparison_df['Train_R2'], width, label='Train R2', color='skyblue', edgecolor='black')
    bars2 = ax.bar(x + width/2, comparison_df['Test_R2'], width, label='Test R2', color='coral', edgecolor='black')
    ax.set_ylabel('R2 Score', fontsize=11, fontweight='bold')
    ax.set_title('R2 Score Comparison', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(comparison_df['Model'])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}', ha='center', va='bottom', fontsize=9)
    
    # 2. RMSE Comparison
    ax = axes[0, 1]
    bars1 = ax.bar(x - width/2, comparison_df['Train_RMSE'], width, label='Train RMSE', color='lightgreen', edgecolor='black')
    bars2 = ax.bar(x + width/2, comparison_df['Test_RMSE'], width, label='Test RMSE', color='salmon', edgecolor='black')
    ax.set_ylabel('RMSE', fontsize=11, fontweight='bold')
    ax.set_title('RMSE Comparison', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(comparison_df['Model'])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}', ha='center', va='bottom', fontsize=9)
    
    # 3. MSE Comparison
    ax = axes[1, 0]
    bars1 = ax.bar(x - width/2, comparison_df['Train_MSE'], width, label='Train MSE', color='lightyellow', edgecolor='black')
    bars2 = ax.bar(x + width/2, comparison_df['Test_MSE'], width, label='Test MSE', color='gold', edgecolor='black')
    ax.set_ylabel('MSE', fontsize=11, fontweight='bold')
    ax.set_title('MSE Comparison', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(comparison_df['Model'])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}', ha='center', va='bottom', fontsize=9)
    
    # 4. Test Metrics Summary
    ax = axes[1, 1]
    ax.axis('off')
    
    summary_text = f"""
    BEST MODEL: {comparison_df.loc[comparison_df['Test_R2'].idxmax(), 'Model']}
    
    LINEAR REGRESSION:
    - Test R2: {comparison_df.loc[0, 'Test_R2']:.4f}
    - Test RMSE: {comparison_df.loc[0, 'Test_RMSE']:.4f}
    - Test MSE: {comparison_df.loc[0, 'Test_MSE']:.4f}
    
    RIDGE REGRESSION (a={best_alpha}):
    - Test R2: {comparison_df.loc[1, 'Test_R2']:.4f}
    - Test RMSE: {comparison_df.loc[1, 'Test_RMSE']:.4f}
    - Test MSE: {comparison_df.loc[1, 'Test_MSE']:.4f}
    
    Difference:
    - R2 Diff: {comparison_df.loc[1, 'Test_R2'] - comparison_df.loc[0, 'Test_R2']:+.4f}
    - RMSE Diff: {comparison_df.loc[1, 'Test_RMSE'] - comparison_df.loc[0, 'Test_RMSE']:+.4f}
    """
    
    ax.text(0.1, 0.5, summary_text, fontsize=11, verticalalignment='center',
            family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('model_comparison_chart.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved: model_comparison_chart.png")
    plt.show()


def plot_alpha_tuning():
    """Create line chart showing Ridge alpha tuning results"""
    # Load and preprocess data
    loader = BostonHousingDataLoader()
    X_train, X_test, y_train, y_test, _, _ = loader.preprocess()
    
    # Tune Ridge
    builder = RegressionModelBuilder()
    ridge_results, best_alpha = builder.tune_ridge_hyperparameters(X_train, y_train, X_test, y_test)
    
    # Prepare data
    alphas = [r['alpha'] for r in ridge_results]
    r2_scores = [r['r2'] for r in ridge_results]
    mse_scores = [r['mse'] for r in ridge_results]
    
    # Create line chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # R2 Score vs Alpha
    ax1.semilogx(alphas, r2_scores, marker='o', markersize=10, linewidth=2.5, color='blue', markerfacecolor='lightblue', markeredgecolor='darkblue')
    ax1.axvline(x=best_alpha, color='red', linestyle='--', linewidth=2, label=f'Best Alpha: {best_alpha}')
    ax1.scatter([best_alpha], [max(r2_scores)], color='red', s=200, zorder=5, edgecolors='darkred', linewidths=2)
    ax1.set_xlabel('Alpha (Log Scale)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('R2 Score', fontsize=12, fontweight='bold')
    ax1.set_title('Ridge Regression - Alpha Tuning (R2 Score)', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.legend(fontsize=11)
    
    # MSE vs Alpha
    ax2.loglog(alphas, mse_scores, marker='s', markersize=10, linewidth=2.5, color='green', markerfacecolor='lightgreen', markeredgecolor='darkgreen')
    ax2.axvline(x=best_alpha, color='red', linestyle='--', linewidth=2, label=f'Best Alpha: {best_alpha}')
    ax2.scatter([best_alpha], [min(mse_scores)], color='red', s=200, zorder=5, edgecolors='darkred', linewidths=2)
    ax2.set_xlabel('Alpha (Log Scale)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('MSE (Log Scale)', fontsize=12, fontweight='bold')
    ax2.set_title('Ridge Regression - Alpha Tuning (MSE)', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, linestyle='--', which='both')
    ax2.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('alpha_tuning_chart.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved: alpha_tuning_chart.png")
    plt.show()


def plot_predictions_comparison():
    """Create scatter plots comparing predictions vs actual values"""
    # Load and preprocess data
    loader = BostonHousingDataLoader()
    X_train, X_test, y_train, y_test, _, _ = loader.preprocess()
    
    # Train models
    builder = RegressionModelBuilder()
    lr_model = builder.train_linear_regression(X_train, y_train)
    ridge_results, best_alpha = builder.tune_ridge_hyperparameters(X_train, y_train, X_test, y_test)
    ridge_model = builder.train_ridge_regression(X_train, y_train, alpha=best_alpha)
    
    # Make predictions
    y_pred_lr = lr_model.predict(X_test)
    y_pred_ridge = ridge_model.predict(X_test)
    
    # Calculate metrics
    from sklearn.metrics import r2_score, mean_squared_error
    lr_r2 = r2_score(y_test, y_pred_lr)
    ridge_r2 = r2_score(y_test, y_pred_ridge)
    lr_rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr))
    ridge_rmse = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
    
    # Create scatter plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Linear Regression
    ax = axes[0]
    ax.scatter(y_test, y_pred_lr, alpha=0.6, s=100, color='blue', edgecolors='darkblue', linewidth=1.5)
    min_val = min(y_test.min(), y_pred_lr.min())
    max_val = max(y_test.max(), y_pred_lr.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2.5, label='Perfect Prediction')
    ax.set_xlabel('Actual Prices', fontsize=12, fontweight='bold')
    ax.set_ylabel('Predicted Prices', fontsize=12, fontweight='bold')
    ax.set_title(f'Linear Regression (R2={lr_r2:.4f}, RMSE={lr_rmse:.4f})', fontsize=13, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3, linestyle='--')
    
    # Ridge Regression
    ax = axes[1]
    ax.scatter(y_test, y_pred_ridge, alpha=0.6, s=100, color='green', edgecolors='darkgreen', linewidth=1.5)
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2.5, label='Perfect Prediction')
    ax.set_xlabel('Actual Prices', fontsize=12, fontweight='bold')
    ax.set_ylabel('Predicted Prices', fontsize=12, fontweight='bold')
    ax.set_title(f'Ridge Regression (R2={ridge_r2:.4f}, RMSE={ridge_rmse:.4f})', fontsize=13, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('predictions_comparison_chart.png', dpi=300, bbox_inches='tight')
    print("[OK] Saved: predictions_comparison_chart.png")
    plt.show()


def main():
    """Run all visualizations"""
    print("\n" + "=" * 80)
    print("BOSTON HOUSING - VISUALIZATION GENERATION".center(80))
    print("=" * 80 + "\n")
    
    print("[1] Generating Feature Importance Chart...")
    plot_feature_importance()
    
    print("\n[2] Generating Model Comparison Charts...")
    plot_model_comparison()
    
    print("\n[3] Generating Alpha Tuning Charts...")
    plot_alpha_tuning()
    
    print("\n[4] Generating Predictions Comparison Charts...")
    plot_predictions_comparison()
    
    print("\n" + "=" * 80)
    print("[OK] ALL VISUALIZATIONS COMPLETE!".center(80))
    print("=" * 80)
    print("\nGenerated files:")
    print("  - feature_importance_chart.png")
    print("  - model_comparison_chart.png")
    print("  - alpha_tuning_chart.png")
    print("  - predictions_comparison_chart.png")
    print("\n")


if __name__ == "__main__":
    main()
