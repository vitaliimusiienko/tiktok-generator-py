import asyncio
import edge_tts
import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, vfx

# Налаштування
BG_VIDEO = "background.mp4"
OUTPUT = "result.mp4"
VOICE = "uk-UA-OstapNeural"
SCRIPT_FILE = "text.txt"
FONT_PATH = "Arial" 

# Функція для отримання тексту з файлу або створення його за замовчуванням
def get_text_from_file():
    if not os.path.exists(SCRIPT_FILE):
        default_text = "Це тестовий текст. Спробуй змінити цей текст у файлі!"
        with open(SCRIPT_FILE, "w", encoding="utf-8") as f:
            f.write(default_text)
        return default_text
    
    with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
        text = f.read().strip()
        if not text: return "Текст відсутній."
        return text

# Функція для генерації голосу з тексту
async def create_voice(text, filename="voice.mp3"):
    print(f"Генерую голос...")
    comm = edge_tts.Communicate(text, VOICE)
    await comm.save(filename)
    return filename

# Функція для монтажу відео з аудіо та текстом
def process_video(video_path, audio_path, text, output_path):
    print(f"Монтаж відео...")
    
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    duration = audio.duration + 1.0
    if video.duration < duration:
        video = video.with_effects([vfx.Loop(duration=duration)])
    else:
        video = video.subclipped(0, duration)

    video = video.with_effects([vfx.Resize(height=1920)])
    w, h = video.size
    target_w = 1080
    if w > target_w:
        x_center = int(w / 2 - target_w / 2)
        video = video.cropped(x1=x_center, y1=0, width=target_w, height=1920)
    
    try:
        txt = TextClip(
            text=text,
            font=FONT_PATH,
            font_size=60,
            color='white',
            method='caption',
            size=(800, None),
            text_align="center",
            stroke_color='black',
            stroke_width=3
        )
        txt = txt.with_position('center').with_duration(duration)
        final = CompositeVideoClip([video, txt]).with_audio(audio)
        final.write_videofile(
            output_path, 
            fps=30, 
            codec="libx264", 
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a", 
            remove_temp=True,
            logger=None
        )
        print(f"\nУспішно! Відео збережено як: {output_path}")
        
    except Exception as e:
        print(f"\nПомилка монтажу: {e}")
    video.close()
    audio.close()

async def main():
    if not os.path.exists(BG_VIDEO):
        print(f"Помилка: Не знайдено файл {BG_VIDEO}. Будь ласка, додайте його в папку з програмою.")
        return

    text = get_text_from_file()
    tmp_audio = await create_voice(text)
    
    process_video(BG_VIDEO, tmp_audio, text, OUTPUT)
    
    if os.path.exists(tmp_audio):
        os.remove(tmp_audio)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nПрограма зупинена користувачем.")
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"\nКритична помилка: {e}")
    finally:
        print("Робота завершена.")