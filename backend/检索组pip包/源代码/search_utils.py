import json
import requests


def _build_url_params(url, params):
  url = url + '?'
  for k, v in params.items():
    url += '{}={}&'.format(k, v)
  return url


def get_suggestion(keyword):
  url = "http://39.96.43.48/suggestion"
  if not keyword:
    return

  params = {
    'keyword': keyword
  }
  request_url = _build_url_params(url, params)
  return requests.get(request_url,timeout=4).json()


def search(query, theme=None, page=None, order=None, year=None):
  url = "http://39.96.43.48/search"
  if not query:
    return

  params = {
    'query': query
  }
  if theme:
    params['theme'] = theme
  if page:
    params['page'] = page
  if order:
    params['order'] = order
  if year:
    params['year'] = year
  request_url = _build_url_params(url, params)
  return requests.get(request_url, timeout=4).json()

if __name__ == '__main__':
    print(get_suggestion("Audrey"))
    theme = "author"
    query = "lilei"
    page = 1
    order = 1
    year = 1997
    print(search(query, theme=theme))
