<img width="1250" alt="title" src="https://user-images.githubusercontent.com/105242871/184062759-713501ca-9afb-48cf-9082-814f94f0582d.png">


## 🟣 Class Demos & Resources
In this module, we will analyze, visualize and model various labeled datasets that are being stored in SQL and have continuous target variables. This means we will do supervised machine learning (because the data is labeled) using regression (because the target variable we are analyzing is continuous) on structured data (because the data can be naturally stored in rows and columns).
### 1️⃣ Acquisition and Preparation
#### 🔸 Acquisition
- **Acquire** structured data from SQL to Pandas

- **Summarize** the data through aggregates, descriptive stats and distribution plots (histograms, density plots, boxplots, etc.).
#### 🔸 Preparation
- **Clean** the data by converting datatypes and handle missing values. (pandas: `.isnull`, `.value_counts`, `.dropna`, `.replace`)

- **Split** our observations into 3 samples, Train, Validate, and Test. (`sklearn.model_selection.train_test_split`).

  [Wrangle](wrangle_lesson.ipynb)

### 2️⃣ Scaling Numeric Data
- **Scale** our numeric data so that all variables are on the same scale, such as between 0 and 1. We will discuss the importance of "scaling", different methods for scaling data, and why to use one type over another. (sklearn.preprocessing: `StandardScaler`, `QuantileTransformer`, `PowerTransformer`, `RobustScaler`, `MinMaxScaler`)

  [Scaling](scaling_lesson.ipynb)

### 3️⃣ Exploration
- **Hypothesize**: We will discuss the meaning of "drivers", variables vs. features, and the target variable. We will discuss the importance of documenting questions and hypotheses, obtaining answers for those questions, and documenting takeaways and findings at each step of exploration.

- **Visualize** the interaction of variables, especially independent variables with the dependent variable using charts such as scatterplots, jointplots, pairgrids, and heatmaps to identify drivers.

- **Test Hypotheses** that involve a continuous variable using t-tests and correlation tests.

  [Exploration](exploration_lesson.ipynb)

### 4️⃣ Evaluating Regression Models
- **Residuals**: The residual of an observed value is the difference between the observed value and the estimated value. Another way to state this is that it is the vertical distance from the original data point to the expected data point (which shares an x and sits on the regression line).

- **SSE**: Sometime the **Sum of the Squared Errors** (SSE, a.k.a RSS, Residual Sum of Squares) will be used as the final metric to evaluate. Most times, however, this is used as a stepping stone to the other metrics, such as MSE and RMSE. If outliers matter, this is a good metric to use.

- **MSE**: We can use the SSE to compute the **Mean Squared Error**, MSE. We arrive at this by dividing your SSE by the total number of data points, i.e. the average of your errors that have each been squared. If outliers don't matter as much, but cost exponential instead of linear, then this is a good metric to use. That means that a residual of 10 (the expected value is 10 units off the actual value) is greater than twice a residual of 5.

- **RMSE**: We can use the MSE to compute the **Root Mean Squared Error**, RMSE. Simply take the square root of the MSE. If you want to see the error in the actual units of the y variable, then this is a good metric to use. In this case, the units will be grade points.

  [Evaluation](regression_evaluation_lesson.ipynb)

### 5️⃣ Feature Engineering
- We will learn ways to identify, select, and create features through feature importance. We will discuss the "Curse of Dimensionality." (`sklearn.feature_selection.f_regression`).

  [Feature Engineering](feature_engineering_lesson.ipynb)

### 6️⃣ Modeling
- **Establish Baseline**: We will learn about the importance of establishing a "baseline model" or baseline score and ways to complete this task. The baseline for regression is often computed by predicting each observation's value to be the mean or median of the dependent variable.

- **Build Models**: We will build linear regression models. What does that mean? We will extract the patterns in the data using well established algorithms, so that we don't have to do that manually. An example of a regression algorithm is the glm (generalized linear model). The algorithm will return to us a mathematical model or function (e.g. y = 3x + 2). That function will be used to compute predictions for each observation. We will learn about the differences in the most common regression algorithms. (sklearn.linear_model)

- **Model Evaluation**: We will compare regression models by computing evaluation metrics, i.e. metrics that measure how well a model did at predicting the target variable. (statsmodels.formula.api.ols, sklearn.metrics, math.sqrt)

- **Model Selection and Testing**: We will learn how to select a model, and we will test the model on the unseen data sample (the out-of-sample data in the validate and then test datasets).

  [Modeling](modeling_lesson.ipynb)

***
## 🟣 Exercises
### 1️⃣ Acquisition and Preparation
[Wrangle](wrangle.ipynb)

[Wrangle Functions](wrangle.py)

[Acquisition](acquire.py)

[Preparation](prepare.py)

### 2️⃣ Scaling Numeric Data
[Scaling](scaling.ipynb)

### 3️⃣ Exploration
[Exploration](explore.ipynb)

[Explore Functions](explore.py)

### 4️⃣ Evaluating Regression Models
[Evaluation](evaluate.ipynb)

[Evaluate Functions](evaluate.py)

### 5️⃣ Feature Engineering
[Feature Engineering](feature_engineering.ipynb)

### 6️⃣ Modeling
[Modeling](modeling.ipynb)
