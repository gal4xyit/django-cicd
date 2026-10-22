from django.test import SimpleTestCase


class PageTests(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertContains(response, "<h1>Головна</h1>", html=True)
        self.assertTemplateUsed(response, "pages/page.html")

    def test_about_page(self):
        response = self.client.get("/about/")
        self.assertContains(response, "<h1>Про проєкт</h1>", html=True)
        self.assertTemplateUsed(response, "pages/page.html")

    def test_contacts_page(self):
        response = self.client.get("/contacts/")
        self.assertContains(response, "<h1>Контакти</h1>", html=True)
        self.assertTemplateUsed(response, "pages/page.html")

    def test_navigation_links(self):
        links = [
            ("/", "Головна"),
            ("/about/", "Про проєкт"),
            ("/contacts/", "Контакти"),
        ]

        for page_url, _ in links:
            with self.subTest(page=page_url):
                response = self.client.get(page_url)

                for link_url, label in links:
                    self.assertContains(
                        response,
                        f'<a href="{link_url}">{label}</a>',
                        html=True,
                    )

    def test_missing_page_returns_404(self):
        response = self.client.get("/missing-page/")
        self.assertEqual(response.status_code, 404)
