import streamlit as st
import pandas as pd
st.title("Калькулятор инициатив")
st.write(
    ''' Даннный калькулятор поможет вам оценить влияние вашей инициативы на результаты. 
    Для того, чтобы им воспользоваться вам не обходимо ввести: 
    
    1. шаг воронки, на который повлияет изменение; 
    
    2. насколько сильно изменится метрика; 
    
    3. платформы, которые проект заденет.'''
)

funnel_steps = ['Первый заход', 'Создание персонажа', 'Покупка первого юнита', 'Проведение первого сражения'
    , 'Получение приза за выполнение еженедельного задания']


base_metrics = {'IOS':{'Первый заход': 600,
                       'Создание персонажа': 489,
                       'Покупка первого юнита': 452,
                       'Проведение первого сражения': 400,
                       'Получение приза за выполнение еженедельного задания': 387},
                'Android':{'Первый заход': 1000,
                           'Создание персонажа': 865,
                          'Покупка первого юнита': 805,
                           'Проведение первого сражения': 740,
                           'Получение приза за выполнение еженедельного задания': 732},
                'Web':{'Первый заход': 400,
                        'Создание персонажа': 340,
                       'Покупка первого юнита': 290,
                       'Проведение первого сражения': 250,
                       'Получение приза за выполнение еженедельного задания': 241}}

st.write('Изначальные показатели')
base_table = pd.DataFrame(base_metrics)
st.write(base_table)

funnel_step = st.selectbox('Выберите этап воронки', funnel_steps[1:])
platforms = st.multiselect('Выберите платформы', ['IOS', 'Android', 'Web'])
uplift = st.number_input('Введите размер изменения метрики в процентных пунтах', step=0.1)


def calculate_uplift(funnel_step, platform, uplift):
    uplift_value = uplift / 100
    previous_step = funnel_steps[funnel_steps.index(funnel_step)-1]
    base_conversion = base_metrics[platform][funnel_step]/base_metrics[platform][previous_step]
    final_step_relative_uplift = (base_conversion+uplift_value)/base_conversion
    final_step_uplift = base_metrics[platform]['Получение приза за выполнение еженедельного задания'] * final_step_relative_uplift
    return round(final_step_uplift,3)


if st.button('Посчитать'):
    if funnel_step == 'Первый заход':
        for platform in platforms:
            st.write(f'При изменении метрики на {uplift}п.п. на {platform}, количество пользователей прошедших всю воронку будет равно {calculate_uplift(funnel_step, platform, uplift)}')
    elif funnel_step == 'Создание персонажа':
        for platform in platforms:
            st.write(f'При изменении метрики на {uplift}п.п. на {platform}, количество пользователей прошедших всю воронку будет равно {calculate_uplift(funnel_step, platform, uplift)}')
    elif funnel_step == 'Покупка первого юнита':
        for platform in platforms:
            st.write(f'При изменении метрики на {uplift}п.п. на {platform}, количество пользователей прошедших всю воронку будет равно  {calculate_uplift(funnel_step, platform, uplift)}')
    elif funnel_step == 'Проведение первого сражения':
        for platform in platforms:
            st.write(f'При изменении метрики на {uplift}п.п. на {platform}, количество пользователей прошедших всю воронку будет равно {calculate_uplift(funnel_step, platform, uplift)}')
    elif funnel_step == 'Получение приза за выполнение еженедельного задания':
        for platform in platforms:
            st.write(f'При изменении метрики на {uplift}п.п. на {platform}, количество пользователей прошедших всю воронку будет равно {calculate_uplift(funnel_step, platform, uplift)}')


st.write('## Проект 1')
st.image('Снимок экрана 2025-03-08 в 15.59.44.png')
st.write('## Проект 2')
st.image('Снимок экрана 2025-03-08 в 16.00.10.png')

