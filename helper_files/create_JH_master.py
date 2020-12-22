
import pandas as pd
import os


def create_JH_master(JH_data_dir):
    
    JH_files = os.listdir(JH_data_dir)[1:-1]
    JH_files = [JH_data_dir + '/' + x for x in JH_files]
    
    JH_master = pd.DataFrame(JH_files[0])
    
    for file in JH_files[1:]:
        
        file_df = pd.DataFrame(file)
    
        JH_master = JH_master.concat(file_df, ignore_index=True)
        
    return JH_master