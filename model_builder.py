"""
Model Training and Evaluation Module for Boston Housing Price Prediction
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score


class RegressionModelBuilder:
    """Build and train regression models"""
    
    def __init__(self):
        self.lr_model = None
        self.ridge_model = None
        self.best_alpha = None
    
    def train_linear_regression(self, X_train, y_train):
        """Train Linear Regression model"""
        self.lr_model = LinearRegression()
        self.lr_model.fit(X_train, y_train)
        return self.lr_model
    
    def train_ridge_regression(self, X_train, y_train, alpha=1.0):
        """Train Ridge Regression model"""
        self.ridge_model = Ridge(alpha=alpha)
        self.ridge_model.fit(X_train, y_train)
        return self.ridge_model
    
    def tune_ridge_hyperparameters(self, X_train, y_train, X_test, y_test, 
                                   alpha_values=None):
        """Hyperparameter tuning for Ridge Regression"""
        if alpha_values is None:
            alpha_values = [0.001, 0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000]
        
        results = []
        for alpha in alpha_values:
            ridge = Ridge(alpha=alpha)
            ridge.fit(X_train, y_train)
            y_pred = ridge.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            results.append({'alpha': alpha, 'r2': r2, 'mse': mse})
        
        # Find best alpha
        best_result = max(results, key=lambda x: x['r2'])
        self.best_alpha = best_result['alpha']
        
        return results, self.best_alpha
    
    def predict(self, model, X):
        """Make predictions using a model"""
        return model.predict(X)
    
    def evaluate_model(self, y_true, y_pred):
        """Evaluate model performance"""
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_true, y_pred)
        
        return {
            'mse': mse,
            'rmse': rmse,
            'r2': r2
        }
    
    def get_model_coefficients(self, model, feature_names):
        """Get feature coefficients from a linear model"""
        coef_df = pd.DataFrame({
            'Feature': feature_names,
            'Coefficient': model.coef_
        }).sort_values('Coefficient', key=abs, ascending=False)
        
        return coef_df


class ModelComparator:
    """Compare multiple regression models"""
    
    @staticmethod
    def compare_models(models_dict, X_train, X_test, y_train, y_test):
        """Compare performance of multiple models"""
        comparison_results = []
        
        for model_name, model in models_dict.items():
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            train_metrics = {
                'mse': mean_squared_error(y_train, y_train_pred),
                'rmse': np.sqrt(mean_squared_error(y_train, y_train_pred)),
                'r2': r2_score(y_train, y_train_pred)
            }
            
            test_metrics = {
                'mse': mean_squared_error(y_test, y_test_pred),
                'rmse': np.sqrt(mean_squared_error(y_test, y_test_pred)),
                'r2': r2_score(y_test, y_test_pred)
            }
            
            comparison_results.append({
                'Model': model_name,
                'Train_MSE': train_metrics['mse'],
                'Train_RMSE': train_metrics['rmse'],
                'Train_R2': train_metrics['r2'],
                'Test_MSE': test_metrics['mse'],
                'Test_RMSE': test_metrics['rmse'],
                'Test_R2': test_metrics['r2']
            })
        
        return pd.DataFrame(comparison_results)
    
    @staticmethod
    def get_best_model(comparison_df, metric='Test_R2'):
        """Get the best model based on a metric"""
        best_idx = comparison_df[metric].idxmax()
        return comparison_df.loc[best_idx]
