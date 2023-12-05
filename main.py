import re
import pandas as pd

file = 'QSK45 33219606.xlsx'
# file_name =   Задать параметр для сохранения выходного файла с таким же именем + пометка о преобразовании
x1 = pd.ExcelFile(file)

df1 = x1.parse('сводный')


def pn_translate():      # добавить функцию удаления пробелов в начале строки
    list_kamss = []
    for i in range(0, df1.shape[0]):
        part_num = str(df1.iloc[i, 0])
        list_pn = list(part_num)
        if part_num.startswith("S"):
            if len(str(part_num)) == 5:
                part_num = part_num.replace(" ", "000")
                part_num += "00"
            elif len(str(part_num)) == 6:
                part_num = part_num.replace(" ", "00")
                part_num += "00"
            elif len(str(part_num)) == 7:
                part_num = part_num.replace(" ", "000", 1)
                part_num = re.sub(r" ", "00 ", part_num)
        elif list_pn[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if len(str(part_num)) == 4:
                part_num = str("000" + part_num + "00")
            elif len(str(part_num)) == 5:
                part_num = str("00" + part_num + "00")
            elif len(str(part_num)) == 6:
                part_num = str("0" + part_num + "00")
            elif len(str(part_num)) == 7:
                part_num = str(part_num + "00")
        list_kamss.append(part_num)
    return list_kamss


kamss_prt = pn_translate()
df1['kamss'] = kamss_prt
df1.to_excel('otkroi_menya.xlsx')
print(df1.head())
