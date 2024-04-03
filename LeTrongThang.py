# Đọc 1 file văn bản gồm nhiều dòng
# Ghi ra màn hình theo thứ tự ngược lại của các dòng
# VD 
    # Nam quốc sơn hà     
    # Nam đế cư           
# ==> Nam đế cư      
    # Nam quốc sơn hà 

import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
def reverse_text():
    file_path = file_var.get()
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1258', 'utf-16', 'utf-16-le', 'cp1252']
    for encoding in encodings:
        try:
            with open(file_path, 'rb') as file:
                content = file.read().decode(encoding)
                reversed_lines = reversed(content)
                reversed_content = '\n'.join(reversed_lines)
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, reversed_content)
                return
        except FileNotFoundError:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Không tìm thấy file.")
            return
        except UnicodeDecodeError:
            continue
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Không thể giải mã file. Vui lòng chọn một file khác hoặc sử dụng encoding khác.")
def browse_file():
    file_path = filedialog.askopenfilename()
    file_var.set(file_path)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Đảo ngược nội dung file")

# Tạo biến lưu trữ đường dẫn file
file_var = tk.StringVar()

# Tạo label và button cho việc chọn file
file_label = tk.Label(root, text="Chọn file:")
file_label.pack(pady=5)

file_name = tk.Label(root, text="")
file_label.pack(pady=5)

browse_button = tk.Button(root, text="Chọn file", command=browse_file)
browse_button.pack(pady=5)

# Tạo button xử lý và kết quả đảo ngược
process_button = tk.Button(root, text="Xử lý", command=reverse_text)
process_button.pack(pady=5)

# Tạo text widget để hiển thị kết quả
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=5)

# Khởi chạy main loop
root.mainloop()