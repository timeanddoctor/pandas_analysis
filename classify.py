import pandas as pd
import re


if __name__ == '__main__':
    data = pd.read_excel('output.xlsx')
    # 读取数据
    data = data.fillna('无')

    data1 = data.loc[data.单位.str.contains('办事处')]
    data1.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\办事处.xlsx')
    print('办事处统计完成')

    data2 = data.loc[data.单位.str.contains('保密办')]
    data2.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\保密办.xlsx')
    print('保密办统计完成')

    data3 = data.loc[data.单位.str.contains('材料')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\材料科学与工程学院.xlsx')
    print('材料科学与工程学院')

    data4 = data.loc[data.单位.str.contains('宣传部')]
    data4.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\宣传部.xlsx')
    print('宣传部')

    data3 = data.loc[data.单位.str.contains('电气')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\电气电子工程学院.xlsx')
    print('电气电子工程学院')

    data3 = data.loc[data.单位.str.contains('改革')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\改革和发展研究室.xlsx')
    print('改革和发展研究室')

    data3 = data.loc[data.单位.str.contains('工程训练中心')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\工程训练中心.xlsx')
    print('工程训练中心')

    data3 = data.loc[data.单位.str.contains('管理学院|工商')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\管理学院.xlsx')
    print('管理学院')

    data3 = data.loc[data.单位.str.contains('国际交流')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\国际交流处.xlsx')
    print('国际交流处')

    data3 = data.loc[data.单位.str.contains('海运')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\海运学院.xlsx')
    print('海运学院')

    data3 = data.loc[data.单位.str.contains('华信')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\华信软件工程.xlsx')
    print('华信软件工程')

    data3 = data.loc[data.单位.str.contains('化学')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\化学化工学院.xlsx')
    print('化学化工学院')

    data3 = data.loc[data.单位.str.contains('机械')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\机械工程学院.xlsx')
    print('机械工程学院')

    data3 = data.loc[data.单位.str.contains('计算机')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\计算机科学与工程学院.xlsx')
    print('计算机科学与工程学院')

    data3 = data.loc[data.单位.str.contains('继续')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\继续教育学院.xlsx')
    print('继续教育学院')

    data3 = data.loc[data.单位.str.contains('理学院')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\理学院.xlsx')
    print('理学院')

    data3 = data.loc[data.单位.str.contains('聋人工学院')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\聋人工学院.xlsx')
    print('聋人工学院')

    data3 = data.loc[data.单位.str.contains('马克思')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\马克思主义学院.xlsx')
    print('马克思主义学院')

    data3 = data.loc[data.单位.str.contains('社会发展学院')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\社会发展学院.xlsx')
    print('社会发展学院')

    data3 = data.loc[data.单位.str.contains('体育')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\体育部.xlsx')
    print('体育部')

    data3 = data.loc[data.单位.str.contains('语言文化')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\语言文化学院.xlsx')
    print('语言文化学院')

    data3 = data.loc[data.单位.str.endswith('天津理工大学')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\未填具体单位.xlsx')
    print('天津理工大学')

    data3 = data.loc[data.单位.str.contains('学刊编辑')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\学刊编辑部.xlsx')
    print('学刊编辑部')

    data3 = data.loc[data.单位.str.contains('保卫')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\安全保卫部.xlsx')
    print('安全保卫部')

    data3 = data.loc[data.单位.str.contains('组织部')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\党委组织部.xlsx')
    print('党委组织部')

    data3 = data.loc[data.单位.str.contains('环境|环安')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\环境科学与安全工程学院.xlsx')
    print('环境科学与安全工程学院')

    data3 = data.loc[data.单位.str.contains('离退')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\离退办.xlsx')
    print('离退办')

    data3 = data.loc[data.单位.str.contains('统战')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\统战部.xlsx')
    print('统战部')

    data3 = data.loc[data.单位.str.contains('语言文化')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\材语言文化学院.xlsx')
    print('语言文化学院')

    data3 = data.loc[data.单位.str.contains('图书馆')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\图书馆.xlsx')
    print('图书馆')

    data3 = data.loc[data.单位.str.contains('低碳')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\新能源材料与低碳技术研究院.xlsx')
    print('新能源材料与低碳技术研究院')

    data3 = data.loc[data.单位.str.contains('研究生')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\研究生院.xlsx')
    print('研究生院')

    data3 = data.loc[data.单位.str.contains('艺术')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\艺术学院.xlsx')
    print('艺术学院')

    data3 = data.loc[data.单位.str.contains('校团委')]
    data3.to_excel('D:\GitHub\personalDEV\pycharm\pandas\classification\校团委.xlsx')
    print('校团委')


