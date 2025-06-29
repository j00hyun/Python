# pypi 에서 사용 가능한 패키지 검색 가능
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())