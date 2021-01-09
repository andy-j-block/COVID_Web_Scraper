
import pandas as pd
import os


def create_JH_master(JH_data_dir, root_dir):
    
    #################
    #
    # This function creates a JH_master csv file if none already exists in the
    # root_dir.  It takes the first csv file in the directory and reads it in as
    # a pandas dataframe, concatenates the other files (except for the 
    # .gitignore and readme) in the directory onto this data frame, and then sorts
    # the dataframe by its 'Last_Update' column so that the dataframe can be 
    # written to a csv file in an ordered way.  This csv is saved to the root
    # directory for further use.
    #
    #################
    
    JH_files = os.listdir(JH_data_dir)[1:-1]
    JH_files = [JH_data_dir + '/' + x for x in JH_files]
    JH_files.reverse()
    
    JH_master = pd.read_csv(JH_files[0])
    
    for file in JH_files[1:]:
        
        file_df = pd.read_csv(file)
        
        if 'Last Update' in file_df.columns:
            file_df.rename(columns={'Last Update':'Last_Update'}, inplace=True)
    
        JH_master = pd.concat([JH_master, file_df], ignore_index=True)
    
    JH_master.sort_values('Last_Update', ascending = True, inplace=True)
    
    JH_master.to_csv(root_dir+'/JH_master.csv')
        
    return JH_master