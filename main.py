import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

# Fungsi untuk memilih file MKV
def pilih_file():
    filepath = filedialog.askopenfilename(
        title="Select mkv file",
        filetypes=[("MKV Files", "*.mkv"), ("All Files", "*.*")]
    )
    if filepath:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, filepath)

# Fungsi untuk memilih folder output
def pilih_folder_output():
    folderpath = filedialog.askdirectory(title="Select output folder")
    if folderpath:
        entry_output_path.delete(0, tk.END)
        entry_output_path.insert(0, folderpath)

# Fungsi untuk mengonversi file
def konversi():
    input_path = entry_file_path.get()
    output_folder = entry_output_path.get()

    if not input_path or not output_folder:
        messagebox.showerror("Error", "Please check the file format and select the output folder destination")
        return

    try:
        # Proses konversi MKV ke MP4
        video = VideoFileClip(input_path)
        output_path = os.path.join(
            output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".mp4"
        )
        video.write_videofile(output_path, codec="libx264")
        video.close()

        messagebox.showinfo("Sukses", f"File was successfully converted {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"File failed to convert: {e}")

# GUI dengan Tkinter
root = tk.Tk()
root.title("Converter mkv to mp4")

# Label dan Entry untuk file MKV
label_file_path = tk.Label(root, text="Select mkv file:")
label_file_path.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=5)
button_browse_file = tk.Button(root, text="Browse", command=pilih_file)
button_browse_file.grid(row=0, column=2, padx=10, pady=5)

# Label dan Entry untuk folder output
label_output_path = tk.Label(root, text="Output folder:")
label_output_path.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_output_path = tk.Entry(root, width=50)
entry_output_path.grid(row=1, column=1, padx=10, pady=5)
button_browse_output = tk.Button(root, text="Browse", command=pilih_folder_output)
button_browse_output.grid(row=1, column=2, padx=10, pady=5)

# Tombol untuk memulai konversi
button_konversi = tk.Button(root, text="Convert", command=konversi, bg="white", fg="black")
button_konversi.grid(row=2, column=1, pady=10)

# Menjalankan aplikasi
root.mainloop()