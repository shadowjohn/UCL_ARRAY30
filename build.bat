rd /S build
SET VS90COMNTOOLS=%VS140COMNTOOLS%
rem c:\python27\scripts\pyinstaller uclliu.pyw -F -w --version-file=metadata.txt --exclude-module socket
rem --exclude-module=_ssl --exclude-module=_bz2 --exclude-module=_lzma --exclude-module=pyconfig
c:\python27\scripts\pyinstaller -F -w --onefile --clean --icon="pic\uclarray30_logo.ico" --version-file=metadata.txt --exclude-module=_ssl --exclude-module=_bz2 --exclude-module=_lzma --exclude-module=pyconfig uclarray30.pyw 