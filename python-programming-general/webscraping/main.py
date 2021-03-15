from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # tags = soup.find('h5')
    courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)
    for course in courses_html_tags:
        print(course.text)
