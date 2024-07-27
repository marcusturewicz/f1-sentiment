from sentiment.analyser import apply_sentiment_analysis
from sentiment.parser import read_driver_reaction_file, read_driver_times_file


if __name__ == '__main__':
    driver_times_file_path = "data/2024/02-saudi/driver-times.txt"
    df_driver_times = read_driver_times_file(driver_times_file_path)

    driver_reaction_file_path = "data/2024/02-saudi/driver-reactions.txt"
    df_driver_reactions = read_driver_reaction_file(driver_reaction_file_path, df_driver_times)

    df_sentiment = apply_sentiment_analysis(df_driver_reactions)

    df_sentiment.to_csv("output.csv", index=False)

    print(df_sentiment)