
import requests
from bs4 import BeautifulSoup
import xlwt

def getPageData(url):
    response = requests.get(url)
    print response.content
    print 'hello world!'
    return response.text

def getPageWeather(htmlText):
    dataList = []
    soup = BeautifulSoup(htmlText,'html.parser')
    weatherDataList = soup.find('div',{"class":"weather-card-wrap"})
    weatherDataItem = weatherDataList.find_all('ul',{"class":"weather-columns"})
    for item in weatherDataItem:
        print 'xixi'
        divs = item.find_all("div")
        excelItem = []
        for i in divs:
            print 'wawa'
            str = i.get_text()
            if len(str)==0:
                continue
            excelItem.append(str)
            print weatherDataItem.index(item)
            print excelItem.index(str)
            print str
            workSheet.write(weatherDataItem.index(item),excelItem.index(str),str)
    workBook.save("excel_text.xls")

if __name__ == '__main__':
    url1 = "https://tianqi.so.com/weather/101220101"
    html = getPageData(url1)
    workBook = xlwt.Workbook(encoding='utf-8')
    workSheet = workBook.add_sheet("My worksheet")
    getPageWeather(html)

    # file_csv = csv.writer(file)
    # file_csv.writerow(titles)
