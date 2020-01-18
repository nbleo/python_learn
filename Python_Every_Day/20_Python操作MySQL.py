import pymysql

# 创建MySQL链接
connection = pymysql.connect(host="127.0.0.1",
                             port=3306,
                             user="leo",
                             password="lrabt004",
                             db="test_data",
                             charset="utf8mb4")

# 创建cursor, 用于执行sql

cursor = connection.cursor()

# 增加两条记录
insert_sql = "insert into fund_info (account, amount) values ('abc@163.com', 100.00)"
insert_sql1 = "insert into fund_info (account, amount) values ('zxc@163.com', 99.00)"

# 执行上面两个sql

cursor.execute(insert_sql)
cursor.execute(insert_sql1)

# 未链接成功
