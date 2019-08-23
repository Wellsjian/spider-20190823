-- 1.左外连接  左表 teacher  右表 Course  关联条件 teacher.Course_id = course.id

/*select *
from teacher left join course
on teacher.course_id = course.id;*/

/*select *
from course left join teacher
on teacher.course_id = course.id;*/

/*select *
from course left join teacher
on teacher.course_id = course.id
where teacher.id is null;*/

-- 右外连接 左表 teacher  右表 Course 关联条件  teacher.Course_id = course.id

/*select * from teacher right join course
on teacher.course_id = course.id;*/

-- 完整外连接(有误)
/*select * from course full join teacher
on teacher.course_id = course.id;*/

-- 查看没有参加过考试的同学的信息
/*select * from student left join score
on score.stu_id = student.id
where score.id is null ;


--飞雪连天射白鹿,笑书神侠倚碧鸳
-- 子查询 .查询student中比李四年龄大的学生信息
select * from student where
age > (select age from student where name = "李四");


-- 1.查询考过"齐天大圣"老师所教课程的学员信息
-- 1.1 查询齐天大圣老师所教课程的id
-- select course_id from teacher where name = "天大圣"
-- 1.2 在score中 查找Course_id 为1 的 stu_id
select stu_id from score where course_id =
(select course_id from teacher where name = "天大圣")
-- 1.3 在student中 查找stu_id 在student中出现的student.id
select * from student where student.id in
(select stu_id from score where course_id =
(select course_id from teacher where name = "天大圣"))
-- 2.查询在score中有成绩的学生学员信息
select * from student where student.id in
(select stu_id from score where score is not null);
-- 3..查询在Python基础课程分数在80分以上的学员的姓名和毕业学校
select name,school from student where
student.id in (select stu_id from score where
score > 80 and course_id = (select id from course
where cname = "Python基础"));
-- 4.查询和张三相同班级以及相同专业的同学的信息
select * from student where name != "张三" and
class_id = (select class_id from student where name = "张三") and
major_id = (select major_id from student where name = "张三");
)*/

/*create table wife (
    id int primary key auto_increment,
    name varchar(32) not null,
    age int not null,
    teacher_id int ,
    constraint fk_teacher_wife foreign key(teacher_id)
    references teacher(id),
    unique(teacher_id)
);

insert into wife(name,age,teacher_id) values
    ("紫霞仙子",25,2),
    ("蜘蛛精",18,1),
    ("白骨精",33,3);


alter table wife add constraint fk_teacher_wife foreign key(teacher_id)
references teacher(id);*/

/*create table goods(
    id int primary key auto_increment,
    gname varchar(32),
    gprice float
);

insert into goods(gname,gprice) values
    ("iphpne",18888.88),
    ("ipad",9999.99),
    ("huaweimate6000",3333.33);

create table shoppingCard(
    id int primary key auto_increment,
    t_id int not null,
    constraint fk_teacher_shoppingCard foreign key(t_id)
    references teacher(id),
    g_id int not null,
    constraint fk_goods_shoppingCard foreign key(g_id)
    references goods(id)
);

insert into shoppingCard values
    (null,1,1),
    (null,1,2),
    (null,1,3),
    (null,2,1),
    (null,2,2),
    (null,2,3),
    (null,3,1),
    (null,3,2),
    (null,3,3);

alter table shoppingCard add count int default 1;*/


select name,g.gname,s.count from teacher
inner join shoppingCard as s
on s.t_id = teacher.id
inner join goods as g
on s.g_id = g.id;





















