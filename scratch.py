import pandas as pd
from thefuzz import fuzz, process

GHC = pd.read_csv("GHC.csv")
DST_List = GHC["DST"]
MOPH_List = GHC["MOPH"]

cleanedDST = [data for data in DST_List if not(pd.isnull(data))]
cleanedMOPH = [data for data in MOPH_List.unique()if not(pd.isnull(data))]

tuples_list = [max([(fuzz.token_set_ratio(i,j),j) for j in cleanedMOPH]) for i in cleanedDST]

similarity, fuz_match = map(list,zip(*tuples_list))

df = pd.DataFrame({"DST_List":cleanedDST, "fuzzy match": fuz_match, "similarity score":similarity})

df.to_excel("fuzzyGHC.xlsx", sheet_name="FuzzMatchGHC", index = False)
