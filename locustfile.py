from locust import HttpUser, TaskSet, between

def index(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {index: 1}

class WebsiteUser(HttpUser):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
