

// 笔青居
// 按照字体去
// desc("评论").findOne()
// comment = desc("评论").findOne()
// log("3333333333333333")
// log(comment);
// log("3333333333333333")
// comment.click()

// good = text("赞").findOne();
// log(good)
// // 赞不能被点击找到其父控件，进行点击
// good.parent().click();

// ============================

// javas数据类型
// "baasfjaf" 字符串
// 12345   数字
// false， true  布尔
// null 检测对象是否存在
// undefined 变量未定义
// Object 对象

// var 声明一个变量
// var name = {"username": "zhagnsan", "age": 13}

// 转换逻辑以及比较

// string + number = string
// string - number = number
// string == number 尝试把字符串转成数字
// boolean==string 转成Boolean
// Object != Object 对象的对比是引用比较
// unll == undefined 未定义
// Object == string 尝试转换Object为string
    // log(new String("123") == "123");
// Object == number 尝试转换Object为bumber

// 字符串转数字  x = "123" - 0
// 数字转字符串  x = 123 + ""
// log(new String("123"))  //{ '0': '1', '1': '2', '2': '3' }


// ============================
// 类型检测
// typeof  typeof("string")
// var  i = "12344";  可用来判断变量类型
// log(typeof(i));   string


// instanceof 检测是否继承
// Object.prototype.toString
// constrctor


// ============================
// 语句

// block  块  {}里面的
// if 如果
// if..else 如果否则
    // if(判断语句){
    //     // 当判断语句为真时，执行
    // }else{
    //     // 这里执行为假语句
    // }

    // var t = "我是文本";
    // if(t == "我是文本"){
    //     // 执行我是文本语句
    // }else{
    //     // 执行我不是文本语句
    // }

// for 循环
    // n = 100
    // for(i=0; i<n; i++){
    //     log(i)
    // }

// switch 选择
    // var a = 3;  //执行第三个
    // switch(a){
    //     case 1:
    //         log("我是1");
    //     break;
    //     case 2:
    //         log("我是2");
    //     break;
    //     case 3:
    //         log("我是3");
    //     break;
    //     case 4:
    //         log("我是4");
    //     break;
    //     case 5:
    //         log("我是5");
    //     break;
    // }

// break 结束
    // var n = 100;
    // for(i=0; i<n; i++){
    //     if(i<10){
    //         log('i小于10');
    //         break;
    //     }
    // }

// continue 跳过
    // var n = 100; //小于50均跳过
    // for(i=0; i<n; i++){
    //     if(i<50){
    //         continue;
    //     }else{
    //         log(i)
    //     }
    // }


// return 返回
    // function fangfa1(){
    //     var a=1;
    //     return;
    // }

// while 直到
    // var s = "条件语句";
    // while(s){
    //     log("在执行");
    // }

// do..while做了再判断
// do{
//     log("在这里执行")
// }while("条件语句");

// while 先判断条件， 如果不满足条件不执行
// do .. while 先执行一次， 再判断条件，true 执行 false 结束


// function 函数
// try ..catch 捕获
// delete 删除



// ============================
// 对象创建:
// var kwargs={x:1,y:"u"};
// var ot = {}; //创建空对象
// var ot = new Object(); //创建一个空对象

// 对象读写:
// var kwargs = {x:1, y:"u"}
// // log(kwargs.x) //函数名.属性名
// // log(kwargs['x']) //与上同样

// // 添加对象
// for (i=0; i<10; i++){
//     kwargs["x" + i] = i; // string + number = number
// }
// log(kwargs)

// 删除对象
// var a = {x: 1, y:"u"};
// log(delete a.x)
// console.log(a);

// 判断a中的属性， 是否存在x属性
// var a = {x: 1, y:"u"};

// x in x; // 如果返回为true， 说明属性存在，否则不存在

// 判断对象是否为空
// if(a == null){
//    log(a.x) 
// }

// 获取对象所有的key值，value值
// a = {z: 1, x: 2, c: 3, d: 4}
// for (key in a){
//     log("KEY" + key)
//     log("value"+ a[key]);
// }


// ============================
// 数组
// var li = [1, 5, 8, "2", "3a", 4]
// 根据下标取值
// log(li[2])
// 数组添加
    // li.length; 数组长度
    // li.push(5); //尾部添加
    // li.unshift(3); //头部部添加
    // li.pop(); //删除尾部
    // li = li.join("_")  //字符串拼接
    // li.sort()  //排序  默认字母排序， 
    // 如果是[75, 453, 11, 2]会把number 转成string类型，再排序[11,2,453,75]
    

    
    // log(li);
// 根据下标取值
// for (i=0; i<li.length; i++){
//     log(li[i])
// }
    
// 数组遍历
// li.forEach(function(i, p, x){
//     //i 具体值 p索引 x数据本身
//     log("具体值-->" + i +  "索引-->" + p + "数据本身"+x)

// })

// 数组检索，判断包含某个元素是否在数组里面,返回索引的位置上
// x = li.indexOf("3a")
// log(x)  // 此时索引为4


// ============================
// 函数 定义一次可以执行多次
// 无参数
// function func(){
//     log("我是函数")
//     return "返回值"
// }

// var a = func();
// log(a)

// 有参数
// function func(a, b){
//     return a+b;
// }

// var x = func(1, 4)
// log(x);

// 作用域
// var a = 0;
// function func(){
//     var a = 2;
//     log(a)
// }
// t = func();

// ============================
// 常见容器控件

// LinearLayout 线性布局容器
// RelativeLayout 相对布局容器
// FrameLayout 帧布局c
// ListVIew 列表容器
// RecyerView 复用容器
// ScorllVIew  滚动容器

// Clickable = false 是不可以被点击的
// 此时要找的他的父控件 有较强亮光的 如微信点赞

// 控件的寻找

// text  通过文本  完全匹配 textCOntains("string")
// desc  通过描述   textStartWith("string")
// id    通过id      textEndWith("string")
// className 

// var name1 = text("张玉超").findOne();
// // log(name1);

// var commentt = desc("评论").findOne();
// // log(commentt)

// var content = id("mk2222").findOne(1000);
// findOne() 找不到控件，会阻塞等待 有参数时可为时间找不到跳过为null
// findOnce() 仅找一次，没有跳过,null
// log(content);

// 找到列表
// var li = className("ListView").findOne();  
// log(li);

// find()
// 查找所有的列表
// var commentt = desc("评论").find();
//  用forEach()
// log(commentt)


// var good = text("赞").findOne().parent();
// log(good);


// ============================
// 单个控件的操作
// 对象.属性     访问属性
// click         点击
// longClick     长按
// scroll...       滚动
// childern      遍历
// find   子控件查找



// =================================================
// 控件操作单个

// 发现司机书店的控件
// var name = text("四季书店").findOne();
// console.log(name);

// // 可以根据上面的对象找到其对应的属性
// var id = name.className();
// console.log(id);

// 长按按钮
// 查看控件longClick要为true
// var lc = id("mk").findOne();
// lc.longClick();

// 滚动scrollable 为true  才能滑动 scrollDown 向下 scrollUp 向上 scrollLeft 向左 scrollRight向右
// var sd = className("ListView").findOne();
// // log(sd)
// // sd.scrollDown();

// // 滚动的子控件列表
// var sdson = sd.children();
// // console.log(sdson);

// sdson.forEach((item, position)=>{ 
//     var name = item.find(className("TextView"));
    // log(name.size());
    // name.forEach(dtl_name=>{
    //     log(dtl_name);
    //     log(dtl_name.text());
    // })

    // log(name.get(1).text());
    // // 获取某一类属行的具体属性值
    // log(name.text() + "========");
    // console.log(item);
    // // console.log(position + "======");
// });
// 总  1获取滚动控件   2 获取滚动控件的子项  3便利滚动控件的子项 4获取子项的具体值

// sdson.forEach(function(item, position){ 
// });

// 文本框 建议根据className 获取 微信评论
// var book = className("EditText").findOne();
// book.setText("hello world")

// var book = desc("评论").findOne();
// log(book.click())
// book.setText("hello world")

// =================================================
// 控件操作多个

// var gb = className("ListView").findOne();
// // console.log(gb);
// var gb_son = gb.children();

// // console.log(gb_son);
// gb_son.forEach((item, position)=>{
//     var comment = item.findOne(desc("评论"));
//     if (comment){
//         sleep(1000)
//         log(comment)
//         sleep(1000)
//         var good = text("赞").findOnce();
//         log("==============" + good)
//         // if(good){
//         //     sleep(1000)
//         //     good.click();
//         // }
//     }
//     comment.click();
// });
// gb.scrollDown();


// 封装一下
// while(true){
//     good_click()
// }


// function good_click(){
//     var gb = className("ListView").findOne();
//     // console.log(gb);
//     var gb_son = gb.children();
//     // console.log(gb_son);
//     gb_son.forEach((item, position)=>{
//         var comment = item.findOne(desc("评论"));
//         if (comment){
//             sleep(1000)
//             log(comment)
//             sleep(1000)
//             var good = text("赞").findOnce();
//             // log("==============" + good)
//             // if(good){
//             //     sleep(1000)
//             //     good.click();
//             //     click("赞")
//             // }
//         }
//         // comment.click();
//     });
//     gb.scrollDown();
// }


// =================================================
// 滑动
// auto.waitFor();

// do{
//     // click(500, 300)
//     sleep(1000);
//     // back();
//     swipe(100, 500, 100, 400, 800)
// }while(true)

// 手势

// gesture(手势时长, [100, 400], [300, 800], [500, 300])

// gesture(4000, [100, 400], [300, 800], [500, 300], [1000, 1800], [500, 600])


// =================================================
// 全局函数
// setTimeout(()=>{
//     console.log('aaaaaaa');
// }, 4000);

// 当前包名
// log(currentPackage() + " 当前包名;
// // 当前活动名(页面)
// log(currentActivity() + "当前活动名(页面));

// 跳转页面
// click(400, 800);
// waitForActivity("com.afollestad.materialdialogs.MaterialDialog")
// click("打招呼")

// =================================================






var s = "hello world"; // String()
var n = 10; // Number
var b = true; // Boolean;

// 取整数
var number = 9.6
// var result = Math.trunc(number);// 9
// 下退
var result = Math.floor(number)  //6 向下一位
var result = Math.ceil(number); // 向上一位
var result = Math.round(number); // 四舍五入
var result = Math.random(); // 随机数
var result = Math.random(1, 10); // 随机数


if (number < 3){
    console.log('1');
}else if (number > 3 && number < 10){
    console.log('2');
}else{
    console.log('3');
}



var number = 8.5;
switch (number){
    case 1:
        console.log('1');
        break;
    case 3:
        console.log('1');
        break;
    case 8.5:
        console.log('1');
        break;
    default:
        console.log('default');
        break;
            
}
















