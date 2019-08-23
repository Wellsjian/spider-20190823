# AJAX发送POST请求

### 1.创建xhr对象

### 2.创建请求

​	**1.请求方式改为POST**

​	**2**.

​	3.

​	4.设置请求消息头   -----Content -Type

```xml
xhr.setRequestHeader("Content -Type","application/x-www-form-urlencoded")
```

​	5.发送请求

​		请求数据放在send()的参数位置处	

```
实例:   xhr.send("name=wang&age=25&gender=男")
```

