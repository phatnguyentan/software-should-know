🚀 Cách cài đặt & sử dụng
1. Copy code về máy

Tạo 1 file export_images.py

Copy đoạn code Python vào file này.

2. Kiểm tra máy đã cài Python chưa

Mở Command Prompt (Windows) hoặc Terminal (Mac/Linux) và gõ:

python --version


hoặc:

python3 --version


Nếu thấy có version (ví dụ: Python 3.11.5) nghĩa là máy đã có Python.

Nếu báo lỗi command not found → cần cài Python từ python.org
.

3. Cài thư viện cần thiết

Script dùng thư viện Pillow để xử lý ảnh.

Với Python 3:

pip3 install -r requirements.txt


Nếu bạn đang dùng Python 2 (không khuyến khích, vì đã lỗi thời):

pip install -r requirements.txt

4. Chạy script

Cú pháp:

python export_images.py <thư_mục_input> <file_output.csv>

pyinstaller --onefile export_images.py
python -m PyInstaller --onefile export_images.py

.\export_images.exe "C:\Users\ADMIN\Downloads" "./images_info.csv"

Ví dụ Windows:

python export_images.py C:\Users\ADMIN\Downloads ./images_info.csv


Ví dụ Linux/Mac:

python3 export_images.py ~/Downloads ./images_info.csv

📄 Ví dụ output CSV
1,photo1.jpg,jpg,1920x1080,
2,logo.png,png,512x512,
3,wallpaper.webp,webp,2560x1440,subfolder
4,icon.gif,gif,128x128,subfolder