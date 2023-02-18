import numpy as np
import pandas as pd

from fastapi import FastAPI, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/chapter1/{q}", summary="Chapter 1")
async def chapter1(q: str = Path()):
    chapter1 = pd.read_csv('media/Chapter1.csv', sep=';')

    chapter1[' Бюджет СРФ, руб '] = chapter1[' Бюджет СРФ, руб '].str.strip().replace('-', np.nan)
    chapter1[' Бюджет СРФ, руб '].astype('float')
    chapter1[' Бюджет МО, руб '] = chapter1[' Бюджет МО, руб '].str.strip().replace('-', np.nan)
    chapter1[' Бюджет МО, руб '].astype('float')

    chapter1[' Кол-во грантов '] = chapter1[' Кол-во грантов '].str.strip().replace('-', np.nan)
    chapter1[' Кол-во грантов '].astype('float')
    chapter1[' Бюджет грантов, руб '] = chapter1[' Бюджет грантов, руб '].str.strip().replace('-', np.nan)
    chapter1[' Бюджет грантов, руб '].astype('float')
    chapter1[' Численность молодeжи, задействованной в программных мероприятиях по направлению '] = chapter1[
        ' Численность молодeжи, задействованной в программных мероприятиях по направлению '].str.strip().replace('-',
                                                                                                                 np.nan)
    chapter1[' Численность молодeжи, задействованной в программных мероприятиях по направлению '].astype('float')
    chapter1[' Количество детских и молодeжных общественных объединений, работающих по данному  '] = chapter1[
        ' Количество детских и молодeжных общественных объединений, работающих по данному  '].str.strip().replace('-',
                                                                                                                  np.nan)
    chapter1[' Количество детских и молодeжных общественных объединений, работающих по данному  '].astype('float')

    # Замена Алтайского края на другие регионы/округа
    chapter1ALLNaprav = chapter1[(chapter1['Регион'] == 'Алтайский край') & (
            (chapter1['№ строки'] == 1.0) | ((8.0 <= chapter1['№ строки']) & (chapter1['№ строки'] <= 17.0)) | (
            (24.0 <= chapter1['№ строки']) & (chapter1['№ строки'] <= 24.0)))]
    if q == "grants-budget":
        # Бюджет Грантов
        data = chapter1ALLNaprav.replace(np.nan, 0).iloc[:, 8]
        labels = chapter1ALLNaprav.iloc[:, 3]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "srf-budget":
        # Бюджет СРФ
        data = chapter1ALLNaprav.replace(np.nan, 0).iloc[:, 5]
        labels = chapter1ALLNaprav.iloc[:, 3]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "mo-budget":
        # Бюджет МО
        data = chapter1ALLNaprav.replace(np.nan, 0).iloc[:, 6]
        labels = chapter1ALLNaprav.iloc[:, 3]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "number-of-grants":
        # Кол-во Грантов
        data = chapter1ALLNaprav.replace(np.nan, 0).iloc[:, 7]
        labels = chapter1ALLNaprav.iloc[:, 3]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "youth-population":
        # Численность молодежи
        data = chapter1ALLNaprav.iloc[:, 8].replace(np.nan, 0).astype('int')
        labels = chapter1ALLNaprav.iloc[:, 3]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    else:
        raise HTTPException(status_code=404, detail="not found")


@app.get("/api/chapter2/{q}", summary="Chapter 2")
async def chapter2(q: str = Path()):
    Chapter2 = pd.read_csv('media/Chapter2.csv', sep=';')

    Chapter2[' Кол-во структур, ед '] = Chapter2[' Кол-во структур, ед '].str.strip().replace('-', np.nan)
    Chapter2[' Кол-во структур, ед '].astype('float')
    Chapter2[' Всего кол-во сотрудников, чел '] = Chapter2[' Всего кол-во сотрудников, чел '].str.strip().replace('-',
                                                                                                                  np.nan)
    Chapter2[' Всего кол-во сотрудников, чел '].astype('float')
    Chapter2[' Всего с профильным образованием '] = Chapter2[' Всего с профильным образованием '].str.strip().replace(
        '-', np.nan)
    Chapter2[' Всего с профильным образованием '].astype('float')
    Chapter2[' Всего объeм финансирования, руб '] = Chapter2[' Всего объeм финансирования, руб '].str.strip().replace(
        '-', np.nan)
    Chapter2[' Всего объeм финансирования, руб '].astype('float')
    Chapter2[' Расходы на мероприятия '] = Chapter2[' Расходы на мероприятия '].str.strip().replace('-', np.nan)
    Chapter2[' Расходы на мероприятия '].astype('float')
    Chapter2[' Расходы на адм функции '] = Chapter2[' Расходы на адм функции '].str.strip().replace('-', np.nan)
    Chapter2[' Расходы на адм функции '].astype('float')
    Chapter2[' Расходы на ремонт '] = Chapter2[' Расходы на ремонт '].str.strip().replace('-', np.nan)
    Chapter2[' Расходы на ремонт '].astype('float')

    Chapter2AltCray = Chapter2[(Chapter2['Регион'] == 'Алтайский край')]

    if q == "number-structural-units-common":
        # КОЛИЧЕСТВО СТРУКТУРНЫХ ЕДИНИЦ для ПАЙ ЧАРТА Региональные структуры и Муниципальные структуры
        labels = Chapter2AltCray.iloc[[0, 3], 3]
        data = Chapter2AltCray.replace(np.nan, 0).iloc[[0, 3], 5]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "number-structural-units":
        # КОЛИЧЕСТВО СТРУКТУРНЫХ ЕДИНИЦ для ПАЙ ЧАРТА общ
        labels = Chapter2AltCray.iloc[[1, 2, 4, 5], 3]
        data = Chapter2AltCray.replace(np.nan, 0).iloc[[1, 2, 4, 5], 5]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "number-of-employees-common":
        # КОЛИЧЕСТВО СОТРУДНИКОВ для ПАЙ ЧАРТА Региональные структуры и Муниципальные структуры
        labels = Chapter2AltCray.iloc[[0, 3], 3]
        data = Chapter2AltCray.replace(np.nan, 0).iloc[[0, 3], 6]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "number-of-employees":
        # КОЛИЧЕСТВО СОТРУДНИКОВ для ПАЙ ЧАРТА общ
        labels = Chapter2AltCray.iloc[[1, 2, 4, 5], 3]
        data = Chapter2AltCray.replace(np.nan, 0).iloc[[1, 2, 4, 5], 6]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "amount-of-funding":
        # ВСЕГО ОБЪЕМ ФИНАНСИРОВАНИЯ для ПАЙ ЧАРТА общ
        labels = Chapter2AltCray.iloc[[1, 2, 4, 5], 3]
        data = Chapter2AltCray.replace(np.nan, 0).iloc[[1, 2, 4, 5], 7]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "share-of-spending-regional":
        # ДОЛИ РАСХОДОВ В РЕГИОНАЛЬНЫХ СТРУКТУРАХ ПАЙ ЧАРТ
        labels = Chapter2AltCray.columns[9:12]
        data = Chapter2AltCray.replace(np.nan, 0).iloc[0, [8, 9, 10]].to_list()
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "share-of-spending-municipal":
        # ДОЛИ РАСХОДОВ В МУНИЦИПАЛЬНЫХ СТРУКТУРАХ ПАЙ ЧАРТ
        labels = Chapter2AltCray.columns[9:12]
        data = Chapter2AltCray.replace(np.nan, 0).iloc[3, [8, 9, 10]].to_list()
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    else:
        raise HTTPException(status_code=404, detail="not found")


@app.get("/api/chapter3/{q}", summary="Chapter 3", )
async def chapter3(q: str = Path()):
    Chapter3 = pd.read_csv('media/Chapter3.csv', sep=';')

    Chapter3[' Значение '] = Chapter3[' Значение '].str.strip().replace('-', np.nan)
    Chapter3[' Значение '].astype('float')

    Chapter3AltCray = Chapter3[(Chapter3['Регион'] == 'Алтайский край')]

    if q == "number-of-mentions":
        # Количество упоминаний регионального органа исполнительной власти,
        # реализующего государственную молодeжную политику ПАЙ ЧАРТ
        labels = Chapter3AltCray.iloc[[5, 6, 7], 3]
        data = Chapter3AltCray.iloc[[5, 6, 7], 6]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    elif q == "general-indicators":
        # ОБЩИЕ ПОКАЗАТЕЛИ НА ОДНОМ ГРАФИКЕ
        labels = Chapter3AltCray.iloc[[0, 1, 2, 3, 4, 8, 9, 10, 11], 3]
        data = Chapter3AltCray.iloc[[0, 1, 2, 3, 4, 8, 9, 10, 11], 6]
        return {"data": data.to_json(),
                "labels": labels.to_json()}
    else:
        raise HTTPException(status_code=404, detail="not found")
