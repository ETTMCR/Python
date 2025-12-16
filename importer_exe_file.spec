# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['importer_exe_file.pyw'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['cv2', 'winsound', 'time', 'threading', 'PIL', 'pyautogui', 'pystray', 'my_gif_mdl', 'time', 'numpy', 'os', 'imageio.v2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='importer_exe_file',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['eat_pixels.PNG'],
)
