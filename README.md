# Pullman Sea Temple Port Douglas Online Comments analysis
Reputation analysis using Natural Language Processing tools (Text analyctics), semisupervised classification and timeseries analysis.

Analyze text content from tripavisors reviews over Pullman resort in Port Douglas, using a varity of methods.

## Check the full jupyter notebook here (Report)

http://nbviewer.jupyter.org/github/anankeman/Pullman/blob/master/Reputation%20Timeline%20Sea%20Temple.ipynb

## TLDR:

I explore the current trends of `customer experience` through online comments on TripAdvisor for Pullman Sea temple (PPD) in Port Douglas, Queensland, Australia.

By analysing the scores, I discovered:
- The [score distribution by comments](#how-scores-distribute). Most comments have a high score (5 bubbles/stars)!

However, when applying a `Time series analysis` I realised that:
- [Monthly average number of comments](#timeseries) has increased through the years, although
- [Score evolution](#score-through-time) shows a declining trend in recient years, and
- when counting the proportion of comments, I dicovered that despite most comments are still positive, negatives are growing

To undertand the customer experience and why the score are declining, I performed several `Text analysis` of the actual comments, to discover:
- By using multiple strategies I extrated [most common phases](#the-comments) to see which factors are the most important for customers, like the swimming pool, the distance to town or the staff
- Applying `vector similarity`, I build a [semi-supervised sentence classifier](#semi-supervised-classification-of-text) to group the text by its content in 5 categories: Housekeeping, Infrastructure, Restaurant, Front Desk and other. I later checked if their prevalence changed through time. Which wasn't the case.
- Also, I used full unsupervised [Topic modelling technique](#other-way-to-classify-reviews-lda) to explore more relevant topics I could miss in the first analysis.
- Then, I applied [Sentiment Analysis](#sentiment-analysis), to score how positive or negative a comment was by its content, and realised that Housekeeping has the most negative sentiment because it was higly impacted by high demand periods. 
- Finally, I validated the result with the associated score to the sentence.


## Author

- @[PippoRamos](#)

## Table of Contents

## Tech Stack

- Python 3.7
- Jupyter notebook
- Spacy
- Gensim 3.8.3
- pyVisLDA
- Pandas
- Numpy
- NLTK
- Scrapy
