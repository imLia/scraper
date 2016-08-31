import mechanize
from bs4 import BeautifulSoup
import urllib2
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_handle_robots(False)





br.set_cookiejar(cj)

# url = 'http://localhost:5000/login'
url = 'https://admindev.acommercedev.com/partner/'
br.open(url)

br.select_form(nr=0)
br.form['username'] = 'joseph_santiago'
br.form['password'] = '@ABcd123'

br.submit()

print br.response().read()


# for form in br.forms():
#     print form
# br.form = list(br.forms())[0]
#
# br.form['username'] = 'username'
# br.form['password'] = 'password.'
# br.submit()
#
# print br.response().read()
