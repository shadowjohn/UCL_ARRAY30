# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['uclarray30.pyw'],
             pathex=['C:\\Users\\John-Home\\Desktop\\UCL_ARRAY30'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_ssl', '_bz2', '_lzma', 'pyconfig'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='uclarray30',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , version='metadata.txt', icon='pic\\uclarray30_logo.ico')
