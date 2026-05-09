import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import cv2
import wave
import os
import numpy as np
import datetime
from PIL import Image, ImageTk

DELIMITER = '1111111111111110'

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Media ShadowCode Framework")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root.geometry("1200x800")
        self.root.resizable(True, True)

        self.container = ctk.CTkFrame(root)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.front_page = ctk.CTkFrame(self.container, corner_radius=12)
        self.main_frame = ctk.CTkFrame(self.container, corner_radius=14)
        self.help_page = ctk.CTkFrame(self.container, corner_radius=12)

        for frame in (self.front_page, self.main_frame, self.help_page):
            frame.grid(row=0, column=0, sticky="nsew")

        self.setup_front_page()
        self.setup_main_app()
        self.setup_help_page()
        self.show_frame(self.front_page)

    def show_frame(self, frame):
        frame.tkraise()

    def setup_front_page(self):
        help_button = ctk.CTkButton(
            self.front_page,
            text="Help",
            width=100,
            command=lambda: self.show_frame(self.help_page)
        )
        help_button.pack(anchor="ne", padx=20, pady=10)

        center_container = ctk.CTkFrame(self.front_page)
        center_container.pack(expand=True)

        welcome_label = ctk.CTkLabel(
            center_container,
            text="Welcome",
            font=("Arial", 28, "bold")
        )
        welcome_label.pack(pady=(0, 35))
 # Load and display the logo image
        logo_path = r"C:\Users\III S I\OneDrive\Desktop\GUI\code\Image.png"  # Change as needed

        try:
            self.logo_image = ctk.CTkImage(
                light_image=Image.open(logo_path),
                dark_image=Image.open(logo_path),
                size=(350, 350)  # Larger logo size for visibility
            )
        except Exception as e:
            messagebox.showerror("Image Load Error", f"Failed to load logo image:\n{str(e)}")
            self.logo_image = None

        if self.logo_image:
            logo_label = ctk.CTkLabel(center_container, image=self.logo_image, text="")
            logo_label.pack(pady=(0, 20))  # small bottom padding

        details_label = ctk.CTkLabel(
            center_container,
            text="An advanced multimedia steganography encoding & decoding application.",
            font=("Arial", 18)
        )
        details_label.pack(pady=(0, 25))

        self.front_datetime_label = ctk.CTkLabel(
            center_container,
            text="",
            font=("Arial", 14, "italic")
        )
        self.front_datetime_label.pack(pady=(0, 40))
        self.update_front_datetime()

        start_button = ctk.CTkButton(
            center_container,
            text="Let's Start",
            font=("Arial", 20),
            width=200,
            command=lambda: self.show_frame(self.main_frame)
        )
        start_button.pack(pady=(0, 0))

    def update_front_datetime(self):
        now = datetime.datetime.now()
        date_str = now.strftime("%A, %Y-%m-%d %H:%M:%S")
        self.front_datetime_label.configure(text=date_str)
        self.root.after(1000, self.update_front_datetime)

    def setup_main_app(self):
        back_button = ctk.CTkButton(
            self.main_frame,
            text="\u2190 Back", font=("Arial", 14), width=100,
            command=lambda: self.show_frame(self.front_page)
        )
        back_button.pack(anchor="nw", padx=10, pady=10)

        header_frame = ctk.CTkFrame(self.main_frame, corner_radius=12)
        header_frame.pack(side="top", fill="x", padx=15, pady=(0, 15))

        title_label = ctk.CTkLabel(
            header_frame,
            text="MULTI-MEDIA SHADOWCODE FRAMEWORK",
            font=("Arial", 24, "bold")
        )
        title_label.pack(expand=True, pady=8)

        self.datetime_label = ctk.CTkLabel(
            header_frame,
            text="",
            font=("Arial", 12)
        )
        self.datetime_label.pack(side="right", pady=8, padx=10)
        self.update_datetime()

        self.notebook = ctk.CTkTabview(self.main_frame, width=900, height=560, corner_radius=13)
        self.notebook.pack(fill="both", expand=True, pady=15, padx=15)

        self.encode_tab = self.notebook.add("Encode")
        self.decode_tab = self.notebook.add("Decode")
        self.setup_encode_tab()
        self.setup_decode_tab()

        self.status_bar = ctk.CTkLabel(
            self.main_frame,
            text="Ready",
            anchor="w",
            fg_color=("gray75", "gray25"),
            font=("Arial", 11)
        )
        self.status_bar.pack(side="bottom", fill="x")

    def update_datetime(self):
        now = datetime.datetime.now()
        day = now.strftime("%A")
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_label.configure(text=f"{day}, {date_time}")
        self.root.after(1000, self.update_datetime)

    def setup_encode_tab(self):
        card = ctk.CTkFrame(self.encode_tab, corner_radius=12)
        card.pack(fill="both", expand=True, padx=40, pady=32)

        ctk.CTkLabel(card, text="Encode Message", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, padx=4, pady=15, sticky="w")

        section1 = ctk.CTkFrame(card, corner_radius=10)
        section1.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        ctk.CTkLabel(section1, text="Select Medium:", font=("Arial", 13)).pack(anchor="w", pady=2)
        self.encode_medium = ctk.StringVar(value="Text")
        for medium in ["Text", "Image", "Audio", "Video"]:
            ctk.CTkRadioButton(section1, text=medium, variable=self.encode_medium, value=medium).pack(anchor="w", padx=8, pady=2)

        section2 = ctk.CTkFrame(card, corner_radius=10)
        section2.grid(row=1, column=1, padx=10, pady=10, sticky="ne")
        ctk.CTkLabel(section2, text="Enter Message:", font=("Arial", 13)).pack(anchor="w", pady=(4, 2))
        self.encode_message = ctk.CTkTextbox(section2, height=80, width=360)
        self.encode_message.pack(padx=8, pady=4)
        self.encode_clear_button = ctk.CTkButton(section2, text="Clear", command=self.clear_encode_section, width=100)
        self.encode_clear_button.pack(pady=(4, 10))

        row_idx = 2
        self.encode_file_button = ctk.CTkButton(card, text="Select Input File", command=self.select_encode_file, width=220)
        self.encode_file_button.grid(row=row_idx, column=0, padx=10, pady=9, sticky="w")

        self.encode_format_frame = ctk.CTkFrame(card)
        ctk.CTkLabel(self.encode_format_frame, text="Format:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.encode_format = ctk.StringVar(value="png")
        ctk.CTkRadioButton(self.encode_format_frame, text="PNG", variable=self.encode_format, value="png").grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ctk.CTkRadioButton(self.encode_format_frame, text="BMP", variable=self.encode_format, value="bmp").grid(row=0, column=2, padx=5, pady=2, sticky="w")

        self.save_path_button = ctk.CTkButton(card, text="Choose Save Path", command=self.select_save_path, width=220)
        self.save_path_button.grid(row=row_idx + 1, column=0, padx=10, pady=9, sticky="w")
        self.save_path_label = ctk.CTkLabel(card, text="Save Path: Not Selected", font=("Arial", 11))
        self.save_path_label.grid(row=row_idx + 1, column=1, padx=10, pady=9, sticky="w")

        self.encode_button = ctk.CTkButton(card, text="Encode", command=self.encode_data, width=140)
        self.encode_button.grid(row=row_idx + 2, column=0, columnspan=2, padx=8, pady=20, sticky="ew")

        self.encode_medium.trace_add("write", lambda *args: self.toggle_encode_format())

    def setup_decode_tab(self):
        card = ctk.CTkFrame(self.decode_tab, corner_radius=12)
        card.pack(fill="both", expand=True, padx=40, pady=10)

        ctk.CTkLabel(card, text="Decode Message", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, padx=4, pady=10, sticky="w")

        section1 = ctk.CTkFrame(card, corner_radius=10)
        section1.grid(row=1, column=0, padx=10, pady=5, sticky="nw")
        ctk.CTkLabel(section1, text="Select Medium:", font=("Arial", 13)).pack(anchor="w", pady=2)
        self.decode_medium = ctk.StringVar(value="")
        for medium in ["Text", "Image", "Audio", "Video"]:
            ctk.CTkRadioButton(section1, text=medium, variable=self.decode_medium, value=medium).pack(anchor="w", padx=8, pady=2)

        self.decode_file_button = ctk.CTkButton(card, text="Select Stego File", command=self.select_decode_file, width=220)
        self.decode_file_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.decode_format_frame = ctk.CTkFrame(card)
        ctk.CTkLabel(self.decode_format_frame, text="Format:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.decode_format = ctk.StringVar(value="png")
        ctk.CTkRadioButton(self.decode_format_frame, text="PNG", variable=self.decode_format, value="png").grid(row=0, column=1, padx=5, pady=2, sticky="w")
        ctk.CTkRadioButton(self.decode_format_frame, text="BMP", variable=self.decode_format, value="bmp").grid(row=0, column=2, padx=5, pady=2, sticky="w")

        ctk.CTkLabel(card, text="Decoded Message:", font=("Arial", 13)).grid(row=3, column=0, padx=10, pady=4, sticky="w")
        self.decoded_message = ctk.CTkTextbox(card, height=80, width=400, state="disabled")
        self.decoded_message.grid(row=4, column=0, columnspan=2, padx=14, pady=5, sticky="ew")

        self.decode_button = ctk.CTkButton(card, text="Decode", command=self.decode_data, width=140)
        self.decode_button.grid(row=5, column=0, columnspan=2, padx=8, pady=10, sticky="ew")
        self.decode_clear_button = ctk.CTkButton(card, text="Clear", command=self.clear_decode_section, width=100)
        self.decode_clear_button.grid(row=6, column=0, columnspan=2, pady=(4, 10))

        self.decode_medium.trace_add("write", lambda *args: self.toggle_decode_format())

    def setup_help_page(self):
        container = ctk.CTkFrame(self.help_page)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(5, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.help_title = ctk.CTkLabel(
            container,
            text="MULTI-MEDIA SHADOWCODE FRAMEWORK QUICK USER GUIDE",
            font=("Arial", 28, "bold", "underline"),
            text_color="black",
            fg_color="white",
            corner_radius=20,
            width=900,
            height=50,
            justify="center"
        )
        self.help_title.grid(row=1, column=0, pady=(20, 15), sticky="n")
        self.help_textbox = ctk.CTkTextbox(
            container,
            width=900,
            height=480,
            font=("Courier New", 14),
        )
        self.help_textbox.grid(row=2, column=0, pady=(0, 10))
        self.help_textbox.configure(state="disabled")

        self.tip_label = ctk.CTkLabel(
            container,
            text="Tip: PNG, BMP, WAV, and AVI (FFV1) work best for hiding data.",
            font=("Arial", 14, "bold", "italic"),
            text_color="black",
            fg_color="white",
            corner_radius=8,
            width=900,
            height=40,
            justify="center"
        )
        self.tip_label.grid(row=3, column=0, pady=(0, 10))
        self.got_it_button = ctk.CTkButton(
            container,
            text="Got it",
            width=120,
            command=lambda: self.show_frame(self.front_page)
        )
        self.got_it_button.grid(row=4, column=0, pady=(0, 20))

    def set_help_text(self, text: str):
        self.help_textbox.configure(state="normal")
        self.help_textbox.delete("0.0", tk.END)
        self.help_textbox.insert("0.0", text)
        self.help_textbox.configure(state="disabled")

    def clear_encode_section(self):
        self.encode_message.delete("1.0", tk.END)
        self.encode_medium.set("")
        self.encode_format.set("png")
        if hasattr(self, 'encode_file_path'):
            del self.encode_file_path
        if hasattr(self, 'save_path'):
            del self.save_path
        self.save_path_label.configure(text="Save Path: Not Selected")
        self.status_bar.configure(text="Ready")

    def clear_decode_section(self):
        self.decoded_message.configure(state="normal")
        self.decoded_message.delete("1.0", tk.END)
        self.decoded_message.configure(state="disabled")
        self.decode_medium.set("")
        self.decode_format.set("png")
        if hasattr(self, 'decode_file_path'):
            del self.decode_file_path
        self.status_bar.configure(text="Ready")

    def toggle_encode_format(self):
        if self.encode_medium.get() == "Image":
            self.encode_format_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        else:
            self.encode_format_frame.grid_forget()

    def toggle_decode_format(self):
        if self.decode_medium.get() == "Image":
            self.decode_format_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        else:
            self.decode_format_frame.grid_forget()

    def select_encode_file(self):
        medium = self.encode_medium.get()
        filetypes = {
            "Text": [("Text Files", "*.txt")],
            "Image": [("Image Files", "*.png *.bmp")],
            "Audio": [("Audio Files", "*.wav")],
            "Video": [("AVI Files", "*.avi")]
        }
        if medium == "":
            messagebox.showerror("Error", "Please select a medium first.")
            return
        self.encode_file_path = filedialog.askopenfilename(title=f"Select {medium} File", filetypes=filetypes[medium])
        if self.encode_file_path:
            self.status_bar.configure(text=f"Selected: {os.path.basename(self.encode_file_path)}")

    def select_decode_file(self):
        medium = self.decode_medium.get()
        filetypes = {
            "Text": [("Text Files", "*.txt")],
            "Image": [("Image Files", "*.png *.bmp")],
            "Audio": [("Audio Files", "*.wav")],
            "Video": [("AVI Files", "*.avi")]
        }
        if medium == "":
            messagebox.showerror("Error", "Please select a medium first.")
            return
        self.decode_file_path = filedialog.askopenfilename(title=f"Select {medium} File", filetypes=filetypes[medium])
        if self.decode_file_path:
            self.status_bar.configure(text=f"Selected: {os.path.basename(self.decode_file_path)}")

    def select_save_path(self):
        medium = self.encode_medium.get()
        filetypes = {
            "Text": [("Text Files", "*.txt")],
            "Image": [("PNG Files", "*.png"), ("BMP Files", "*.bmp")],
            "Audio": [("Audio Files", "*.wav")],
            "Video": [("AVI Files", "*.avi")]
        }
        if medium == "":
            messagebox.showerror("Error", "Please select a medium first.")
            return
        if medium == "Image":
            if self.encode_format.get() == "png":
                self.save_path = filedialog.asksaveasfilename(
                    title="Save Image File",
                    defaultextension=".png",
                    filetypes=[("PNG Files", "*.png")]
                )
            else:
                self.save_path = filedialog.asksaveasfilename(
                    title="Save Image File",
                    defaultextension=".bmp",
                    filetypes=[("BMP Files", "*.bmp")]
                )
        else:
            defaultext = {
                "Text": ".txt",
                "Audio": ".wav",
                "Video": ".avi"
            }
            self.save_path = filedialog.asksaveasfilename(
                title=f"Save {medium} File",
                defaultextension=defaultext.get(medium, ""),
                filetypes=filetypes[medium]
            )
        if self.save_path:
            self.save_path_label.configure(text=f"Save Path: {os.path.basename(self.save_path)}")

    def text_to_binary(self, message):
        return ''.join(format(ord(c), '08b') for c in message) + DELIMITER

    def binary_to_text(self, binary):
        chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
        return ''.join([chr(int(char, 2)) for char in chars if len(char) == 8])

    def check_file_extension_match(self, file_path, medium, selected_format=None):
        ext = os.path.splitext(file_path)[1].lower()
        if medium == "Text":
            if ext != ".txt":
                return False, "Selected file is not a text file (.txt)."
        elif medium == "Image":
            if selected_format is None:
                return True, ""
            if selected_format == "png" and ext != ".png":
                return False, "Selected format is PNG but file extension is not .png."
            if selected_format == "bmp" and ext != ".bmp":
                return False, "Selected format is BMP but file extension is not .bmp."
        elif medium == "Audio":
            if ext != ".wav":
                return False, "Selected file is not a WAV audio file (.wav)."
        elif medium == "Video":
            if ext != ".avi":
                return False, "Selected file is not an AVI video file (.avi)."
        return True, ""

    def encode_data(self):
        medium = self.encode_medium.get()
        message = self.encode_message.get("1.0", tk.END).strip()
        if medium == "":
            messagebox.showerror("Error", "Please select a medium.")
            return
        if not message:
            messagebox.showerror("Error", "Please enter a message to encode.")
            return
        if not hasattr(self, 'encode_file_path'):
            messagebox.showerror("Error", "Please select an input file.")
            return
        if not hasattr(self, 'save_path'):
            messagebox.showerror("Error", "Please select a save path.")
            return
        valid_input, msg = self.check_file_extension_match(self.encode_file_path, medium, self.encode_format.get())
        if not valid_input:
            messagebox.showerror("Error", f"Input file error: {msg}")
            return
        valid_save, msg = self.check_file_extension_match(self.save_path, medium, self.encode_format.get())
        if not valid_save:
            messagebox.showerror("Error", f"Save file error: {msg}")
            return
        try:
            if medium == "Text":
                with open(self.save_path, 'w') as f:
                    f.write(message)
                messagebox.showinfo("Success", f"Message encoded in text and saved to:\n{self.save_path}")
            elif medium == "Image":
                img = cv2.imread(self.encode_file_path)
                if img is None:
                    raise ValueError("Invalid image file.")
                binary_msg = self.text_to_binary(message)
                idx = 0
                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        for k in range(3):
                            if idx < len(binary_msg):
                                img[i][j][k] = (img[i][j][k] & 0xFE) | int(binary_msg[idx])
                                idx += 1
                cv2.imwrite(self.save_path, img)
                messagebox.showinfo("Success", f"Message encoded in image and saved to:\n{self.save_path}")
            elif medium == "Audio":
                with wave.open(self.encode_file_path, 'rb') as audio_file:
                    params = audio_file.getparams()
                    frames = audio_file.readframes(params.nframes)
                frames = bytearray(frames)
                binary_msg = self.text_to_binary(message)
                if len(binary_msg) > len(frames):
                    raise ValueError("Message too large for the audio file.")
                for i in range(len(binary_msg)):
                    frames[i] = (frames[i] & 0xFE) | int(binary_msg[i])
                with wave.open(self.save_path, 'wb') as output_file:
                    output_file.setparams(params)
                    output_file.writeframes(frames)
                messagebox.showinfo("Success", f"Message encoded in audio and saved to:\n{self.save_path}")
            elif medium == "Video":
                cap = cv2.VideoCapture(self.encode_file_path)
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = cap.get(cv2.CAP_PROP_FPS)
                fourcc = cv2.VideoWriter_fourcc(*'FFV1')
                out = cv2.VideoWriter(self.save_path, fourcc, fps, (width, height))
                binary_msg = self.text_to_binary(message)
                msg_index = 0
                encoded = False
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    for i in range(frame.shape[0]):
                        for j in range(frame.shape[1]):
                            for k in range(3):
                                if msg_index < len(binary_msg):
                                    frame[i][j][k] = (frame[i][j][k] & ~1) | int(binary_msg[msg_index])
                                    msg_index += 1
                    out.write(frame)
                    if msg_index >= len(binary_msg):
                        encoded = True
                        break
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    out.write(frame)
                cap.release()
                out.release()
                if encoded:
                    messagebox.showinfo("Success", f"Message encoded successfully into:\n{self.save_path}")
                else:
                    messagebox.showwarning("Warning", "Message too large for the video!")
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed: {str(e)}")

    def decode_data(self):
        medium = self.decode_medium.get()
        if medium == "":
            messagebox.showerror("Error", "Please select a medium.")
            return
        if not hasattr(self, 'decode_file_path'):
            messagebox.showerror("Error", "Please select a stego file.")
            return
        selected_format = None
        if medium == "Image":
            selected_format = self.decode_format.get()
        valid_file, msg = self.check_file_extension_match(self.decode_file_path, medium, selected_format)
        if not valid_file:
            messagebox.showerror("Error", f"Stego file error: {msg}")
            return
        try:
            if medium == "Text":
                with open(self.decode_file_path, 'r') as f:
                    decoded_msg = f.read()
            elif medium == "Image":
                img = cv2.imread(self.decode_file_path)
                if img is None:
                    raise ValueError("Invalid image file.")
                binary_msg = ""
                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        for k in range(3):
                            binary_msg += str(img[i][j][k] & 1)
                if DELIMITER in binary_msg:
                    binary_msg = binary_msg[:binary_msg.index(DELIMITER)]
                decoded_msg = self.binary_to_text(binary_msg)
                if not decoded_msg:
                    decoded_msg = "No hidden message found."
            elif medium == "Audio":
                with wave.open(self.decode_file_path, 'rb') as audio_file:
                    params = audio_file.getparams()
                    frames = audio_file.readframes(params.nframes)
                frames = bytearray(frames)
                binary_msg = ""
                for i in range(len(frames)):
                    binary_msg += str(frames[i] & 1)
                if DELIMITER in binary_msg:
                    binary_msg = binary_msg[:binary_msg.index(DELIMITER)]
                decoded_msg = self.binary_to_text(binary_msg)
                if not decoded_msg:
                    decoded_msg = "No hidden message found."
            elif medium == "Video":
                cap = cv2.VideoCapture(self.decode_file_path)
                binary_data = ""
                found = False
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    for i in range(frame.shape[0]):
                        for j in range(frame.shape[1]):
                            for k in range(3):
                                binary_data += str(frame[i][j][k] & 1)
                                if binary_data.endswith(DELIMITER):
                                    found = True
                                    break
                            if found:
                                break
                        if found:
                            break
                    if found:
                        break
                cap.release()
                if not found:
                    decoded_msg = "No hidden message found."
                else:
                    binary_data = binary_data[:-len(DELIMITER)]
                    decoded_msg = self.binary_to_text(binary_data)
            self.decoded_message.configure(state="normal")
            self.decoded_message.delete("1.0", tk.END)
            self.decoded_message.insert(tk.END, decoded_msg)
            self.decoded_message.configure(state="disabled")
            self.status_bar.configure(text=f"Decoded message from {medium.lower()} file.")
            messagebox.showinfo("Success", "Message decoded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed: {str(e)}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = SteganographyApp(root)
    user_manual_text = """
Supported Media:

 Text (.txt)
 Image (.png, .bmp)
 Audio (.wav)
 Video (.avi, FFV1 codec only)

Encoding Steps:

1. Go to 'Encode' tab.
2. Select a medium (Text/Image/Audio/Video).
3. Enter the message.
4. Select the input file.
5. (For images) Choose PNG or BMP.
6. Choose where to save the output.
7. Click 'Encode' to embed the message.

Decoding Steps:

1. Go to 'Decode' tab.
2. Select the medium and format (if image).
3. Select the stego file.
4. Click 'Decode' to reveal the hidden message.

Notes:

•Use only uncompressed formats.
•The 'Clear' button resets inputs on the Encode tab.
•Max message size depends on file size.
•A delimiter is used to mark message end.
"""
    app.set_help_text(user_manual_text)
    root.mainloop()
