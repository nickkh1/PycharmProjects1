import pandas as pd
pd.set_option('display.max_columns', None)

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

# print(melb_df.groupby(['Rooms', 'Type'])['Price'].mean().unstack())

# # print(melb_df.pivot_table(
#     values='Price',
#     index='Rooms',
#     columns='Type',
#      fill_value = 0
# ).round(2))

# print(melb_df.pivot_table(
#     values='Price',
#     index='Regionname',
#     columns='Weekend',
#     aggfunc='count',
# ))

# print(melb_df.pivot_table(
#     values='Landsize',
#     index='Regionname',
#     columns='Type',
#     aggfunc=['median', 'mean'],
#     fill_value=0
# ))

# print(melb_df.pivot_table(
#     values='Price',
#     index=['Method','Type'],
#     columns='Regionname',
#     aggfunc='median',
#     fill_value=0
# ))


# pivot = melb_df.pivot_table(
#     values='Landsize',
#     index='Regionname',
#     columns='Type',
#     aggfunc=['median', 'mean'],
#     fill_value=0
# )
# print(pivot.columns)
# print(pivot['mean']['unit'])
#
# mask = pivot['mean']['house'] < pivot['median']['house']
# filtered_pivot = pivot[mask]
# print(filtered_pivot)
#
# print(list(filtered_pivot.index))


# pivot = melb_df.pivot_table(
#     values='BuildingArea',
#     index='Type',
#     columns='Rooms',
#     aggfunc='median',
#     fill_value=0
# )
# print(pivot)

pivot = melb_df.pivot_table(
        values='Price',
        index='SellerG',
        columns='Type',
        fill_value=0
)
max_unit_price = pivot['unit'].max()
print(pivot[pivot['unit'] == max_unit_price].index[0])
