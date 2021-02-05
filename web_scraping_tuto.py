'''
realpython.com/python-web-scraping-practical-introduction
'''

'''
Web scraping is the process of collecting and parsing raw data from the Web

- Parse website data using string methods and regular expressions
- Parse website data using an HTML parser
- Interact with forms and other website components
'''

'''
python standard library for web scraping: urllib.request
'''

from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/aphrodite'

page = urlopen(url)

print(page)

'''
To extract the HTML from the page, first ust the HTTPResponse object's.read()
method, which returns a sequence of bytes. Then use .decode() to decode the
bytes to a string using UTF-8
'''

html_bytes = page.read()
html = html_bytes.decode('utf-8')

#print(html)

'''
Extract Text from HTML with String methods
'''

title_index = html.find('<title>')
print('title index: ', title_index) # count including '\n'

# <title> Tag does not have info, get rid of it
start_index = title_index + len('<title>')
end_index = html.find('</title>')

title = html[start_index: end_index]
print(title)

'''
But, the real world is much more compicate
'''

url2 = 'http://olympus.realpython.org/profiles/poseidon'
page = urlopen(url2)

html = page.read().decode('utf-8')
print(html)

print(html.find('<title>'))
'''
will return -1 because there is not <title>
there is <title >
'''

start_index = html.find('<title>') + len('<title>')
end_index = html.find('</title>')

title = html[start_index: end_index]
print(title)
'''
Undesirable result
<head>
<title >Profile: Poseidon
'''

'''
pattern
- .* : stands for any character repeated any number of times.
       python regular expression is greedy so, it will find the longest
       possible match

- .*? : the shortest possible string
'''

import re
pattern = '<title.*?>.*?</title.*?>'

match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()

'''
result
<head>
<title >Profile: Poseidon
<title >Profile: Poseidon</title>
'''
print(title)

title = re.sub('<.*?>', '', title) # Remove HTML Tag
print('title:', title)


'''
Exercise
'''
url = 'http://olympus.realpython.org/profiles/dionysus'

page = urlopen(url)

html = page.read().decode('utf-8')

print(html)

pattern = 'Name:.*?<'

for string in ['Name: ', 'Favorite Color:']:

    start_index = html.find(string)
    text_start_index = start_index + len(string)

    next_html_tag_offset = html[text_start_index:].find('<')
    text_end_index = text_start_index + next_html_tag_offset

    raw_text = html[text_start_index: text_end_index]

    #print(raw_text) # There is empty spaces

    cleaned_text = raw_text.strip(' \r\n\t')

    print(cleaned_text)

'''
Future works
- Use an HTML Parser for web scraping in python

'''
