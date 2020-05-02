import mechanize



br = mechanize.Browser()
br.open("https://www.w3schools.com/css/default.asp")

# follow second link with element text matching regular expression
response1 = br.follow_link(text_regex=r"Start", nr=2)
assert br.viewing_html()
print(br.title())
print(response1.geturl())
print(response1.info())  # headers
print(response1.read())  # body

response2 = br.follow_link(text_regex=r"Java*", nr=1)
print(response2.geturl())

req = br.click_link(text='Start Java Quiz')
br.open(req)
print(br.geturl())
print(br.response().read())

'''
br.select_form(name="order")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm.
br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
# Submit current form.  Browser calls .close() on the current response on
# navigation, so this closes response1
response2 = br.submit()
'''


'''
Notes: 
https://stackoverflow.com/questions/30607410/web-scraper-for-dynamic-forms-in-python - Read a page and submitting a form in that.
https://stackoverflow.com/questions/44557234/how-to-use-mechanize-to-fill-out-form - Filling a form
https://www.pythonforbeginners.com/mechanize/python-mechanize-cheat-sheet
https://www.pythonforbeginners.com/python-on-the-web/browsing-in-python-with-mechanize/

## Important::
http://wwwsearch.sourceforge.net/mechanize/
http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/
http://stockrt.github.io/p/handling-html-forms-with-python-mechanize-and-BeautifulSoup/


'''