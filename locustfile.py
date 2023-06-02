from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # wait time between requests (in seconds)

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def about_page(self):
        self.client.get("/about")

    @task(2)
    def contact_page(self):
        self.client.get("/contact")

    @task(1)
    def products_page(self):
        self.client.get("/products")

    def on_start(self):
        # called when a Locust user starts before any task is scheduled
        pass
