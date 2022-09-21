from django.test import TestCase

# Create your tests here.
class MyWatchListTest(TestCase):
    @classmethod
    def html_url_exists(self):
        response = self.client.get("/mywatchlist/html", follow=True)
        self.assertEqual(response.status_code, 200)

    def xml_url_exist(self):
        response = self.client.get("/mywatchlist/xml", follow=True)
        self.assertEqual(response.status_code, 200)

    def json_url_exist(self):
        response = self.client.get("/mywatchlist/json", follow=True)
        self.assertEqual(response.status_code, 200)

