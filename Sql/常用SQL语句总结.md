

### SQL介绍

SQL是一种结构化的数据库查询和程序设计的编程语言，用于存取数据以及查询、更新和管理数据库。SQL分为4大类：数据定义语言(DDL)、数据操纵语言(DML)、数据查询语言(DQL)和数据控制语言(DCL)

- 数据定义语言(DDL)是对数据库和表进行定义，关键字有create/alter/drop/truncate
    
- 数据操纵语言(DML)是对表中的记录进行增删改的操作，关键字有insert/update/delete
    
- 数据查询语言(DQL)是对表中的记录进行查询的操作，关键字是selete
    
- 数据控制语言(DCL)是对数据库的用户、权限、事务等进行操作，关键字有grant/revoke/commit/set/rollback等
    

本文使用的是：MySQL-8.0.26

SQL中的关键字不区分大小写

### 登录数据库

在命令窗口连接数据使用，使用以下命令

登录本地数据库`mysql -u root -p`，输入数据库密码

登录远程数据库：`mysql -h ip地址 -u 用户名 -p`，输入数据库密码

可以使用远程工具进行连接数据库，例如：Navicat、PyCharm、IDEA、VSCode等，都有联想提示，写SQL语句更方便

### 数据库操作

#### 数据库的增删改查操作

```sql
SHOW DATABASES;			# 查看所有数据库
CREATE DATABASE dyd;	# 使用默认参数创建名为dyd的数据库
CREATE DATABASE dyd DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;	# 创建UTF-8字符编码的数据库
ALTER DATABASE dyd DEFAULT CHARACTER SET gbk;	# 修改数据库字符编码为GBK
USE dyd;				# 使用数据库
SHOW TABLES;			# 查看当前数据库下所有表
DROP DATABASE dyd;		# 删除数据库
```

#### 数据表的增删改查操作

```sql
CREATE TABLE workers (	# 创建名为workers的数据库表，并对数据库字段进行约束，对表字段进行备注
	id INT PRIMARY KEY AUTO_INCREMENT,				 # 主键，自增长约束
	sid INT UNIQUE COMMENT '员工id',					# 唯一约束
	sname VARCHAR (20) NOT NULL COMMENT '姓名',		# 非空约束
	gender VARCHAR (2) DEFAULT '-1' COMMENT '1表示男，0表示女，-1表示未知',	# 默认值约束
    IDNum VARCHAR (20) NOT NULL UNIQUE COMMENT '身份证号码',	# 非空,唯一约束
	birthday DATE COMMENT '生日',
	email VARCHAR (20) COMMENT '邮箱',
	remark VARCHAR (50) COMMENT '备注'
) DEFAULT CHARSET = utf8 COMMENT = '员工信息表';		# 默认字符编码使用UTF-8

DESCRIBE workers;	# 查看表结构
ALTER TABLE workers ADD COLUMN age INT (20) COMMENT '年龄';		# 添加一个表字段
ALTER TABLE workers ADD a INT,ADD b CHAR(2),ADD c FLOAT(5,2);	 # 一次添加多个表字段
ALTER TABLE workers MODIFY COLUMN gender INT(2);	# 修改表字段gender类型为INT(2)
ALTER TABLE workers CHANGE COLUMN gender sex INT(2);# 修改表字段名gender为sex
ALTER TABLE workers DROP COLUMN c;					# 删除一个表字段
ALTER TABLE workers DROP COLUMN a,DROP COLUMN b;	# 一次删除多个表字段
ALTER TABLE workers RENAME TO employees;			# 修改表名workers为employees
DROP TABLE employees;								# 删除表
```

### 数据操作

#### 插入数据

```sql
# 单条全量插入数据时，需根据表结构的字段顺序赋值
INSERT INTO workers VALUES(1,00001,'小白典',1,'410928200207196688','2002-07-19','8@qq.com','#');
# 给指定字段插入数据，插入值的顺序需根据指定字段顺序赋值，指定字段添加时不可缺少有非空约束的字段，即不插入的字段可为null
INSERT INTO workers (sid,sname,IDNum) VALUES(00002,'小段','410928200407196688');
# 批量插入数据，跟插入单条数据一样，注意字段顺序，每组数据英文逗号分隔
INSERT INTO workers (sid,sname,IDNum) VALUES
(00003,'小天',410928200507196688),
(00004,'小白',410928200607196688),
(00005,'小黑',410928200707196688);
```

#### 修改数据

```sql
# 修改sid为00003的sname为‘小彩’
UPDATE workers SET sname = '小彩' WHERE sid = 000003;
# 修改sid为00003的姓名为‘小菜’，备注为‘试用中’
UPDATE workers SET sname = '小菜',remark = '试用中' WHERE sid = 000003;
# 修改birthday字段所有数据为‘2002-06-06’
UPDATE workers SET birthday = '2002-06-06';
# 修改birthday字段所有数据为‘2002-08-08’，email字段所有数据为‘8@qq.com’
UPDATE workers SET birthday = '2002-08-08',email = '8@qq.com';
```

**跨表更新**

跟下文介绍的多表查询类似，若初次学习SQL，建议先跳过此部分，update至set之间就是两表联查时用到的语句，set后是要修改的值，where后是判断条件，可以理解为先把两张表合并为一张表，然后修改此表

```sql
# 更新a表中totalSales字段的值，等于a表中的单价乘以a表中的销量，然后加上b表中的等级
UPDATE sales a LEFT JOIN workers b USING(sid) SET a.totalSales=a.price*a.saleVolume+b.levels;
# 当满足ab两表id相等时，更新a表的productID等于b表的id
UPDATE sales a LEFT JOIN product b ON a.id=b.id SET a.productID=b.id WHERE a.id=b.id;
UPDATE sales a LEFT JOIN product b USING(id) SET a.productID=b.id WHERE a.id=b.id;	# 或者使用using
```

#### 删除数据

```sql
# 删除id为4的员工
DELETE FROM workers WHERE id = 4;
# 删除所有表数据，此方式清理数据，不影响自增长约束，数据库依然会记录当前增长到哪里
DELETE FROM workers;
# 截断表，又叫重置表，此方式清空表只保留表结构，自增长约束也会重新开始，相当于删除表后再新建的表
TRUNCATE TABLE workers;
```

**跨表删除**

跟update…join类似，若初次学习SQL，建议先跳过此部分，在一个sql语句中同时删除多个表的记录，也可以根据多个表之间的关系来删除某一个表中的记录

```sql
# 删除ab两表中id等于7的一行数据
DELETE a.*,b.* FROM sales a LEFT JOIN workers b ON a.id=b.sid WHERE a.id=7 AND b.sid=7;
# 当a表id等于b表sid时，删除a表中id等于7的一行数据
DELETE a FROM sales a LEFT JOIN workers b ON a.id=b.sid WHERE a.id=7;
```

#### 查询数据

**简单查询**

```sql
SELECT * FROM workers;	# 查询workers表中所有信息
SELECT sid '编号',sname AS '姓名' FROM workers;	# 查询workers表中的sid和sname，表头使用别名，AS可有可无
SELECT CONCAT(sname,'-',sid) AS '姓名-编号' FROM workers;	# 使用函数concat合并列，使结果合并为一个字符串
```

**条件查询**

```sql
SELECT sid+id FROM workers;					# 支持算数运算，加(+)、减(-)、乘(*)、除(/)、取余(%)
SELECT sname FROM workers WHERE age < 20;	# 查询年龄小于20的员工姓名，支持比较运算（<、>、<=、>=、（!=、<>））
SELECT sid,sname FROM workers WHERE age BETWEEN 18 AND 20;	# 查询年龄在18~20的员工编号和姓名，包含18和20岁
SELECT sid,sname FROM workers WHERE age NOT BETWEEN 18 AND 20;	# 查询不在18~20岁之间的员工编号和姓名
SELECT sname FROM workers WHERE sname IN('小段','小白','小红');	# 查询在集合中的员工姓名，不在集合中则使用NOT IN
SELECT sid FROM workers WHERE sname LIKE '小%';	# 模糊查询，查询名称以‘小’开头的员工id，%(匹配多个字符)
SELECT sid FROM workers WHERE sname LIKE '_段'; # 查询名称不是以‘段’结尾的员工id，_(匹配1个字符，可多个一起使用)
SELECT sname FROM workers WHERE email IS NULL;	# 查询邮箱为空的员工姓名，is not null与之相反
SELECT sname FROM workers WHERE email IS NOT NULL AND sname LIKE '小_';	# 查询邮箱非空且名称以‘小’开头的两字姓名
SELECT sname FROM workers WHERE id = 1 OR sid = 00002;	# 查询id为1或者sid为00002的员工姓名，同时满足则结果都返回
SELECT id FROM workers WHERE (sid=1 AND age<20) OR age>=22;	# 查询sid为1且年龄小于18，或者年龄大于等于20的员工id
SELECT DISTINCT sname FROM workers WHERE age>18;	# 查询年龄大于18的员工姓名，进行去重处理
select c.atitle,d.atitle,e.atitle from china c,china d,china e	# 查询河南省市区
where c.aid=d.pid 
and d.aid=e.pid 
and c.atitle='河南省';
```

**聚合查询**

```sql
SELECT MAX(saleVolume) FROM sales;	# 最大值，查询最大销量
SELECT MIN(saleVolume) FROM sales;	# 最小值，查询最低销量
SELECT AVG(saleVolume) FROM sales;	# 平均值，查询平均销量
SELECT SUM(saleVolume) FROM sales;	# 求和，查询总销量
SELECT COUNT(sid) FROM sales WHERE saleVolume IS NOT NULL;	# 计数，查询共有多少员工有销量
SELECT SUM(price*saleVolume) '总销售额' FROM sales;	# 计算总销售额，并设置表头别名为‘总销售额’
SELECT SUM(price*saleVolume)/COUNT(sid) FROM sales WHERE productID=1;	# 查询电脑的平均销售额
SELECT SUM(price*saleVolume) FROM sales WHERE MONTH(date)=04;	# 查询4月份的销售额
```

**分组查询**

一般与聚合查询结合使用，针对分组去做聚合查询，分组后可以使用聚合查询对结果进行筛选，分组后的条件判断使用having，然后跟聚合查询条件，支持在分组之后再次分组

```sql
SELECT SUM(price*saleVolume) FROM sales GROUP BY salesGroup;	# 查询各小组的销售额
SELECT salesGroup,AVG(saleVolume) FROM sales GROUP BY salesGroup;	# 查询各销售小组的平均销量
SELECT salesGroup,AVG(saleVolume) FROM sales GROUP BY sid,salesGroup;	# 查询结果先根据员工分组，再根据小组分组
SELECT salesGroup,SUM(saleVolume) FROM sales WHERE price=5600 GROUP BY salesGroup;	# 查询各小组的总销量
SELECT salesGroup,COUNT(sid) FROM sales GROUP BY salesGroup HAVING COUNT(sid)<3;	# 统计销售人数低于3的小组
```

**排序查询**

```sql
SELECT * FROM sales ORDER BY saleVolume DESC;	# 查询结果根据销量降序排列
SELECT * FROM sales ORDER BY saleVolume ASC;	# 查询结果根据销量正序排列，正序排列可以省列ASC
SELECT * FROM sales ORDER BY price,saleVolume DESC;	# 先根据单价降序排列，再根据销量降序排列
SELECT * FROM sales ORDER BY price DESC,saleVolume ASC;	# 先根据单价降序排列，再根据销量正序排列
SELECT * FROM sales WHERE saleVolume>5 ORDER BY price;	# 根据单价正序排列，有where条件时，排序应在where之后
```

**分页查询**

截取查询结果集中的一部分，第一个数字表示偏移量，即查询的起始位置到第一行数据的差的行数，第一行为0，第二个表示步长，即每次显示多少条结果。当有where条件、分组、排序和分页时，先根据条件查询结果集，再进行分组，然后进行排序，最后再分页查看

```sql
SELECT * FROM sales LIMIT 0,2;	# 查询前两条数据
SELECT * FROM sales LIMIT 2,4;	# 查询结果为从第3条数据开始之后的4条数据(包括第3条数据)
SELECT * FROM sales WHERE price=5600 ORDER BY saleVolume DESC LIMIT 1,3;	# 先判断再排序最后分页
```

查询中若有where、group by(包含having)、order by、limit，使用顺序是`where`→`group by`→`order by`→`limit`，如下示例

```sql
# 查询各小组的销售量，输出小组名称和销售量，结果根据单价进行降序排列，且只查看查询结果中的第二和第三条数据
SELECT salesGroup,SUM(saleVolume) FROM sales WHERE price=5600 GROUP BY salesGroup ORDER BY price DESC LIMIT 1,2;
```

通过上面的练习操作可以看出where和having的区别：

- where子句是在group by分组和数据汇总之前对数据进行过滤的
    
- having子句是在group by分组和数据汇总之后对数据进行过滤的
    

**子查询**

```sql
# 查询id为2的员工姓名和销售量
SELECT sname '姓名',(SELECT saleVolume FROM sales WHERE sid=2) '销售量' FROM workers WHERE sid=2;	
# 查询id为2的员工姓名、销售额及销售的商品
SELECT sname '姓名',(SELECT SUM(price*saleVolume) FROM sales WHERE sid=2) '销售额',
	(SELECT productName FROM product WHERE productID IN(SELECT productID FROM sales WHERE sid=2)) '销售商品' 
FROM workers WHERE sid=2;
# 查询id为2的员工姓名及其在销售部的销售占比
SELECT sname '姓名',
	(SELECT SUM(price*saleVolume) FROM sales WHERE sid=2)/(SELECT SUM(price*saleVolume) FROM sales)*100 '销售额占比(%)'
FROM workers WHERE sid=2;	
# 若子查询有结果则返回产品表中的产品名称，exists()返回的是一个布尔值，ture或flase，not exists()与之相反
SELECT productName FROM product WHERE EXISTS(SELECT productID FROM sales);
# 查询所有销量低于15的员工ID，然后查询大于最大员工ID的员工姓名，这里的all取得就是子查询中的最大值
SELECT sname '姓名' FROM workers WHERE sid >ALL(SELECT sid FROM sales WHERE saleVolume<15);
# 查询所有销量低于15的员工ID，然后查询大于子查询中获取的任意员工ID的员工姓名，这里的any取子查询中的所有值
SELECT sname '姓名' FROM workers WHERE sid >ANY(SELECT sid FROM sales WHERE saleVolume<15);
# 表达意思与上一条相同，any和some是等价的，表达的含义一样
SELECT sname '姓名' FROM workers WHERE sid >SOME(SELECT sid FROM sales WHERE saleVolume<15);
```

**多表联查**

查询多张表一般用到的连接方法有：内连接：inner join；外连接：left join，right join，union；交叉连接：cross join

内连接又叫做等值连接、自然连接，作用是根据两个或多个表中列之间的关系，然后从这些表中查询数据，内连接只匹配行

外连接又分为左连接、右连接及合并连接，此连接方式至少有一方保留全部数据，没有匹配行会用null代替

交叉连接又叫做笛卡尔积连接，查询结果会返回左表中的所有行，右表中的行会与左表中的每一行进行组合

```sql
# inner join为内连接，可以简写为join，查询的是两张表的交集部分，即取得两个表中存在连接匹配关系的数据
SELECT * FROM workers a INNER JOIN sales b ON a.sid=b.sid;	# 两表联查
SELECT * FROM workers a JOIN sales b ON a.sid=b.sid JOIN product c ON b.productID=c.productID;	# 三表联查
# 查询级别为2的员工的姓名和销售量
SELECT a.sname,b.saleVolume FROM workers a JOIN sales b ON a.sid=b.sid WHERE levels=2;
# left join为左连接，又叫左外连接，取得左表的所有数据，右表如果有条件相符合的数据就匹配，否则为null
SELECT * FROM workers a LEFT JOIN sales b ON a.sid=b.sid;
SELECT * FROM workers a LEFT JOIN sales b ON a.sid=b.sid LEFT JOIN product c ON b.productID=c.productID;
# 使用左连接同样能够查询到级别为2的员工的姓名和销售量
SELECT a.sname,b.saleVolume FROM workers a LEFT JOIN sales b ON a.sid=b.sid WHERE levels=2;
# right join为右连接，与左连接相反，以右表为基础，根据on后面的条件匹配数据
SELECT * FROM workers a RIGHT JOIN sales b ON a.sid=b.sid;
SELECT * FROM workers a RIGHT JOIN sales b ON a.sid=b.sid RIGHT JOIN product c ON b.productID=c.productID;
# 此处使用右连接同样能够查询到级别为2的员工的姓名和销售量，具体以实际表数据为准，并非使用inner/left/right都能查到相同的数据
SELECT a.sname,b.saleVolume FROM workers a RIGHT JOIN sales b ON a.sid=b.sid WHERE levels=2;
# union为合并连接，用于合并两个或多个select语句，查询结果为进行去重处理后而派生出一个结果集，注意：查询的多张表列数必须一致
SELECT * FROM sales UNION SELECT * FROM sales_copy;
# 当all随union一起使用时（即UNION ALL），查询结果不会进行去重处理，重复行会正常显示
SELECT * FROM sales UNION ALL SELECT * FROM sales_copy;
# CROSS JOIN为交叉连接，取得左表的所有数据，右表中的数据会与左表中的每一行进行组合
SELECT * FROM sales b CROSS JOIN workers a ON b.sid=a.sid;
```

若两个判断键值同名，则可以使用using代替on，内连接、外连接和交叉连接都可以使用，如下示例

```sql
SELECT * FROM workers a LEFT JOIN sales b ON a.sid=b.sid;
SELECT * FROM workers LEFT JOIN sales USING(sid);	# 可以使用using代替上面的on判断
SELECT * FROM sales a LEFT JOIN product b ON a.id=b.id AND a.productID=b.productID;
SELECT * FROM sales a LEFT JOIN product b USING(id,productID);	# 只要键值同名，多条判断也可以使用using
SELECT * FROM workers a LEFT JOIN sales b ON a.sid=b.id;	# 此条SQL因为键不同名，所以不能使用using
```

#### 存储过程

存储过程是指带有处理业务逻辑的SQL语句，就像使用java、python等代码实现业务逻辑并操作数据库一样，存储过程就是只用数据库的语法实现此操作，简单说，就是一组为了完成特定功能的SQL语句集

因为存储过程是在数据库的服务端执行的，所以具有执行效率快的特点，只有首次执行时需要经过编译和优化步骤，后续被调用可以直接执行，但是移植性太差，不同数据库的存储过程不能移植，而且消耗数据库服务器的资源，工作中用的比较少，所以此处简单总结一下

**创建存储过程**

示例如下

```sql
delimiter $						# 存储过程开始识别符，后面符号使用$、//、$$都可以
CREATE PROCEDURE FindProduct()	# 创建名为FindProduct的存储过程
BEGIN
SELECT * FROM product;			# 要执行的SQL语句
END $;							# 存储过程结束，后面符号要与开始时使用的符号一致
```

**执行存储过程**

使用call执行存储过程

```sql
CALL FindProduct();	# 以后查看product产品表数据，执行此SQL即可
```

**查看存储过程**

```sql
SHOW PROCEDURE STATUS;			# 会显示所有数据库中的存储过程，包括mysql系统的
```

**删除存储过程**

```sql
DROP PROCEDURE test_loop;		# 删除存储过程test_loop
```

**存储过程出入参**

1. 存储过程入参 - in
    
    定义输入参数，使用“in 参数名 数据类型”定义入参
    
    ```sql
    delimiter $
    CREATE PROCEDURE Findoneproduct(IN pname VARCHAR(10))	# 使用“in 参数名 数据类型”定义参数
    BEGIN
    SELECT * FROM product WHERE productName=pname;	# 调用参数
    END $;
    ```
    
    定义多个入参
    
    ```sql
    delimiter $
    CREATE PROCEDURE Find_id_pro(IN pid INT(10),uid INT(5))	# 多个参数使用英文逗号分隔
    BEGIN
    SELECT						# 根据传入的商品id和员工id，查询员工的姓名、所销售的商品名及对应的销售额
    	b.sname '员工姓名',
    	a.productName '商品名称',
    	c.price * c.saleVolume '销售额'
    FROM product a
    LEFT JOIN workers b USING (id)
    JOIN sales c USING (sid)
    WHERE
    	a.productID = pid AND b.sid = uid ;
    END $;
    ```
    
    执行上面的创建的存储过程
    
    ```sql
    CALL Find_id_pro(0,2);	# 根据定义的参数，按顺序传参
    ```
    
2. 存储过程出参 - out
    
    定义输出参数，和输入类似，使用out表示出参，出入参可以一起使用
    
    ```sql
    delimiter $
    CREATE PROCEDURE emp(IN emp_id INT,OUT emp_name VARCHAR(30))	# 使用“out 参数名 数据类型”定义出参
    BEGIN
    SELECT sname INTO emp_name FROM workers WHERE sid=emp_id;	# 传入员工id后返回员工姓名，将结果赋值emp_name参数
    END $;
    ```
    
    执行上面创建的存储过程
    
    ```sql
    CALL emp(2,@emp_name);	# 按顺序传参，传入员工id，返回员工姓名，名字前需加@符号
    SELECT @emp_name;		# 查看出参结果
    ```
    
3. 存储过程出入参 - inout
    
    inout具有in和out双重功能，既可以使用传入变量的值也可以使用修改变量后的值
    
    ```sql
    delimiter $	# # 使用“out 参数名 数据类型”定义出参
    CREATE PROCEDURE saleinfo(INOUT uid INT,INOUT sal_price INT(2),INOUT sal_vol INT(2),INOUT sal_total INT(2))
    BEGIN
    SELECT price INTO sal_price FROM sales WHERE sid=uid;		# 传入用户id获取其销售商品的单价
    SELECT saleVolume INTO sal_vol FROM sales WHERE sid=uid;	# 传入用户id获取其销售商品的销量
    SET sal_total = sal_price * sal_vol;						# 计算销售额
    END $;
    ```
    
    执行上面创建的存储过程
    
    ```sql
    SET @uid = 2;# 员工id不是通过查询获得的，需要自己赋值时使用set给变量初始值
    CALL saleinfo(@uid,@sal_price,@sal_vol,@sal_total);	# 调用变量，uid已经赋值，其它参数通过查询计算获取
    SELECT @uid,@sal_price,@sal_vol,@sal_total;	# 查看获取的结果
    ```
    

##### 流程控制

使用if…elseif…else进行流程控制，使用方式与python中代码类似，如下示例

```sql
delimiter $
CREATE PROCEDURE if_age( IN age INT)				# 定义入参
BEGIN
DECLARE str VARCHAR(20) DEFAULT NULL;				# 声明内部变量，设置数据类型，默认为空
IF age<18 THEN SET str='未成年人';
ELSEIF age>=18 AND age<=65 THEN  SET str='青年人';
ELSEIF age>65 AND age<=99 THEN  SET str='老年人';
ELSE  SET str= '哇哦！高寿啊！';
END IF;
SELECT str;			# 打印变量名
END $;

CALL if_age(100);	# 执行存储过程，传入年龄返回相应变量值，返回'哇哦！高寿啊！'
```

##### 三种循环

###### while循环

```sql
drop procedure if exists test_while;				# 如果名为test_while的存储过程存在则删除
delimiter $
CREATE PROCEDURE test_while (IN i INT)				# 创建名为test_while的存储过程，参数为i
BEGIN
WHILE i < 10 DO										# 当i小于10时跳出while循环
	INSERT INTO product (productID) VALUES(i + 4);	# 往product表插入数据
SET i = i + 1 ;					# 每次循环i+1
END WHILE ;						# 结束while循环
SELECT productID FROM product;	# 查看插入字段的数据
END $; 

CALL test_while(6)		# 执行存储过程
```

###### repeat循环

```sql
drop procedure if exists test_repeat;				# 如果名为test_repeat的存储过程存在则删除
delimiter $
CREATE PROCEDURE test_repeat()						# 创建名为test_repeat的存储过程，无参数
BEGIN
DECLARE i INT;										# 声明变量，即参数，也可以以此种方式定义参数
SET i = 0;											# 给变量赋值，默认值
REPEAT
	INSERT INTO product (productID) VALUES(i + 4);
SET i = i + 1; 
UNTIL i < 10 END REPEAT; 							# 直到当i小于10时跳出repeat循环
SELECT productID FROM product;
END $;

CALL test_repeat();		# 因为已经给默认值，所有调用存储过程参数可为空
```

###### loop循环

```sql
drop procedure if exists test_loop;					# 如果名为test_loop的存储过程存在则删除
delimiter $
CREATE PROCEDURE test_loop()						# 创建名为test_loop的存储过程，无参数
BEGIN
DECLARE i INT;										# 定义变量
SET i = 0; 											# 设置变量默认值
yd:LOOP												# yd为自定义的循环体名, loop是关键字
	INSERT INTO product (productID) VALUES(i + 4);
SET i = i + 1;
IF i < 10 THEN LEAVE yd;			当i小于10时离开yd循环体，即跳出循环，leave表示离开循环体，iterate表示退出当前循环继续下一个循环
END IF;
END LOOP; 
SELECT productID FROM product;
END $;

CALL test_loop();		# 因为已给默认值，所有执行存储过程参数为空时使用默认值
```

#### 触发器

当操作了某张表时，希望同时触发一些其它的行为动作，就可以使用触发器完成，可以保证数据的完整性，起到约束作用，比如向产品表添加数据之后向日志表中新增一条数据

```sql
CREATE TRIGGER tri_log 	# 创建一个名为tri_log的触发器
AFTER INSERT 		# 插入之后触发，还有after update/delete,before insert/update/delete 5种操作
ON product 			# 触发事件表名，表示哪张表有插入数据时执行此触发器
FOR EACH ROW		# 表示任何一条记录上的操作满足触发事件都会触发此触发器
BEGIN
	INSERT INTO oper_log (content, time)VALUES('新增了一条添加产品记录',SYSDATE());	# 触发器执行的SQL语句
END ;
```

当执行向产品表插入数据时，日志表也会新增一条记录

```sql
INSERT INTO product VALUES(6,8,'桌椅','https://www.dyd.com');	# 向产品表新增一条数
SELECT * FROM oper_log;		# 查看操作日志，会新增一条记录
```

**查看触发器**

```sql
SHOW TRIGGERS;
```

**删除触发器**

```sql
DROP TRIGGER tri_log;	# 删除名为tri_log的触发器
```

#### 函数

**常用内置函数**

1. case函数
    
    case函数能够实现复杂的逻辑判断，跟代码中的if...else功能类似，使用方法如下示例
    
    ```sql
    SELECT	# 查询员工id，姓名和性别
    	sid '员工ID',sname '姓名',
    	( CASE gender
    		WHEN 0 THEN '女'	# 查询结果为0则返回‘女’
    		WHEN 1 THEN '男'	# 查询结果为1则返回‘男’
    		ELSE '未知'		# 其它结果则返回‘未知’
    		END ) '性别'		# 表头设置别名为性别
    FROM workers;
    ```
    
    还可以使用判断条件
    
    ```sql
    SELECT	# 查询员工id，姓名和年龄段
    	sid '员工ID',sname '姓名',
    	( CASE
    		WHEN age >= 65 THEN '老年人'	# 查询年龄大于等于65则返回‘老年人’
    		WHEN age >= 18 THEN '青年人'	# 查询年龄大于等于18则返回‘青年人’
     		ELSE age		  # 否则返回实际年龄
    		END ) '年龄段'		# 表头设置别名为身份证号码
    FROM workers;
    ```
    
2. if()函数
    
    if函数可以理解为case函数的简化版，若只是简单的逻辑判断，IF函数才更适合，使用方法如下示例
    
    ```sql
    # 查询员工id、姓名，判断性别是否正确，性别为0或1则返回‘正常性别’，否则返回‘未知性别’
    SELECT sid,sname,IF(gender=0 OR gender=1,'正常性别','未知性别') FROM workers;
    # 查询员工id、姓名，判断邮箱是否已填写，邮箱为空则返回提示信息，否则返回已有的邮箱
    SELECT sid,sname,IF(email IS NULL,'邮箱为空，请及时完善',email) FROM workers;
    # 上面的判空语句可以简写为以下方式，使用ifnull进行判断
    SELECT sid,sname,IFNULL(email,'邮箱为空，请及时完善') FROM workers;
    ```
    
3. substring_index()函数
    
    substring_index函数用来按分隔符截取字符串，如下示例
    
    ```sql
    SELECT SUBSTRING_INDEX(salesURL,'/',-1) FROM product;	# 从http://www.dyd.com/d166中截取d166
    SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(salesURL,'/',3),'//',-1) FROM product;	# 截取www.dyd.com
    ```
    
4. concat()函数
    
    concat函数可以连接一个或者多个字符串，如下示例
    
    ```sql
    SELECT CONCAT(price,'*',saleVolume,'=',price*saleVolume) FROM sales;	# 计算销售额，结果为5*20=100
    ```
    
5. 大小写转换函数
    
    ```sql
    # 查询workers表中email和名称全拼，并把email转为大写显示，全拼转为小写显示
    SELECT UPPER(email),LOWER(fullpin) FROM workers;
    ```
    
6. 时间函数
    
    处理时间的函数有很多，比如获取当前时间，获取年月日，时分秒，计算周数，计算当日是周几等，周几是从0开始的，即查出0表示当天是周一
    
    ```sql
    # 获取当前时间(年月日时分秒)，当前日期(年月日)，当前时间(时分秒)，当前系统时间(年月日时分秒)
    SELECT NOW(),CURDATE(),CURTIME(),SYSDATE();
    # 获取workers表中birthday字段的年月日，并计算是当年的第几周，当天是周几
    SELECT NOW(),YEAR(birthday),MONTH(birthday),DAY(birthday),WEEK(birthday),WEEKDAY(birthday) FROM workers;
    # 获取sales表中销售时间的年月日时分秒
    SELECT YEAR(saledate),MONTH(saledate),DAY(saledate),HOUR(saledate),MINUTE(saledate),SECOND(saledate) FROM sales;
    ```
    
7. 聚合函数
    
    上文中的聚合查询用到的也是内置的聚合函数
    
    ```sql
    sum(),avg(),max(),min(),count()
    ```
    

**自定义函数**

还可以自定义函数，如下示例

```sql
CREATE FUNCTION sel_totalsale(uid INT) RETURNS INT		# 创建一个名为sel_totalsale的函数
BEGIN
 DECLARE totalSale INT DEFAULT 0;	# 声明局部名为totalSale的变量，默认为1
 SELECT SUM(price*saleVolume) INTO totalSale FROM sales WHERE sid=uid;	# 查询员工销售额，赋值给变量totalSale
 RETURN totalSale;					# 返回totalSale变量的值
END;
```

**调用自定义函数**

```sql
SELECT sel_totalsale(5);		# 查询员工编号为5的销售额
```

**删除自定义函数**

```sql
DROP FUNCTION sel_totalsale;	# 删除名为sel_totalsale的自定义函数
```

#### 索引

索引的建立对于MySQL的高效运行至关重要，索引可以大大提高MySQL的检索速度，创建表时基本都会有一个id作为主键，会作为主键索引使用，在创建表的同时也可以创建索引，如下示例

```sql
CREATE TABLE tab_index (
	id INT PRIMARY KEY AUTO_INCREMENT,	# 作为主键索引
	sid INT, 
    sname VARCHAR(10),
	content VARCHAR(20),
	ustatus VARCHAR(10),
	INDEX sid_index (sid),	# 创建名为sid_index的索引
	INDEX (content)			# 创建名为content的索引，因为没有设置索引名，所以会自动将字段名作为索引名
) DEFAULT CHARSET = utf8 COMMENT = '创建包含索引的表';
```

**单独创建索引**

```sql
# 使用create命令创建索引
CREATE INDEX sta_index ON tab_index(ustatus);	# 使用tab_index表中ustatus字段创建名为sta_index索引
CREATE INDEX sta_index ON tab_index(ustatus,sname);		# 创建复合索引
CREATE UNIQUE INDEX sta_index ON tab_index(ustatus);	# 创建唯一索引
# 使用alter命令创建索引
ALTER TABLE tab_index ADD INDEX name_index (sname);
ALTER TABLE tab_index ADD UNIQUE INDEX (sid);
```

**删除索引**

```sql
DROP INDEX sname ON tab_index;				# 删除tab_index表中名为sname的索引
ALTER TABLE tab_index DROP INDEX sname;		# 或者使用此方式删除
ALTER TABLE sname DROP PRIMARY KEY;			# 删除主键索引
```

**索引失效**

在一些条件下索引会失效，所以在查询时应尽量避免，比如以下情况

- 索引本身失效
    
- 使用like查询时以通配符(%)开头，索引会失效，变成全表扫描
    
- 查询条件中带有`or`，除非所有的查询条件都建有索引，否则索引会失效
    
- 索引列的值参与计算，索引会失效，可以先将参与计算的数值算好再查询
    
- 违背最左匹配原则，比如创建了组合索引(sid,sname)，当查询条件没有sid时索引会失效
    
- 字符串不加单引号也会导致索引失效，等还有其它情况请自行了解
    

### 性能分析

用法：`explain+SQL语句`，用于解释SQL语句，是我们通常讲的SQL语句优化基础，通常检查`type`字段，排序为：all<index<range<ref<eq_ref<const<system，一般情况下至少要达到range级别，最差也要达到index，以下面的SQL为例

```sql
EXPLAIN SELECT sname '姓名',
	(SELECT SUM(price*saleVolume) FROM sales WHERE sid=2)/(SELECT SUM(price*saleVolume) FROM sales)*100 '销售额占比(%)'
FROM workers WHERE sid=2;
```

创建以下索引后type类型由ALL变为ref

```sql
CREATE INDEX idx_sid ON sales(sid);
```

### 用户管理

**查看用户**

```sql
SELECT * FROM mysql.user;	# 查看用户和相关权限信息
```

**创建用户**

```sql
CREATE USER 'dy'@'%' IDENTIFIED BY '123456';	# 创建dy用户，该用户可访问任意IP数据库
CREATE USER 'dyd'@'localhost' IDENTIFIED BY '123456';	# 创建dyd用户，密码为123456，指定该用户只能访问本地数据库
CREATE USER 'yd'@'192.166.66.23' IDENTIFIED BY '123456';	# 创建yd用户，该用户只能在IP地址为.23的主机上访问数据库
CREATE USER 'yd'@'192.166.66.23,192.166.66.24' IDENTIFIED BY '123456';	# 多个IP地址用逗号分隔
```

**修改用户名**

```sql
UPDATE mysql.user SET USER='yadian' WHERE user='dy';	# 修改dy用户名为yadian
FLUSH PRIVILEGES;	# 刷新权限，否则修改可能不生效
```

**修改用户密码**

```sql
ALTER USER 'dy'@'%' IDENTIFIED BY '654321';	# 把host为%，用户名为dy的密码改为654321
FLUSH PRIVILEGES;	# 刷新权限，否则修改可能不生效
```

**删除用户**

```sql
DROP USER yadian;	# 删除名为yadian的用户
DELETE FROM mysql.user WHERE user = 'yd';	# 也可是使用此方式删除，但是不推荐，系统会有残留信息
```

### 权限管理

用户创建后，能够对数据库做哪些操作，需要通过权限管理完成

**查看用户权限**

```sql
SHOW GRANTS FOR 'dyd'@'localhost';	# 查看host为localhost，用户名为dyd的权限
```

**授权**

```sql
GRANT SELECT ON *.* TO 'dyd'@'%' WITH GRANT OPTION;			# 给用户dyd查询权限，并且可以给其它用户授予当前权限
GRANT ALL PRIVILEGES ON *.* TO 'dyd'@'%' WITH GRANT OPTION;	# 给用户dyd所有权限，并且可以给其它用户授予权限
GRANT SELECT,UPDATE,INSERT,DELETE ON *.* TO 'dyd'@'%';		# 给dyd用户查询增删改查的权限，但不能给其它用户授权
GRANT SELECT,INSERT ON dyd.workers TO 'duanyd'@'%';	# 只给duanyd用户操作dyd数据库中workers表的查询和插入数据权限
GRANT SELECT ON dyd.* TO 'duanyd'@'%';				# 给duanyd用户查询dyd数据库中所有表的权限
FLUSH PRIVILEGES;	# 每次授权后需刷新权限，否则权限可能不生效
```

**撤销权限**

```sql
REVOKE DELETE ON *.* FROM 'dyd'@'%';			# 撤销dyd用户的删除权限
REVOKE ALL PRIVILEGES ON *.* FROM 'dyd'@'%';	# 撤销dyd用户的所有权限
```

在SQL语句后分号改为`\G`，表示将查询结果按列打印，可以使每个字段打印到单独的行，对于在表字段较多，命令行窗口查询结果凌乱时建议使用，查询结果更加一目了然，如下图所示

![](http://r.photo.store.qq.com/psc?/V54C2OLx3pQy8a0fgch71esxCP2J9hMe/TmEUgtj9EK6.7V8ajmQrEEiNDOFG.le6EbkPnIKUG7bkMW6kK30f3HpscnZBP7lyqLYXZ36g51FTBxEqaQjiULqCh3iNVL5Q9TYqmVGAXkU!/r)

### 踩过的坑

1. 创建函数报`This function has none of DETERMINISTIC, NO SQL, or READS SQL DATA in its declaration and binary logging is enabled (you *might* want to use the less safe log_bin_trust_function_creators variable)`，这是因为开启了bin-log，必须先给function指定一个参数
    
    **解决办法：**
    
    先执行以下语句，再执行创建函数的SQL语句
    
    ```sql
    set global log_bin_trust_function_creators=TRUE;
    ```
    
2. 创建用户报`Your password does not satisfy the current policy requirements`，这是因为默认密码策略为中，要求较高，可以降低密码策略等级并缩短密码长度
    
    **解决办法：**
    
    - 查看 mysql 初始的密码策略
        
        ```sql
        SHOW VARIABLES LIKE 'validate_password%'
        ```
        
    - 设置密码的验证强度等级，设置 validate_password.policy 的全局参数为LOW
        
        ```sql
        SET GLOBAL validate_password.policy=LOW;
        ```
        
    - 修改密码长度，设置 validate_password.length 的全局参数为6
        
        ```sql
        SET GLOBAL validate_password.length=6;
        ```
        
        之后简单的密码就可以设置啦
        
3. 给非root用户授权报`You are not allowed to create a user with GRANT`，因为root缺少系统权限
    
    **解决办法：**
    
    先授予root全部权限，执行以下SQL
    
    ```sql
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;	# 授予全部权限
    ```
    
    再次执行以下命令就能成功啦！
    
    ```sql
    GRANT SELECT ON *.* TO 'dyd'@'%' WITH GRANT OPTION;	# 授予dyd用户查询权限
    ```
    
    授予非root用户权限后，可以再撤销授予root的所有权，恢复root默认权限
    
    ```sql
    REVOKE ALL PRIVILEGES ON *.* FROM 'root'@'%';
    ```