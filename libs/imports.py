# This used to import other module for modules/bin/*

import importlib
import importlib.util
import sys

MODULE_PATH = sys.path[0]


def __import(path: str):
    return importlib.import_module(path)


def import_api(api: str):
    return __import(f'apis.{api}')


def import_config():
    return __import('config')


def import_consts():
    return __import('libs.consts')


def import_mod(module: str):
    return import_lib(module, '__init__')


def import_lib(module: str, lib: str):
    module_path = import_api('path_utils').build_path([MODULE_PATH, 'modules', 'bin', module]) + lib + '.py'
    spec = importlib.util.spec_from_file_location(lib, module_path)
    module_var = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module_var)
    return module_var


def set_module_path(path):
    global MODULE_PATH
    MODULE_PATH = path
