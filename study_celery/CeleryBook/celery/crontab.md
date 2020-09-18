## crontab
一个表示时间间隔的对象，语法与linux的crontab类似。
minute和hour可以设置为*/15，*/2，分别表示每隔15分钟和每隔2小时。
day_of_week用可以0-6的数字表示，也可以文字表示mon-fri。*/2并不是每2天，而是每半天。
官网一些具体例子：

- 每分钟执行

  ```python
  crontab(minute="*/1")
  ```

- 每小时执行

  ```python
  crontab(minute=0, hour="*/1")
  ```

- 每天凌晨执行

  ```python
  crontab(minute=0, hour=0)
  ```

- 每三个小时执行: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm

  ```python
  crontab(minute=0, hour=’*/3’)*
  ```

  ```python
  crontab(minute=0,hour=‘0,3,6,9,12,15,18,21’) 
  ```

- 星期天每分钟执行

  ```python
  crontab(day_of_week='sunday') 
  ```

  ```python
  crontab(minute='',hour='', day_of_week='sun') 
  ```

- 每十分钟执行, 但是只在星期四、五的 3-4 am, 5-6 pm, and 10-11 pm

  ```python
   crontab(minute='/10',hour='3,17,22', day_of_week='thu,fri')
  ```

- 每两个小时及每三个小时执行，除了下面时间的每个小时: 1am, 5am, 7am, 11am, 1pm, 5pm, 7pm, 11pm

  ```python
   crontab(minute=0, hour='/2,/3') 
  ```

- 每五个小时执行。这意味着将在 3pm 而不是 5pm 执行 (因为 3pm 等于 24 小时制的 15, 能被 5 整除) 

  ```python
  crontab(minute=0, hour=’*/5’) 
  ```

- 每三个小时, 以及 (8am-5pm) 之间的小时执行

  ```python
  crontab(minute=0, hour='*/3,8-17')
  ```

- 每个月的第二天执行

  ```python
  crontab(0, 0, day_of_month='2') 
  ```

- 每个月的偶数天执行

  ```python
  crontab(0, 0, day_of_month='2-30/3')
  ```

- 每个月的第一个和第三个星期执行

  ```python
  crontab(0, 0, day_of_month=‘1-7,15-21’) 
  ```

- 每年五月份的第十一天执行

  ```python
  crontab(0, 0, day_of_month='11',month_of_year='5')
  ```

- 每个季度的第一个月执行 

  ```python
  crontab(0, 0, month_of_year='*/3')
  ```

  