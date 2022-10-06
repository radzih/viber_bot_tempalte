from viberio.types.requests import ViberMessageRequest

class TextFilter:
    
    def __init__(self, text: str):
        self.text = text
        
    def __call__(self, request: ViberMessageRequest):
        return request.message.text == self.text