"""
Visualization Module for Boston Housing Price Prediction
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score


class ModelVisualizer:
    """Create visualizations for model analysis"""
    
    @staticmethod
    def plot_predictions_vs_actual(y_true, y_pred, model_name, r2_score_val, rmse):
        """Plot predicted vs actual values"""
        plt.figure(figsize=(8, 6))
        plt.scatter(y_true, y_pred, alpha=0.6, edgecolors='k')
        plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 
                'r--', lw=2, label='Perfect Prediction')
        plt.xlabel('Actual Prices', fontsize=12, fontweight='bold')
        plt.ylabel('Predicted Prices', fontsize=12, fontweight='bold')
        plt.title(f'{model_name}\nR² = {r2_score_val:.4f}, RMSE = {rmse:.4f}', 
                 fontsize=12, fontweight='bold')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        return plt
    
    @staticmethod
    def plot_residuals(y_true, y_pred, model_name):
        """Plot residuals"""
        residuals = y_true - y_pred
        plt.figure(figsize=(8, 6))
        plt.scatter(y_pred, residuals, alpha=0.6, edgecolors='k')
        plt.axhline(y=0, color='r', linestyle='--', lw=2)
        plt.xlabel('Predicted Prices', fontsize=12, fontweight='bold')
        plt.ylabel('Residuals', fontsize=12, fontweight='bold')
        plt.title(f'{model_name} - Residuals Plot', fontsize=12, fontweight='bold')
        plt.grid(alpha=0.3)
        plt.tight_layout()
        return plt
    
    @staticmethod
    def plot_correlation_heatmap(corr_matrix):
        """Plot correlation heatmap"""
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                   square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
        plt.title('Boston Housing Dataset - Correlation Heatmap', 
                 fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        return plt
    
    @staticmethod
    def plot_feature_correlation(target_correlation):
        """Plot feature correlation with target"""
        plt.figure(figsize=(10, 8))
        colors = ['green' if x > 0 else 'red' for x in target_correlation[:-1].values]
        plt.barh(target_correlation[:-1].index, target_correlation[:-1].values, 
                color=colors, edgecolor='black')
        plt.xlabel('Correlation with Price', fontsize=12, fontweight='bold')
        plt.title('Feature Correlation with Housing Prices', 
                 fontsize=14, fontweight='bold')
        plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        return plt
    
    @staticmethod
    def plot_alpha_tuning(alpha_results):
        """Plot Ridge alpha tuning results"""
        alphas = [r['alpha'] for r in alpha_results]
        r2_scores = [r['r2'] for r in alpha_results]
        
        plt.figure(figsize=(10, 6))
        plt.semilogx(alphas, r2_scores, marker='o', markersize=8, linewidth=2)
        plt.xlabel('Alpha (Regularization Parameter)', fontsize=12, fontweight='bold')
        plt.ylabel('R² Score', fontsize=12, fontweight='bold')
        plt.title('Ridge Regression - Alpha Tuning', fontsize=14, fontweight='bold')
        plt.grid(alpha=0.3)
        plt.tight_layout()
        return plt
    
    @staticmethod
    def plot_model_comparison(comparison_df):
        """Plot model comparison"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # R² comparison
        comparison_df.set_index('Model')[['Train R²', 'Test R²']].plot(kind='bar', ax=ax1)
        ax1.set_title('Model Comparison - R² Scores', fontsize=12, fontweight='bold')
        ax1.set_ylabel('R² Score', fontsize=11)
        ax1.grid(alpha=0.3, axis='y')
        ax1.legend(loc='lower right')
        
        # RMSE comparison
        comparison_df.set_index('Model')[['Train RMSE', 'Test RMSE']].plot(kind='bar', ax=ax2)
        ax2.set_title('Model Comparison - RMSE', fontsize=12, fontweight='bold')
        ax2.set_ylabel('RMSE', fontsize=11)
        ax2.grid(alpha=0.3, axis='y')
        ax2.legend(loc='upper right')
        
        plt.tight_layout()
        return plt
