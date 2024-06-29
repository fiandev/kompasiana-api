from application.utilities.response import api_response_error, api_response_success
from application.utilities.scraper import get_elements

HOST_URL = "https://www.kompasiana.com"

class ProfileController:
    @staticmethod
    def index (username: str):
        try:
            if not username:
                raise Exception(f"username is must be passing")
            url = f"{ HOST_URL }/{ username }"
            elements = get_elements(url)
            posts = []

            for post in elements.find_all(class_="artikel"):
                posts.append({
                    "title": post.find(class_="artikel--content").find("h2").get_text().strip(),
                    "thumbnail": post.find(class_="artikel--img").find("img").get("src"),
                    "slug": post.find(class_="artikel--img").find("a").get("href").replace(f"{ HOST_URL }/{ username }/", "").split("/").pop(),
                    "prefix": post.find(class_="artikel--img").find("a").get("href").replace(f"{ HOST_URL }/{ username }/", "").split("/")[0],
                })
            return api_response_success({
                "point": int(elements.find(class_="poin-total").find("b").get_text()),
                "level": elements.find(class_="poin-pangkat").get_text(),
                "name": elements.find("title").get_text().split("-")[0].replace("Halaman Artikel Profil", "").strip(),
                "avatar": elements.find(class_="user-img").find("img").get("src"),
                "posts": posts
            })
        except Exception as err:
            return api_response_error(str(err))