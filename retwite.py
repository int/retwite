import re
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api.urlfetch import fetch

class Twitter(webapp.RequestHandler):
    def doit(self, method):
        p = re.compile(r'retwite.appspot.com/search/')
        if p.search(self.request.url):
            url = p.sub('search.twitter.com/', self.request.url, 1)
        else:
            p = re.compile(r'retwite.appspot.com')
            url = p.sub('twitter.com', self.request.url, 1)
        r = fetch(url, self.request.body, method, self.request.headers)
        self.response.set_status(r.status_code)
        self.response.headers = r.headers
        self.response.out.write(r.content)

    def get(self):
        self.doit('GET')

    def delete(self):
        self.doit('DELETE')

    def post(self):
        self.doit('POST')

application = webapp.WSGIApplication([('/.*', Twitter)], debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
