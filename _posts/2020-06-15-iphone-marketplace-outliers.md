---
layout: post
title: iPhone Marketplace Analysis - Outliers
excerpt:
---


While in college, I dreaded selling my books at the end of the quarter. After 10 weeks of use, I had to utilize Craigslist and Facebook to convince a stranger to buy my books. This was only after I spent time and energy obsessing over a fair price.  I’ve been out of college for sometime now, so the books I read are either free—thanks to the open source community—or in the $5 to $50 range. However, every year or two Apple announces an iPhone that I need to get my hands on. This mean I need to sell my current phone. These online markets let users sell their phones and they handle the transaction. Whenever I put up my phones, I get flashbacks of stressing in my dorm-room contemplating a fair price. The same questions run through my head. Will my ask price deter buyers or will I leave money on the table?


Perhaps I overthink it, but this process makes me wonder—are people losing money on these websites? As a side project, I have been scraping data from an iPhone resale website called Swappa. My web-scraper logs sale data into an Amazon Web Services database. The data contains model, color, condition, memory-size and sell price. The following plot shows the data over time with color representing the different models.


![Sold]({{ "/assets/sold.png" | absolute_url }}){:height="300px"}


The light blue data point up top closed with a price of $1475. Initially, I was sad for the person who paid this much for an iPhone XS Max. However, I found the archived listing and it turned out to be a two phone bundle. The buyer paid an average of $737.50 per phone, which is within 2 standard deviations of the average price for this model. The price is reasonable.  *Note: The phones are within 1 standard deviation when corrected for memory-size and condition.*


![price_stats]({{ "/assets/price_stats.png" | absolute_url }}){:height="300px"}


On the bottom of the plot there are two distinct purple dots—iPhone 7 pluses—priced at $1 and $30. I looked at the listings (below) and to my surprise, these phones were fully functional! The sellers must have made a mistake when they posted them.


![misprice_1]({{ "/assets/misprice_1.png" | absolute_url }}){:height="150px" width="550px"}

![misprice_2]({{ "/assets/misprice_2.png" | absolute_url }}){:height="200px" width="550px"}


What about less obviously mispriced phones? I searched the dataset for underpriced phones—where sale price was less than average per model minus 2 standard deviations—or overpriced—the sale was over the average plus 2 standard deviations. There were total of 361 underpriced phones and 1073 overpriced phones. The imbalance might be explained by the loss aversion cognitive bias. The seller is afraid to lose money so they tend to skew towards the higher end.


![outliers]({{ "/assets/outliers.png" | absolute_url }}){:height="300px"}


Marketplaces are unforgiving, especially for the non-experienced. Whenever a phone is listed, there is a risk of mispricing—just as we saw. Luckily, there are mathematical techniques that help remove guesswork and reduce headaches. I applied a few of these techniques to the data I collected. This model can determine a fair price for the user. You can check it out here: [phone-price-tool](phone-price-tool.herokuapp.com). Hopefully it makes it easier for people to sell their phones and give them confidence in the marketplace. As Albert Einstein said “Computers are incredible fast, accurate and stupid; humans are incredibly slow, inaccurate and brilliant; together they are power beyond imagination.”
