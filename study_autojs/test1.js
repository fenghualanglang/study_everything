// // // launchApp("打开某个应用");
// launchApp("微信");
// sleep(5000)  //休眠3.5秒
// // click(x, y) 点击某个坐标
// click(520, 450)
// sleep(3050)  //休眠3.5秒
// click(305, 2315)
// setText("开心")
// sleep(2050)  //休眠3.5秒
// click(650, 163)
// // click(980, 1502)

// ===================================



// while() 循环
// while 包含一个循环条件和一个代码块，只要条件为真，就不断循环执行代码块
// var i = 0;
// while( i < 100){ 
//     log(i)
//     i = i + 1;
// }
// log("log 等于或大于5")


// 帮助-->切换开发人员工具


// 下面这个是无限循环
// while(true){
//     console.log("hello world")
// }

// ===================================

// 寻找界面控件并点击
// 基于控件的操作值得是选择屏幕上的控件，获取其信息对其进行操作，依赖于无障碍服务
// auto.waitFor：检查无障碍服务是否已经启用，如果没有启用则跳转到无障碍服务启用界面
    // 并等待无障碍服务启动；当无障碍服务启动后脚本会继续运行
// 控件属性  ("名称").findOne().click(); 寻找控件并点击它

// swip滑动命令
// swipe(x1,y1, x2, y2, duration)
// x1{number} 滑动的起始坐标的x值
// y1{number} 滑动的起始坐标的y值
// x2{number} 滑动的终止坐标的x值
// y2{number} 滑动的终止坐标的y值
// duration {number}  滑动的时长
// 模拟以坐标{x1, y1}滑动到坐标{x2, y2}, 并返回是否成功。
// 只有滑动动作完成时脚本才会执行下去
// swipe(525, 376, 550, 2000, 6)



// 自动刷抖音无限制的刷去
// launchApp("微信");
// sleep(3050)  //休眠3.5秒
// while(true){
//     swipe(525, 376, 550, 2000, 6)
// };
// while(true){
//     swipe(525, 376, 550, 2000, 6)
// };


// launchApp("抖音短视频");
// sleep(3500)
// // id("az_").findOne().click();
// id("a6d").findOne().click();
// sleep(3500)
// id("a6i").findOne().click();
// sleep(3500)
// setText("开心")
// id("a6z").findOne().click();
// sleep(3500)

// // back(); 返回
// back();
// sleep(1000)
// swipe(525, 376, 550, 2000, 600);
// sleep(1000)

// ===================================


// 随机数字制作
// random(min, max)
// min{number} 随机数字产生的区间下界
// man{number} 随机数字产生的区间上界
// 返回{number}
// 返回一个在{min，max}之间的随机数，例如random(0, 2) 可能产生0,1,2

// var i= random(0, 4);
// console.log(i);

// var i= random(65, 90);
// var s = String.fromCharCode(i)
// log(s);
// // 下面这个需要在搜索框里才能显示
// setText(s+'helloworld')

// id("bn5").findOne().click();
// sleep(3500)
// id("dbc").findOne().click();
// sleep(1000)
// id("dyu").findOne().click();
// sleep(1000)
// id("cnu").findOne().click();
// setText('亲， 你也要注意防护呦'+ "")
// id("dyh").findOne().click();
// sleep(1000)
// back();
// sleep(1000)
// back();

// ===================================

// function函数命令
// function命令声明的代码区块。
// function命令后面是函数
// 函数名后面是一对圆括号，圆括号后面是传入的参数。
// 函数体放在圆括号里面

// function test(){
    // log("我被调用了")
// }

// 上面的代码命令了一个函数，以后使用测试()这种形式，就可以调用相应的代码，这叫函数声明
// return 返回值，返回一个数值，就是把return<表达式>后面表达式的值给返回调用它的函数值

// function test1(){
//     return "住隔壁的是"
// }

// log(test1() + '老王')
// log(test1() + '老李')

// ===================================
// 随机生成汉字

// Array对象
// Array是JavaScript的原生对象，同时也是一个构造函数，可以用它生成新的数组
// Array构造函数，不同的参数，会导致它的行为不一致

// var m = random(0, 9)
// var n  = random(0, 9)
// q = new Array() // []
// q[0] = '赵'
// q[1] = '钱'
// q[2] = '孙'
// q[3] = '李·'
// log(q)
// var t = q[n]
// var s = q[m]
// log(t + s)


// ===================================
// if结构
// 结构先判断一个表达式的布尔值，然后根据它的布尔值的判断真伪，执行不同的语句

// if (布尔值) {
//     语句A;
// } 
// else{
//     语句B;
// }

// var i = 14
// if (i < 2){
//     log(i + '为true条件成立')
// }
// else{
//     log(i + '为false条件不成立')
// }


// ===================================
// do ... while 循环
// 注意于前文的判断while区别
// while 先执行再判断，如果条件满足就执行，不满足就结束拉
// do ... while 先执行一次再判断，然后再判断循环条件
// var i = 0
// do {
//     log(i)
//     i = i + 1
// }
// while(i < 2)


// ===================================
// 赋值运算符 等号 =  将1 赋值变量x  var x = 1
// 两种相等运算符 ==和===
    // == 值一样即可，不考虑类型 
    // = 值一样，类型一样

// var o = 1
// var i = "1"
// if (o === i){
//     log("o, i 值一样，类型一样")
// }
// else{
//     log("o, i 值一样，类型不一样")
// }

// < 小于运算符
// > 大于运算符
// <= 小于等于运算符
// >= 大于等于运算符


// ===================================

// break 跳出循环，跳出循环代码块
// continue 跳出本次循环, 开始下一轮循环
// var i = 0;
// while (i < 9){
//     if (i == 5)break;
//     i ++;
// }
// console.log("跳出循环啦");

// var i = 0;
// while (i < 9){
//     i = i + 1;
//     if (i % 2 === 0) continue;
//     console.log(i);
//     i++;
// }
// console.log("循环运行啦");


// ===================================
// for 循环怎么写


// for (var i=0; i<15; i++){
//     console.log(i);
// }





























