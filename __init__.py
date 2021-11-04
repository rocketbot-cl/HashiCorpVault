# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'HashiCorpVault' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from hashiCorpObj import HashiCorpObj

global vaultClient_I

module = GetParams("module")

try:

    if (module == "connectToVault"):
        url = GetParams("url")
        token = GetParams("token")
        namespace = GetParams("namespace")

        vaultClient_I = HashiCorpObj(url, token, namespace)

        resultConnection = vaultClient_I.client.is_authenticated()
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultConnection)

    if (module == "read_secret"):

        path = GetParams("path")
        mount_point = GetParams("mount_point")
        
        result = vaultClient_I.read_secret(path, mount_point)
        result = result["data"]
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, result)

    if (module == "create_or_update_secret"):
        
        path = GetParams("path")
        mount_point = GetParams("mount_point")
        secret = eval(GetParams("secret"))
        
        result = vaultClient_I.create_or_update_secret(path, secret, mount_point)
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, result)

    if (module == "delete_secret"):
        
        path = GetParams("path")
        mount_point = GetParams("mount_point")
        
        result = vaultClient_I.delete_secret(path, mount_point)
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, result)

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e

