


def Get_API():
    file=open('ScanProcess/API_KEY/API_KEY.txt', "r")
    api_key=file.read()
    file.close()
    return api_key
