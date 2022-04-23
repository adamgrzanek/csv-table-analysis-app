import requests
import unittest
import datetime


class TestAPP(unittest.TestCase):

    BASE = 'http://127.0.0.1:5000/'

    def test_page(self):
        url = self.BASE + 'test'
        resp = requests.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, f'test OK - {str(datetime.datetime.now())[:-7]}')

    def test_home_page(self):
        url = self.BASE + 'postcsv'
        resp = requests.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_post_file(self):
        url = self.BASE + 'postcsv'
        with open('data/example_file.csv', 'rb') as f:
            file = {'csvfile': f}
            resp = requests.post(url, files=file)
            self.assertEqual(resp.status_code, 200)

    def test_result_page(self):
        url = self.BASE + f'results/example_file_30x6_{datetime.date.today()}'
        resp = requests.get(url)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)

