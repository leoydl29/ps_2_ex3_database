import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_team_founding_years(con, teams_display):
    """
    Plots a bar chart of NBA teams and their earliest founding year.

    Args:
        con: A database connection object (e.g., from sqlite3,
             duckdb) that pandas.read_sql can use.

    Returns:
        matplotlib.axes.Axes: The Axes object containing the bar chart,
        or None if data fetching fails.
    """
    
    # This SQL query finds the earliest (MIN) founding year for each
    # unique team nickname. It groups all "Hawks" or "Warriors"
    # entries into a single row representing the franchise's start.
    query = f"""
    SELECT
        city,
        nickname,
        year_founded
    FROM
        team_history
    ORDER BY year_founded ASC
    LIMIT {teams_display}
    """
    
    df = pd.read_sql(query, con)
    df["Team_Name"] = df["city"] + df ["nickname"]

    # Set the size of the plot
    # A tall figure is needed to display all team names clearly
    plt.figure(figsize=(12, teams_display))

    # Create the horizontal bar chart
    # Y-axis = team nickname
    # X-axis = founding year
    ax = sns.barplot(
        x='year_founded',
        y='Team_Name',
        data=df,
        color='blue'
    )

    # Set titles and labels for clarity
    ax.set_title('NBA Team Founding Years (Earliest Record)', fontsize=20, pad=15)
    ax.set_xlabel('Year Founded', fontsize=14)
    ax.set_ylabel('Team', fontsize=14)
    ax.set_xlim(left=1900, right = 2025)
    
    # Add the year labels directly to the end of the bars
    ax.bar_label(
        ax.containers[0], 
        fmt='%d',          # Format as an integer
        padding=15,         # Add some space
        fontsize=10
    )

    # Clean up the plot aesthetics
    sns.despine(left=True, bottom=True) # Remove top and right spines
    
    plt.tight_layout() # Adjust plot to prevent labels from overlapping
    
    print("Chart generation complete.")
    return ax
