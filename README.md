# Insurance

## Demo

![insurance_demo](images/insurance.gif)

## Descripción

El seguro de vida es una cobertura de riesgo que se aplica a una persona que está en un estado de emergencia, como un accidente de tránsito, una enfermedad grave, etc.

* ¿Qué problema resuelve?

    A veces puede resultar difícil conocer cuánto costará tener un seguro de salud contratado, ya que depende de muchas variables, por lo que este proyecto, tiene como fin entregar un estimado de cuánto podría ser este costo, dependiendo de los datos que se tienen sobre el costo que están pagando otras personas.

    De esta manera, ingresando los datos de la persona, el sistema puede calcular el costo estimado de un seguro de vida de manera anual.

* ¿Qué tecnologías y librerías se usan?

    El proyecto está realizado completamente en Python, utilizando diferentes librerías, las que se detallan a continuación.

    [Pandas:](https://pandas.pydata.org) Es una herramienta open source rápida, poderosa, flexible y fácil de usar, la cual nos permite manipular y analizar datos.

    [Numpy:](https://numpy.org/) Es una librería de Python que nos permite trabajar con arrays y matrices.

    [Matplotlib:](https://matplotlib.org/) Es una librería de Python que nos permite crear gráficos.

    [Seaborn:](https://seaborn.pydata.org/) Es una librería de Python que nos permite crear gráficos sobre matplotlib, de una manera más sencilla.

    [Scikit-learn:](https://scikit-learn.org/) Es una librería de Python que nos permite trabajar con modelos de machine learning.

    [Streamlit](https://streamlit.io) Es una librería de Python que nos permite crear de manera sencilla aplicaciones web, generalmente utilizada para crear demostraciones.

## Instalación

Para poder replicar este proyecto de manera local, se debe ejecutar los siguientes comandos en la terminal:

1. Clonar de manera local el repositorio.

```
git clone https://github.com/Gab0Jorq/insurance.git
```

2. Crear un entorno virtual y activarlo.

    Windows:

    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

    Linux:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Instalar las librerías requeridas, a través de requirements.txt.

```
pip install -r requirements.txt
```


