import unittest
from app import meu_web_app


class TestPerfilDenis(unittest.TestCase):

    def setUp(self):
        # Método de TestCase sempre executado quando irá iniciar um test
        app = meu_web_app.test_client()
        self.response = app.get('/denis')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def tearDown(self):
        # Método de TestCase sempre executado quando irá terminar um test
        pass

    def test_content(self):
        # self.response.data.decode('utf-8') -> Transforma bytes para string
        self.assertIn('Denis M. Sousa', self.response.data.decode('utf-8'))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="#"', response_str)
        self.assertIn('Me siga no Instagram', response_str)

class TestPerfilDrica(unittest.TestCase):

    def setUp(self):
        # Método de TestCase sempre executado quando irá iniciar um test
        app = meu_web_app.test_client()
        self.response = app.get('/drica')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def tearDown(self):
        # Método de TestCase sempre executado quando irá terminar um test
        pass

    def test_content(self):
        # self.response.data.decode('utf-8') -> Transforma bytes para string
        self.assertIn('Adrilene Fonseca', self.response.data.decode('utf-8'))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="#"', response_str)
        self.assertIn('Me siga no Instagram', response_str)

if __name__ == '__main__':
    unittest.main()