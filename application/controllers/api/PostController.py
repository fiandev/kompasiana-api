import minify_html, re
from application.utilities.response import api_response_error, api_response_success
from application.utilities.scraper import get_elements

HOST_URL = "https://www.kompasiana.com"

class PostController:
    @staticmethod
    def get_content (elements):
        # remove ads
        for item in elements.select(".read-artikel *"):
            if not item.name == "p" or (item.has_attr("class") and "img-read" in item["class"]):
                # item.decompose()
                pass
        article = str(elements.find(_class="read-artikel"))
        return minify_html.minify(article.replace('"', "\"").replace("  ", ""), minify_js=True, minify_css=True, remove_processing_instructions=True)
    @staticmethod
    def show (username: str, prefix: str, slug: str):
        try:
            if not prefix or not slug or not username:
                raise Exception(f"username, prefix and slug is must be passing")
            url = f"{ HOST_URL }/{ username }/{ prefix }/{ slug }?page=all#section1"
            elements = get_elements(url)

            images = []
            for element in elements.find_all(class_="slidesSmall"):
                image = element.find("img").get("src")
                if not image == 'https://assets-a1.kompasiana.com//statics/2019_kompasiana/images/gambar-default-karusel2.jpg?t=o&amp;v=260':
                    images.append(image)
            
            return api_response_success({
                "title": elements.find("h1", class_="title").get_text().strip(),
                "tag": elements.find(class_="artikel--tag").find("span").get_text().strip(),
                "thumbnail": elements.find(class_="slidesBig").find("img").get("src"),
                "images": images,
                "content": PostController.get_content(elements),
            })
        except Exception as err:
            return api_response_error(str(err))