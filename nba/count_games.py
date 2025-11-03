import pandas as pd 
import matplotlib.pyplot as plt

def count_yearly_games(con):

    query = """
    SELECT    
        game_date_est
    FROM    
        game_summary

    """

    df = pd.read_sql(query, con)
    df["game_date_est"] = pd.to_datetime(df["game_date_est"])
    df["year"] = df["game_date_est"].dt.year
    yearly_counts = df.groupby('year').size().reset_index(name='game_count')

    plt.figure(figsize=(10, 6)) # Set the figure size
    plt.bar(yearly_counts['year'], yearly_counts['game_count'], color='skyblue')
        
    plt.title('Number of Games Played Per Year', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Games', fontsize=12)
        
    # Ensure all years are shown as integer ticks on the x-axis
    plt.xticks(yearly_counts['year'][::2], rotation=45, ha='right')
        
    # Add a light grid for readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
        
    # Adjust layout to prevent labels from overlapping
    plt.tight_layout()
        
    # Show the plot
    plt.show()