from django.contrib.sitemaps import Sitemap
from polls.models import Question,New
from django.urls import reverse

class QuestionSitemap(Sitemap):

    priority = 0.5

    changefreq = "always"

    def items(self):
        return Question.objects.all()
    def lastmod(self, obj):
        return obj.pub_date


class NewSitemap(Sitemap):

    priority = 0.5
    
    changefreq = "never"

    def items(self):
        return New.objects.all()
    def lastmod(self, obj):
        return obj.pub_date

class StaticViewSitemap(Sitemap):

    priority = 0.5  

    def items(self):
        return ["index","faq","news","about"]

    def location(self, item):
        return reverse(item)