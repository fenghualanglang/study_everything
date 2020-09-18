from celery_demo.main import app


@app.task
def send_sms(username, phone):

    return username + phone

