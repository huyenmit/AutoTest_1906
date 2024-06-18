import csv
class readDatatest:
    def getLink(link):
        linkFile = []
        with open(link, 'r') as f:
            csv_reader = csv.DictReader(f)
            rows = []
            for row in csv_reader:
                _action = row['Action']
                _link = row['LinkData']
                linkFile.append([_action, _link])
        return linkFile

    def dataTestLogin(linkFile):
        datas = []
        with open(linkFile, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                _account = row['Account']
                _pass = row['Pass']
                _url = row["url"]
                _title = row["title"]
                datas.append([_account, _pass, _url, _title])
        return datas

