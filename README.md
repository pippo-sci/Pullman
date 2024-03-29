![GitHub](https://img.shields.io/github/license/pippo-sci/Pullman)

# Pullman Sea Temple Port Douglas Online Comments analysis

## Table of Contents

- [General Description](#general-description)
- [Author](#author)
- [TLDR](#TLDR:)
- [Business Problem](#business-problem)
- [Tech Stack](#tech-stack)
- [Run locally](#run-locally)
- [Key findings](#key-findings)

## General description

Reputation analysis using Natural Language Processing tools (Text analyctics), semisupervised classification and timeseries analysis.

Analyse text content from tripavisors reviews over Pullman resort in Port Douglas, using a varity of methods.

[Check the full jupyter notebook here (Report)](http://nbviewer.jupyter.org/github/anankeman/Pullman/blob/master/Reputation%20Timeline%20Sea%20Temple.ipynb)


## TLDR:

I explore the current trends of `customer experience` through online comments on TripAdvisor for Pullman Sea temple (PPD) in Port Douglas, Queensland, Australia.

By analysing the scores, I discovered:
- The [score distribution by comments](#how-scores-distribute). Most comments have a high score (5 bubbles/stars)!

![users_score](images/post_numb_by_score_bar.png)

However, when applying a `Time series analysis` I realised that:
1. [Monthly average number of comments](#timeseries) has increased through the years, although
2. [Score evolution](#score-through-time) shows a declining trend in recent years, and
3. when counting the proportion of comments, I discovered that despite most comments are still positive, negatives are more predominant
4. When checking the absolute values we see negative comments remaining the same but there are fewer new positive comments

![avg_month_score](images/monthly_avg_score.png)
![Prop_avg_score](images/proportion_post_by_score_v_time.png)
![Abs_avg_score](images/abs_numb_post_by_score_v_time.png)

To understand the customer experience and why the score is declining, I performed several `Text analysis` of the actual comments, to discover:
1. By using multiple strategies I extracted [most common phases](#the-comments) to see which factors are the most important for customers, like the swimming pool, the distance to town or the staff
2. Applying `vector similarity`, I build a [semi-supervised sentence classifier](#semi-supervised-classification-of-text) to group the text by its content in 5 categories: Housekeeping, Infrastructure, Restaurant, Front Desk and others. I later checked if their prevalence changed over time. Which wasn't the case: All 5 topics are relevant all the time.

![semi-supervised topics](images/Dist_sent_score_by_topic.png)

3. Also, I used full unsupervised [Topic modelling technique](#other-way-to-classify-reviews-lda) to explore more relevant topics I could miss in the first analysis.
This analysis showed again that distance to town the swimming pool and the staff, specially from front desk, were the most important, but also: 
    - The restaurant and room service
    - Most rooms are fully equipped apartments with clean and spacious rooms with kitchen and laundry
    - The latest is important for families with kids, it is likely the main type of customer
    - Also the hotel configuration and the different types of buildings
    - Atmosphere: luxury and tropical
    - Other surrounding attractions like the Daintree and the Coral Reef

![unsupervised_topics](images/Dist_sent_score_by_selected_lda_topic.png)
    
4. Then, I applied [Sentiment Analysis](#sentiment-analysis), to score how positive or negative a comment was by its content, and realised that Housekeeping has the least positive sentiment. While the Front desk was mostly positive.

![Sentiment_score](images/avg_sent_score_by_topic_v_time.png)

5. Finally, I used [Signal Decomposition](#seasonal-decomposition) over the sentiment score through time:
    - Seasonality creates pressure over both Food and beverage and Housekeeping areas.
    - Environmental and infrastructure factors may need renewal as its novelty use decay over time, as shown by its declining trend.
    - Because rooms are functional apartments with independent access, some rooms are privately owned and rented through other media such AirBnB. And those may not include services from the hotel management and may have separate housekeeping and other services. Those can impact the comments score as more and more rooms are being sold to private owners.

![Sentiment_score](images/signal_decomp_frontdesk.png)
![Sentiment_score](images/signal_decomp_housekeep.png)

## Author
- @[PippoRamos](https://github.com/pippo-sci)

## Business Problem

Pullman Sea temple Resort constantly check online reviews to improve service. However, it is difficult to have a systematical view of the text content of such reviews, specially to compare evolution and trends.


## Tech Stack
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

- Python 3.8
- Jupyter notebook
- Spacy
- Gensim 3.8.3
- pyVisLDA
- Pandas
- Numpy
- NLTK
- Scklearn
- Scrapy

## Run locally

### Repository structure

* [.ipynb_checkpoints/](.\Pullman\.ipynb_checkpoints)
* [tripullman/](.\Pullman\tripullman)
  * [.ipynb_checkpoints/](.\Pullman\tripullman\.ipynb_checkpoints)
  * [tripullman/](.\Pullman\tripullman\tripullman)
    * [spiders/](.\Pullman\tripullman\tripullman\spiders)
      * [__pycache__/](.\Pullman\tripullman\tripullman\spiders\__pycache__)
      * [pull.py](.\Pullman\tripullman\tripullman\spiders\pull.py)
      * [__init__.py](.\Pullman\tripullman\tripullman\spiders\__init__.py)
    * [__pycache__/](.\Pullman\tripullman\tripullman\__pycache__)
    * [items.py](.\Pullman\tripullman\tripullman\items.py)
    * [middlewares.py](.\Pullman\tripullman\tripullman\middlewares.py)
    * [pipelines.py](.\Pullman\tripullman\tripullman\pipelines.py)
    * [settings.py](.\Pullman\tripullman\tripullman\settings.py)
    * [__init__.py](.\Pullman\tripullman\tripullman\__init__.py)
  * [scrapy.cfg](.\Pullman\tripullman\scrapy.cfg)
  * [test.csv](.\Pullman\tripullman\test.csv)
* [README.md](.\Pullman\README.md)
* [Reputation Timeline Sea Temple.ipynb](#)
* [requirements.txt](.\Pullman\requirements.txt)


### Install requirements
```
pip install requirements.txt
```
### Run Scrapy script

to run scrapy script go to /tripullman and run
```
scrapy crawl pull -o test.csv
```
### Run Report (Jupyter Notebook)

Open the file using VSCODE and jupyter notebook plugin OR 

alternative open the terminal in the main folder and run

```
jupyter notebook
```


