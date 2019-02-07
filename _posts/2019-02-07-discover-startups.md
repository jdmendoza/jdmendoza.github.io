---
layout: post
title: Discovering Startups With Clustering
---

Using Clustering Methods To Discover Startups

## Introduction
For this blog post, I'd like to run through a project that showcases the usefulness of clustering. The project was to prototype a new way of discovering startup companies. Generally, searching for companies is done by filtering company data with rules such as the type of industry or funding range. However, I thought it would be interesting to tackle this problem in an exploratory manner. This type of approach could aide job seekers or investors find companies that are similar to a company they already know and love. The philosophy that differentiates this approach from most the often used method is the idea of exploration vs exploitation. 

## Exploration vs Exploitation
From an algorithmic perspective, the exploration vs exploitation tradeoff can be thought of in the context of maximizing an unknown function. Say we want to find the max value of the function. One approach is to check all the points on the curve, but this would take forever and is not practical. A different approach is to pick a random point on the function then travel in the direction of increasing function values. If we alternate these two steps, we can find various candidate points, choose the best one and search a little more around that point. This may not always find the optimal maximum but in practice, it does pretty well. As a side note, an application of this process is called bayesian optimization and it is great way to tune your supervised machine learning algorithms.

Here is an analogy to think about this method. Imagine you are a beer drinker who wants to find a beer that maximizes tastiness. Let's say you randomly tried Keystone for your first beer. It's not very flavorful, but it's not that disgusting. Should you try something in the same family of beers such as Coors (exploitation), or do I go with an exploratory approach and try a Lagunitas IPA?

The most common search engine for startups is CrunchBase and they use a purely exploitative method of searching. The software uses hard-coded rules to determine what startups will be shown to the user. Here is a video with the [search in action](https://www.youtube.com/watch?v=HsJBoMbsV-M). The recommendation engine that I prototyped performs an explorative approach by grouping the companies.

## Clustering
In order to group the various startups, I used a method of unsupervised machine learning known as clustering. Unsupervised means that a human does not tell the algorithm which group the data points belong too. These algorithms find patterns in the data points and lump them together. *Show and example ere* The specific clustering algorithm I used was [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) with [k-means ** initialization](https://en.wikipedia.org/wiki/K-means%2B%2B).


## Data
The data for this project can be found online [here](https://www.dropbox.com/s/brtuewlpskwk07l/crunchbase_monthly_export_d43b4klo2ade53.xlsx?dl=0). It is CrunchBase data from 2004 to 2014. This data set was filtered to only show startups in the San Francisco Bay Area. The relevant features with a short description are as follows:

## Raw Features
- **company_name:** Name of the company
- **company_market:** The market the company 
- **company_city:** The location of the start
- **company_category_list:** Relevant categories that CrunchBase uses
- **total_funding:** Total amount of funding raised
- **company_max_round:** The total number of rounds the company has had

## Feature Engineered
- **investor_rating:** Value from 0–10 based on the rankings of the investors 


## Natural Language Processing
The features, *company_category_list* and  *company_market* in the dataset are categorical features. These cannot be handled by the clustering algorithm, so they have to preprocessed. Usually, categorical features can be converted into dummy variables, where all categories become columns names with 0 or 1 entries, but in this case the feature space would explode. Instead, I use natural language processing techniques to convert the categories into numerical vectors. I used the technique, Term Frequency - Inverse Document Frequency (TF-IDF), which converts each word into a numerical vector that the clustering algorithms can understand. Another benefit of using TF-IDF is that highly occurring words are given less importance. Words like “software” may not give a good idea of the work that a startup does, TF-IDF allows other keywords in the dataset to better describe the company.

## Clustering Pipeline
![Block Diagram]({{ "/assets/startup_recommender_diagram.png" | absolute_url }}){:height="300px"}
Above is a block diagram visualization of the data pipeline.

Note: the Market data is not implemented in the public version of the project. Still optimizing the cluster number.

## Dashboard
Once the startups were clustered, I used Plotly along with Dash to create a website that displays a dashboard. The site asks for a startup name to be input and the cluster that the company belongs to is shown on the page with several graphs and metrics. See the demo below.

## Demo
Dashboard in Action

![Dashboard](https://media.giphy.com/media/2wU7GtEEBXaM3JS97p/giphy.gif)

## Future Updates
I’m working on deploying the application to the web. Meanwhile, feel free to clone my git repo and run it locally.
