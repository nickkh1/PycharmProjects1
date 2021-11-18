import pandas as pd

melb_data = pd.read_csv('C:/Users/nick-/Documents/DS/projects/SF_tasks/melb_data_fe.csv', sep=',')

melb_data['Date'] = pd.to_datetime(melb_data['Date'])
quarter_series = melb_data['Date'].dt.quarter
# print(quarter_series.value_counts())
melb_df = melb_data.copy()

cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_unique_count = 150
for col in melb_df.columns:
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')


# mask1 = melb_df['AreaRatio'] < -0.8
# mask2 = melb_df['Type'] == 'townhouse'
# mask3 = melb_df['SellerG'] == 'McGrath'
# melb_df_Mc = melb_df[mask1 & mask2 & mask3].sort_values(by=['Date', 'AreaRatio'],ascending=[True, False],ignore_index=True).loc[:, ['SellerG','Date', 'AreaRatio']]
# print(melb_df_Mc)

# print(int(melb_df.sort_values(by='AreaRatio',ignore_index=True,ascending=False).loc[1558, 'BuildingArea']))

mask1 = melb_df['Type'] == 'townhouse'
mask2 = melb_df['Rooms'] > 2
print(int(melb_df[mask1&mask2].sort_values(by=['Rooms', 'MeanRoomsSquare'],ascending=[True, False],ignore_index=True).loc[18, 'Price']))