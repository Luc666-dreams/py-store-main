# Store

Esta biblioteca fornece funcionalidade webscraping pra website (brasileiros) de produtos.
## Instalação

Digite isto no seu cmd, terminal e afins.

    pip install git+https://github.com/Naegin/py-store.git

### Lista de websites.
1° - [Nike](https://www.nike.com.br)

### Como usar (Nike)

```py
from store import Nike

proxies = {"https": "link em https"}

nike = Nike()

product = nike.product(url='/air-jordan-13-153-169-211-323815', proxies=proxies)

print(product.name)
print(product.img)
print(product.url)
print(product.price)
print(product.sold)
print(product.available)
print(product.store)
print([product.size for product in product.sizes])

snkrs = nike.snkrs(page='1', demanda='True')

print([product.url for product in snkrs])
print([product.name for product in snkrs])
print([product.image for product in snkrs])

```