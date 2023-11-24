import numpy as np

def medal_tally(df):
    medal_tally=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    medal_tally=medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
    medal_tally['Total']= medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    # medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    # medal_tally['Silver'] = medal_tally['Gold'].astype('int')
    # medal_tally['Bronze'] = medal_tally['Gold'].astype('int')
    # medal_tally['Total'] = medal_tally['Gold'].astype('int')

    return medal_tally


def country_year_list(df):
    years=df['Year'].unique().tolist()
    years.sort
    years.insert(0,'Overall')

    country=np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,'Overall')

    return years,country