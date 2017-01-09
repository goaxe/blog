from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.http import HttpRequest
from blogpost.views import index, view_post
from models import Blogpost
from datetime import datetime
from django.contrib.sitemaps.views import sitemap


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn(b'Welcome to my blog', response.content)


class BlogpostTest(TestCase):
    def test_blogpost_url_resolves_to_blog_post_view(self):
        found = resolve('/blog/this_is_a_test.html')
        self.assertEqual(found.func, view_post)

    def test_blogpost_create_with_view(self):
        Blogpost.objects.create(title='hello', author='admin', slug='this_is_a_test',
                                posted=datetime.now(), body='This is a blog')
        response = self.client.get('/blog/this_is_a_test.html')
        self.assertIn(b'This is a blog', response.content)

    def test_blogpost_create_with_show_in_homepage(self):
        Blogpost.objects.create(title='hello', author='admin', slug='this_is_a_test',
                                posted=datetime.now(), body='This is a blog')
        response = self.client.get('/')
        self.assertIn(b'This is a blog', response.content)

    def test_sitemap(self):
        found = resolve('/sitemap.xml')
        self.assertEqual(found.func, sitemap)
        print found


