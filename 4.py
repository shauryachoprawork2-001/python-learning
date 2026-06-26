class Laptop:
    storage_typ="ssd"
    @classmethod
    def get_storage_type(cls):
        print(f"{cls.storage_typ}")
Laptop.get_storage_type()
       

