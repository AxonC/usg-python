$version = Read-Host "Enter the Version of the Application"

pyinstaller main.py --onefile --windowed `
 --icon=usgfavicon.ico `
 --paths=C:\Python36-32 `
 --paths=C:\Python36-32\Lib\site-packages\PyQt5\Qt\bin `
 --paths=C:\Python36-32\Lib\site-packages\requests `
 --name=usg-bottool `
 --distpath=".\release";
 
 Copy-Item -Path ".\usgfavicon.ico" -Destination ".\release";
 Copy-Item -Path ".\config.ini" -Destination ".\release";
 
Compress-Archive -Path ".\release" -DestinationPath ".\bottool-$version.zip"