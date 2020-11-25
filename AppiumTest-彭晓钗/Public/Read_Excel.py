#coding:utf-8
'''
关于excel表格操作的一些方法
'''



import xlrd

class Excel_Data():
    #初始化方法
    def __init__(self, excel_path, sheet_name):
        #打开excel表读取数据
        self.data = xlrd.open_workbook(excel_path)
        #根据工作表名称获取工作表的内容
        self.table = self.data.sheet_by_name(sheet_name)
        #获取第一行为key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols

    # 定义一个读取excel表的方法
    def dict_data(self):
        # 定义一个空列表
        datas = []
        # j = 1
        for i in range(1, self.rowNum):
            # 定义一个空字典
            sheet_data = {}
            # 从第二行取对应values的值
            sheet_data['rowNum'] = i + 1
            for j in range(self.colNum):
                # 获取单元格数据类型
                # c_type = self.table.cell(i, j).ctype
                # 获取单元格数据
                c_cell = self.table.cell_value(i, j)
                # # 如果是整形
                # if c_type == 2 and c_cell % 1 == 0:
                #     c_cell = int(c_cell)
                # elif c_type == 3:
                #     # 转成datetime对象
                #     date = datetime.datetime(*xldate_as_tuple(c_cell, 0))
                #     c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
                # elif c_type == 4:
                #     c_cell = True if c_cell == 1 else False
                sheet_data[self.keys[j]] = c_cell
            # 再将字典追加到列表中
            datas.append(sheet_data)
            j = j + 1
        # 返回从excel中获取到的数据：以列表存字典的形式返回
        return datas

if __name__ == "__main__":
    filepath = "E:\\AppiumTest\\Data\\Automation.xlsx"
    sheetName = "Sheet1"
    data = Excel_Data(filepath, sheetName)
    print(data.dict_data())





