# challenge_week_one
News Sentiment and Stock Market movements
Introduction
Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost its financial forecasting accuracy and operational efficiency through advanced data analysis. As a Data Analyst at Nova Financial Solutions, your primary task is to conduct a rigorous analysis of the financial news dataset. The focus of your analysis should be two-fold:

Sentiment Analysis: Perform sentiment analysis on the ‘headline’ text to quantify the tone and sentiment expressed in financial news. This will involve using natural language processing (NLP) techniques to derive sentiment scores, which can be associated with the respective 'Stock Symbol' to understand the emotional context surrounding stock-related news.

Correlation Analysis: Establish statistical correlations between the sentiment derived from news articles and the corresponding stock price movements. This involves tracking stock price changes around the date the article was published and analyzing the impact of news sentiment on stock performance. This analysis should consider the publication date and potentially the time the article was published if such data can be inferred or is available.
installation
To set up this project, you will need to clone the repository and install the necessary dependencies. This project uses Python 3.11 and Conda for environment management.

1.Clone the repository:
2.Create and activate a new Conda environment:
3.Install the required dependencies:

Usage
Currently, the project is in the preprocessing stage. Here are the steps you can follow to preprocess the data and perform sentiment analysis:

Data Preprocessing: Use the preprocessing.py script located in the scripts/ directory to clean and prepare the data for analysis.

python scripts/preprocessing.py
Sentiment Analysis: Run the sentiment.py script to perform sentiment analysis on the cleaned data.

python scripts/sentiment.py
Exploratory Data Analysis (EDA): Use the eda.py script to conduct EDA on the dataset to understand the data distribution and key characteristics.

python scripts/eda.py
Notebooks: The notebooks/ directory contains Jupyter notebooks for analysis for each stock (e.g., AAPL.ipynb for Apple). You can use these notebooks to experiment with detailed analysis.
