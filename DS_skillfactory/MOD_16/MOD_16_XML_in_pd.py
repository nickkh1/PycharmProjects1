import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('C:/Users/nick-/Documents/DS/projects/SF_tasks/menu.xml')
root = tree.getroot()


column_names = ['name', 'price', 'weight', 'class']
df = pd.DataFrame(columns=column_names)


for dish in root:
    row = [dish.attrib['name'], dish[0].text, dish[1].text, dish[2].text]
    df = df.append(pd.Series(row, index=column_names), ignore_index=True)
print(df)