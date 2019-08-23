[TOC]

#  AJAX  异步 javascript  And Xml

## 主流的异步对象是  *XMLHttpRequest*

## 1.创建异步对象(异步对象由js来提供的)  

 支持XMLHttpRequest

​		通过    new  XMLHttpRequest()   来创建

不支持  XMLHttpRequest

​		通过	new	ActiveXObject("Microsoft.XMLHttp")        

判断浏览器的版本支持:

​		if(window.XMLHttpRequest){

 			说明支持浏览器			

​		}else{
``
​			不支持浏览器}

## 2.XHR的成员

### 	1.方法   -  open()

​		作用:创建请求	

```javascript
语法:xhr.open(method,url,async)
	method: get  post
	url : 请求地址  字符串
	async: 是否采用异步的方式发送请求
		true:异步的
		false:同步的
```

```javascript
实例 :  xhr('get','/02_server',true)  表示向02_server路由发送异步get请求
```

### 	2.属性    ------readyState

​		作用:表示请求状态,.通过不同的请求状态值来判断xhr与服务器的交互状况	

​				由0-4共5个不同的状态来表示不同的状态

| 状态值 |         服务情况         |
| :----: | :----------------------: |
|   0    |      请求尚未初始化      |
|   1    |     已经与服务器连接     |
|   2    | 服务器端已经接收请求信息 |
|   3    |      服务器端处理中      |
|   4    |         响应完成         |

### 	3.属性     -------status

​		作用:表示服务器端的响应状态码

| 响应码 | 响应状态                       |
| ------ | ------------------------------ |
| 200    | 服务器端正确处理请求并给出响应 |
| 404    | Not Found                      |
| 500    | Internal   Server   Error      |

```javascript
实例 :  if (xhr.readyStatus == 4 && xhr.status == 200){//可以接收服务端的响应信息}
```

### 	4.属性    ------responseText

​		作用:表示服务器端响应回来的信息

```javascript
实例:   if (xhr.readyStatus == 4 && xhr.status == 200){//可以接收服务端的响应信息
		console.log(xhr.resposeText)}
```

### 	5.事件   ---------onreadystatechange

​		作用:   每当xhr的readystate值发生变化的时候,要触发的操作 -------回调函数

```javascript
实例    xhr.onreadystatechange = function(){
		 if (xhr.readyStatus == 4 && xhr.status == 200){//可以接收服务端的响应信息
		console.log(xhr.resposeText)
			}
		}
```

### 	6.方法    ------send()

​		作用:通知xhr向服务器端开始发送请求

```javascript
语法    xhr.send(body):    body   :  请求主体
get 请求  xhr.send(null)
post 请求  xhr.send('请求数据')
```

## 3.AJAX的操作步骤

### 	1.get请求

#### 	1.创建XHR

```javascript
function createXhr(){
	var xhr;
	if(window.XMLHttpRequest){
		xhr = new  XMLHttpRequest()
	}else{
		xhr = new	ActiveXObject("Microsoft.XMLHttp"
	}
   return xhr                               
}
```

#### 	2.创建请求

```javascript
xhr.open(method,url,async)
	method: get post
	url : 请求地址  字符串
	async: 是否采用异步的方式发送请求
		true:异步的
		false:同步的
```

#### 	3.设置回调函数

​			(1)判断状态

​			(2)接受响应

 			(3)业务处理

```javascript
xhr.onreadystatechange = function(){
	if(xhr.readyState == 4 && xhr.status == 200){
		alert(xhr.responseText)
		}
	}
```
#### 	4.发送请求

```javascript
xhr.send(null)
```

### 	2.post请求

#### 	1.创建XHR

```javascript
		function createXhr(){
var xhr;
if(window.XMLHttpRequest){
	xhr = new  XMLHttpRequest()
}else{
	xhr = new	ActiveXObject("Microsoft.XMLHttp"
}
return xhr
}
```
#### 	2.创建请求

```javascript
xhr.open(method,url,async)
method: post
url : 请求地址  字符串
async: 是否采用异步的方式发送请求
	true:异步的
	false:同步的		
```
#### 	3.设置回调函数

​			(1)判断状态

​			(2)接受响应

 			(3)业务处理

```javascript
xhr.onreadystatechange = function(){
	if(xhr.readyState == 4 && xhr.status == 200){
		alert(xhr.responseText)
		}
	}
```

#### 	4.设置请求消息头

```javascript
 xhr.setRequestHeader(
     'Content-Type',
     'application/x-www-form-urlencoded');
```

#### 	5.发送请求.

```javascript
xhr.send(params)
params  为  拼接的发送的数据
实例var uname = $("#uname").val();
      var upwd = $("#upwd").val();
      //通过属性选择器获取隐藏域的csrfmiddlewaretoken的值
      var csrf = $("[name ='csrfmiddlewaretoken']").val();
      var params = 'uname=' + uname + '&upwd=' + upwd + "&csrfmiddlewaretoken=" + csrf;
      xhr.send(params)
```

### 	3.JSON

#### 	1.JSON介绍

​			json :    Javascript   Object Notation

​								js             对象      表现方式

#### 	2.JSON  -----   JS对象

​			使用 JS  对象表示一个人的信息   

```javascript
实例  :    var obj = {
	name:"wangwc",
	age :30,
	height : 180
}
```

#### 	3.JSON规范

​			1.使用**JSON**表示单个对象

​				1.使用 {} 表示一个对象

​				2.在 {} 中 使用**key:value** 来表示属性

​				3.key 必须使用 "" 引起来

​				4.value如果是字符串的话, 也必须用""引号	

​				5.多对key : value 使用, 隔开			

```javascript
实例     var obj = '{"name":"wangwc","age":30}'
```

​			2.使用JSON表示多个对象		

​				使用  []  来表示一组信息对象

```javascript
实例     var users = '[{"name":"wangwc"."age":30},{"name":"qtx"."age":28}]'
```

#### 	4.前端中处理JSON

​			**在JS中将得到的  JSON字符串  转换为JS对象/数组**

```javascript
 实例    var js对象  =  JSON.parse(json字符串)
```

​			**在JS中将得到的    JS对象/数组   转换为      JSON字符串**

```javascript
 实例    var json字符串  =  JSON.stringify(js对象)
```

#### 	5.服务器端JSON处理

​			1.在Python中的处理情况

​				允许将  元组   列表    字典    转换为 JSON字符串

​				元组    字典    列表   的内容必须是    字符串   元组

​				**Python中提供了一个模块  json 模块   其中的方法提供了dumps方法实现转换为JSON字符串**

​						**loads 方法为将JSON字符串转换为普通字典或者数组方法**

​			2.在Django中的处理情况

​				使用django中提供的序列化模块来完成QuarySet到JSON字符串的转化

```python
from django.core import serialiaers

serializers.serlialize( 'json',QuerySet)
		参数一:  需要转换的目标语言类型
		参数二:  需要转换的目标字符串
```

### 4.JQ对AJAX的支持

#### 	1.$obj.load()

```
$obj.load(url,data,callback)
		url: 路由地址
		data:请求参数
		callback:响应成功后函数的回调
```

​			作用:  加载远程地址的内容到$obj中

​			用法:

​	1.data:  请求参数可选   默认为get方法

​				1.通过字符串传参

```javascript
"key1= value1&key2 = value2"    会使用get方式传参
```

​				2.通过JS对象传参

```javascript
{

key1:value1,

key2:value2

}     会使用post方式传参发送请求


```

​	2.callback   ---->   回调函数

​		响应后成功后的回调函数[可选]

```javascript
function(responseText){
	responseText
					}
```

#### 	2.$.get()

​		作用: 通过 get  方法 **异步的**  向远程地址发送请求

​		语法 $.get(url, data,callback,type)	

```javascript
$.get(url, data,callback,type)
		url: 路由地址
		data:请求参数[可选]  默认为GET方式
		callback:响应成功后函数的回调[可选]
		type:响应回来的数据的格式[可选]
			1.html : 响应回来的文本当做HTML文本处理
			2.text : 响应回来的文本当做普通文本处理
			3.script : 响应回来的文本当做JS脚本处理
			4.json : 响应回来的文本当做JSON格式,直接转换为JS对象/数组
```

#### 	3.$.post()

​		作用: 通过 post  方法 **异步的**  向远程地址发送请求

​		语法 $.post(url, data,callback,type)

​		注意      {% csrf_token %}   跨网站的防伪识别

```javascript
$.post(url, data,callback,type)
		url: 路由地址
		data:请求参数[可选]  默认为GET方式
		callback:响应成功后函数的回调[可选]
		type:响应回来的数据的格式[可选]
			1.html : 响应回来的文本当做HTML文本处理
			2.text : 响应回来的文本当做普通文本处理
			3.script : 响应回来的文本当做JS脚本处理
			4.json : 响应回来的文本当做JSON格式,直接转换为JS对象/数组
```

#### 	4.$.ajax()

​	作用:  自定义AJAX的说有参数

​	语法: $.ajax({ajax的参数对象})

​		1.url :  请求的地址

​		2.data  :   请求到服务端的参数

​			1.字符串  :     "key1= value1&key2 = value2"

​			2.JS对象   :       {key1:value1,ey2:value2}

​		3.type  :  请求方式    'get'    'post'

​		4.dataType   :   响应回来的数据格式         JSON    HTML   text    script 

​		5.async  :     是否采用异步的方式发送请求

​					true    异步的

​					false   同步的

​		6.sucess  :   响应成功后的回调函数

​				function(responseText){}

​		7.

