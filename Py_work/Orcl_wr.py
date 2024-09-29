import datetime

import cx_Oracle

# 数据库连接配置
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'dsn': 'your_dsn'  # 或者是 'hostname:port/service_name'
}

# 日志文件路径
log_file_path = '/path/to/your/update_log.txt'

# 连接到Oracle数据库
conn = cx_Oracle.connect(**db_config)
cursor = conn.cursor()

# 日志文件头部信息
log_header = f"Update Log - Start Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
log_header += "ID, Old DEPTSTUDYID, New DEPTSTUDYID, Update Time\n"

# 写入日志文件头部
with open(log_file_path, 'w') as log_file:
    log_file.write(log_header)

# SQL更新语句
sql_update = """
UPDATE studyinfo
SET DEPTSTUDYID = (
    SELECT CSSFXM.fid
    FROM CSSFXM
    WHERE REGEXP_LIKE(CSSFXM.h0, '^' || REGEXP_REPLACE(TRIM(studyinfo.STUDYDESCRIBE), '[^\u4e00-\u9fff]', '') || '$')
    AND studyinfo.registertime BETWEEN TO_DATE('2023-01-01', 'YYYY-MM-DD') AND TO_DATE('2023-12-31', 'YYYY-MM-DD')
)
WHERE EXISTS (
    SELECT 1
    FROM CSSFXM
    WHERE REGEXP_LIKE(CSSFXM.h0, '^' || REGEXP_REPLACE(TRIM(studyinfo.STUDYDESCRIBE), '[^\u4e00-\u9fff]', '') || '$')
    AND studyinfo.registertime BETWEEN TO_DATE('2023-01-01', 'YYYY-MM-DD') AND TO_DATE('2023-12-31', 'YYYY-MM-DD')
)
"""

try:
    # 执行更新操作
    cursor.execute(sql_update)
    conn.commit()

    # 获取更新的记录数
    cursor.execute("SELECT COUNT(*) FROM studyinfo WHERE DEPTSTUDYID IS NOT NULL")
    updated_count = cursor.fetchone()[0]

    # 记录更新操作到日志文件
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"Updated {updated_count} records.\n")
        log_file.write(f"Update Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"Update completed. {updated_count} records updated.")

except cx_Oracle.Error as e:
    # 错误处理
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    # 关闭游标和连接
    cursor.close()
    conn.close()

# 注意：这个脚本没有记录每个受影响记录的详细信息（如旧值和新值），因为这需要更复杂的逻辑。
# 如果需要记录每个记录的详细信息，你可能需要在更新之前查询这些值，并在更新之后将它们写入日志文件。
