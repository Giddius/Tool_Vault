import os
import shutil
import subprocess
from gidtools.gidfiles import pathmaker, readbin, readit, writebin, writeit, work_in, writejson, loadjson, linereadit, QuickFile, pickleit, get_pickled
from fpdf import FPDF

THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))
HELP_FOLDER = pathmaker(THIS_FILE_DIR, 'pipx_help_files')


def get_help(script_name):
    _cmd = subprocess.run([script_name, '-h'], shell=True, check=True, capture_output=True)
    return _cmd.stdout.decode('utf-8', errors='replace')


def create_pdf(raw_output, name):
    if raw_output == '':
        return
    pdf = FPDF()
    pdf.set_title(name.title())
    pdf.add_page()
    pdf.set_font("Times", style='B', size=9)
    pdf.write(6, raw_output)
    pdf.output(pathmaker(HELP_FOLDER, f'{name}_help.pdf'))


if __name__ == '__main__':
    if os.path.exists(HELP_FOLDER) is True:
        shutil.rmtree(HELP_FOLDER)
    os.makedirs(HELP_FOLDER)

    _json_dict = loadjson("pipx_list.json")
    for key, value in _json_dict['scripts'].items():
        if key != "pyqt5-tools":
            for exe_name in value:
                _help = get_help(exe_name)
                create_pdf(_help, key)
                _out = QuickFile()
                _out.write(get_help(exe_name))
