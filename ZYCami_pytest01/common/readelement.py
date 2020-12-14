# readelement.py
import os
import yaml
from config.conf import ELEMENT_PATH


'''class Element:
    """获取元素"""

    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))'''

def read_yaml(file_name):
    '''
    读取yaml文件获取数据
    :return:
    '''
    dic = {}
    path = ELEMENT_PATH + '/' + file_name + '.yaml'
    with open(path,encoding='utf-8') as f:
        data = yaml.safe_load(f)
        dic.update(data)
    return dic

if __name__ == '__main__':

    print(read_yaml('Camera')['相机1'][int(len(read_yaml('Camera')['相机1']) - 1)])


