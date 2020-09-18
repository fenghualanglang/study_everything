<font color=red>Tornado</font>提供支持WebSocket的模块是tornado.websocket, <font color=red><b>WebSocketHandler</b></font>类用来处理通讯。 


- WebSocketHandler.open()
    
    ```
    当一个WebSocket连接建立后被调用
    ```
    
- WebSocketHandler.on_message(message)
    
    ```
    当客户端发送消息message过来时被调用，**注意此方法必须被重写**。
    ```
    
- WebSocketHandler.on_close()
    
    ```
    当WebSocket连接关闭后被调用。
    ```
    
- WebSocketHandler.write_message(message, binary=False)
    
    ```
    向客户端发送消息messagea，message可以是字符串或字典（字典会被转为json字符串）。
    若binary为False，则message以utf8编码发送；二进制模式（binary=True）时，可发送任何字节码。
    ```
    
- WebSocketHandler.close()
    
    ```
    关闭WebSocket连接。
    ```
    
- WebSocketHandler.check_origin(origin)
    
    ```
    判断源origin，对于符合条件（返回判断结果为True）的请求源origin允许其连接，否则返回403。
    可以重写此方法来解决WebSocket的跨域请求（如始终return True）
    ```



【参考资料】 

- [tornado官方]( https://www.tornadoweb.org/en/stable/websocket.html )

- [简书-tornado](https://www.jianshu.com/p/3a928ade93dc )







