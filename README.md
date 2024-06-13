
DO NOT FORGET THAT THIS PYTHON CODE ONLY CAN WORK WITH PYINSTALLER PACKAGES!

This code can create an exe for the application downloadings or updatings.
run setup script:

pyinstaller.exe -F setup.py

For embedding my zip file to the Python script :

pyinstaller --onefile --windowed --add-data "Example_Archive_Folder.zip;." --add-data "some-icon.ico;." setup.py


Then i changed and added to setup.exe file a icon and a splash image for preventing to wait a long time without an startup image for displaying to the user too:

pyinstaller --noconfirm --onefile --name=Setup --add-binary "some-icon.ico;." --icon=some-icon.ico --splash splash_image.png --windowed --add-data "Example_Archive_Folder.zip;." --add-data "some-icon.ico;." setup.py

If with copying or moving the setup does not change the icon as our some-icon.ico then try the change --name parameter of the setup.

For give the directory version of the exe to the user, command can be change as a :

pyinstaller --noconfirm --onedir --console --name=Setup --add-binary "some-icon.ico;." --icon=some-icon.ico  --windowed  --add-data "Example_Archive_Folder.zip;." --add-data "some-icon.ico;." "C:\sena_folder\Scripts\setup.py"

I removed the splash because of the exe size is decreased it starts fastly, i do not need the splash anymore. Terminal command at the above can be used for decreasing the size and work exe so much faster. But if you want to give user only the exe not as a folder or archive file then other command with the --onefile at the above not --onedir can be used.  
