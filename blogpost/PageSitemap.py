from django.contrib.sitemaps import Sitemap, reverse


class PageSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['main']

    def location(self, item):
        url = reverse(item)
        print 'location: ', url
        return url
