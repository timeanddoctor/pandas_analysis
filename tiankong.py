for n in range(0, 2794):
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
#第十一题
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
