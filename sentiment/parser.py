import pandas as pd

def read_driver_times_file(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def fill_drivers(df):     
    # Get the list of tuples with the time and driver when a driver starts speaking
    driver_starts = [(row['time'], row['driver']) for _, row in df[df['driver'].notna()].iterrows()]
    
    # Fill driver names and their finishing places in the 'driver' and 'place' columns
    current_driver = None
    for i, row in df.iterrows():
        # Update the current driver and place if a new driver starts speaking
        for start_time, driver_name in driver_starts:
            if row['time'] >= start_time:
                current_driver = driver_name
            else:
                break
        df.at[i, 'driver'] = current_driver
    
    return df

def read_driver_reaction_file(file_path: str, df_driver_times: pd.DataFrame) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    merged_df = pd.merge(df, df_driver_times, on='time', how='left')

    merged_df = fill_drivers(merged_df)

    merged_df = merged_df.groupby(['driver'])['reaction'].apply(' '.join).reset_index()

    merged_df = merged_df.sort_values(by='place', ascending=True)

    return merged_df
    