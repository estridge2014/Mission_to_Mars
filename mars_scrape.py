# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Set the executable path & browser
scrape_all():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #Set up the HTML parser

    html = browser.html
    news_soup = soup(html, 'html.parser')
    slide_elem = news_soup.select_one('div.list_text')

    slide_elem.find('div', class_='content_title')


    # Use the parent element to find the first `a` tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()

    # Use the parent element to find the paragraph text

    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()


    # ### Featured Images


    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)



    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()



    browser.find_by_tag('button')[0]



    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'


    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    table = df.to_html(classes="table table-striped")

    # ### Visit the NASA Mars News Site

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')


    slide_elem.find('div', class_='content_title')


    # Use the parent element to find the first a tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()

    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    # ### JPL Space Images Featured Image




    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)



    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()



    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')




    # find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')



    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'



    # ### Mars Facts



    df = pd.read_html('https://galaxyfacts-mars.com')[0]




    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)



    table = df.to_html(classes = "table table-striped")


    # # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

    # ### Hemispheres



    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    html_soup = soup(html, 'html.parser')

    # html_soup


    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    # hemisphere_images = html_soup.find_all('h3').text
    # hemisphere_images

    for i in range(4):
        browser.find_by_css("a.product-item img")[i].click()
        html = browser.html
        html_soup = soup(html, 'html.parser')
        title = html_soup.find("h2", class_="title").get_text()
        sample = html_soup.find("a", text = "Sample").get("href")
        hemisphere = {
            "title": title, 
            "img_url": url + sample
        }
        hemisphere_image_urls.append(hemisphere) 
        browser.back()



    # 4. Print the list that holds the dictionary of each image url and title.
    print(hemisphere_image_urls)


    # 5. Quit the browser
    browser.quit()




    hemisphere_image_urls[1]["title"]




    blah = {
        "news_title": news_title, 
        "news_p": news_p,
        "featured_image": img_url,
        "hemispheres": hemisphere_image_urls,
        "facts": table
    }
    return blah

if __name__="__main__":
    print(scrape_all())






