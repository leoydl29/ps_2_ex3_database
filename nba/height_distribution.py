import pandas as pd 
import matplotlib.pyplot as plt


def height_graph(con): 


    query = """

    SELECT 
        height_wo_shoes_ft_in
    FROM 
        draft_combine_stats
    """

    df = pd.read_sql(query, con)
    df = df.dropna()

    height_counts = df.groupby('height_wo_shoes_ft_in').size().reset_index(name='height_count')

    plt.figure(figsize=(10, 6)) # Set the figure size
    plt.bar(height_counts["height_wo_shoes_ft_in"], height_counts['height_count'], color='skyblue')
        
    plt.title('Number of Players of Certain Height', fontsize=16)
    plt.xlabel('Height', fontsize=12)
    plt.ylabel('Number of Players', fontsize=12)
        
    # Ensure all years are shown as integer ticks on the x-axis
    plt.xticks(height_counts['height_wo_shoes_ft_in'][::4], rotation=45, ha='right')
        
    # Add a light grid for readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
        
    # Adjust layout to prevent labels from overlapping
    plt.tight_layout()
        
    # Show the plot
    plt.show()
   