
This code can create an exe for the application downloadings or updatings.
run setup script:

pyinstaller.exe -F setup.py

For embedding my zip file to the Python script :

pyinstaller --onefile --windowed --add-data "Example_Archive_Folder.zip;." --add-data "some-icon.ico;." setup.py


Then i changed and added to setup.exe file a icon and a splash image for preventing to wait a long time too:

pyinstaller --noconfirm --onefile --name=Setup --add-binary "some-icon.ico;." --icon=some-icon.ico --splash splash_image.png --windowed --add-data "Example_Archive_Folder.zip;." --add-data "some-icon.ico;." setup.py

If with copying or moving the setup does not change the icon as our some-icon.ico then try the change --name parameter of the setup.
