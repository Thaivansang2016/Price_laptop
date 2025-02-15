import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from tkinter import filedialog
import string

# Hàm để tải file CSV và huấn luyện mô hình
def load_csv():
    file_path = filedialog.askopenfilename(title="Chọn tệp CSV", filetypes=[("CSV files", "Laptop_price11.csv")])
    
    if file_path:
        try:
            # Đọc dữ liệu từ file CSV
            data = pd.read_csv(file_path)

            # Giả sử file CSV có các cột: 'RAM', 'CPU', 'Ổ cứng', 'Giá'
            X = data[['Processor_Speed', 'RAM_Size', 'Storage_Capacity','Screen_Size', 'Weight']].values
            y = data['Price'].values

            # Huấn luyện mô hình
            model.fit(X, y)
            messagebox.showinfo("Thành công", "Đã tải và huấn luyện mô hình từ tệp CSV!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc hoặc xử lý tệp CSV.\nLỗi: {str(e)}")

# Hàm dự đoán giá
def predict_price():
    try:
        cpu = float(cpu_entry.get())
        ram = float(ram_entry.get())
        storage = float(storage_entry.get())
        screen = float(screen_entry.get())
        weight = float(weight_entry.get())
        
        # Dự đoán giá dựa trên input
        features = np.array([[cpu, ram, storage, screen, weight]])
        predicted_price = model.predict(features)[0]
        
        # Hiển thị kết quả
        result_label.config(text=f'Giá dự đoán: ${predicted_price:.2f}')
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo một mô hình dự đoán
model = LinearRegression()

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Dự đoán giá laptop")
window.geometry('500x350')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)




# Nút tải file CSV
load_button = tk.Button(window, text="Tải dữ liệu CSV", command=load_csv)
load_button.grid(row=0, column=0, columnspan=2, pady=10)

# Nhãn và ô nhập liệu cho CPU
cpu_label = tk.Label(window, text="Tốc độ CPU (GHz):")
cpu_label.grid(row=1, column=0,sticky="we", padx=0, pady=10 )
cpu_entry = tk.Entry(window)
cpu_entry.grid(row=1, column=1, sticky="we", padx=50)

# Nhãn và ô nhập liệu cho RAM
ram_label = tk.Label(window, text="RAM (GB):")
ram_label.grid(row=2, column=0,sticky="we", padx=0, pady=5)
ram_entry = tk.Entry(window)
ram_entry.grid(row=2, column=1,sticky="we", padx=50)


# Nhãn và ô nhập liệu cho dung lượng ổ cứng
storage_label = tk.Label(window, text="Ổ cứng (GB):")
storage_label.grid(row=3, column=0,sticky="we", padx=0, pady=5)
storage_entry = tk.Entry(window)
storage_entry.grid(row=3, column=1,sticky="we", padx=50)

# Nhãn và ô nhập liệu cho kích thước màn hình
screen_label = tk.Label(window,text="Screen Size:")
screen_label.grid(row=4,column=0,sticky="we", padx=0, pady=5)
screen_entry = tk.Entry(window)
screen_entry.grid(row=4,column=1,sticky="we", padx=50)
# Nhãn và ô nhập liệu cho trọng lượng
weight_label =tk.Label(window,text="Weight:")
weight_label.grid(row=5,column=0,sticky="we", padx=0, pady=5)
weight_entry = tk.Entry(window)
weight_entry.grid(row=5,column=1,sticky="we", padx=50)
# Nút dự đoán
predict_button = tk.Button(window, text="Dự đoán giá", command=predict_price)
predict_button.grid(row=6, columnspan=2,pady=20)

# Nhãn hiển thị kết quả
result_label = tk.Label(window, text="Giá dự đoán: $0")
result_label.grid(row=7, columnspan=2)

# Chạy vòng lặp chính
window.mainloop()