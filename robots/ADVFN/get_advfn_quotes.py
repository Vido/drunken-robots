import re
import time
import mechanize

def debug_write_response(response):
    with open(str(time.time())+'.html', 'w') as fp:
        fp.write(response.read())

def follow_link(browser, keyword):
    regex = re.compile(keyword)
    for link in browser.links():
        match = regex.search(link.url)
        if match:
            browser.follow_link(link)
            break
    else:
        raise Exception('"quote" link not found')

def login_advfn(browser, username, password):
    print 'login_advnf'
    # Based on 4/01/2014 HTML response:
    response = browser.open("http://br.advfn.com/common/account/login")
    #debug_write_response(response)  # debug
    # The first form seens to be a popup
    browser.select_form(nr=1)
    assert browser.form.name == 'login_form'

    browser.form['login_username'] = username
    browser.form['login_password'] = password
    return browser.submit()

def search_tickers(browser, ticker):
    print 'search_tickers'
    print 'quote'
    follow_link(browser, 'quote')

    print 'quote search', ticker
    browser.select_form(nr=0)
    assert 'common/search/exchanges/quote' in browser.form.action
    browser.form['symbol'] = ticker
    response = browser.submit()
    debug_write_response(response)

    print 'follow historic'
    follow_link(browser, 'historic')
    follow_link(browser, 'historico/download')

    # TODO
    # Can't download with a free account

def logout_advfn(browser):
    print 'logout_advfn'
    # Based on 4/01/2014 HTML response:
    follow_link(browser, 'logout=1')

if __name__ == '__main__':
    browser = mechanize.Browser()
    r = login_advfn(browser, 'junkmen', 'vstr1510!!')
    search_tickers(browser, 'BOV:PETRA26')
    r = logout_advfn(browser)
