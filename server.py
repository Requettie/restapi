from flask import Flask
from data import data

app = Flask()

if __name__ == '__main__':
    app.run()

me = {
    "name" : "Sergio",
    "last" : "Inzunza",
    "email" : "sinzunza@sdgku.edu",
}


    @app.route("/")
    @app.route("/")
    def index():
        return "hello from Flask"

    @app.route("/about")
    def about():
        # dictionary
        me = {
            "name" : "Sergio",
            "last" : "Inzunza",
            "email" : "sinzunza@sdgku.edu",
        }

    @app.route("/api/catalog")
    def get_catalog():
        return products

    @app.route("/api/catalog")
    def get_catalog()
        return products


#add
products.append("strawberry")
products.append("dragon fruit")

#length
print(f"You have:{len(products)} products in your catalog")

#iterate
for fruit in products:
    print(fruit)

for i in range(0, 10, 1):
    print(i)




    
    return MemoryError
    

    if __name__ = '__main__':
        app.run(debug=True)