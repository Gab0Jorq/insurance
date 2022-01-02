import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

#Cargando el modelo y el Scaler
model = pickle.load(open('insurance_model_gb.sav', 'rb'))
sc = pickle.load(open('scaler.sav','rb'))

#Función para predecir el costo del seguro
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
    return prediction[0]


def run():
    from PIL import Image
    image_hospital = Image.open('images/insurance.jpg')

    #Creación de la barra lateral
    st.sidebar.markdown('Esta aplicación fue creada para estimar el costo de un seguro de salud de alguna institución, según las características \
    de los clientes, para mayor información puede ver el código utilizado [pinchando aquí](https://github.com/Gab0Jorq/insurance/blob/master/insurance.ipynb).')
    st.sidebar.image(image_hospital)

    #Título de la aplicación
    st.title('Ingrese sus datos:')

    #Creación del formulario
    with st.form(key='formulario'):
        #Ingreso de datos
        age = st.number_input('Edad', min_value=1, max_value=100, value=25)
        sex = st.selectbox('Género', ['male', 'female'])
        bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
        children = st.selectbox('Hijos', [0,1,2,3,4,5,6])
        if st.checkbox('Fumador'):
            smoker = 'yes'
        else:
            smoker = 'no'
        region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

        #Transformación de la data para el formato del modelo.
        input_dict = {'age':age, 'bmi':bmi, 'children':children, 'sex': sex, 'region':region, 'smoker':smoker}
        input_df = pd.DataFrame([input_dict])
        
        #Creación del botón de predicción
        submit_button = st.form_submit_button(label = 'Enviar')
        
        #Acción del botón de predicción
        if submit_button==True:
            #Predicción del costo del seguro
            output = model_predict(data=input_df, modelo = model)
            output_str = '$' + str(int(round(output, 0)))

            #Mostrar el resultado
            st.success('El costo aproximado es: {} {}'.format(output_str, 'USD'))
            st.write('')

            #En caso de que la persona sea fumadora.
            #Mostrar la diferencia del costo aproximado.
            if smoker == 'yes':
                input_df['smoker'] = 'no'
                output2 = model_predict(data=input_df, modelo = model)
                output_str2 = '$' + str(int(round(output2, 0))) + ' USD'
                st.metric(label = 'El costo aproximado si no fuera fumador es:', value = output_str2, delta = '-$' + str(int(round(-output2+output, 0))), delta_color = 'inverse')

if __name__ == '__main__':
    run()
