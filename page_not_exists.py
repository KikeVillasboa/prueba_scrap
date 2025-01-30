import webbrowser, requests

# Pasamos una url que no existe
url = 'https://www.google.come/search?q=no exist'

try:
    res = requests.get(url)
    res.raise_for_status()
    print(res.text[:500])
except Exception as exc:
    print('There was a problem: %s' % (exc))

webbrowser.open(url)