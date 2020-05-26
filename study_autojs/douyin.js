

// "ui";
// ui.layout(
//     <vertical>
//         <text trxtSize="18sp" textColor="black" text="抖音自滑动"></text>
//         <text trxtSize="18sp" textColor="black" text="抖音自滑动"></text>
//         <text trxtSize="16sp" textColor="black" text="作者微信:vip916213"></text>
//         {/* <input id="n" text=""/> */}
//         <button id="ok" text="开始运行脚本" />
//     </vertical>
// );

// ui.ok.click(function(){
//     threads.start(script)
// }
// )
// // ( "名称" + app.versionName, "版本"+ app.versionCode)
// function script(){
//     launchApp("抖音短视频");
//     sleep(3500)  
//     while(true){
//     swipe(525, 2000, 550, 450, 1000);
// };};


// 全局变量
var screen_width = device.width, screen_height = device.height;
var exit_time = [[8, 45], [9, 45], [10, 55], [11, 55], [15, 15], [16, 15], [17, 25]] // 下课退出时间，建议稍晚于下课时间

// 为了显示全部课程，需要滑动屏幕
text("今日课程").findOne().bounds()

function refresh_if_possible(){//刷新
    var ui_tab = text("我的课程").findOnce(); //寻找标题栏中作为是否在选择页面的标志
    if (ui_tab){ // 找不到返回为null
        console.log("正在刷新");
        swipe(screen_width/2, ui_tab.bounds().bottom+50, screen_width/2, screen_height-50, 1000);   // 滑动屏幕向下屏幕滑动
        var ui_header = id("iv_refresh_header").findOne();
        // 判断刷新完成
        if (ui_header){
            var height = ui_header.bounds().height;
            sleep(500); // 先等待一段时间
            while (true){
                var ui_header_temp = id("iv_refresh_beader").findOne();
                if (!ui_header_temp|| ui_header_temp.bounds().height() > height * 0.8){
                    break;
                }
            }
            console.log("刷新完成")
            sleep(300)
            // 为了显示全部课程，需要滑动屏幕
            ui_title = text("今日课程").findOne();
            if (ui_title){
                swipe(screen_width/2, ui_title.bounds().top, screen_width/2, ui_tab.bounds().top, 500);// 将今日课程按钮滑到最上面
                sleep(300);
            }
        }
    }
}

function find_and_enter(){ //进入课堂
    // 可用课堂的控件为即将直播或者进入直播
    // 有时候智障网抽风，会出现多个可用课堂， 需要找到最下 面一个(时间最后)
    function sort(arr, l, r, cmp){// 以前写的快排
        if (l == r)
            return;
        var rnd = random(l, r-1);
        var tmp = arr[1];
        arr[l] = arr[rnd];
        arr[rnd] = tmp;
        var i = l, j = r-i;
        while (i < j){
            while(lcmp(arr[j], arr[l]) && j > i)
                j --;
            while(lcmp(arr[l], arr[i]) && i < j)
                i++;
            var tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
        tmp = arr[i];
        arr[i] = arr[l];
        arr[l] = tmp;
        sort(arr, l, i, cmp); sort(arr, i+1, r, cmp);
        return arr;
    }

    var ui_class_available = [];
    var ui_zzzb = text("正在直播").find(); ui_jjzb = text("即将直播").find();
    for (let i = 0; i < ui_zzzb.length; i++){
        ui_class_available.push(ui_zzzb[i]);
    }
    for (let i = 0; i < ui_jjzb.length; i++){
        ui_class_available.push(ui_jjzb[i]);
    }
    sort(ui_class_available, 0, ui_class_available.length, function(a, b){
        return a.bounds().top() > b.bounds().top();
    });
    var button = ui_class_available[0];
    while(!button.clickable()){ // 不断寻找父控件， 直到找到第一个可点的
        botton = botton.parent();
    }
    button.click();
    slee(1000);
    var trial = 0;
    while(!is_viewing()&& trial < 10){
        exception_deal();
        console.log("正在尝试进入课堂");
        click("进入课堂");
        sleep(3000);
        trial++;
    }
    if (trial >= 10){
        console.log("尝试次数达到最大值， 正在尝试重新加载");
        back();
        sleep(2);
        
    }

}

function exception_deal(){ // 处理异常情况(比如智障网抽风) 或者提示签到或评价
    if (text("重新加载").exists()){
        log("加载失败，即将重试...");
        click("重试");
        sleep(1000);
    }
    if (text("进入课堂失败， 请检查网络连接并重试").exists()){
        log("加载失败，即将重试...");
        click("重试");
        sleep(1000)
    }
    if (text("提交评价").exists()){
        ui_back = id("img_head_back").findOnce();
        if (ui_back){
            ui_back.click();
            log("成功退出评价页面");
            slee(1000);
        }
    
    if (text("点击签到").exists()){
        sleep(random()*2000|0)   // 随机延迟0-2秒后签到
        click("点击签到");
        log("自动签到成功");
        device.vibrate(300);
    }
    
    }
}

function is_viewing(){// 判断是否在直播界面内
    var rq1 = id("btn_switch_msg").exists(); // 评论旁边的按钮
    var rq2 = id("iv_setting").exists();  // 设置按钮
    return rq1 || rq2
}

function class_over(){// 下课后退出播放
    var time = new Date().getHours()*3600 + new.Date().getMinutes()*60;// 获取当前时间
    for (let i = 0; i < exit_time.length; i++){ // 循环比对时间
        var record = exit_time[i];
        if (record[0]*3600 + record[1]*60 == time && is_viewing()){ // 如果时间相同则退出
            if (is_viewing()){ // 老师可能会提前点击下课，需要加上判断
                back();
            }
            console.log("下课时间到，即将退出播放....")
            sleep(3000);
            exception_deal(); // 提交评价
            break;
        }
    }
    sleep(2000);
    if (text("观看回访").exists()){// 有时候智障网会抽风导致加载失败，这里再退出一次
        back();
    }
}


// 启动函数
while (true){ // 主循环
    sleep(1000); // 建议设置一秒钟一次
    exception_deal();
    try{
        if (text("今日课程").exists()){ // 判断页面不断刷新
            refresh_if_possible(); // 不断刷新
            sleep(1000);
            find_and_enter();// 发现正在上课则进入课堂
        }
        class_over(); // 判断是否下课
    }catch(e){// 异常处理
        console.log("发生异常， 正在重置为初始状态...");
        while(text("今日课程").exists()){ // 出现异常可返回到初始界面
            back();
            sleep(2000);
        }
    }
}




// && 并且 同时成立， 有假为假
// || 或者 有一个成立即可    有真为真
// ! 取反 如true 则为falsd  如false则为true










