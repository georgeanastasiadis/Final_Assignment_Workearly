import pandas as pd

df = pd.read_csv("finance_liquor_sales(2016-2019).csv")

#Item sold based on zip_code
item_per_zipcode = df.groupby(['zip_code','item_description']).agg({'bottles_sold': 'max'}).reset_index()

#We find the item with max sales based on zip_code
popular_item = item_per_zipcode.sort_values('bottles_sold', ascending=False).drop_duplicates('zip_code')
popular_item = popular_item.sort_values('zip_code')

#Total amount of bottles sold
sum_of_bottles_sold = df['bottles_sold'].sum()
#sold bottles for every store
sb_for_each_store = df.groupby(['store_number','store_name']).agg({'bottles_sold': 'sum'})
#The result as a percentage
sb_for_each_store['bottles_sold'] = ((sb_for_each_store['bottles_sold']/sum_of_bottles_sold)*100).round(3)
#Rename the column 'bottles_sold'
sb_for_each_store.rename(columns= {'bottles_sold': 'Percentage_of_bottles_sold'}, inplace=True)



print(popular_item,'\n')
print(sb_for_each_store.to_string())


