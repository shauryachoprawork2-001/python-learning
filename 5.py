#static no copulsary parameter cannot access class or instance they ar stand alone function
#they are tied up with the logic of the class

class laptop:
    storage:"ssd"
    @staticmethod
    def get_mefinal_price(price,discount):
     final_price= price - (discount*price/100)
     print(f"{final_price}")
l1 = laptop()
l1.get_mefinal_price(400,5)
    
     
    