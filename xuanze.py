for n in range(1, 100):
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
    if ((A&D)&(B|C)):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1
# 第三题
    A = B =C = D = 0
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
    elif (A|B|C|D):
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
    elif (D&(A|B|C)):
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
    elif (C & (A|B|D)):
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
    A = B =C = D = 0
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
    elif (A|B|C|D):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

# 第二十题



