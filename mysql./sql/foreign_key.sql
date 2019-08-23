-- 单行注释
/*多行注释*/
/*create table course(
    id int primary key auto_increment,
    cname varchar(30) not null,
    cduration int not null
);*/
/*向表中插入数据*/
/*insert into course(cname,cduration)
values
    ("Python基础",20),
    ("Python基高级",15),
    ("Web基础",9),
    ("Python Web",15),
    ("爬虫",10),
    ("人工资能",20);*/
-- 创建teacher表:id name age gender hobby course_id
-- course_id 是外键 ,需要引用course表的主键id
/*create table teacher(
    id int primary key auto_increment,
    name varchar(30) not null,
    age int not null,
    gender char(2) not null,
    hobby varchar(32) not null,
    course_id int,
    constraint fk_course_teacher foreign key(course_id) references course(id)
);*/

/*insert into teacher
values
    (null,"齐天大圣",28,"M","大保健",1),
    (null,"吕泽Maria",30,"M","拍片",2),
    (null,"赵蒙蒙",28,"F","看帅哥",3);*/

-- 创建major表,id   m_name
/*create table major(
    id int primary key auto_increment,
    m_name varchar(30) not null
);

insert into major(m_name)
values
    ("AID"),
    ("UID"),
    ("JID"),
    ("WEB");*/

-- 创建student表 id name age gender school class_id major_id
/*create table student(
    id int primary key auto_increment,
    name varchar(32),
    age int not null,
    gender char(2) not null,
    school varchar(100) not null,
    class_id int not null,
    major_id int not null
);*/

-- 更新student表,增加外键关系在major_id上,引用到major表的主键id 上
/*alter table student
add constraint fk_major_student
foreign key(major_id)
references major(id);*/

/*insert into student values
    (null,"张三",18,"M","哈佛大学",5,1),
    (null,"李四",19,"M","麻省理工学院",4,1),
    (null,"王二麻子",26,"F","蓝翔技校",4,3),
    (null,"朱刚",19,"M","五道口技术学院",4,1);


-- 创建classinfo表 ,id classname status
create table classinfo(
    id int primary key auto_increment,
    classname varchar(10),
    status char(2)
);

insert into classinfo(classname,status)
values
    (1901,0),
    (1902,1),
    (1903,1),
    (1904,1),
    (1905,1);*/
-- 修改student 表结构 在student中 增加外键关系在class_id 上,引用到student表主键id 上
/*alter table student
add constraint fk_class_student
foreign key(class_id)
references class(id);
-- 创建score表 id stu_id course_id score
create table score(
    id int primary key auto_increment,
    stu_id int not null,
    course_id int not null,
    score int not null,
    constraint fk_student_score
    foreign key(stu_id)
    references student(id),
    constraint fk_course_score
    foreign key(course_id)
    references course(id)
);


insert into score values
    (null,1,1,98),
    (null,2,1,99),
    (null,1,2,86),
    (null,4,3,68);*/


-- 删除score中的fk_student_score
/*alter table score drop foreign key fk_student_score;*/


-- 为score表中的stu_id增加外键,引用student主键id ,并设置级联操作

/*alter table score
add constraint fk_student_score
foreign key(stu_id)
references student(id)
on delete cascade
on update cascade;*/

-- 使用内连接查询teacher,Course中的数据(姓名,年龄,课程,名称,课时)
select t.name,t.age,c.cname,c.cduration
from teacher as t
inner join course as c
on t.course_id = c.id;


-- 1.查询学员的姓名  年龄  所在班级名称  专业名称
select s.name,s.age,c.classname,m.m_name
from student as s
inner join classinfo as c
on s.class_id = c.id
inner join major as m
s.major_id = m.id;

-- 2.查询学员姓名  毕业学校  所在班级 考试科目  考试成绩
select s.name,s.school,c.classname,cs.cname,sc.score
from student as s
inner join classinfo as c
on s.class_id = c.id
inner join score as sc
on sc.stu_id = s.id
inner join course as cs
on sc.course_id = cs.id;