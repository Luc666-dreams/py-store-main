from bs4 import BeautifulSoup
from .request import Request
from .model import Error, Boot, Size
from .data import headers, info

#Classe do site da nike
# self.request = Obter a conexão através do modulo request, é passar a url.
class Nike:
    def __init__(self, proxy=None):
        self.request = Request(base_url='https://www.nike.com.br')
        self.headers = headers
        self.info = info
    
    #Puxar todo os produto da aba Snkrs
    def snkrs(self, page='1', demanda='True', count=10, proxies=None):
       try:
          #Passar a página pra dar o get, e alguns valores como proxy e pagina e se a demanda é valida.
          r = self.request.get('/Snkrs/Estoque', headers=self.headers, params={'p':page, 'demanda':demanda}, proxies=proxies)
          #Passar o texto obtido da url no Bs4 pra conveter os valores.
          soup = BeautifulSoup(r.text, 'html.parser')
          #Obter todo os valores que contem 'produto produto--comprar'
          products  = soup.find_all('div', {'class':'produto produto--comprar'})
          data = []
          #Pegar os valores obtido e passar por um for pra categorizar-los.
          for product in products[:count]:
             #Informações que tem no botão.
             url =  product.find('a', attrs={'class': 'btn'})
             #Informaçoes que tem na imagem.
             img =  product.find('img', attrs={'class': 'aspect-radio-box-inside'})
             #Obter o link do produto.
             url = None if url is None else url['href']
             #Obter o primeiro nome do produto.
             name = None if img is None else img['alt'].split(' - ')[0]
             #Obter a img do produto.
             img = None if img is None else img['data-src']
             #Passar os valores json é converter eles em um objeto.
             data.append(Boot({'url':url, 'img':img, 'name':name}))
          #Retornar o 'data' com os valores do produto em objeto.   
          return data
       except Exception as e:
           #Retornar o erro em objeto.
           return Error({'error':True, 'e':e})    	
    
    def get_sizes(self, soup):
       sizes  = soup.find_all('input', {'class':'tamanho__item_pdp js-tamanho__item_pdp'})
       data = []
       for size in sizes:
            data.append(Size({'size':size['data-tamanho'], 'url':size['value']}))
       return data    
    
    #Puxar todo os size de um produto.
    def sizes(self, url, proxies=None):
       try:
          self.headers['referer'] = url
          #Passar a página pra dar o get, e alguns valores como proxy e pagina e se a demanda é valida.
          r = self.request.get('/Snkrs/PdpDependeCaptcha', headers=self.headers, proxies=proxies)
          #Passar o texto obtido da url no Bs4 pra conveter os valores.
          soup = BeautifulSoup(r.text, 'html.parser')
          return soup
       except Exception as e:
           #Retornar o erro em objeto.
           return Error({'error':True, 'e':e})      

    #Puxar as inforamções de um produto.
    def product(self, url, proxies=None):
       try:
          link = str(url).replace('https://www.nike.com.br', '')
          #Passar a página pra dar o get, e alguns valores como proxy e pagina e se a demanda é valida.
          r = self.request.get(link, headers=self.headers, proxies=proxies)
          #Passar o texto obtido da url no Bs4 pra conveter os valores.
          soup = BeautifulSoup(r.text, 'html.parser')
          #Obter todo os valores que contem 'produto produto--comprar'
          logo  = soup.find('div', attrs={'class': 'logo'})
          #verificar se a loja é snkrs ou normal
          store = 'nike-snkrs' if 'snkrs' in logo.a['href'] else 'nike'
          #Obter os nome e imagem do produto
          product = soup.find(self.info[store]['product']['type'], attrs={'class': self.info[store]['product']['value']})
          #Obter o preço do produto
          price = soup.find(self.info[store]['price']['type'], attrs={'class': self.info[store]['price']['value']})
          #Verificar se o produto estar esgotado.
          sold = soup.find(self.info[store]['sold']['type'], attrs={'class': self.info[store]['sold']['value']})
          #Verificar se o produto vai ser disponibilizado dia xx.
          available = soup.find(self.info[store]['available']['type'], attrs={'class': self.info[store]['available']['value']})
          
          #Nome do produto.
          name = None if product is None else product['title']
          #Imagem do produto.
          img = None if product is None else product['href']
          #Preço do produto.
          price = None if price is None else price.get_text(strip=True)
          #Produto esgotado.
          sold = False if sold is None else sold.get_text(strip=True)
          #Disponibilidade do produto.
          available = False if available is None else available.get_text(strip=True)
          
          #Verificar se o produto tá esgotado ou sua disponbilidade para obter os sizes.
          if sold is False or available is False:
             #Obter os size do produto, porém verificar se o produto é da aba principal ou´um snkrs.
             sizes = self.get_sizes(soup if store == 'nike' else self.sizes(url=r.url, proxies=proxies))
          else:
            sizes = []
          #Retornar o objeto do produto.
          return Boot({'name':name, 'img':img, 'price':price, "url":r.url, 'sold':sold, 'store':store, 'available':available, 'sizes':sizes})
       except Exception as e:
           #Retornar o erro em objeto.
           return Error({'error':True, 'e':e})                 
