from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame
import os

# Fungsi untuk membuat gambar kartu ucapan
def create_birthday_card(text, image_path):
    try:
        # Buka gambar latar belakang
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Pilih font dan ukuran teks
        font_path = "arial.ttf"
        if not os.path.exists(font_path):
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Path alternatif untuk Linux
        font = ImageFont.truetype(font_path, 40)

        # Tentukan posisi dan warna teks
        text_position = (50, 50)
        text_color = (255, 255, 255)

        # Tambahkan teks ke gambar
        draw.text(text_position, text, fill=text_color, font=font)

        # Simpan gambar kartu ucapan
        card_path = "Foto.jpg"
        image.save(card_path)

        return card_path
    except Exception as e:
        print(f"Terjadi kesalahan saat membuat kartu ucapan: {e}")
        return None

# Fungsi untuk animasi sederhana
def animate_text(text):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    text_obj = ax.text(0.5, 0.5, text, ha='center', va='center', fontsize=20, color='blue')

    def update(frame):
        text_obj.set_fontsize(20 + frame * 2)
        text_obj.set_color(plt.cm.viridis(frame / 50))

    ani = FuncAnimation(fig, update, frames=50, interval=100, repeat=False)
    plt.show()

# Fungsi untuk memutar musik
def play_music(music_file):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # Loop musik
    except Exception as e:
        print(f"Terjadi kesalahan saat memutar musik: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    # Buat kartu ucapan
    text = "Happy Birthday, Wish u always be happy and strong!"
    text = "Don't forget to smile, because your smile is the most beautiful gift that God created!"
    image_path = "bg.jpeg"  # Ganti dengan path gambar latar belakang yang diinginkan
    card_path = create_birthday_card(text, image_path)
    if card_path:
        print(f"Kartu ucapan disimpan di {card_path}")

    # Putar musik
    music_file = "hbd.mp3"  # Ganti dengan path file musik yang diinginkan
    play_music(music_file)

    # Animasi teks
    animate_text(text)
