class Catalogue:
    def __init__(self, name: str):
        self.name = str(name)
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(str(product_name))

    def get_by_letter(self, first_letter: str):
        res = list(filter(lambda prod: prod[0] == first_letter, self.products))
        return res

    def __repr__(self):
        x = '\n'
        new = sorted(self.products)
        result = f"Items in the {self.name} catalogue:\n{x.join(new)}"
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
