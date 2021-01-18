import requests
import pandas as pd

from urllib.parse import urlencode

DBLP_API = 'http://dblp.org/search/publ/api'

ccf_catalog = pd.read_csv('ccf_catalog.csv')
queries = pd.read_csv('query.csv', header=None)[0]
paper_info_list = []

for idx, query in enumerate(queries.array):
    paper_info = {
        'Query': query,
        'Title': 'N/A',
        'Year': 'N/A',
        'Venue': 'N/A',
        'CCF Class': 'N/A',
        'DOI': 'N/A',
        'URL': 'N/A'
    }
    options = {
        'q': query,
        'format': 'json',
        'h': 1
    }
    r = requests.get(f'{DBLP_API}?{urlencode(options)}').json()
    hit = r.get('result').get('hits').get('hit')
    if hit is not None:
        info = hit[0].get('info')
        paper_info['Title'] = info.get('title')
        paper_info['Year'] = info.get('year')
        paper_info['Venue'] = info.get('venue')
        paper_info['DOI'] = info.get('doi')
        paper_info['URL'] = info.get('ee')
        venue = paper_info['Venue']
        if len(series := ccf_catalog.loc[ccf_catalog.get('abbr').str.lower() == venue.lower(), 'class']) > 0:
            paper_info['CCF Class'] = series.item()
        elif len(series := ccf_catalog.loc[ccf_catalog.get('url').str.contains(f'/{venue.lower()}/'), 'class']) > 0:
            paper_info['CCF Class'] = series.item()
    print(idx + 1, paper_info)
    paper_info_list.append(paper_info)

pd.DataFrame(paper_info_list).to_csv('output.csv', index=False)
