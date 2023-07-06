import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

def preview(roomsParam: float, metersParam: float) -> float:
    page = requests.get("https://www.vivareal.com.br/venda/santa-catarina/joinville/apartamento_residencial")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    items = soup.find_all(class_='property-card__container')
    
    data = []
    
    for item in items:
        title = item.find(class_='property-card__title').get_text().strip()
        price = item.find(class_='property-card__price').get_text().strip()
        address = item.find(class_='property-card__address').get_text().strip()
    
        title_parts = title.split(',')
        if len(title_parts) >= 2:
            rooms = title_parts[0].strip()
            area = title_parts[1].strip()
    
        address_parts = address.split('-')
        if len(address_parts) >= 3:
            estado       = address_parts[2].strip()
            bairroCidade = address_parts[1].strip()
            rua          = address_parts[0].strip()
            bairroCidade_parts = bairroCidade.split(',')
            bairro = bairroCidade_parts[0].strip()
            cidade = bairroCidade_parts[1].strip()

        print(bairro)
    
        numbers = re.findall(r'\d+', rooms)
        rooms = ''.join(numbers)
    
        price_numbers = re.findall(r'\d+', price)
        price = float(''.join(price_numbers))
    
        area_numbers = re.findall(r'\d+', area)
        area = ''.join(area_numbers)
    
        data.append({'Rooms': rooms, 'm²': area, 'Price': price, })
    
    df = pd.DataFrame(data)
    
    df.head()
    
    X = df[['Rooms', 'm²']]
    y = df['Price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.37, random_state=42)
    
    model = LinearRegression()
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", math.sqrt(mse))
    
    new_data = {'Rooms': [roomsParam], 'm²': [metersParam]}
    new_df = pd.DataFrame(new_data)
    
    prediction = model.predict(new_df)
    print("Predicted Price:", prediction)
    return prediction