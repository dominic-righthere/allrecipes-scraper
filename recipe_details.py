from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json
import lxml

def get_recipe_details(str_url = 'https://www.allrecipes.com/recipe/68943/slow-cooker-pork-cacciatore/'):


    html_content = requests.get(str_url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    arr_result = []
    arr_recipe_meta = []
    str_json = ''
    
    with urlopen(str_url) as response:
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.find_all('script', type='application/ld+json'):
            str_json = str(anchor)
            str_json = str_json[len('<script type="application/ld+json">'):-len('</script>')]
            
    if str_json == '':
        pass
    else:
        json_result = json.loads(str_json)

        arr_result.append(json_result[1]['name'])
        arr_result.append(json_result[1]['nutrition'])
        arr_result.append(json_result[1]['recipeIngredient'])
        arr_result.append(json_result[1]['prepTime'])
        arr_result.append(json_result[1]['cookTime'])
        arr_result.append(json_result[1]['totalTime'])
        arr_result.append(str_url)
        #arr_result.append(arr_recipe_meta[3][1]) # servingSize

    return arr_result

if __name__ == "__main__":
    get_recipe_details()