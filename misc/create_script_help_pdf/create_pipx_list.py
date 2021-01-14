import os
import shutil
import subprocess
from gidtools.gidfiles import pathmaker, readbin, readit, writebin, writeit, work_in, writejson, loadjson, linereadit, QuickFile, pickleit, get_pickled


def get_raw_pipx_list():
    _cmd = subprocess.run(['pipx', 'list'], shell=True, check=True, capture_output=True)
    return _cmd.stdout.decode('utf-8', errors='ignore')


def modify_raw_pipx_list(raw_text: str):
    _out_lines = []
    for line in raw_text.splitlines():
        if line != '' and 'venvs are in' not in line:

            line = line.strip()
            if 'apps are exposed on your $PATH at' in line:
                line = '## location: ' + line.replace('apps are exposed on your $PATH at', '').strip()

            elif line.startswith('-'):
                line = line.replace('-', '').strip()

            else:
                _name = line.split(' ')[1].strip()
                line = f"# package_name: {_name}"

            _out_lines.append(line)

    print(_out_lines)
    return _out_lines


def raw_pipx_list_to_json():
    raw_text = get_raw_pipx_list()
    _json_dict = {'meta': {}, 'scripts': {}}
    _name = ''
    for line in raw_text.splitlines():
        if line != '' and 'venvs are in' not in line:
            line = line.strip()
            if 'apps are exposed on your $PATH at' in line:
                _json_dict['meta']['location'] = line.replace('apps are exposed on your $PATH at', '').strip()

            elif not line.startswith('-'):
                _name = line.split(' ')[1].strip()
                if _name not in _json_dict['scripts']:
                    _json_dict['scripts'][_name] = []

            else:
                _script = line.replace('-', '').strip()
                _json_dict['scripts'][_name].append(_script)
    writejson(_json_dict, 'pipx_list.json', sort_keys=False, indent=2)


if __name__ == '__main__':
    pass
