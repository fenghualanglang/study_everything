// "ui";
// ui.layout(
//     <vertical>
//         <text textColor="#CD0000" 
//         bg="#000000"
//         textSize="20sp"
//         id="ik"
//         lines="3"/>

//         <input hint="请输入验证码"/>
//         <input hint="请输入密码" password="true"/>
//         <button text="点击此处开始脚本" />
//         <button style="Widget.AppCompat.Button.Colored" text="漂亮的按钮"/>
//         <button style="Widget.AppCompat.Button.Borderless" text="漂亮的按钮"/>
//         <button style="Widget.AppCompat.Button.Borderless.Colored" text="漂亮的按钮"/>
//     </vertical>
// )

// // 可以根据id添加文本
// ui.ik.setText("本软件仅供学习与交流，\n请勿用于非法用途，\n如用于非法用途与本人无关")


// ===================================
// UI界面
// 文字样式控件
    // text 设置文本内容
    // textColor 设置文字颜色
    // textSize设置字体的大小
    // lines设置文本控件的行数
    // bg="#000000" 背景颜色
    // <text text 第一个表示文字输入框，还是显示框 第二个

    // <text textColor="#CD0000"  bg="#000000" textSize="20sp" id="ik" lines="3" text="本软件仅供学习与交流，请勿用于非法用途，如用于非法用途与本人无关"/>

// 文字输入框控件
    // hint  输入提示
    // password 指定输入框是否为密码输入框  password="true"

// 按钮控件
    // button  text按钮上显示的文字
    // Widget.AppCompat.Button.Colored 带颜色的按钮
    // Widget.AppCompat.Button.Borderless 无边框按钮
    // Widget.AppCompat.Button.Borderless.Colored 带颜色的无边框按钮




// ===================================
// UI界面
// 文字控件
    // text 设置文本内容
    // textColor 设置文字颜色
    // textSize设置字体的大小
    // lines设置文本控件的行数

    // <text text 第一个表示文字输入框，还是显示框 第二个
// "ui";
// ui.layout(
//     <vertical>
//         <text text="本软件仅供学习与交流，请勿用于非法用途，如用于非法用途与本人无关"/>
//     </vertical>
// )




// ===================================
// ui界面交互获取ui界面输入框内容for计次循环ui界面和脚本代码的交互
// "ui";
// ui.layout(
//     <vertical>
//         <text trxtSize="16sp" textColor="black" text="请输入话术"></text>
//         <input id="n" text=""/>
//         <button id="ok" text="开始运行脚本" />
//     </vertical>
// );

// ui.ok.click(function(){
//     threads.start(script)
// }
// )

// function script(){
//     toString("启动脚本")
//     sleep(1500)
//     launchApp("抖音短视频")
//     sleep(1500)
//     var h = device.height/1.2
//     var i = device.height/4
//     console.log(i + 'i');
//     console.log(h + 'h');
//     swipe(500, h, 500, i, 400)
//     sleep(2000)
//     id("a6d").findOne().click();
//     sleep(2000)
//     id("a6i").findOne().click();
//     sleep(2000)
//     id("a6z").findOne().click();
//     //  获取ui界面输入的值  n 为上面input 的id
//     var r = ui.n.getText()
//     setText(r)
// }

// u获取ui界面输入框的内容
// ui.id.getText()
// id 属性是链接xml布局和JavaScript代码的桥梁， 在代码中
// 可以通过一个View的id来获取这个VIew，并对他进行操作(设置点击动作 设置属性 获取属性值)



// device.height
// 设备屏幕额分辨率高度，例如 1920

// var h = device.height/1.2
// var i = device.height/4

// console.log(i + 'i');
// console.log(h + 'h');

// swipe(500, h, 500, u, 400)
// sleep(2000)

// 别激动，我连字母都不认识，跟孩子学点拼音就来了。
// 下拉菜单控件
// ui界面设置图片背景

// ===================================
// 选择框控件 radio
// 作用: 用于用户方便选择功能，从而执行不同的代码
// 相关知识  选择框布局： radiogroup -- 可以限制选择框只能选择一个防止用户多选
// 比如：一个选择框是点赞，另一个是评论，如果同时勾选两个那肯定不行的

// 默认 是垂直布局，可以用代码设置成水平
// orientation="horizontal"

// "ui";
// ui.layout(
//     // 设置背景图片
//     // <drawer bg="///cdcard/1.png">
//         <vertical>
//             {/* 选择框布局: radiogroup  设置单选框 */}
//             <radiogroup orientation="horizontal">
//                 {/* 选择框控件: radio */}
//                 <radio id="choose1" text="单选框1"></radio>
//                 <radio id="choose2" text="单选框2"></radio>
//             </radiogroup>

//             {/* 水平布局: horizontal */}
//             <horizontal>
//                 {/* 下拉框 */}
//                 <text text="请选择功能"></text>
//                 <spinner id="spinner" entries="功能一|功能二|功能三|"></spinner>
//             </horizontal>
//             <button text="确定" id="ok"></button>
//         </vertical>
//     // </drawer>
// )

// ui.choose1.on("check", (checked)=>{
//     if(checked){
//         toast("第一个被勾选了")
//     }
// });

// ui.choose2.on("check", (checked)=>{
//     if (checked){
//         toast("第二个被勾选了")
//     }
// }
// );
// // 此时点击界面，会显示第一二个勾选了

// // 调用下面的函数
// ui.ok.on("click", ()=>{
//     threads.start(items)
// });

// function items(){
//     var i = ui.spinner.getSelectedItemPosition();
//     log(i);
//     switch(i){
//         case 0: // 0， 1，2数字
//             log("功能一");
//             break; // 中断操作
//         case 1:
//              log("功能二"); 
//              break;
//          case 2:
//             log("功能三");
//             break;
//     }

// }

// ===================================
// 页面的滚动刷新

// ListView 列表容器
// PerfWidgetExternal.RecyclerView  列表容器
// scrollView   滚动容器
// scrollForward 对控件执行向前滑动操作,并返回是否操作是否成功
// scrollBackrward 对控件执行向后滑动操作,并返回是否操作是否成功


// 布局范围分析 - > 找到相应的控件 - > 在布局层次中查看 -> 找到五上述对应的控件
// - > 拷贝下来 进行上下左右滑动
// className ("android.support.v7.widget.RecyclerView").scrollForward()
// className ("android.widget.ListView").scrollForward()


// ===================================
// find() 根据当前的选择器所确定的筛选条件, 对屏幕上的控件进行搜索
// 这个搜素只进行一次,并不能一定能找到,因而会出现返回的控件集合为空的情况

// 不同与findOne()或者findOnce()只找到一个控件并返回一个控件,
//  find()函数会找出所有满足条件的控件并返回一个控件集合,之后可以对控件集合进行操作

// length属性 返回数组中的元素的数目


// var u=id ("bn5").find()

// var e=u.length //有时最后一个报错,可以u.length - 1

// for(var i=0; i<e; i++){
//     var tv=u[i];
//     if(tv){
//         var tr=tv.bounds()
//         click(tr.centerX(), tr.centerY()); //左右滑动
//         sleep(1200)
//         log("点击了" + i + "次");
//         back();
//         sleep(1200)
//     }
// }

for (var r=0; r<3; r++){
    var u=id ("bn5").find()
    var e=u.length //有时最后一个报错,可以u.length - 1
    for(var i=0; i<e; i++){
        var tv=u[i];
        if(tv){
            var tr=tv.bounds()
            click(tr.centerX(), tr.centerY()); //左右滑动
            sleep(1200)
            log("点击了" + i + "次");
            back();
            sleep(1200)
        }
    }
    className ("android.support.v7.widget.RecyclerView").scrollForward();
    sleep(1500)
}




















































