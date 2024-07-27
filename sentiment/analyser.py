import pandas as pd
from transformers import pipeline

# TODO: pin the version of the model
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text) -> float:
    sentiment = sentiment_pipeline(text)[0]
    label = sentiment['label']
    score = sentiment['score']
    sentiment = score if label == 'POSITIVE' else 1-score
    return sentiment

def apply_sentiment_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df['sentiment'] = df['reaction'].apply(get_sentiment)
    return df