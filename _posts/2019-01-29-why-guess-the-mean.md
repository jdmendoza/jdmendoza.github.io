---
layout: post
title: Why Guess The Mean?
---

In this short blog post, I will show mathematically why the mean of a random variable is an optimal guess for the value it will take on.
To make this rigorous, we define "optimal guess" as a value b that has a minimum distance to a random variable X. 

We need to minimize the difference between X and b, or minimize (X - b) with respect to b.
This is equivalent to minimizing (X - b)². X is a random variable, so we need to apply the expected value function for this to make sense.

So we have, E(X - b)² which is expanded out to E(X² - 2bX + b²)

The expected value E is a linear operator, so we can write, 
E(X)² - 2bE(X) + b² and since E(X) = u  the mean, 

u² - 2bu + b or (u - b)²

We can use the derivative to find the inflection point of the function. The derivative of (u-b)² = 0, which by using the chain rule is, 
-2(u - b) = 0 or b = u


The mean u is an inflection point but we still need to determine if this is a minimum. To determine this, we need to check the second derivative, which is f''(b) = 2. Since this is larger than 0, we know that this point is a minimum. 


Thus, the mean u is the constant which has a minimum distance to the random variable X.
So there we go, the mean is the best guess for the value a random variable will take on.
