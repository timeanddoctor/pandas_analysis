>环境 Anaconda3 python3
>data_analysis为主程序，其余均为测试



学校新闻中心搞了一个调查问卷，要求老师和每班的积极分子填写，人数估计在5000人左右。我在腾讯问卷创建了问卷，但是学校还要求根据正确答案为每个人判分。我想到了可以用相关数据分析工具完成这项任务。

---
## 准备阶段
- 腾讯问卷导出的数据为 `.csv`文件，可以Excel打开编辑。
- 工具选择Pandas
- 环境使用anaconda3，里面包含了pandas库。
- 代码在jupyternotebook编写，可以实时看运行结果。

## 代码架构
答卷由填空题，不定项选择题，简答题三部分组成。
1. 读取统计数据文件
2. 在文件最右侧新加一列score，作为答卷人每人的分数，初始为0
3. 填空题判断每一列的是否包含正确答案，若包含在其所在行为score加1
4. 选择题4个为一组，若正确为其所在行为score加2，若不完全正确加1
5. 简答题分数由命中答案关键词数量决定，全部命中为10分，依次递减。
6. 统计完成后根据score列重新排序

## 代码
- 主函数

```
import pandas as pd
import re

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
```
- panjuan函数

```
def panjuan(n):
    m = re.search('发展和安全', str(data.loc[n, 'A9']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

    m = re.search('人民安全|政治安全|国家利益至上', str(data.loc[n, 'A10']))
    if (m != None):
        data.loc[n, 'score'] = data.loc[n, 'score'] + 1

```
填空题，使用正则表达从回答中搜索标准答案，若找到则加分。  
若一个空可能有多个答案，搜索时使用 `人民安全|政治安全|国家利益至上` 或关系。
```
# 选择题
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
    # 单选

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
	# 多选
```
选择题，完美实现不定项选择评分结构，是整个代码最精彩的一部分。

```
# 简答题
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
```
简答题，在回答中搜索关键词，按点给分。
