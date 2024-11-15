# -*- mode: python -*-

import sys, site, os
from path import Path

block_cipher = None

occt_dir = os.path.join(Path(sys.prefix), 'Library', 'share', 'opencascade')
ocp_path = (os.path.join(HOMEPATH, 'OCP.cp39-win_amd64.pyd'), '.')

a = Analysis(['src/run.py'],
             pathex=['.'],
             binaries=[ocp_path],
             datas=[(occt_dir, 'opencascade')],
             hiddenimports=['ipykernel.datapub', 'vtkmodules', 'vtkmodules.all',
                            'pyqtgraph.graphicsItems.ViewBox.axisCtrlTemplate_pyqt5',
                            'pyqtgraph.graphicsItems.PlotItem.plotConfigTemplate_pyqt5',
                            'pyqtgraph.imageview.ImageViewTemplate_pyqt5', 'debugpy', 'xmlrpc',
                            'zmq.backend', 'cq_warehouse', 'cq_warehouse.bearing', 'cq_warehouse.chain',
                            'cq_warehouse.drafting', 'cq_warehouse.extensions', 'cq_warehouse.fastener',
                            'cq_warehouse.sprocket', 'cq_warehouse.thread', 'cq_gears', 'cq_cache'],
             hookspath=[],
             runtime_hooks=['pyinstaller/pyi_rth_occ.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# future warning for local build: add the following getfullnameof('libssl-1_1-x64.dll'), getfullnameof('libcrypto-1_1-x64.dll') to a.datas
# if you build on github actions the pyinstaller-builds-actions.yml does the work for you

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='CQ-editor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)

exclude = ()
a.binaries = TOC([x for x in a.binaries if not x[0].startswith(exclude)])

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='CQ-editor')
