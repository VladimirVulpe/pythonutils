from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup 

def one_de_prices(notebook_types):
    my_url = 'https://www.one.de/notebooks/' +notebook_types
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class":"product--info-box"})
    
    for container in containers:
        info_text_container = container.findAll("a", {"class":"product--title"})
        info_price_container = container.findAll("div", {"class":"price--default-list"})

        print info_text_container[0].text.strip() + ": " + info_price_container[0].text.strip()


def jax_enter_artikel_authoren(author_name, anzahl_bisheriger_artikel):
    url_jax_enter = 'https://jaxenter.de/author/' +author_name
    jax_enter_Client = uReq(url_jax_enter)
    jax_enter_page_html = jax_enter_Client.read()
    jax_enter_Client.close()

    jax_enter_page_soup = soup(jax_enter_page_html, "html.parser")
    container_jax_enter = jax_enter_page_soup.findAll("div", {"class":"info"})
    author_name = jax_enter_page_soup.findAll("span", {"class":"author-name"})
    
    for container in container_jax_enter:
        info_text_container = container.a
        
        print  author_name[0].text.strip() + ": " + info_text_container.text
    
    if len(container_jax_enter) > anzahl_bisheriger_artikel:
        print "Unter der URL gibt es einen neuen Artikel: " + url_jax_enter


#ONE.de gaming notebooks
one_de_prices('one-gaming-notebooks/')
print
one_de_prices('one-business-notebooks/')
print
one_de_prices('ultrabooks/')
print

#JAX Enter Authoren
jax_enter_artikel_authoren('axelfontaine', 1)
