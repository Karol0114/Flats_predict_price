import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
## Dataset i used: https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset?select=House_Rent_Dataset.csv ##

df = pd.read_csv('predict_flat_price\House_Rent_Dataset.csv')

print(df.shape)

df_copy = df.copy()


df_copy.index.name = 'ID'


### Analiza:

#def check_value_counts(column_name):
    #return df_copy[column_name].value_counts

# Wpływ bhk na cene:
def lowercase_columns(col):
    return col.lower()

df_copy = df_copy.rename(columns = str.lower)


count_bhk = df_copy['bhk'].value_counts().sum
print(count_bhk)



## Jak ilośc BHK wpływa na średnią cene wynajmu mieszkania.
flat_1_bhk_mean_rent = df_copy[df_copy['bhk'] == 1]['rent'].mean()
flat_2_bhk_mean_rent = df_copy[df_copy['bhk'] == 2]['rent'].mean()
flat_3_bhk_mean_rent = df_copy[df_copy['bhk'] == 3]['rent'].mean()
flat_4_bhk_mean_rent = df_copy[df_copy['bhk'] == 4]['rent'].mean()
flat_5_bhk_mean_rent = df_copy[df_copy['bhk'] == 5]['rent'].mean()
flat_6_bhk_mean_rent = df_copy[df_copy['bhk'] == 6]['rent'].mean()

## Wizualizacja na wykresie

bhk_counts = ['1BHK', '2BHK', '3BHK', '4BHK', '5BHK', '6BHK']
bhk_mean_price = [flat_1_bhk_mean_rent, flat_2_bhk_mean_rent,flat_3_bhk_mean_rent,flat_4_bhk_mean_rent,flat_5_bhk_mean_rent,flat_6_bhk_mean_rent]


plt.bar(bhk_counts, bhk_mean_price)
plt.xlabel('Ilość BHK')
plt.ylabel('Średnia cena')
plt.title('Wykres średniej ceny wynajmu dla poszczególnej ilości BHK')
plt.show()

### Ilość bhk ma wpływ na cene, więcej bhk podwyższa cene



## Wpływ rozmairu mieszkania na cene:

small_size_flats = df_copy[(df_copy['size'] >= 10.00) & (df_copy['size'] < 809.00)]['rent'].mean()
medium_size_flats = df_copy[(df_copy['size'] >= 809.00) & (df_copy['size'] < 1608.00)]['rent'].mean()
big_size_flats = df_copy[(df_copy['size'] >= 1608.00) & (df_copy['size'] <= 8000)]['rent'].mean()


#Wizualizacja danych na wykresie:

size_of_flats = ['Small', 'Medium', 'Big']
size_mean_price = [small_size_flats, medium_size_flats, big_size_flats]


plt.bar(size_of_flats, size_mean_price)
plt.xlabel('Rozmiary mieszkań')
plt.ylabel('Średnia cena ')
plt.title('Wykres średniej ceny wynajmu dla poszczególnej wielkości mieszkania')
plt.show()

##Wpływ miasta na średnią cene mieszkania
#print(df_copy['city'].value_counts().sum)

mumbai = df_copy[df_copy['city'] == 'Mumbai']['rent'].mean()
chennai = df_copy[df_copy['city'] == 'Chennai']['rent'].mean()
bangalore = df_copy[df_copy['city'] == 'Bangalore']['rent'].mean()
hyderabad = df_copy[df_copy['city'] == 'Hyderabad']['rent'].mean()
delhi = df_copy[df_copy['city'] == 'Delhi']['rent'].mean()
kolkata = df_copy[df_copy['city'] == 'Kolkata']['rent'].mean()


#Wizualizacja na wykresie:

city_names = ['Mumbai', 'Chennai', 'Bangalore', 'Hyderabad', 'Delhi', 'Kolkata']
city_mean_price = [mumbai, chennai, bangalore, hyderabad, delhi, kolkata]

plt.bar(city_names, city_mean_price)
plt.xlabel('Nazwy miejscowości')
plt.ylabel('Średnia cena')
plt.title('Wykres średniej ceny wynjamu dla poszczególnej miejsowości')
plt.show()

df_copy.columns = [col.replace(' ', '_') for col in df_copy.columns]
df_copy.head()

## Wpływ statusu wykończenia mieszkania na średnią cene:

semi_furnished = df_copy[df_copy['furnishing_status'] == 'Semi-Furnished']['rent'].mean()
unfurnished = df_copy[df_copy['furnishing_status'] == 'Unfurnished']['rent'].mean()
furnished = df_copy[df_copy['furnishing_status'] == 'Furnished']['rent'].mean()

furnishing_status = ['Semi Furnished', 'Unfurnished', 'Furnished']
furnishing_price = [semi_furnished, unfurnished, furnished]

# Wizualizacja danych:

plt.bar(furnishing_status, furnishing_price)
plt.xlabel('Stan wykończenia mieszkania')
plt.ylabel('Średnia cena')
plt.title('Wykres śednich cen dla poszczegółnego stanu wykończenia mieszkania')
plt.show()


## Ilośc łazienek i ich wpływ na średnią cene mieszkania

print(df_copy['bathroom'].value_counts().sum)

one_bathroom = df_copy[df_copy['bathroom'] == 1]['rent'].mean()
two_bathroom = df_copy[df_copy['bathroom'] == 2]['rent'].mean()
three_bathroom = df_copy[df_copy['bathroom'] == 3]['rent'].mean()
four_bathroom = df_copy[df_copy['bathroom'] == 4]['rent'].mean()
five_bathroom = df_copy[df_copy['bathroom'] == 5]['rent'].mean()
six_bathroom = df_copy[df_copy['bathroom'] == 6]['rent'].mean()
seven_bathroom = df_copy[df_copy['bathroom'] == 7]['rent'].mean()
ten_bathroom = df_copy[df_copy['bathroom'] == 10]['rent'].mean()

number_of_bathrooms = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'ten']
mean_price_of_bathrooms = [one_bathroom, two_bathroom, three_bathroom, four_bathroom, five_bathroom, six_bathroom, seven_bathroom, ten_bathroom]

plt.bar(number_of_bathrooms, mean_price_of_bathrooms)
plt.xlabel('Ilość łazieniek w mieszkaniu')
plt.ylabel('Średnia cena')
plt.title('Wykres średniej ceny mieszkań w zależności od ilości łazienek')
plt.show()


## Area type:

print(df_copy['area_type'].value_counts().sum)

super_area = df_copy[df_copy['area_type'] == 'Super Area']
carpet_area = df_copy[df_copy['area_type'] == 'Carpet Area']
built_area = df_copy[df_copy['area_type'] == 'Built Area']

area_type = ['Super Area', 'Carpet Area', 'Built Area']
mean_price_area_type = [super_area, carpet_area, built_area]

# Wizualizacja na wykresie: 

plt.bar(area_type, mean_price_area_type)
plt.xlabel('Typ ')
plt.ylabel('Średnia cena')
plt.title('Wykreś dla średniej ceny dla poszczególnego typu:')
plt.show()