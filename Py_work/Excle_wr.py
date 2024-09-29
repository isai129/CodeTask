import re

import pandas as pd
import spacy

# 加载spaCy的中文模型
nlp = spacy.load("zh_core_web_sm")

# 读取Excel文件
df = pd.read_excel('/home/initial/Desktop/a.xlsx')

# 打印所有列名
print("列名列表：", df.columns.tolist())

# 确认B列的确切名称
if 'B' not in df.columns.tolist():
    print("列 'B' 不存在于DataFrame中。请检查列名是否正确。")
else:
    # 确保B列存在后，进行数据处理
    pass

# 定义用于存储结果的DataFrame
results_df = pd.DataFrame()


# 定义一个函数来提取测量信息
def extract_measurements(text):
    doc = nlp(text)
    measurements = []
    # 使用spaCy识别实体
    for ent in doc.ents:
        if ent.label_ == 'QUANTITY':
            measurements.append((ent.text, ent.label_))
    # 使用正则表达式匹配医学术语和数值
    pattern = r'(\d+(\.\d+)?)([A-Za-z]+)'
    matches = re.finditer(pattern, text)
    for match in matches:
        value, _, unit = match.groups()  # 正确解包三个元素
        measurements.append((f"{value}{unit}", 'QUANTITY'))
    return measurements


# 使用apply函数处理
measurements_list = df['B'].apply(lambda x: extract_measurements(x))

# 将列表转换为多个行
exploded_df = pd.concat([pd.DataFrame(mo) for mo in measurements_list], ignore_index=True)

# 保存到新的Excel文件
exploded_df.to_excel('/home/initial/Desktop/updated_file.xlsx', index=False)
