//创建AJAX对象
function createXhr() {
        //根据不同的浏览器创建不同的异步对象
    if(window.XMLHttpRequest){
       var Xhr = new XMLHttpRequest()
    }else{
       var Xhr = new ActiveXObject("Microsoft.XMLHttp")
        }
    /*console.log(Xhr)*/
    return Xhr
        }

//检查用户名是否存在的函数
function checkName() {
    //做出标志
    var flag = false
    //1.创建xhr
    var xhr = createXhr();
    //2.创建请求
    var uname = $("#uname").val();//获取输入框的值
    console.log(uname)
    var url = '/ajax01/04_server?uname='+ uname;
    xhr.open('get',url,false)
    //3.设置回调函数
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status ==200){
            //$('#uname_tip').html(xhr.responseText)
            if(xhr.responseText == "1"){
                $('#check').html("用户已经存在")
                flag = true
                }else{
                $('#check').html("通过")
                }
            }
        }
    //4.发送请求
    xhr.send(null)
    return flag
    }
