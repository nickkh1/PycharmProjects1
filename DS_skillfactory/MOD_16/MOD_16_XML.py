import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.parse('C:/Users/nick-/Documents/DS/projects/SF_tasks/menu.xml')

# смотрим корневое значние
root = tree.getroot()
print(root)

# посмотреть список потомков корневого узла
print(list(root))


# список потомков второго блюда в нашем меню и вывести его на экран
print(list(root[1]))


# Мы можем непосредственно обратиться к атрибутам, используя attrib.
print(root[0].attrib)


# В XML-узлах часто хранятся количественные показатели. Эти показатели хранятся в виде текста, и прочитать их можно, обратившись к атрибуту text у соответствующего объекта типа ElementTree.Element.
print(root[0][0])
print(root[0][0].text)

# наименование тега конкретного узла, необходимо использовать tag
print(root.tag)

print(root[0][2].tag)



for dish in root:
    for param in dish:
        print(dish.attrib['name'], param.tag, param.text)
    print()