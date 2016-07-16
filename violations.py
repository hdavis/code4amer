# -*- coding: utf-8 -*-

'''
Python script to load and summarize a building code violations dataset:
Violations-2012.csv.  Summary calculations include determining the number of
violations in each category, and the earliest and latest violation date for
each category.

By Holly Davis for the Code for America Fellowship Application.

Last update: July 15, 2016
'''
import pandas as pd

df = pd.read_csv('Violations-2012.csv')

df_stats = pd.DataFrame(columns=('count_of_category', 'earliest_date', 'latest_date'))

df_stats['count_of_category'] = df.groupby('violation_category')['violation_category'].count()

df_stats['earliest_date'] = df.groupby('violation_category')['violation_date'].min()

df_stats['latest_date'] = df.groupby('violation_category')['violation_date'].max()

# export to .csv file for future use
df_stats.to_csv('summary_violations.csv')

'''
A quick look at the df_stats DataFrame by typing "df_stats" at the console 
command line gives the following listing of the data contained in the 
summary_violations.csv

                          count_of_category        earliest_date  \
violation_category                                                 
Air Pollutants and Odors                  2  2012-12-05 00:00:00   
Animals and Pests                       180  2012-01-03 00:00:00   
Biohazards                                7  2012-04-13 00:00:00   
Building Conditions                      62  2012-01-12 00:00:00   
Chemical Hazards                         17  2012-02-08 00:00:00   
Garbage and Refuse                      126  2012-01-03 00:00:00   
Retail Food                               1  2012-12-20 00:00:00   
Unsanitary Conditions                    83  2012-01-03 00:00:00   
Vegetation                               67  2012-02-01 00:00:00   

                                  latest_date  
violation_category                             
Air Pollutants and Odors  2012-12-19 00:00:00  
Animals and Pests         2012-12-28 00:00:00  
Biohazards                2012-12-18 00:00:00  
Building Conditions       2012-12-26 00:00:00  
Chemical Hazards          2012-12-06 00:00:00  
Garbage and Refuse        2012-12-21 00:00:00  
Retail Food               2012-12-20 00:00:00  
Unsanitary Conditions     2012-12-19 00:00:00  
Vegetation                2012-12-05 00:00:00 
'''
