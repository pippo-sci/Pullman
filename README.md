/github/license/:user/:repo

# Pullman Sea Temple Port Douglas Online Comments analysis
Reputation analysis using Natural Language Processing tools (Text analyctics), semisupervised classification and timeseries analysis.

Analyse text content from tripavisors reviews over Pullman resort in Port Douglas, using a varity of methods.

[Check the full jupyter notebook here (Report)](http://nbviewer.jupyter.org/github/anankeman/Pullman/blob/master/Reputation%20Timeline%20Sea%20Temple.ipynb)


## TLDR:


I explore the current trends of `customer experience` through online comments on TripAdvisor for Pullman Sea temple (PPD) in Port Douglas, Queensland, Australia.

By analysing the scores, I discovered:
- The [score distribution by comments](#how-scores-distribute). Most comments have a high score (5 bubbles/stars)!

However, when applying a `Time series analysis` I realised that:
1. [Monthly average number of comments](#timeseries) has increased through the years, although
2. [Score evolution](#score-through-time) shows a declining trend in recent years, and
3. when counting the proportion of comments, I discovered that despite most comments are still positive, negatives are more predominant
4. When checking the absolute values we see negative comments remaining the same but there are fewer new positive comments

To understand the customer experience and why the score is declining, I performed several `Text analysis` of the actual comments, to discover:
1. By using multiple strategies I extracted [most common phases](#the-comments) to see which factors are the most important for customers, like the swimming pool, the distance to town or the staff
2. Applying `vector similarity`, I build a [semi-supervised sentence classifier](#semi-supervised-classification-of-text) to group the text by its content in 5 categories: Housekeeping, Infrastructure, Restaurant, Front Desk and others. I later checked if their prevalence changed over time. Which wasn't the case: All 5 topics are relevant all the time.
3. Also, I used full unsupervised [Topic modelling technique](#other-way-to-classify-reviews-lda) to explore more relevant topics I could miss in the first analysis.
This analysis showed again that distance to town the swimming pool and the staff, specially from front desk, were the most important, but also: 
    - The restaurant and room service
    - Most rooms are fully equipped apartments with clean and spacious rooms with kitchen and laundry
    - The latest is important for families with kids, it is likely the main type of customer
    - Also the hotel configuration and the different types of buildings
    - Atmosphere: luxury and tropical
    - Other surrounding attractions like the Daintree and the Coral Reef
    
4. Then, I applied [Sentiment Analysis](#sentiment-analysis), to score how positive or negative a comment was by its content, and realised that Housekeeping has the least positive sentiment. While the Front desk was mostly positive.
5. Finally, I used [Signal Decomposition](#seasonal-decomposition) over the sentiment score through time:
    - Seasonality creates pressure over both Food and beverage and Housekeeping areas.
    - Environmental and infrastructure factors may need renewal as its novelty use decay over time, as shown by its declining trend.
    - Because rooms are functional apartments with independent access, some rooms are privately owned and rented through other media such AirBnB. And those may not include services from the hotel management and may have separate housekeeping and other services. Those can impact the comments score as more and more rooms are being sold to private owners.


## Author
- @[PippoRamos](https://github.com/pippo-sci)

## Table of Contents

- [Tech Stack](#tech-stack)
- [Run locally](#run-locally)
- [Business Problem](#business-problem)
- [Key findings](#key-findings)

## Tech Stack

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
  * [Reputation Timeline Sea Temple-checkpoint.ipynb](.\Pullman\.ipynb_checkpoints\Reputation Timeline Sea Temple-checkpoint.ipynb)
* [tripullman/](.\Pullman\tripullman)
  * [.ipynb_checkpoints/](.\Pullman\tripullman\.ipynb_checkpoints)
    * [test-checkpoint.csv](.\Pullman\tripullman\.ipynb_checkpoints\test-checkpoint.csv)
  * [tripullman/](.\Pullman\tripullman\tripullman)
    * [spiders/](.\Pullman\tripullman\tripullman\spiders)
      * [__pycache__/](.\Pullman\tripullman\tripullman\spiders\__pycache__)
        * [pull.cpython-36.pyc](.\Pullman\tripullman\tripullman\spiders\__pycache__\pull.cpython-36.pyc)
        * [Simple Scraper TripAdvisor.cpython-36.pyc](.\Pullman\tripullman\tripullman\spiders\__pycache__\Simple Scraper TripAdvisor.cpython-36.pyc)
        * [__init__.cpython-36.pyc](.\Pullman\tripullman\tripullman\spiders\__pycache__\__init__.cpython-36.pyc)
      * [pull.py](.\Pullman\tripullman\tripullman\spiders\pull.py)
      * [Simple Scraper TripAdvisor.py](.\Pullman\tripullman\tripullman\spiders\Simple Scraper TripAdvisor.py)
      * [__init__.py](.\Pullman\tripullman\tripullman\spiders\__init__.py)
    * [__pycache__/](.\Pullman\tripullman\tripullman\__pycache__)
      * [items.cpython-36.pyc](.\Pullman\tripullman\tripullman\__pycache__\items.cpython-36.pyc)
      * [settings.cpython-36.pyc](.\Pullman\tripullman\tripullman\__pycache__\settings.cpython-36.pyc)
      * [__init__.cpython-36.pyc](.\Pullman\tripullman\tripullman\__pycache__\__init__.cpython-36.pyc)
    * [items.py](.\Pullman\tripullman\tripullman\items.py)
    * [middlewares.py](.\Pullman\tripullman\tripullman\middlewares.py)
    * [pipelines.py](.\Pullman\tripullman\tripullman\pipelines.py)
    * [settings.py](.\Pullman\tripullman\tripullman\settings.py)
    * [__init__.py](.\Pullman\tripullman\tripullman\__init__.py)
  * [pull1.csv](.\Pullman\tripullman\pull1.csv)
  * [scrapy.cfg](.\Pullman\tripullman\scrapy.cfg)
  * [test.csv](.\Pullman\tripullman\test.csv)
* [README.md](.\Pullman\README.md)
* [Reputation Timeline Sea Temple.ipynb](.\Pullman\Reputation Timeline Sea Temple.ipynb)
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

## Business Problem

Pullman Sea temple Resort constantly check online reviews to improve service. However, it is difficult to have a systematical view of the text content of such reviews, specially to compare evolution and trends.

## Key findings


