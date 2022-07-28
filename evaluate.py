import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt
import prepare
import acquire
import warnings
warnings.filterwarnings('ignore')

def plot_residuals(y, yhat):
    residual = yhat-y
    plt.figure(figsize = (6,6))
    plt.scatter(y, residual)
    plt.axhline(y = 0, ls = ':')
    plt.xlabel('y')
    plt.ylabel('residual')
    plt.title('OLS model residuals')

def regression_erros(y,yhat):
    SSE = ((yhat-y)**2).sum()
    ESS = ((yhat-y.mean())**2).sum()
    TSS = ((y-y.mean()**2)).sum()
    MSE = mean_squared_error(y,yhat)
    RMSE = sqrt(MSE)
    print(f'SSE = {SSE}, ESS = {ESS}, TSS = {TSS}, MSE = {MSE}, RMSE = {RMSE}')
    
def baseline_mean_errors(y):
    baseline = y.mean()
    residual = baseline-y
    SSE = (residual**2).sum()
    MSE = SSE/y.shape[0]
    RMSE = sqrt(MSE)
    print(f'SSE = {SSE}, MSE = {MSE}, RMSE = {RMSE}')

def better_than_baseline(y,yhat):
    baseline = y.mean()
    baseline_residual = baseline-y
    residual = yhat -y
    SSE = (residual**2).sum()
    baseline_SSE = (baseline_residual**2).sum()

    if SSE < baseline_SSE:
        print('Result: model performs better than baseline model')
    else:
        print('Result: model does not perform better than baseline model')