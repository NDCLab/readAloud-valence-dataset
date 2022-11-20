import pandas as pd
import sys
import math

data_tracker_file = "/home/data/NDClab/datasets/readAloud-valence-dataset/data-monitoring/central-tracker_readAloud-valence.csv"

check_columns = [
    "stai5_scrdS_s1_r1_e1",
    "stai5_scrdT_s1_r1_e1",
    "bfne_scrdTotal_s1_r1_e1",
    "aq10_scrdTotal_s1_r1_e1",
    "bmis_scrdVal_s1_r1_e1",
    "phq8_scrdTotal_s1_r1_e1",
    "panasnow_scrdPA_s1_r1_e1",
    "panasnow_scrdNA_s1_r1_e1",
    "scaared_scrdTotal_s1_r1_e1",
    "erq_scrdCogRea_s1_r1_e1",
    "erq_scrdExpSup_s1_r1_e1",
    "sias6sps6_scrdSIAS_s1_r1_e1",
    "sias6sps6_scrdSPS_s1_r1_e1",
    "ari_scrdRaw_s1_r1_e1",
    "ari_scrdProrat_s1_r1_e1"]

if __name__ == "__main__":
    file = sys.argv[1]
    file_df = pd.read_csv(file, index_col="record_id")
    tracker_df = pd.read_csv(data_tracker_file, index_col="id")

    for index, row in file_df.iterrows():
        id = row.name
        # check if id exists in tracker
        if id not in tracker_df.index:
            print(id, "missing in tracker file, skipping")
            continue
        for key in check_columns:
            try:
                val = file_df.loc[id, key]
                if tracker_df.loc[id, key] ==  1 or tracker_df.loc[id, key] == 0:
                    continue
                tracker_df.loc[id, key] = 0 if math.isnan(val) else 1
            except Exception as e_msg:
                tracker_df.loc[id, key] = 0

    tracker_df.to_csv(data_tracker_file)
    print("Success: data tracker updated.")
