import urllib.parse

def chuyeniframesanginitdata():
    alliframes = []
    try: 
        with open("iframe.txt", "r") as file: 
            for iframes in file: 
                alliframes.append(iframes)
    except:
        print("file iframe lỗi rồi!")

    for url in alliframes:
        parsed_url = urllib.parse.urlparse(url.strip())
        fragment = parsed_url.fragment
        parsed_params = urllib.parse.parse_qs(fragment)
        tgWebAppData = parsed_params['tgWebAppData'][0]
        initdata = open('initdata.txt', 'a')
        test = f"{tgWebAppData}\n"
        initdata.write(test)
chuyeniframesanginitdata()