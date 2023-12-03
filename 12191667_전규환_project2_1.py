import pandas as pd

def top10_players(dataset_df, year):
    players = dataset_df[dataset_df["year"] == year]
    labels = ['H', 'avg', 'HR', 'OBP']
    for label in labels:
        top10 = players.nlargest(10, label)[["batter_name", label]]
        top10 = top10.reset_index(drop=True)
        top10.index+=1
        print(f"Top 10 players in {label} from {year}.")
        print(top10)
        print("\n")
        
def best_2018(dataset_df):
    players = dataset_df[dataset_df["year"] == 2018]
    positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
    print("2) Highest War Players by each Positions in 2018: ")
    print("\n")
    for cp in positions:
        cp_players = players[players["cp"] == cp]
        best_player = cp_players.nlargest(1, "war")[["batter_name", "war"]]
        player_name = best_player["batter_name"].values[0]
        player_war = best_player["war"].values[0]
        print(f"In 2018, Highest War Player by {cp}: {player_name}, War: {player_war}")
    print("\n")

def highest_correlation(dataset_df):
    labels = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
    correlation = dataset_df[labels].corrwith(dataset_df['salary'])
    high_correlation = correlation.sort_values(ascending=False).index[0]
    print(f"3) Highest Correlation with Salary: {high_correlation}")
    
if __name__=='__main__':
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
    # 1) Print the top 10 players
    print("1) Top 10 Players: ")
    print("\n")
    top10_players(data_df, 2015)
    top10_players(data_df, 2016)
    top10_players(data_df, 2017)
    top10_players(data_df, 2018)
    # 2) Print Highest war players in 2018
    best_2018(data_df)
    # 3) Print Highest correlation with Salary
    highest_correlation(data_df)