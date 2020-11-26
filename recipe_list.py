from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_recipe_list(
        ingIncl = 'pork, tomato', 
        ingExcl = 'ragout', 
        keyword = 'pork', 
        sort = 'best'
    ):
    arr_ingIncl = list(map(str.strip, ingIncl.split(',')))
    arr_ingExcl = list(map(str.strip, ingExcl.split(',')))

    str_allrecipes_url = 'https://www.allrecipes.com'
    #re = best match / n = newest / p = popular
    if sort == 'best':
        str_sort = '&sort=re'
    elif sort == 'new':
        str_sort = '&sort=n'
    else :
        str_sort = '&sort=p'
    
    '''        
    if len(arr_keyword) == 0 :
        str_keyword = ''.join(arr_keyword)
    else:
        str_keyword = '%20'.join(arr_keyword)
    '''
    
    if len(arr_ingIncl) == 0 :
        str_ingIncl = ''
    else:
        str_ingIncl = ','.join(arr_ingIncl)

    if len(arr_ingExcl) == 0 :
        str_ingExcl = ''
    else:
        str_ingExcl = ','.join(arr_ingExcl)


    arr_search = []
    arr_search.append(str_allrecipes_url)
    arr_search.append('/search/results/?wt=')
    arr_search.append(keyword)
    arr_search.append('&ingIncl=')
    arr_search.append(str_ingIncl)
    arr_search.append('&ingExcl=')
    arr_search.append(str_ingExcl)
    arr_search.append(str_sort)

    str_url = ''.join(arr_search)

    recipe_result = []

    # Parse the html content
    with urlopen(str_url) as response:
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.find_all('a', 'fixed-recipe-card__title-link'):
            recipe_result.append(anchor.get('href', '/'))
    return recipe_result

if __name__ == "__main__":
    get_recipe_list()