# -*- mode: python -*-

import os

if (os.environ['NIX_BUILD'] == "1"):
    from PyInstaller.utils.hooks.qt import pyqt6_library_info

    qt_prefix = os.environ["QT_ENV_PREFIX"]
    pyqt6_library_info.location.update({
        "PrefixPath": qt_prefix,
        "TranslationsPath": os.path.join(qt_prefix, ""),
        "LibraryExecutablesPath": os.path.join(qt_prefix, "libexec"),
        "DataPath": qt_prefix,
        "PluginsPath": os.path.join(qt_prefix, "lib/qt-6/plugins"),
    })

block_cipher = None

added_files = [
    ('./gui', 'gui'),
]

a = Analysis(['./src/index.py'],
             pathex=['./dist'],
             binaries=None,
             datas=added_files,
             hiddenimports=['clr'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='pywebview-react-app',
          debug=False,
          strip=True,
          #icon='./src/assets/\logo.ico',
          upx=True,
          console=False ) # set this to see error output of the executable
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='pywebview-react-app')
