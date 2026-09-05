# -*- mode: python -*-

block_cipher = None

# Bundle the React build output folder into the exe.
# Format: ('source_path', 'destination_relative_path_inside_app')
added_files = [
    ('gui', 'gui'),  # bundles entire gui/ directory and unpacks it beside the exe at runtime
]

a = Analysis(
    ['src/index.py'],
    pathex=['.'],                 # keep project root on search path
    binaries=[],                  # or None, both are fine
    datas=added_files,            # include your React build
    hiddenimports=['clr'],        # pythonnet for WinForms renderer
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# One-file build: pass a.binaries, a.zipfiles, a.datas to EXE and DO NOT use COLLECT
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,                   # include binaries
    a.zipfiles,                   # include python archive
    a.datas,                      # include your gui/ assets
    name='pywebview-react-app',
    debug=False,
    strip=False,
    upx=True,
    console=False,                # windowed app; set True to see console logs
    icon='src\\assets\\logo.ico'
)

