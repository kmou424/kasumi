# This used to import other module for modules/bin/*

import importlib


def __import(path: str):
    return importlib.import_module(path)


def import_mod(module: str):
    return __import(f'modules.bin.{module}')


def import_lib(module: str, lib: str):
    return __import(f'modules.bin.{module}.' + lib)


def import_api(api: str):
    return __import(f'apis.{api}')


def import_config():
    return __import('config')


def import_consts():
    return __import('libs.consts')
