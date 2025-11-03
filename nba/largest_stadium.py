import pandas as pd


def largest_stadium(con):

    query = """

    SELECT 
        nickname,
        arena,
        arenacapacity
    FROM 
        team_details
    ORDER BY arenacapacity DESC
    LIMIT 1

    """

    df = pd.read_sql(query, con)
    print(df)