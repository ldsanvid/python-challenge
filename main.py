import pandas as pd

file = "Resources/election_data.csv"

election_df = pd.read_csv(file)
election_df.head()

nuevas_columnas = election_df["Voter ID,County,Candidate"].str.split(",", n = 2, expand=True)
election_df["Voter ID"]= nuevas_columnas[0]
election_df["County"]= nuevas_columnas[1]
election_df["Candidate"]= nuevas_columnas[2]
del election_df["Voter ID,County,Candidate"]

election_df.head()

casted_votes = election_df["Voter ID"].count()
casted_votes

candidates_ballot = election_df["Candidate"].value_counts()
candidates_ballot

percentage_candidate = candidates_ballot * 100 / casted_votes
percentage_candidate

print("Election Results")
print("----------------")
print("Total votes: " + str(casted_votes) + " votes")
print(candidates_ballot)
print(percentage_candidate)