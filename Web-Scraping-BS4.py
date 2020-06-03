headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'
}

res = requests.get(url, headers=headers)
if res.status_code == requests.codes.ok:
    ressoup = bs4.BeautifulSoup(res.text, 'lxml')
    elems = ressoup.select('.link')
    elems[i].getText()
    elems[i].get('attr')
else:
    print('Something went wrong')