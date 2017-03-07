import concurrent.futures

import requests


def dowload(args):
    filename, url = args
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    return True


def dowload_many(url, qtd=100, poolsize=300, caminho='baixados/captcha{0}.jpg'):
    with concurrent.futures.ThreadPoolExecutor(max_workers=poolsize) as executor:
        executor.map(dowload, [(caminho.format(i), url) for i in range(qtd)])


dowload_many('https://sodexosaldocartao.com.br/saldocartao/jcaptcha.do', qtd=400)
