from celery_demo.main import app


@app.task
def send_email(username, email):

    return username + email


