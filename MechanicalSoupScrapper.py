import mechanicalsoup as ms

br = ms.StatefulBrowser()

br.open("https://www.w3schools.com/css/default.asp")


response1 = br.follow_link(link_text="Start CSS Quiz!")
#assert br.viewing_html()
#print(br.soup())
print(br.get_url())
print(response1.headers)# headers
##print(response1.text)  br.get_current_page() # body

response2 = br.follow_link(link_text='Java Tutorial')
print(br.get_url())

domainurl = 'https://www.w3schools.com/'
## Click link is not there in MechanicalSoup.
req = br.find_link(link_text='Start Java Quiz')['href']
print(req)
br.open(domainurl+req)
print(br.get_url())
print(br.get_current_page())


'''
Notes::
https://mechanicalsoup.readthedocs.io/en/stable/index.html

'''