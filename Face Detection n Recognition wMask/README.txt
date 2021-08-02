Requirements
1) First of all anaconda3 should be installed in your computer. In the advanced system settings 
section of your computer, the necessary file paths should be found in the environment 
variables (\anaconda3, \anaconda3\Library\bin, and anaconda3\Scripts.) (To be able to pip 
install; no need if pip install is running)

Required installations can be done by command prompt with entering the following items 
separately.
- pip install Tkinter
- pip install Pillow
- pip install pymysql
- pip install tkcalendar
- pip install opencv-python
- pip install tensorflow

2) For the database connection to work, xampp must be installed on your computer.

3) Python extension must be installed in Visual Studio Code compiler.

4) You need to adapt the file path "pb_path = r"C:\Users\profo\OneDrive\Belgeler\Healthy 
Faces\pb_model_select_num=15.bp" on line 220 in real_time_face_recognition.py according 
to the file path on your computer. And in the same way, you need to adapt the "ref_dir = 
r"C:\Users\profo\OneDrive\Belgeler\Healthy Faces" file path in line 226 according to the file 
path on your own computer.
* In the process of adapting this file path in the codes with the file path on your own computer; 
There should be no Turkish characters anywhere from the beginning to the end in the file path 
you specify.