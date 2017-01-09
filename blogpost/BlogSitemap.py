from django.contrib.sitemaps import Sitemap
from models import Blogpost


class BlogSitemap(Sitemap):
    changefreq = 'nerver'
    priority = 0.5

    def items(self):
        return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.posted
