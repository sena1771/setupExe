
This code can create an exe for the application downloadings or updatings.
run setup script:

pyinstaller.exe -F setup.py

For embedding my zip file to the Python script :

pyinstaller --onefile --windowed --add-data "Example_Archive_Folder.zip;." --add-data "some-icon.ico;." setup.py


