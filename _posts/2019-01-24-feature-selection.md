# Feature Selection Blog Post


Feature selection is a critical step in applying machine learning to data problems. In feature selection, the data scientist determines the subset of data that contains the most predictive signal. Feature selection is crucial for various reasons, which include:
- **Numerical Stability**: Some models such as linear regression are not stable when features are collinear.
- [**Curse of Dimensionality**](https://en.wikipedia.org/wiki/Curse_of_dimensionality): As the number of features increases, the distance between data points increases. This makes it challenging for models to determine boundaries. The need for more data increases drastically.
- **Redundancy**: Highly correlated features are measuring the same underlying information.

There are many techniques that should be in a data scientists tool belt. In this post, I’ll share some techniques that I came across while reading the amazing books: [Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) and [Applied Predictive Modeling](http://appliedpredictivemodeling.com/toc/).

## Table of Contents

The topics covered in this blog post are:
- Model Metrics
- Optimal Subset Selection
- Forward Stepwise Selection
- Backward Stepwise Selection
- Heuristic with Correlation
- Lasso Regression

## Model Metrics
During model selection we need metrics to compare modes. Below are commonly used metrics in regression analysis. See [this page](https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers) for metrics used with classification problems.

- [**Cross-validated prediction error**](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) - This is a method to get an estimation of the out-of-sample performance of a model. This is used in conjunction with the metrics below.
- [**Residual Sum of Squares (RSS)**](https://en.wikipedia.org/wiki/Residual_sum_of_squares) - This metric is calculated by squaring and adding errors in predictions.
- [**Akaike Information Criterion (AIC) and Cp**](https://en.wikipedia.org/wiki/Akaike_information_criterion) - A penalized RSS metric that takes into account error variance and number of predictors.
- [**Bayesian Information Criterion (BIC)**](https://en.wikipedia.org/wiki/Bayesian_information_criterion) - Similar to AIC, but places a heavier penalty on models with more features.
- [**R-squared (R^2)**](https://en.wikipedia.org/wiki/Coefficient_of_determination) - This is the explained variance by a model. It ranges from zero to one. Where one is a model that explains all the variance in a data set.
- [**Adjusted R^2**](https://en.wikipedia.org/wiki/Coefficient_of_determination) - This uses the R-squared metric, but penalized models with a larger number of features.

## Optimal Subset Selection

Just like most computer science problems, the ideal approach to feature selection is to use brute force. Given enough computing power, a brute force approach can solve many problems. Assuming p predictors, there are 2^p combinations of features that need to be tested. If a model has a small number of features and samples, bruce force can be used.

***Algorithm 1: Optimal Subset Selection***

	1. Let Mo denote the null model, which contains no predictors. This model simply predicts the sample mean for each observation.

	2. For k=1,2...p:
		a) Fit all p choose k models that contain exactly k predictors.
		b) Pick the best among these p choose k models, and call it Mk. Here the best is defined as having the smallest RSS, or equivalently largest R^2.

	3. Select a single best model from among the Mo...Mp using cross-validated prediction error, Cp (AIC), BIC, or adjusted R^2

	Source 1

Most of the time, we cannot bruce force search the entire space of feature combinations, so we have to make a trade off in the algorithms. This is where forward and back subset selection come in.

## Forward Stepwise Selection
In forward subset selection, we apply a greedy optimization approach by selecting the best model at each iteration. This allows us to search a smaller subset of the feature space. In total, there are 1 + p(p+2)/2 combinations of features that need to be trained and tested.

***Algorithm 2: Forward Stepwise Selection***

	1. Let Mo denote the null model, which contains no predictors.

	2. For k=0,...,p-1:
		a) Consider all p-k models that augment the predicts in Mk with one additional predictor.
		b) Choose the best among these p-k models, and call it Mk+1. Here best is defined as having smallest RSS or highest R^2.

	3. Select a single best model from among Mo,...,Mp using cross-validated prediction error, Cp (AIC), BIC, or adjusted R^2

	Source 1

## Backward Stepwise Selection
Backward subset selection, is the inverse of FSS algorithm. We begin with a full model and incrementally remove features. The number of feature combinations is 1 + p(p+2)/2, just like FSS.

***Algorithm 3: Backward Stepwise Selection***

	1. Let Mo denote the full model, which contains all p predictors.

	2. For k=p,p-1,...1:
		a) Consider all k models that augment the contains all but one of the predictors in Mk, for a total of k-1 predictors.
		b) Choose the best among these k models, and call it Mk+1. Here best is defined as having smallest RSS or highest R^2.

	3. Select a single best model from among Mo,...,Mp using cross-validated prediction error, Cp (AIC), BIC, or adjusted R^2

	Source 1

## Correlation Heuristic
This algorithm is based on the heuristic that features that are highly correlated measure the same underlying information. The data scientist chooses an absolute correlation threshold, the correlation matrix is generated and highly correlated pairwise features are tested to be thrown out.

***Algorithm 4: Heuristic with Correlation***

	1. Calculate the correlation matrix of the features

	2. Determine the two predictors associated with the largest absolute pairwise correlation (call them predictors A and B).

	3. Determine the average correlation between A and the other variables, do the same for predictor B

	4. If A has a larger average correlation, remove it; otherwise, remove predictor B

	5. Repeat Steps 2-4 until no absolute correlations are above the threshold

	Source 2

## Lasso Regression
If we take the traditional linear regression algorithm and apply an L1 norm to the coefficient vector, we get lasso regression. In other words, an extra term is added to the linear regression cost function that penalizes the model if coefficients get to big. This has the effect of applying pressure on the coefficients, so they stay near the origin. Lasso regression will reduce the weight of a feature to zero if it has no predictive signal, effectively selecting the important features.

![L1 Norm]({{ "/assets/l1_norm.png" | absolute_url }}){:height="150px"}

The L1 norm is applied with a tuning variable to control the flexibility of the model. This tuning parameter requires experimentation by the data scientist to find the optimal value to maximize cross-validated prediction error, Cp (AIC), BIC, or adjusted R^2.


## Conclusion
Feature selection is a very important part in applying machine learning to problems. Hopefully, this blog post added another technique to your tool belt. If you have a technique that you really love and would like to share it in the comments.

## References
Source 1: [Introduction To Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)

Source 2: [Applied Predictive Modeling](http://appliedpredictivemodeling.com/toc/)
