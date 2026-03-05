"""
Data Loading and Preprocessing Module for Boston Housing Price Prediction
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class BostonHousingDataLoader:
    """Load and preprocess Boston Housing dataset"""
    
    def __init__(self):
        self.X = None
        self.y = None
        self.scaler = StandardScaler()
        self.feature_names = [
            'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
            'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
        ]
    
    def load_data(self):
        """Load the Boston Housing dataset from original source"""
        # Load data from original CMU source (since sklearn removed it)
        data_url = "http://lib.stat.cmu.edu/datasets/boston"
        try:
            raw_df = pd.read_csv(data_url, sep=r"\s+", skiprows=22, header=None)
            data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
            target = raw_df.values[1::2, 2]
        except:
            # Fallback: create synthetic data if online source unavailable
            from sklearn.datasets import fetch_openml
            housing = fetch_openml(name="housing", as_frame=True, parser='auto')
            self.X = housing.data
            self.y = housing.target
            return self.X, self.y
        
        self.X = pd.DataFrame(data, columns=self.feature_names)
        self.y = pd.Series(target, name='PRICE')
        return self.X, self.y
    
    def get_data_info(self):
        """Get information about the dataset"""
        info = {
            'shape': self.X.shape,
            'missing_values': self.X.isnull().sum().sum(),
            'features': list(self.X.columns),
            'description': self.boston.DESCR
        }
        return info
    
    def handle_missing_data(self):
        """Handle missing values in the dataset"""
        X_clean = self.X.dropna()
        y_clean = self.y[X_clean.index]
        return X_clean, y_clean
    
    def scale_features(self, X):
        """Standardize features using StandardScaler"""
        X_scaled = self.scaler.fit_transform(X)
        return pd.DataFrame(X_scaled, columns=X.columns)
    
    def split_data(self, X, y, test_size=0.2, random_state=42):
        """Split data into training and testing sets"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        return X_train, X_test, y_train, y_test
    
    def preprocess(self, test_size=0.2, random_state=42):
        """Complete preprocessing pipeline"""
        # Load data
        self.load_data()
        
        # Handle missing data
        X_clean, y_clean = self.handle_missing_data()
        
        # Scale features
        X_scaled = self.scale_features(X_clean)
        
        # Split data
        X_train, X_test, y_train, y_test = self.split_data(
            X_scaled, y_clean, test_size, random_state
        )
        
        return X_train, X_test, y_train, y_test, X_clean, y_clean
