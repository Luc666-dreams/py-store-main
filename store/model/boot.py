class Error:
    def __init__(self, data):
        self.data = data
        self.error = data.get('error', False)
        self.response = data.get('response', None)

class Boot:
    def __init__(self, data):
        self.data = data
        self.name = data.get('name', None)
        self.img = data.get('img', None)
        self.url = data.get('url', None)
        self.price = data.get('price', None)
        self.sizes = data.get('sizes', None)
        self.store = data.get('store', None)
        self.sold = data.get('sold', False)
        self.available = data.get('available', False)
        
class Size:
    def __init__(self, data):
        self.data = data
        self.size = data.get('size', None)
        self.url = data.get('url', None)

