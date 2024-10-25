import requests

def get_waifu(type: str, category: str) -> dict:
    """Get waifu image.
    Keyword arguments:
    type:str - Type of category (sfw or nsfw)
    category:str - Category of waifu image
    Return:dict - JSON data
    """
    url = f"https://api.waifu.pics/{type}/{category}"
    print("requested url: "+ url)
    response = requests.get(url)

    return response.json()