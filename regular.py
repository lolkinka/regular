from pprint import pprint
import re
import csv
with open("phonebook_raw.csv",encoding= 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


for lists in contacts_list:
  pattern_for_telephone = r"(\+7|8)\s*\(*(\d{3})\)?\-?\s?(\d{3})\-?(\d{2})\-?(\d+)\s?\(?([доб.]*\s\d*)?\)?"
  res = re.sub(pattern_for_telephone, r"+7(\2)\3-\4-\5 \6",lists[-2])
  lists[-2] = res
  pattern = "[\s]"
  sent_list = re.split(pattern, lists[0])
  sent_list_2 = re.split(pattern, lists[1])
  if lists[1] or lists[2] == '':
    while len(sent_list) != 1:
      index = sent_list.index(sent_list[-1])
      lists[index] = sent_list[-1]
      del sent_list[-1]
      lists[0] = sent_list[0]
    while len(sent_list_2) != 1:
      index = sent_list_2.index(sent_list_2[-1])
      lists[index+1] = sent_list_2[-1]
      del sent_list_2[-1]
      lists[1] = sent_list_2[0]


#объединение дублирующихся списков
for i in contacts_list:
  for j in contacts_list:
    if i[0] == j[0] and i[1] == j[1] and i is not j:
        if i[2] == '':
          i[2] = j[2]
        if i[3] == '':
          i[3] = j[3]
        if i[4] == '':
          i[4] = j[4]
        if i[5] == '':
          i[5] = j[5]
        if i[6] == '':
          i[6] = j[6]
        if len(i) > 7:
          del i[-1]
  contacts_list_updated = list()
  for card in contacts_list:
    if card not in contacts_list_updated:
      contacts_list_updated.append(card)
      contacts_list = contacts_list_updated
pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w",encoding= 'utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
