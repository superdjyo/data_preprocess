# -*- coding: utf-8 -*-


import pandas  as pd
import numpy as np




class check_func():
    def  __init__(self):
        self.test = 'a'
        
        
    def dup(self,df,group_list,var_str):
           a1 = df.groupby(group_list).count().reset_index(drop=False).sort_values(var_str)
           a2 = a1[a1[var_str]>1]
           return a2

    def r_fun(self,df,col_list,group_list):
        #col_list = ['YEAR','PRODUCT_BU']
        #group_list= 'PRODUCT_BU'
        df = df[col_list].groupby(group_list).count().reset_index(drop=False)
        df.columns=[group_list,'a_cnt']
        df_sum = df['a_cnt'].sum()
        df['a_ratio']=round(df['a_cnt']/df_sum*100,1)
        return df.sort_values('a_cnt',ascending=False)
    
    def cnt_func(self,df,group_list):
       df_1 =  df[group_list].groupby(group_list[0]).count().reset_index(drop=False).sort_values(group_list[1],ascending=False)
       return df_1

    #檢驗df是否有空值 並且列出佔比
    def check_null_func(self,df):
        #df = data
        df_max = df.count().max()
        df_1 = df.isnull().sum().reset_index()
        df_1['ratio']=round(df_1[0]/int(df_max)*100,2) 
        df_1.columns = ['columns','null_cnt','ratio']
        return df_1        

    #查看欄位描述統計    
    def check_column_info_func(self,df):
        #df =column_type_func(data)
        #dtypes = 'object'
        #df_1 =column_type_func(df)
        data_tmp =[]    
        df_1 =df.dtypes.reset_index()
        df_2 = df_1.values.tolist()
        for i in df_2:
            #print(i)
            #i = 0
            if i[1].name=='object':
                df_3 = data[[i[0]]].describe().T.reset_index(drop=False)
                df_3.insert(1,'dtype',i[1]) 
                data_tmp.append(df_3)
            else :
                df_3 = data[[i[0]]].describe().T.reset_index(drop=False)
                df_3.insert(1,'dtype',i[1]) 
                data_tmp.append(df_3)            
        data_all = pd.concat(data_tmp,sort=False)       
        return data_all
    #查看欄位統計   
    def check_column_type_func(self,df):
        #df =data
        df_1 = df.dtypes.reset_index()
        df_2 = df_1.groupby(0).count().reset_index()
        df_2.columns = ['columns','columns_cnt']
        return df_2
    
    

    
    
    
    
    