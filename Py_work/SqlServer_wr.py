import pyodbc

# 连接到数据库
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_username;PWD=your_password')

# 创建游标
cursor = conn.cursor()

# 执行查询
cursor.execute("SELECT your_column FROM your_table")

# 获取所有记录
rows = cursor.fetchall()

# 遍历记录并截取字符串
for row in rows:
    str_value = row[0]
    part_str = str_value[:5]  # 例如，截取前5个字符
    print(part_str)

# 关闭游标和连接
cursor.close()
conn.close()
