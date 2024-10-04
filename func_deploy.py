import os 
import shutil
import subprocess
from pathlib import Path

PATH = Path(__file__).parent 

PATH_UI_QTDESIGNER = os.path.join(PATH, 'ui')
PATH_UI_DEPLOY = os.path.join(PATH, 'src','ui')
PATH_PY_BACKUP = os.path.join(PATH, 'src','ui','backup')

def backup_py(file:str):
    py_backup_file = os.path.join(PATH_PY_BACKUP,file)
    py_deploy_file = os.path.join(PATH_UI_DEPLOY, file)

    if os.path.exists(py_deploy_file):
        if  not os.path.exists(py_backup_file):
            shutil.move(py_deploy_file,py_backup_file)
        else:
            if os.path.exists(f"{py_backup_file}.old"):
                os.remove(f"{py_backup_file}.old")
            os.rename(py_backup_file,f'{py_backup_file}.old')
            shutil.move(py_deploy_file,py_backup_file)

    print(f"Arquivo {file} movido")           


# Listar arquivos de .iu que está salvos no diretorio do qtdesigner

def func_list_ui_qt():
    list_ui_qt = []
    temp = os.listdir(PATH_UI_QTDESIGNER)
    for i in temp:
        if i.endswith('.ui'):
            list_ui_qt.append(i)
    return list_ui_qt   

def main():
    func = func_list_ui_qt()
    # Iterar sobre a lista de arquivos .ui e converter cada um deles
    for ui in func:
        # Definir os caminhos de origem e destino
        ui_path = os.path.join(PATH_UI_QTDESIGNER, ui)
        py_filename = os.path.splitext(ui)[0] + '.py'  # Remove a extensão .ui e adiciona .py
        py_path = os.path.join(PATH_UI_DEPLOY, py_filename)

        backup_py(py_filename)
        # Comando para converter .ui em .py
        command = f'pyside6-uic "{ui_path}" -o "{py_path}"'

        try:
            # Executar o comando
            subprocess.run(command, check=True, shell=True)
            print(f'Converção {ui} Para {py_filename} sucesso.')
        except subprocess.CalledProcessError as e:
            print(f'Erro de  converção {ui}: {e}')

if __name__ == "__main__":
    main()
