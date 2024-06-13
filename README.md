# Python_GDS
This Python library uses the naszca Python libraries (https://nazca-design.org/) to create a commonly used photonic object and export it in GDSII format. These can then be passed on to the production facilities for manufacture.

# How to used
1) Clone/download the Git repo on your PC
2) Open "nazca-0.5.13" and copy the "nazca" Folder to your python side-packages. You can 
find them on your Windows PC in "C:\Program Files\Python\Lib\site-packages\". This step 
is needed since nazca could not be installed from PiPy. If you plan to use this Library 
on our servers simpli create an new Project with PyCharm. Go to File->Settings->Project:<Name of Project> -> Python Interpreter
click on the "+" icon and searcha nd install nazca. This Nazca is different one but hold the same name. After you install it just 
copy and paste the one from git in your "PyCharm Project Folder"->venv->lib->python3.6->site-packages.
3) You are ready to go! You can now use the "Controll.py" File that is in the Git Repo to see an examples of how this 
library work. For more information and help just call the Help() function (see an Example in "Controll.py")


# Chip Area 
Board Function
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/Board.PNG?raw=true)

# S Bends
S-Bends Function with 3 Types of Bends (Cubic Betier, Euler or Cosinus)
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/S_Bends.PNG?raw=true)

# Coupler
1x2 MMI, Directional Coupler and Y-Junction functions
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/2x1MMI.PNG?raw=true)
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/DC.PNG?raw=true)
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/Y_Junction.PNG?raw=true)

# Electro Optical Modulators
MZM Function 
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/MZM.PNG?raw=true)

# Electro Optical Modulators
Straight Waveguide and Point-to-Point straight Waveguide functions
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/StraightWG.PNG?raw=true)
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/StraightWG_P2P.PNG?raw=true)

# Example of Chip Designt with all the passive components and MZM
- ![alt text](https://github.com/MartinMiroslavovMihaylov/Python_GDS/blob/main/Documentation/Bilder/TestChip.PNG?raw=true)

