import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

#load pikle model
model = pickle.load(open('insurance_model_gb.sav', 'rb'))
sc = pickle.load(open('scaler.sav','rb'))

def model_predict(data, modelo):
    #Transformación de variables para que funcione el modelo guardado.
    data['sex_male'] = [1 if i == 'male' else 0 for i in data['sex']]
    data['region_northwest']= [1 if i == 'northwest' else 0 for i in data['region']]
    data['region_southeast']= [1 if i == 'southwest' else 0 for i in data['region']]
    data['region_southwest']= [1 if i == 'southwest' else 0 for i in data['region']]
    data['smoker_yes'] = [1 if i == 'yes' else 0 for i in data['smoker']]
    data = data.drop(columns=['sex', 'region', 'smoker'])

    #Usamos el Scaler guardado para estandarizar la data.
    data = sc.transform(data)
    #El modelo predice el valor logarítmico, por lo que hay que transformarlo.
    prediction_log = modelo.predict(data)
    prediction = np.exp(prediction_log)  
    return prediction


def run():
    from PIL import Image
    image = Image.open('images/logo_git.png')
    image_hospital = Image.open('images/insurance.jpg')

    st.sidebar.info('Esta aplicación fue creada para predecir el cobro del seguro de salud de los clientes, según sus características.')
    st.sidebar.success('https://github.com/Gab0Jorq')

    st.sidebar.image(image_hospital)

    st.title('Ingresa tus datos, para saber un estimado del costo de tu seguro de salud.')

    age = st.number_input('Edad', min_value=1, max_value=100, value=25)
    sex = st.selectbox('Género', ['male', 'female'])
    bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
    children = st.selectbox('Hijos', [0,1,2,3,4,5,6])
    if st.checkbox('Fumador'):
        smoker = 'yes'
    else:
        smoker = 'no'
    region = st.selectbox('region', ['southwest', 'northwest', 'northeast', 'southeast'])
    input_dict = {'age':age, 'bmi':bmi, 'children':children, 'sex': sex, 'region':region, 'smoker':smoker}
    input_df = pd.DataFrame([input_dict])
    output = ''


    if st.button('Predecir'):
        
        output = model_predict(data=input_df, modelo = model)
        output = '$' + str(round(output[0], 0))

        st.success('El precio es: {} {}'.format(output, 'USD'))


if __name__ == '__main__':
    run()
