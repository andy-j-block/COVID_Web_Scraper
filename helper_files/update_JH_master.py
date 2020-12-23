
import pandas as pd
import os


def update_JH_master(JH_master, JH_data_dir):
    
    ####################
    
    def set_datetime(JH_master):
        
        JH_master['Last_Update'] = pd.to_datetime(JH_master['Last_Update'], 
                                                  format='%Y-%m-%d %H:%M:&S')
        JH_master['Last_Update'] = JH_master['Last_Update'].dt.date

        JH_master = JH_master.sort_values('Last_Update', ascending = True)
        
        return JH_master
    
    #####################

    
    JH_master = set_datetime(JH_master)


    #####################
    
    def get_date_last_pull(JH_master):
        
        last_pull = JH_master['Last_Update'].iloc[-1]
        last_pull = last_pull - pd.Timedelta('1 day')
        last_pull = last_pull.dt.strftime('%m-%d-%Y')
        last_pull = str(last_pull) + '.csv'
        
        return last_pull
    
    #####################
    
    
    last_pull = get_date_last_pull(JH_master)
    
    
    #####################
    
    def add_new_data(JH_master, last_pull, JH_data_dir):
        
        # identify csv's to add to master
        JH_files = os.listdir()[1:-1]
        
        new_JH_files = JH_files[JH_files.index(last_pull):]
        new_JH_files = [JH_data_dir + '/' + x for x in new_JH_files]
        
        for i in new_JH_files:
            
            new_data = pd.read_csv(i)
            
            new_data['Last_Update'] = pd.to_datetime(new_data['Last_Update'],
                                                   format='%Y-%m-%d %H:%M:&S')
            
            new_data['Last_Update'] = new_data['Last_Update'].dt.date
        
            JH_master = pd.concat([JH_master, new_data], ignore_index=True)

        return JH_master

    #####################
    
    JH_master = add_new_data(JH_master, last_pull, JH_data_dir)

    return JH_master