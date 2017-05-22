import requests
from bs4 import*
#https://www.google.com/finance?q=
price=[]
while(1):
    print("1-Stock Prices")
    print("2-Market News")
    choice=input("Enter your choice: ")
    if choice=='1':
        url="https://www.google.com/finance?q="
        stock=input("Enter the name of your stock: ")
        url=url+stock
        try:
            data=requests.get(url)
            soup=BeautifulSoup(data.text,"html.parser")
            data1=soup.find('span',{'class':"pr"})
            print("The value of stock "+stock+" is: "+data1.span.string)
            price.append(data1.span.string)
            try:
                data2 = soup.find_all('span', {'class': 'chg'})
                print("The change is: " + data2[0].string + data2[1].string)
            except:
                data2 = soup.find_all('span', {'class': 'chr'})
                print("The change is: "+data2[0].string+data2[1].string)
        except:
            print("Stock does't exist or no internet connection")
#https://www.google.com/finance/market_news?ei=p2JtV9i4KYOxuwTW-otg
    elif choice=='2':
        try:
            url="https://www.google.com/finance/market_news?ei=p2JtV9i4KYOxuwTW-otg"
            data=requests.get(url)
            soup=BeautifulSoup(data.text,"html.parser")
            data1=[]
            data2=[]
            data3=[]
            data4=[]
            for i in range(0,10):
                data1.extend(soup.find_all('span',{'class','name'}))
            for var in range(1,11):
                data2.append(soup.find('div',id='Article'+str(var)))
            for var in range(0,10):
                data3.extend(soup.find_all('span',{'class','date'}))
            for var in range(0,10):
                data4.extend(soup.find_all('div',{'class','byline'}))
            for res in range(0,10):
                print('\n')
                print(data1[res].a.string)
                print(data4[res].span.string)
                print(data3[res].string)
                print(data2[res].div.string)
        except:
            print("No news for today")
    else:
        print("Invalid choice")
    print("\n")
    print("do u want to continue(y/n)")
    dep=input()
    if dep=='y' or dep=='Y':
        print("\n")
        continue
    elif dep=='n' or dep=='N':
        break
    else:
        print("Invalid Choice")
        print("\n")
 
