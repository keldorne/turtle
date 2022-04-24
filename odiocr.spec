# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
		(r'files\son_fin.mp3', 'files'),
		(r'files\*.dat', 'files'),
		(r'mode_test\fichier_test\*.xlsx', r'mode_test\fichier_test'),
		(r'C:\Users\Audio69\AppData\Local\Programs\Tesseract-OCR', r'Tesseract-OCR')
		]
		

a = Analysis(['odiocr.py'],
             datas = added_files,
			 pathex=[],
             binaries=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='OdioCR',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
		  icon='odiocr.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
