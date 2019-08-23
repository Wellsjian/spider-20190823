# 高级Mysql数据库

## 索引

### 1.主键索引

### 2.唯一索引

- 对已有的表创建索引      create unique index 索引名  on  表名(字段名)
- 创建表时添加索引          create table  表名(id int ,phone varchar(32) unique)

### 3.普通索引

- 对已有表进行创建索引     create  index  索引名  on  表名(字段名)
- 创建表时添加索引             create   table 表名 (id int ,name varchar, index(name),index(字段名))

### 4.查询和删除索引	

- ```
  show index from 表名
  ```

- ```sql
  drop index 索引名  on  表名
  ```

  

## 外键    Foreign key

### 	1.基本语法

- 作用 :   用于建立与另一张表的关联,,,约束当前表的某列值必须取自于另一张表的主键列值
- 外键列:  外键所在的列称之为外键列
- 外键表/子表:   外键所在的表称之为外键表 或者子表
- 主键:   能够唯一标示一条记录的字段或属性
- 主键列:  主键所在的列称之为主键列
- 主键表/主表:   被外键所引用的表成为主表或者是主键表		

### 	2.语法

#### 		1.创建表的同时指定外键

```sql
create table 表名(
	id int primary key auto_increment,
	class_id int not null,
	constraint fk_主键表_外键表
	foreign key(class_id) 需要绑定的本表的字段名
	references 主键表(id));
```

#### 		2.在已有的表上更改结构增加外键

```sql
alter table 表名 add constraint fk_外检表_主键表 foreign key(class_id) references 主键表(id);
```

​		3.查询外键     show create table student;

​		4.删除外键     alter  table  表名  drop  foreign  key  外键名 

### 	3.级联操作

#### 		1.实现语法

```sql
alter table  表名(
	add constraint 外键名
	foreign key(字段名)
	references 主表(主键)
	on delete 级联操作
	on update 级联操作)
```

#### 		2.级联操作取值			

| 1.cascade        | 数据级联删除 更新                                            |
| ---------------- | ------------------------------------------------------------ |
| 2.restrict(默认) | 子表中有关联数据,主表不允许删除 更新                         |
| 3.set null       | 主表删除数据,子表相关数据设置为null  ,前提子表外键列允许为空 |

### 	4.表连接查询

#### 			 1.交叉连接 -  笛卡尔积

```sql
e.g.   查询teacher和Course表中所有的数据     select  *  from  teacher,course where 条件;
```

#### 			2.内连接

​					在关联的两张表中,把满足条件的表筛选出来

​					e.g.    select   字段,...,...  from  表1 inner join  表2 on  条件

​				1.练习

​					1.查询学员的姓名  年龄  所在班级 名称  专业名称

```sql
select s.name,s.age,c.classname,m.m_name
from student as s
inner join classinfo as c
on s.class_id = c.id
inner join major as m
s.major_id = m.id;
```

​					2.查询学员姓名  毕业学校  所在班级 考试科目  考试成绩

```sql
select s.name,s.school,c.classname,cs.cname,sc.score
from student as s
inner join classinfo as c
on s.class_id = c.id
inner join score as sc
on sc.stu_id = s.id
inner join course as cs
on sc.course_id = cs.id;
```

#### 		3.外连接

​			1.左外连接

​				1.作用:

​						 1.左表中的所有的数据都会查询出来(不满足的也会也查出来)

​						 2.将右表中的满足关联的条件的数据查询出来

​						 3.关联不上的关联字段即将一null作为填充

​						  4.子表作为左表查询的结果和内连接的效果一样

​				2.语法结构:

```sql
select 字段  from 表1 left  join   表2  on  关联条件
```

​			2.右外连接	

​				1.作用

​					1.右表中的所有的数据都会查询出来(不满足的也会也查出来)	

​					2.将左表中的满足关联的条件的数据查询出来

​					3.关联不上的关联字段即将一null作为填充

​					4.子表作为右表查询的结果和内连接的效果一样

​				2.语法结构

```sql
select 字段  from 表1 right  join   表2  on  关联条件
```

​			3.完整外连接

​				1.作用:

​					1.将两张表的数据做关联查询,关联出来的数据显示出来,关联不出来的数据以null填充

​				2.语法

```sql
select * from 表1 full join 表2 on 满足条件
```

### 5.子查询

#### 	1.定义

​		讲一个查询的结果作为外侧操作的一个条件出现

#### 	2.语法

```
select .... from  表名 where 条件=(select ...from  表名 where 条件)
```

#### 	3.练习

​		1.查询考过"齐天大圣"老师所教课程的学员信息

```sql
select * from student where student.id 
in (select stu_id from score where 
course.id =(select id from teacher where name = "齐天大圣"));
```

​		2.查询在score中有成绩的学生学员信息

```
select * from student where student.id 
in (select stu_id from score where score is not null);
```

​		3.查询在Python基础课程分数在80分以上的学员的姓名和毕业学校

```
select name,school from student where student.id in 
(select stu_id from score where score > 80 and 
course_id = (select id from course where cname = "Python基础"));
```

​		4.查询和张三相同班级以及相同专业的同学的信息

```sql
select * from student where name != "张三" and
class_id = (select class_id from student where name = "张三") and
major_id = (select major_id from student where name = "张三");
)
```

### 6.   E ----R  模型

#### 	1.定义

​		Entity - Relationship  实体关系模型

​		在数据库设计阶段一定会使用,以图形的方式来展示数据库之间的表以及表关系

#### 	2.概念

​		1.实体

​			表示数据库中的一个表

​			图形表示 : 矩形框

​		2.属性 : 

​			表示某实体中的某一特性,如果实体为表,那么属性可以说是字段

​			图形表示: 椭圆形

​		3.**关系  ----- Relationship**

​			表示实体与实体之间的关联关系

##### 			1.一对一的关系(1:1)

​				表1中的一条记录只能关联到表2中的一条记录上

​				表2中的一条记录只能关联到表1中的一条记录上

​			    在数据库中的实现手段

​				在任意的一张表中增加

​					1.外键,并引用自另一张表的表主键

​					2.在外键列加上唯一索引,进行索引约束

​						练习:

```sql
create table wife (
    id int primary key auto_increment,
    name varchar(32) not null,
    age int not null,
    teacher_id int ,
    constraint fk_teacher_wife foreign key(teacher_id)
    references teacher(id),
    unique(teacher_id)
);
```

##### 			2.一对多的关系(1:m)

​				表1中的一条记录可以关联到表2中的多条记录

​				表2中的一条记录只能关联到表1中的一条记录

​				在数据库中的实现手段

​					1.在多对应的表中增加外键    引用自一 对应表的主键

##### 			3.多对多的关系(m;n)			

​				表1中的一条记录可以关联到表2中的多条记录中

​				表2中的一条记录可以关联到表1中的多条记录中

​				在数据库中的实现手段

​					1.在第三张表中添加两个外键,分别引用自两个表的主键,确定关联,实现多对多的关系

### 7.SQL语句优化(面试可能问题)

​	1.索引:经常 select,where,order by的字段应该建立索引

​	2.单条查询语句最后添加  limit 1 ,  停止全表扫描    切记  切记

​	3.where语句中尽量不使用 != , 否则放弃了索引全局扫描

​	4.尽量避免null值判断,否则放弃索引全局扫描

​	5.尽量避免  or  连接条件 ,  否则放弃索引全表扫描

​	6.模糊查询尽量避免使用前置的%号,否则全表都会扫描

​	7.j尽量避免使用in not in ,否则全局都会扫描

​	8.尽量避免使用select * ,不要返回用不到的任何字段

 