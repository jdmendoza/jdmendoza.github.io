---
layout: post
excerpt: "Walkthrough of using linear regression to value a used iPhone"
title: Automatically Price Your Used iPhone
---

Using Data Science To Make Selling Your Phone Easy

# The Problem
Every year, Apple releases new phones and sometimes we end up purchasing one. The problem is, what do we do with our old phone? We can sell it in an online marketplace like Swappa, but pricing the phone is such a hassle. If you price it high relative to the market value, it will never sell and it collects dust in a drawer. If you price it too low, you lose out on potential profit aka beer money.

As a data scientist, I figured it would be worth a shot to attempt to solve the problem by training an algorithm for automatic valuation.

# Gathering Data
Before any algorithm could be trained, a dataset was required. I’ve had great experiences selling iPhones on the website Swappa, so I decided to use it for gathering data. I needed to get the data onto my computer, so I wrote a web-scraper in Python. Swappa only shows the five most recently sold phones for each model/carrier combo (e.g. 5 iPhone X’s that connect to ATT). For each scraped phone, I included the following features: phone model, carrier, condition, color, release price, memory size, and the recently sold price. I ran the scraper each day from Oct 3–6 to gather a dataset of 347 entries in a CSV file.

![Dataset]({{ "/assets/swappa_data.png" | absolute_url }}){:height="300px"}

*Four Rows in The Dataset of iPhones*

Note: Non-technical readers may choose to jump directly to the “Field Testing” section.

***

# Selection Of Important Features
In order to increase the performance and data efficiency of the algorithm, the data had to be processed. We needed the most critical features to remain in the dataset, and any unimportant features to be dropped. It is important to note that categorical features such as “Condition”, where the entries are “Fair”, “Good”, “Mint” or “New (Resale)”, were converted to their own column with binary entries.

Below are the two tools used to determine the correlation between the features and price.

1) **F Regression**: This performs a linear regression with each feature and determines the correlation of the feature variable and the target variable. It then calculates the F-statistic and an associated p-value. A low p-value is evidence that a feature may be important for prediction.

2) **Lasso Regression**: This is an extension of linear regression where “pressure” is applied to the weights of the linear regressor coefficients during training. This is useful in feature selection because features of low importance get coefficients of small magnitudes.

By harmoniously using these two tools, we can determine which features don’t provide us value or predictive power and can be thrown out. Once applied to the iPhone dataset, it turns out that the most important features are: iPhone model, the condition, and memory size. Once I had the data filtered, I could train up some models.

# Algorithms
Since the algorithm needed to provide numerical data, I needed to use a regression model. Additionally, I only had ~400 samples of data, so this ruled out a neural network. I decided that either a linear regression or KNN regression model were worth trying.

# Resources For Relevant Algorithms
Here are some great resources for learning about the libraries I used for implementation.

**kNN Regression**: Sci-kit Learn Documentation

**Linear Regression**: Sci-kit Learn Documentation

**Lasso Regression**  : Sci-kit Learn Documentation

An amazing technical breakdown of algorithms can be found in chapter 3 of ISL. See my Jupyter notebook for code breakdown.

# Algorithm Comparison
Before we compare performances, a note on the meaning of the relevant metrics:

**R² Score**: This quantifies the correlation between the features and the target variable. It is a number that generally falls between 0 and 1, where 0 is no correlation and 1 is a perfect correlation.

**Root Mean Square Error (RMSE)**: This measures the average “wrongness” of the predictor, that is calculated on training/test data. Wikipedia has a nice explanation.

Both of the algorithms were trained and cross-validated on the same data. Below is an image of the results.

![Comparison of Metrics]({{ "/assets/model_performance_swappa.png" | absolute_url }}){:height="300px"}

*Comparison of Metrics*

The better of the algorithm was the lasso, but only by a small margin. The Lasso is on average off by $32.64 on it’s predictions according to the gathered dataset. This seems to be pretty good. The lasso algorithm will be used moving forward.

# Model Breakdown
The great thing about linear parametric models is that we can look under the hood and see how the model values each feature. It is important to note that any features under a dummy variables label mean that they are binary inclusion. For example, an iPhone X will have a 1 in the “X” column and 0s in all other Phone Model columns.

The “iPhone 7+” and “Mint” dummy variables were dropped due to information redundancy. If all iPhone models have 0s in row, we know that the phone must be an iPhone 7+. Due to the dropped columns, the intercept can be interpreted as the average price of a Mint iPhone 7+ with an effective memory of 0. All other variables are relative to this constant.

![Field Test Data]({{ "/assets/field_test_data.png" | absolute_url }}){:height="300px"}

*Predictive Model Coefficients*

***

# Field Testing
As mentioned previously, I used data from Oct 3–6 to design and train the model. In order to test the robustness of the algorithm, I re-scraped a new dataset on Oct 10 and fed those data-points to my model. Below is a table that compares the sold price and predicted price. The percent error was computed and inserted in the right-most column. On average it is about 5% accurate, with just one outlier. Quite good!

![Model Coefficients]({{ "/assets/model_coeff_swappa.png" | absolute_url }}){:height="300px"}

*Dataset Unseen During Training/Testing*

I deployed the algorithm onto a website. See the gif below for an example of usage. The link to the page is at the bottom of this post.


# Demo!!
The deployed MPV can be accessed at the following link: https://used-iphone-valuation.herokuapp.com/

Note: the model has not been updated. For educational purposes only.

# Thank You!!
If you are interested in the code, see my GitHub!
