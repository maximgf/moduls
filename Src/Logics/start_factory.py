from Models.nomen import nomen_model
from Models.nomen_grope import nomen_group_model
from Models.recipe import recipe_model, recipe_row_model
from Models.unit import unit_model
from Src.Models import *
from Src.settings import Settings
from Src.Storage.Storage import storage


class start_factory:
    __options: Settings = None
    __storage: storage = None


    def __init__(self, options: Settings, storage_: storage = None) -> None:
        self.__options = options
        self.__storage = storage_
        self.__shape()


    def __shape(self):
        
        #cоздание данных в словаре
        if not self.__storage:
            self.__storage = storage()

        nomens = start_factory.create_nomenculature()
        recepts = start_factory.create_recipets()
        self.__storage.data[storage.nomenculature_key] = nomens
        self.__storage.data[storage.unit_key] = list(set([x.units for x in nomens]))
        self.__storage.data[storage.group_key] = list(set([x.group for x in nomens]))
        self.__storage.data[storage.recipe_key] = recepts


    @property
    def storage(self):
        return self.__storage


    def create(self) -> list:
        if not self.__options.is_first_start: return []
        if not self.__storage: self.__shape()

        self.__options.is_first_start = False
        result = list(self.__storage.data.values())
            
        return result

    
    @staticmethod
    def create_nomenculature():
        nomen_group = nomen_group_model.create_group()
        return [
        nomen_model(name='Пшеничная мука', full_name='Пшеничная мука', group=nomen_group, units=unit_model.create_kilogramm()),
        nomen_model(name='Сахар', full_name='Сахар', group=nomen_group, units=unit_model.create_kilogramm()),
        nomen_model(name='Сливочное масло', full_name='Сливочное масло', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Яйца', full_name='Яйца', group=nomen_group, units=unit_model.create_count()),
        nomen_model(name='Ванилин', full_name='Ванилин', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Куриное филе', group=nomen_group, units=unit_model.create_kilogramm()),
        nomen_model(name='Салат Романо', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Сыр Пармезан', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Чеснок', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Белый хлеб', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Соль', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Чёрный перец', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Оливковое масло', group=nomen_group, units=unit_model.create_litres()),
        nomen_model(name='Лимонный сок', group=nomen_group, units=unit_model.create_litres()),
        nomen_model(name='Горчица дижонская', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Яичный белок', group=nomen_group, units=unit_model.create_count()),
        nomen_model(name='Сахарная пудла', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Корица', group=nomen_group, units=unit_model.create_gramm()),
        nomen_model(name='Какао', group=nomen_group, units=unit_model.create_gramm())
        ]


    @staticmethod
    def create_recipets():
        return [
            recipe_model(
                name='ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ',
            rows=[recipe_row_model(
                nomenculature = nomen_model(name='Пшеничная мука', group=nomen_group_model.create_group(), units=unit_model.create_kilogramm()),
                unit=unit_model.create_gramm(),
                size=100
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Сахар', group=nomen_group_model.create_group(), units=unit_model.create_kilogramm()),
                unit=unit_model.create_gramm(),
                size=80
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Сливочное масло', group=nomen_group_model.create_group(), units=unit_model.create_gramm()),
                unit=unit_model.create_gramm(),
                size=70
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Яйца', group=nomen_group_model.create_group(), units=unit_model.create_count()),
                unit=unit_model.create_count(),
                size=1
                ),
            recipe_row_model(
                nomenculature = nomen_model(name='Ванилин', group=nomen_group_model.create_group(), units=unit_model.create_gramm()),
                unit=unit_model.create_gramm(),
                size=5
                )],)]