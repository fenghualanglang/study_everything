// 由于后续进行的bug修复，代码逻辑和B站视频中的逻辑有一些差异
	
var order = '数语英自化物生';  // 课程顺序
// 两数组长度必须与课程节数相同
var stime = [ 7.55,  9.05, 10.15, 11.15, 14.25, 15.35, 16.45];  // 进入时间，整数部分为小时，小数部分为分
var etime = [ 8.55, 10.05, 11.15, 12.05, 15.25, 16.35, 17.45];  // 退出时间，格式同上
//目前:        数     语     英     自     化     物     生    调试

var tc = '语数英物化生';  // (自习:-1)
var qid = ['10567****1', '10******19', '9815****', '822865****', '822*****67', '10****6966'];  // 直播间群号
var signMsg = ['手动打卡', '1', 'qwq', '暗中观察', '(0_0)', ':D', ':)', '打卡', '√', '233'];  // 设定手动打卡文本
var width = device.width, height = device.height;
var wjxUrls = {};  // 记录匹配到问卷星(打卡入口)的链接
var exceptionCount = [];  // 记录报错的次数和内容
//                                 这是40，调试完记得改回来  ↓↓↓↓
var roundTime = 99, rollTime = 0, viewing = null, threshold = 40;  // 阈值，大于这个人数正在观看才认为是有效的课程
var firstLoop = true, lastRepeat = ['', '', ''], coolDown = 0, lastOne = '';  // 设置复读的条件，避免过快复读
var type = 'share';  // 当前课程的直播方式share/live (屏幕分享/群直播)
var activities = [  // 两种直播方式的Activity
    'com.tencent.av.ui.AVActivity', 
    'com.tencent.intervideo.sixgodcontainer.proxyactivitys.PluginSingleTask5ProxyActivity'
];
var myName = '70649许三多', chats = [[0, '', false]];  // 记录群里的聊天内容

// 这脚本难度太大，为方便编写，决定引用jsp模块
var jsp = require('./Jsp.js'); jsp(); // chynb!!! jspnb!!!!!!
require('./屏幕日志.js');

/**
 * 由于腾讯经常抽风，老师也可能不会操作或操作失误，所以可能会发生各种意外情况
 * 如今使用 基于时间+基于控件 的操作模式，根据当前时间，决定进哪个群，根据当前控件，决定应该干什么
 * 垃圾腾讯经常发生获取不到View或获取不准的情况，通过加入无用代码让页面鬼畜得以解决
 * 监听聊天记录中的问卷星链接，启动WebView打开链接自动填写打卡
 */ 

events.on('exit', function () {
    console.info('运行过程中共拦截到' + exceptionCount.length + '次错误、');
    for (let i in iter(exceptionCount)) {
        console.log('时间: ' + exceptionCount[i][0] + '/1440  错误信息:');
        console.error(exceptionCount[i][1]);
    }
});

init();
while (true) {  // 主循环，基于时间的操作
    try {
        rollTime = rollTime + 1;
        if (rollTime >= 20) {  // 循环20次刷新一次复读
            rollTime -= 20;
            lastRepeat.push(''), lastRepeat.shift();
            swipe(width/2, height/3, width/2, height/4, 500);
            console.verbose('[新完成了20轮主循环]');
        }
        var now = getTime();
        exceptionDeal();
        whatToDo(now);
        coolDown && coolDown--;
        updateChatContent(), repeatAndSign();
        roundTime += 1;
        if (roundTime >= 100) {
            roundTime -= 100;
            console.log('当前在上:' + viewing + ' 课程类型:' + type + ' 当前应上:' + shouldInClass(getTime()));
        }
    } catch(e) {
        if (e != 'JavaException: com.stardust.autojs.runtime.exception.ScriptInterruptedException: null') {
            exceptionCount.push([getTime(), e]);
            console.warn('好像出了点问题，已作拦截处理、');
            console.error('错误信息: ' + e);
        }
    }
    sleep(800);  // 逻辑复杂，操作较多，稍微提升频率
}

// 函数区
function init() {  // 执行各种初始化操作
    // 导入类
    importClass(android.net.Uri);
    importClass(android.content.Intent);
    importClass(android.view.animation.AlphaAnimation);
    auto.setWindowFilter(function () {  // 设置窗口过滤器，获取所有窗口
        return true;
    });
    for (let i in iter(stime)) {  // 把时间转化为一天中的分钟数来表示
        stime[i] = stime[i]*60+(stime[i]-(stime[i]|0))*40;
        etime[i] = etime[i]*60+(etime[i]-(etime[i]|0))*40;
    }
    console.info('----   开  始  运  行  ----');
}

function whatToDo(time) {  // 根据时间决定行为
    var should = shouldInClass(time);
    if (should != null && order[should] != '自') {
        if (should != null && viewing != should && viewing != -1) {  // 这里viewing != should貌似会
            var classToWatch = order[should];  // 确定当前课程后尝试进入直播间
            console.info('达到预设时间，即将尝试进入课堂['+ classToWatch + ']');
            enterClass(classToWatch, 0, time);
        }
    } else {  // 如果已经到下课时间且还在直播间内直播则退出直播间
        activityFix();
        sleep(500);
        while (!(text('消息').exists() && text('联系人').exists() && text('动态').exists())) {
            back();
            sleep(3000);
        }
        if (viewing != null) {
            if (viewing > 0) {
                console.log('下课时间已到，但仍在上[' + order[viewing] + '?]，即将退出直播');
            } else {
                console.log('下课时间已到，即将结束当前通话');
            }
            exitClass();
            sleep(500);
            viewing = null;
        }
    }
}

function enterClass(classToWatch, trial, now) {  // 进入课堂
    if (trial > qid.length) {  // 如果循环搜索一圈后没有发现可用课程，则认为此节课是自习
        console.error('循环搜索一圈后未发现课程，此节课或为自习？');
        device.vibrate(1000);
        return;
    }
    var cid = tc.indexOf(classToWatch);  // 这节课的科目
    jumpToChat(qid[cid]);  // 跳转到当节课使用的群
    var entrance = null;
    console.log('等待课程开启...');
    var sd = 0;
    //  这是'7'调试完记得改回来        ↓↓↓↓  
    while (getTime() < now+(trial ? 1 : 7) && (entrance == null || parseInt(entrance.text().match(/\d+/)[0]) < threshold)) {
        // 最多等待7分钟，如果人数达到阈值，则进入直播间
        exceptionDeal();
        if (viewing != null) {
            console.warn('已经位于直播间内，认为已在上课');
            return;
        }
        if (!entrance) {
            console.verbose('未检测到可用课程，稍后将再次检测');
        } else if (parseInt(entrance.text().match(/\d+/)[0]) < threshold) {
            console.verbose('人数未达到阈值，暂不进入直播间');
        }
        sd = 1 - sd;  // 针对获取不到view的情况做的跳转优化
        sd && jumpToChat(qid[cid]);
        sleep(1000);
        entrance = textMatches(/\d+\+?人正在(?:语音通话|视频聊天)/).findOnce();
        sleep(1000);
    }
    if (entrance == null) {
        trial ? console.error('即将转到下一个群...') : console.error('没有找到可用直播，即将轮换搜索各群');
        enterClass(tc[(cid+1)%tc.length], trial+1, getTime());
    } else {
        if (!trial && shouldInClass(getTime()-5) == null) {  // 进入课堂时如果刚开始上课则从列表选择随机一条消息发送
            console.log('即将随机选择一条打卡消息发送...');
            sendMessage(signMsg[(random()*signMsg.length)|0]);
        }
        sleep(500);
        var population = parseInt(entrance.text().match(/\d+/)[0]);
        if (population < threshold) {
            console.warn('检测到正在直播，但人数未达到阈值，依设定以一定概率进入');
            if (random() > (population/threshold))  {
                return;
            }
        } else {
            console.log('发现课程，即将进入...');
        }
        rClick(entrance);
        exceptionDeal();  // 有可能会提示正在语音通话中，点击"继续"按钮
        sleep(2000);

        function onSucceeed(_type) {  // 进入直播间成功后的事件处理
            exceptionDeal();
            viewing = shouldInClass(getTime());
            console.info('进入课堂成功! 课程序号:' + viewing);
            type = _type;
        }

        if (entrance.text().match(/语音通话/)) {
            var ui_enter = text('立即加入').findOne(30*1000);  // 等待加入按钮出现
            if (ui_enter) {
                sleep(1000);
                ui_enter.click();
                onSucceeed('share');
                text('挂断').findOne(30*1000);  // 等待进入直播后退出到聊天界面
                if (!text('挂断').exists()) {
                    click(width/2, height/2);
                    text('挂断').findOne(10*1000);
                    if (!text('挂断').exists()) {
                        device.vibrate(3000);
                        console.error('自动进入课程失败!!!请人工检查!!!!!');
                    }
                }
                sleep(2000);
                back();
                sleep(2000);
                while (text('挂断').exists()) {
                    sleep(2000);
                    back();
                }
                sleep(8*1000);
            }
        } else {
            var ui_enter = text('加入本群房间').findOne(30*1000);  // 等待加入按钮出现
            if (ui_enter) {
                sleep(1000);
                pClick(ui_enter);
                onSucceeed('live');
                id('exit_room_img_view').findOne(30*1000);  // 等待进入直播后退出到聊天界面
                if (!id('exit_room_img_view').exists()) {
                    device.vibrate(3000);
                    console.error('自动进入课程失败!!!请人工检查!!!!!');
                }
                sleep(2000);
                back(), sleep(2000), back();
                sleep(10*1000);
            }
        }
    }
}

function sendMessage(msg) {  // 在聊天界面发送文本消息
    var editText = id('input').findOne(3000);
    if (editText) {
        editText.setText(msg);
        var btn = id('fun_btn').findOne(3000);
        btn && btn.click();
        console.info('刚刚自动发送了消息，注意安全。');
        device.vibrate(300);
    }
}

function jump(num) {  // 跳转到指定群资料卡
    console.verbose('正在跳转到'+num+'['+tc[qid.indexOf(num)]+'?]');
    var intent = new Intent(Intent.ACTION_VIEW, Uri.parse(
        'mqqapi://card/show_pslcard?src_type=internal&version=1&card_type=group&uin=' + num
    ));
    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    context.startActivity(intent);
}

function jumpToChat(num) {  // 进入指定群聊天界面
    jump(num);
    var btn = text('发消息').findOne(5000);
    btn && btn.click();
}

function repeatAndSign() {  // 复读，如果匹配到问卷星的连接则自动完成打卡
    var textCount = {}, now = new Date().getTime() / 1000;
    for (let i = chats.length-1; i >= 0; i--) {
        // 若果消息是10秒内发送的且没有复读过则复读这条消息
        if (chats[i][0] > now-10 && !chats[i][2]) {
            var content = chats[i][1].match(/.*?:([\S\s]*)/)[1];
            (textCount[content] == undefined) && (textCount[content] = []);
            textCount[content].push(i);
        }

    }
    for (let s in textCount) {
        if (textCount[s].length > 2) {
            var flag = false
            for (let i in range(lastRepeat.length)) {
                (lastRepeat[i] == s) && (flag = true);
            }
            if (!firstLoop && !flag) {
                if (!coolDown && s != lastOne && s.length <= 4) {
                    console.log('正在尝试复读:\"' + s + '\"');
                    sendMessage(s);
                    lastOne = s;
                }
                lastRepeat.push(s), lastRepeat.shift();
                coolDown = 20;
            }
            for (let i in iter(textCount[s])) {
                chats[textCount[s][i]][2] = true;
            }
        }
    }
    firstLoop = false;
}

function exceptionDeal() {  // 异常状况处理函数
    viewing = getViewing();
    click('继续');
    var root = auto.windowRoots.infer(function (view) {
        return view;
    }, function (view) {
        return view.packageName() == 'com.sohu.inputmethod.sogou.xiaomi';
    });
    root.length && back();
}

function shouldInClass(time) {  
    // 判断某一时间点是否应在上课，若应上课，返回课程序号，否则返回null
    var flag = null, latest = 0;
    for (let i in iter(stime)) {
        if (stime[i] <= time && stime[i] >= latest) {
            latest = stime[i];
            flag = parseInt(i);
        }
        if (etime[i] <= time && stime[i] >= latest) {
            latest = etime[i];
            flag = null;
        }
    }
    return flag;
}

function wjxSign(url) {  // 语文问卷星打卡
    var window = floaty.rawWindow(
        <frame id='frame' w='{{width}}px' h='{{height}}px'>
            <webview id='web'/>
            <text>#Sign#</text>
        </frame>
    );
    window.setPosition(0, 0);
    var alpha = new AlphaAnimation(0.5, 0.5);
    alpha.setDuration(0);
    alpha.setFillAfter(true);
    window.frame.startAnimation(alpha);
    ui.run(function () {
        var settings = window.web.getSettings();
        settings.setJavaScriptEnabled(true);
        window.web.loadUrl(url);
    });
    sleep(7000);
    var root = auto.windowRoots.infer(function (view) {
        return view;
    }, function (view) {
        return view.packageName() == 'org.autojs.autojspro' && view.child(0).child(0).text() == '#Sign#';
    });
    var child = root[0].children()
    var classId = child.findOne(text('6班'));
    classId && classId.parent().click();
    sleep(500);
    var q2 = child.findOne(id('q2'));
    q2 && q2.setText('49');
    sleep(500);
    var q3 = child.findOne(id('q3'));
    q3 && q3.setText('许三多');
    sleep(500);
    click('提交');
    console.info('语文科目 自动打卡 请检查是否成功!');
    device.vibrate(500);
    sleep(1000);
    window.close();
}

function updateChatContent() {  // 获取聊天消息列表，记录最近10秒内发出的消息，最多50条
    var list = id('listView1').findOnce(), now = new Date().getTime() / 1000;
    var newCount = 0, newChat = null, isaid = false;  // 如果屏幕内有自己的消息则不记录
    if (list) {  // 在列表控件内搜索消息框
        var collention = list.children(), ui_chat = [];
        for (let i in range(collention.length)) {
            ui_chat.push(collention[i]);
        }
        ui_chat.sort(function (view) {  // 懒得改代码了，这里实际上是效率极低的写法
            var name = view.children().findOne(id('chat_item_nick_name'));
            if (name) {
                (name.text() == myName) && (isaid = true);
                // 使用正则表达式匹配问卷星打卡链接
                if (name.text() == '语文-陈老师') {
                    var content = view.findOne(className('android.widget.TextView').id('chat_item_content_layout'));
                    if (content) {
                        var mch = content.text().match(/https?:\/\/www\.wjx\.cn\/[A-Za-z0-9/]+\.aspx?/);
                        if (mch && !wjxUrls[mch[0]]) {
                            console.log('检测到问卷星链接，即将启动打卡');
                            console.log('链接: ' + mch[0]);
                            wjxUrls[mch[0]] = true;
                            wjxSign(mch[0]);
                        }
                    }
                }
            }
            return -view.bounds().top;
        });
        var child = ui_chat[0].children();
        var name = child.findOne(id('chat_item_nick_name'));
        var content = child.findOne(className('android.widget.TextView').id('chat_item_content_layout'));
        if (name && content) {
            var lower = content.text();
            (/^[A-Za-z0-9]+$/).test(content) && (content = content.toLowerCase());
            if (name.text() != myName) {                  
                newChat = [now, name.text()+':'+lower, false];
            }
        }
    }
    var delCount = 0;
    while (chats.length && chats[0][0] < now-10 && chats.length > 50) {  // 删除多余的消息
        chats.shift();
        delCount++;
    }
    if (!isaid && newChat && chats[chats.length-1][1] != newChat[1]) {
        newCount = 1; 
        chats.push(newChat);
    }
    (newCount || delCount) && console.verbose('消息记录: 新增'+newCount+'条,删除'+delCount+'条.');
}

function getViewing() {  // 判断当前是否正在看直播并修正type的值
    function trans(v) {
        (v == null) && (v = -1);
        return v;
    }

    var current = currentActivity();
    if (current == activities[0]) {
        type = 'share';
        return trans(viewing);
    } else if (current == activities[1]) {
        type = 'live';
        return trans(viewing);
    }
    var root = auto.windowRoots.infer(function (view) {
        return view;
    }, function (view) {
        return view.packageName() == 'com.tencent.mobileqq' && (view.desc() == '返回视频通话' || view.clickable());
    });
    if (root.length) {
        type = root[0].desc() ? 'share' : 'live';
    }
    return root.length ? trans(viewing) : null;
}

function exitClass() {  // 退出直播
    if (type == 'share') {
        var root = auto.windowRoots.infer(function (view) {
            return view;
        }, function (view) {
            return view.packageName() == 'com.tencent.mobileqq' && view.desc();
        });
        if (!root.length) {
            console.warn('退出过程中发现直播未开启。');
            return;
        }
        if (root[0].clickable()) {
            var ui_float = root[0].children().findOne(textMatches(/\d{2}:\d{2}(?::\d{2})?/));
            ui_float || (ui_float = root[0].children().findOne(text('等待中')));
            pClick(ui_float);
        } else {
            pClick(root[0]);  // 这里不知道是Auto.js的问题还是QQ的问题，有时候找到的控件坐标错误
        }
        sleep(10*1000);
        click('挂断') && console.info('成功退出直播间!');
    } else {
        var root = auto.windowRoots.infer(function (view) {
            return view;
        }, function (view) {
            return view.packageName() == 'com.tencent.mobileqq' && view.clickable() && !view.desc();
        });
        pClick(root[0].child(0).child(1));
        console.info('坐标点击无法检测直播间是否退出成功。');
    }
}

function activityFix() {
    var intent = new Intent(Intent.ACTION_VIEW, Uri.parse(
        'mqqapi://qzone/open_homepage'
    ));
    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    context.startActivity(intent);
}

function getTime() {  // 获取脚本使用的表示法(当前时间在一天中的分钟数)表示的时间
    return new Date().getHours()*60 + new Date().getMinutes();
}

function rClick(view) {  // 找到第一个可点击的父控件点击
    while (!view.clickable()) {
        view = view.parent();
    }
    view.click();
}

function pClick(view) {  // 直接用7.0+自动操作函数点击控件的坐标中心
    var b = view.bounds();
    click(b.centerX(), b.centerY());
}
