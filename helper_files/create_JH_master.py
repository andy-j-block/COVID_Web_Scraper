
####### TODO
#
# write function description


import pandas as pd
import os


def create_JH_master(JH_data_dir):
    
    JH_files = os.listdir(JH_data_dir)[1:-1]
    JH_files = [JH_data_dir + '/' + x for x in JH_files]
    JH_files.reverse()
    
    JH_master = pd.read_csv(JH_files[0])
    
    for file in JH_files[1:]:
        
        file_df = pd.read_csv(file)
    
        JH_master = pd.concat([JH_master, file_df], ignore_index=True)
        
    return JH_master