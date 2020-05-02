import mechanize


br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.google.com")

print(br.title())

br.select_form(name="f")
br.set_handle_equiv(False)
br.set_handle_robots(False)
br['q'] = "santhosh"
print(br.form)
#br.submit()


response = mechanize.urlopen("http://www.google.com/search?q=santhosh")
print(response.read())