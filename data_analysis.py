import pandas as pd
import re

def panjuan(n):
    m = re.search('人民安全', str(data.loc[n, 'A1']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('政治安全', str(data.loc[n, 'A2']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('经济安全', str(data.loc[n, 'A3']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('社会安全', str(data.loc[n, 'A4']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('促进国际安全', str(data.loc[n, 'A5']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('国家安全', str(data.loc[n, 'A6']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('维护国家安全', str(data.loc[n, 'A7']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('总体国家安全观', str(data.loc[n, 'A8']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('发展和安全', str(data.loc[n, 'A9']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('人民安全|政治安全|国家利益至上', str(data.loc[n, 'A10']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('人民安全|政治安全|国家利益至上', str(data.loc[n, 'A11']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('人民安全|政治安全|国家利益至上', str(data.loc[n, 'A12']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第四题
    m = re.search('底线思维', str(data.loc[n, 'A13']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('忧患意识', str(data.loc[n, 'A14']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('防控能力', str(data.loc[n, 'A15']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('防范化解重大风险', str(data.loc[n, 'A16']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第五题
    m = re.search('中国共产党对国家安全工作的领导', str(data.loc[n, 'A17']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第六题
    m = re.search('国家基本经济制度|社会主义市场经济秩序', str(data.loc[n, 'A18']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('国家基本经济制度|社会主义市场经济秩序', str(data.loc[n, 'A19']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第七题
    m = re.search('生物安全', str(data.loc[n, 'A20']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    # 第八题
    m = re.search('共同安全', str(data.loc[n, 'A21']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第九题
    m = re.search('国家安全机关|公安机关|有关军事机关', str(data.loc[n, 'A22']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('国家安全机关|公安机关|有关军事机关', str(data.loc[n, 'A23']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('国家安全机关|公安机关|有关军事机关', str(data.loc[n, 'A24']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十题
    m = re.search('4月15日|四月十五', str(data.loc[n, 'A25']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十一题
    m = re.search('机关|人民团体|企业事业组织|其他社会组织', str(data.loc[n, 'A26']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('机关|人民团体|企业事业组织|其他社会组织', str(data.loc[n, 'A27']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('机关|人民团体|企业事业组织|其他社会组织', str(data.loc[n, 'A28']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('机关|人民团体|企业事业组织|其他社会组织', str(data.loc[n, 'A29']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 十二题
    m = re.search('情况', str(data.loc[n, 'A30']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('证据', str(data.loc[n, 'A31']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('如实提供', str(data.loc[n, 'A32']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十三题
    m = re.search('中华人民共和国境内外', str(data.loc[n, 'A33']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十四题
    m = re.search('恐怖主义', str(data.loc[n, 'A34']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('恐怖主义', str(data.loc[n, 'A35']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十六题
    m = re.search('公安机关|国家安全机关', str(data.loc[n, 'A36']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('公安机关|国家安全机关', str(data.loc[n, 'A37']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十七题
    m = re.search('安全检查|开封验视', str(data.loc[n, 'A38']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('安全检查|开封验视', str(data.loc[n, 'A39']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十八题
    m = re.search('预防为主', str(data.loc[n, 'A40']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十九题
    m = re.search('省.*自治区.*直辖市人民政府直辖市人民政府', str(data.loc[n, 'A41']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第二十题
    m = re.search('出售|购买|利用', str(data.loc[n, 'A42']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    m = re.search('出售|购买|利用', str(data.loc[n, 'A43']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('出售|购买|利用', str(data.loc[n, 'A44']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1


    # 填空题
    A = B = D = 1
    C = 0
    if data.loc[n, 'A45']:
        A = 0
    if data.loc[n, 'A46']:
        B = 0
    if data.loc[n, 'A47']:
        C = 1
    if data.loc[n, 'A48']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第一题
    A = B = C = 1
    D = 0
    if data.loc[n, 'A49']:
        A = 0
    if data.loc[n, 'A50']:
        B = 0
    if data.loc[n, 'A51']:
        C = 0
    if data.loc[n, 'A52']:
        D = 1
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第二题
    A = D = 1
    C = B = 0
    if data.loc[n, 'A53']:
        A = 0
    if data.loc[n, 'A54']:
        B = 1
    if data.loc[n, 'A55']:
        C = 1
    if data.loc[n, 'A56']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    if ((A & D) & (B | C)):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第三题
    A = B = C = D = 0
    if data.loc[n, 'A57']:
        A = 1
    if data.loc[n, 'A58']:
        B = 1
    if data.loc[n, 'A59']:
        C = 1
    if data.loc[n, 'A60']:
        D = 1
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    elif (A | B | C | D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    # 第四题
    A = B = C = 1
    D = 0
    if data.loc[n, 'A61']:
        A = 0
    if data.loc[n, 'A62']:
        B = 0
    if data.loc[n, 'A63']:
        C = 0
    if data.loc[n, 'A64']:
        D = 1
    elif (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第五题
    A = B = D = 1
    C = 0
    if data.loc[n, 'A65']:
        A = 0
    if data.loc[n, 'A66']:
        B = 0
    if data.loc[n, 'A67']:
        C = 1
    if data.loc[n, 'A68']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第六题
    A = C = D = 1
    B = 0
    if data.loc[n, 'A69']:
        A = 0
    if data.loc[n, 'A70']:
        B = 1
    if data.loc[n, 'A71']:
        C = 0
    if data.loc[n, 'A72']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第七题
    A = B = D = 1
    C = 0
    if data.loc[n, 'A73']:
        A = 0
    if data.loc[n, 'A74']:
        B = 0
    if data.loc[n, 'A75']:
        C = 1
    if data.loc[n, 'A76']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第八题
    A = C = D = 1
    B = 0
    if data.loc[n, 'A77']:
        A = 0
    if data.loc[n, 'A78']:
        B = 1
    if data.loc[n, 'A79']:
        C = 0
    if data.loc[n, 'A80']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第九题
    A = C = D = 1
    B = 0
    if data.loc[n, 'A81']:
        A = 0
    if data.loc[n, 'A82']:
        B = 1
    if data.loc[n, 'A83']:
        C = 0
    if data.loc[n, 'A84']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第十题
    D = 1
    A = B = C = 0
    if data.loc[n, 'A85']:
        A = 1
    if data.loc[n, 'A86']:
        B = 1
    if data.loc[n, 'A87']:
        C = 1
    if data.loc[n, 'A88']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    elif (D & (A | B | C)):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    # 第十一题
    C = B = D = 1
    A = 0
    if data.loc[n, 'A89']:
        A = 1
    if data.loc[n, 'A90']:
        B = 0
    if data.loc[n, 'A91']:
        C = 0
    if data.loc[n, 'A92']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第十二题
    A = B = D = 1
    C = 0
    if data.loc[n, 'A93']:
        A = 0
    if data.loc[n, 'A94']:
        B = 0
    if data.loc[n, 'A95']:
        C = 1
    if data.loc[n, 'A96']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第十三题
    A = B = D = 0
    C = 1
    if data.loc[n, 'A97']:
        A = 1
    if data.loc[n, 'A98']:
        B = 1
    if data.loc[n, 'A99']:
        C = 0
    if data.loc[n, 'A100']:
        D = 1
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    elif (C & (A | B | D)):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十四题
    A = B = D = 1
    C = 0
    if data.loc[n, 'A101']:
        A = 0
    if data.loc[n, 'A102']:
        B = 0
    if data.loc[n, 'A103']:
        C = 1
    if data.loc[n, 'A104']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第十五题
    A = B = D = 0
    C = 1
    if data.loc[n, 'A105']:
        A = 1
    if data.loc[n, 'A106']:
        B = 1
    if data.loc[n, 'A107']:
        C = 0
    if data.loc[n, 'A108']:
        D = 1
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    elif (C & (A | B | D)):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十六题
    A = C = D = 1
    B = 0
    if data.loc[n, 'A109']:
        A = 0
    if data.loc[n, 'A110']:
        B = 1
    if data.loc[n, 'A111']:
        C = 0
    if data.loc[n, 'A112']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第十七题
    A = B = D = 0
    C = 1
    if data.loc[n, 'A113']:
        A = 1
    if data.loc[n, 'A114']:
        B = 1
    if data.loc[n, 'A115']:
        C = 0
    if data.loc[n, 'A116']:
        D = 1
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    elif (C & (A | B | D)):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
    # 第十八题
    C = B = D = 1
    A = 0
    if data.loc[n, 'A117']:
        A = 1
    if data.loc[n, 'A118']:
        B = 0
    if data.loc[n, 'A119']:
        C = 0
    if data.loc[n, 'A120']:
        D = 0
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    # 第十九题
    A = B = C = D = 0
    if data.loc[n, 'A121']:
        A = 1
    if data.loc[n, 'A122']:
        B = 1
    if data.loc[n, 'A123']:
        C = 1
    if data.loc[n, 'A124']:
        D = 1
    if (A & B & C & D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    elif (A | B | C | D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
# 第二十题
# 选择题
    x1 = x2 = x3 = x4 = 0
    m = re.search('坚持中国共产党对国家安全工作的领导.*建立集中统一.*高效权威的国家安全领导体制', str(data.loc[n,'A125']))
    if (m != None):
        x1 = 1
    m = re.search('坚持法治和保障人权原则', str(data.loc[n,'A125']))
    if ( m!= None):
        x2 = 1
    m = re.search('坚持维护国家安全与经济社会发展相协调', str(data.loc[n,'A125']))
    if (m != None):
        x3 = 1
    m = re.search('坚持预防为主.*标本兼治.*专门工作与群众路线相结合', str(data.loc[n,'A125']))
    if (m != None):
        x4 = 1
    if (x1+x2+x3+x4==1):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    if (x1+x2+x3+x4==2):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 4
    if (x1+x2+x3+x4==3):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 6
    if (x1+x2+x3+x4==4):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 10

    x1 = x2 = x3 = x4 = 0
    m = re.search('加强国家安全新闻宣传和舆论引导', str(data.loc[n,'A126']))
    if (m != None):
        x1 = 1
    m = re.search('通过多种形式开展国家安全宣传教育活动', str(data.loc[n,'A126']))
    if ( m!= None):
        x2 = 1
    m = re.search('将国家安全教育纳入国民教育体系和公务员教育培训体系', str(data.loc[n,'A126']))
    if (m != None):
        x3 = 1
    m = re.search('增强全民国家安全意识', str(data.loc[n,'A126']))
    if (m != None):
        x4 = 1
    if (x1+x2+x3+x4==1):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 2
    if (x1+x2+x3+x4==2):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 4
    if (x1+x2+x3+x4==3):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 6
    if (x1+x2+x3+x4==4):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 10
# 简答题

if __name__ == '__main__':
    data = pd.read_excel('test.xlsx')
    # 读取数据
    data['score'] = 0
    # 新建一列作为成绩，初始为0
    data = data.fillna(0)
    # 将空缺值填充为0
    print('开始判卷')
    for n in range(0,2795):
        panjuan(n)
        print('正在判卷，第'+str(n)+'份，共2794份')
    print('判卷完成')
    output = data.loc[:, :'单位']
    # 只取个人信息部分，生成另一张表。
    output['score'] = data['score']
    # 将成绩复制到新表中
    output.to_excel('D:\GitHub\personalDEV\pycharm\pandas\output.xlsx')

