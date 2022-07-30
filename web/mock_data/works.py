class MyWorks:
    title:str
    sub_title:str
    alt_text:str
    category1:str
    category2:str
    image_url:str
    store_url:str

    def __init__(self, title, sub_title, alt_text, category1, category2, image_url, store_url) -> None:
        self.title = title
        self.sub_title = sub_title
        self.alt_text = alt_text
        self.category1 = category1
        self.category2 = category2
        self.image_url = image_url
        self.store_url = store_url        


    def getAll() -> list:
        return [
            MyWorks(
                title="Invoice, Receipt & Memo generator",
                sub_title="An office document custom file generator",
                category1="app",
                category2="document",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1643395081/my_website/work/website_advert_dazon6.png",
                alt_text="image for invoice receipt and memo application",
                store_url="https://play.google.com/store/apps/details?id=com.anthonyaniobi.invoicereceiptandmemo"
            ),
            MyWorks(
                title="Solar Consult",
                sub_title="Solar PV sizing and installation support",
                category1="app",
                category2="electronics",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1634043542/my_website/work/advert_image_ckfy6f.png",
                alt_text="image for solar consult app",
                store_url="https://play.google.com/store/apps/details?id=com.aniobianthony.solarconsult"
            ),
            MyWorks(
                title="Nigerian Cuisine",
                sub_title="Nigerian Recipe application",
                category1="app",
                category2="",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1634043536/my_website/work/advert_image_xyhsa2.png",
                alt_text="application for learning how to cook",
                store_url="https://apkcombo.com/nigerian-cuisine/com.devessentials.nigeriancuisine/"
            ),
            MyWorks(
                title="Notekeeping App",
                sub_title="A Website built in React (typescript) for keeping notes and todos",
                category1="app",
                category2="website",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1651212150/my_website/work/screenshot_notekeeper_o9r8r7.png",
                alt_text="image for notekeeping app",
                store_url="https://github.com/AnthonyAniobi/NotekeepingReactApp"
            ),
            MyWorks(
                title="Movie Review App",
                sub_title="A Website built in Django for writing reviews of movies",
                category1="website",
                category2="app",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1651212209/my_website/work/screenshot_yz2lcm.png",
                alt_text="image for movie review app",
                store_url="https://github.com/AnthonyAniobi/MovieReviewApp"
            ),
            MyWorks(
                title="Intercontinental Food Recipes",
                sub_title="A Website built in React (typescript) for getting customized food recipes from arround the world",
                category1="website",
                category2="app",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1651212534/my_website/work/intercontinentalRecipe_ck9vrk.png",
                alt_text="image for movie review app",
                store_url="https://github.com/AnthonyAniobi/Intercontinental_Food_Recipes"
            ),
            MyWorks(
                title="Recipe App",
                sub_title="A Recipe application using flutter",
                category1="app",
                category2="",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1634242491/my_website/work/advert_mwmmhi.png",
                alt_text="image for recipe app",
                store_url="https://github.com/AnthonyAniobi/Recipe_Application"
            ),
            MyWorks(
                title="Travel App",
                sub_title="A Travel application using flutter",
                category1="app",
                category2="",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1634242486/my_website/work/advert_j6kd43.png",
                alt_text="image for travel application",
                store_url="https://github.com/AnthonyAniobi/Travel_App"
            ),
            MyWorks(
                title="Login Ui",
                sub_title="A login design in adobe xd for signin and login",
                category1="app",
                category2="design",
                image_url="https://res.cloudinary.com/aniobi/image/upload/v1634139801/my_website/work/advert_small_mfv8j5.png",
                alt_text="a login image design",
                store_url="https://dribbble.com/shots/16647079-Simple-Signup-Ui"
            )
        ]

    def categories():
        category_set = set()
        for x in MyWorks.getAll():
            if x.category1 != "":
                category_set.add(x.category1)
            if x.category2 != '':
                category_set.add(x.category2)
        return category_set
    
    def getMore():
        if(len(MyWorks.getAll()) < 7):
            return False
        else:
            return True

if __name__ == "__main__":
    val = MyWorks.categories()
    print(val)