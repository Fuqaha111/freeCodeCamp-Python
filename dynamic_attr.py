class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}


config_obj = Configuration()


for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)


# hasattr 

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_1 = Product("Iphone", 350)
        
inventory = ["name", "price", "inventoryID"]


for attr in inventory:
    if not hasattr(product_1, attr):
        print (f"{attr} is not  a valid attribute")

    else:
        print(f"{attr}: {getattr(product_1, attr)}")