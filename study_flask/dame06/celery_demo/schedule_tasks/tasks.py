from celery_demo.main import app


# 手动执行任务
@app.task
def manual_task(a, b):
    # 手动执行任务
    return a+b

# 半自动执行任务
@app.task
def semi_auto_task(phone):
    return phone

# 自动执行任务
@app.task
def auto_task(email):
    return email

# 定时任务
@app.task
def scheduler(weather):
    return weather
