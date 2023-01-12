from bs4 import BeautifulSoup
soup = BeautifulSoup()
soup = BeautifulSoup(open('index.html'))
#print soup.prettify();' //all element in this html
#print soup.title
#<title>The Dormouse's story</title> results
#print soup.head
#<head><title>The Dormouse's story</title></head> results
#print soup.a a tag
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a> results
#print soup.p p tag
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p> results
#print soup.name
#print soup.head.name
#[document] resluts
#head results
#print soup.p.attrs get attributes
#{'class': ['title'], 'name': 'dromouse'} results
#print soup.p['class'] #print soup.p.get('class') same method
#['title'] results
#soup.p['class']="newClass"
#print soup.p can change the tage content
#<p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>
#print soup.p.string get string in tag
#The Dormouse's story
#if type(soup.a.string)==bs4.element.Comment: directly and only get content
    #print soup.a.string;
    # Elsie  results
#print soup.head.contents[0] can use to get the first element
#<title>The Dormouse's story</title>
for child in  soup.body.children:
    print(child)
'''<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>'''
#results
for child in soup.descendants:
    print(child)
#recursion way to get all tag without header
""""<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body></html>
<head><title>The Dormouse's story</title></head>
<title>The Dormouse's story</title>
The Dormouse's story


<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>


<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<b>The Dormouse's story</b>
The Dormouse's story


<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
Once upon a time there were three little sisters; and their names were

<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
 Elsie 
,

<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
Lacie
 and

<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
Tillie
;
and they lived at the bottom of a well.


<p class="story">...</p> results"""
for string in soup.stripped_strings:
    print(repr(string))#could remove blank content
"""
'html = """
"The Dormouse's story"
"The Dormouse's story"
'Once upon a time there were three little sisters; and their names were'
','
'Lacie'
'and'
'Tillie'
';\nand they lived at the bottom of a well.'
'...'
""""""
#results
print(soup.find_all('a'))#find all a element
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]results
for tag in soup.find_all(True): # get all tag
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
#soup.find_all(id='link2')  find keyword
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
#soup.find_all(href=re.compile("elsie")) find herf keywords
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
#soup.find_all(text="Elsie")
# [u'Elsie']
#soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']
#soup.find_all(text=re.compile("Dormouse"))
#[u"The Dormouse's story", u"The Dormouse's story"]
#useful for upper 3 line could used in research keywords focus on it
