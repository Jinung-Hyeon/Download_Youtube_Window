import tkinter

from pytube import YouTube
from pytube.cli import on_progress
import os
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd


def clickEvent():
    # print(entry.get())
    # youtube_download(youtube_url_entry.get())
    text_widget.delete('1.0', 'end')

    if len(youtube_url_entry.get()) == 0:
        # print("문자열 입력하세요")
        mb.showinfo("URL을 입력하세요", "URL을 입력하세요.")
        return
    elif len(saveFilePath_entry.get()) == 0:
        mb.showinfo("저장경로를 입력하세요", "저장경로 입력하세요.")
        return

    try:
        # 저장 폴더 만들기
        save_folder = saveFilePath_entry.get()
        # save_folder = 'C:\YoutubeDownload'
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)
        else:
            pass

        # YouTube 객체 생성
        yt = YouTube(youtube_url_entry.get(), on_progress_callback=on_progress)
        # print(yt.streams) # streams 처리 전체 정보
        # print(f'영상 제목: {yt.title}')
        # print(f'영상 설명: {yt.description}')
        # print(f'영상 조회수: {yt.views}')
        # print(f'영상 길이: {yt.length} sec. [{str(yt.length // 60).zfill(2)}:{str(yt.length % 60).zfill(2)}]')
        # print(f'영상 평점: {yt.rating}')
        # print(f'영상 썸네일 링크: {yt.thumbnail_url}')
        # print(f'영상 나이 제한: {yt.age_restricted}')
        # print(f'영상 제작자: {yt.author}')
        # print(f'영상 채널 URL: {yt.channel_url}')
        # print(f'영상 아이디: {yt.video_id}')
        # print(f'영상 URL: {yt.watch_url}')
        # print(f'영상 게시 날짜: {yt.publish_date}')
        # print(f'영상 키워드: {yt.keywords}')

        text_widget.insert(tkinter.CURRENT, f'영상 제목 = {yt.title}\n')
        text_widget.insert(tkinter.CURRENT, '다운로드 완료!')

        # 영상 다운로드
        yt.streams.get_highest_resolution().download(save_folder)

        # print(f'\n\n유튜브 영상 "{yt.title}"\n다운로드 완료!')

    except AttributeError:
        youtube_url_entry.delete(0, 'end')
    except Exception as e:
        # print(e)
        # text_widget.insert(tkinter.CURRENT, f'에러가 발생 했습니다. {e}\n')
        mb.showerror("Error Message!!!", '잘못된 주소입니다. 다시 입력해 주세요.')
        # text_widget.delete('1.0', 'end')
        youtube_url_entry.delete(0, 'end')


def eraseUrl():
    # print('eraseUrl')
    text_widget.delete('1.0', 'end')
    youtube_url_entry.delete(0, 'end')


def closeEvent():
    # print('close')
    root.destroy()


def openSaveFilePath():
    dir_path = fd.askdirectory(parent=root, title='Please select a directory')
    # 기존에 입력 되어있던 저장겨로 지우기
    if len(saveFilePath_entry.get()) != 0:
        saveFilePath_entry.delete(0, 'end')

    saveFilePath_entry.insert(0, dir_path)


root = tk.Tk()

# 윈도우 창 제목
root.title('YouTube Downloader')
root.geometry('500x500')

# 창 크기 조절 가능 여부
root.resizable(False, False)

photo = tk.PhotoImage(file='save_photo.png').subsample(20)

# header_frame
header_frame = tk.Frame(root)
header_frame.pack(fill='both', expand=0, padx=15)

# Label
header_label = tk.Label(header_frame, text='유튜브 영상 다운로드 Mini-Program.', fg='blue', font=30)
header_label.pack(side='left')

# frame
frame = tk.LabelFrame(root, text='유튜브 URL 입력 후 \'추출 시작\' 버튼을 클릭하세요.', pady=20, padx=20)
frame.pack(fill='both', expand=0, padx=10, pady=10)

# url_label
fileSave_url_label = tk.Label(frame, text='저장 경로 : ')
fileSave_url_label.grid(row=0, column=0)

# entry
saveFilePath_entry = tk.Entry(frame, width=40)
saveFilePath_entry.grid(row=0, column=1)

# button
saveDirPath = tk.Button(frame, width=15, height=15, image=photo, command=openSaveFilePath)
saveDirPath.grid(row=0, column=2)

# url_label
url_label = tk.Label(frame, text='유튜브 URL : ')
url_label.grid(row=1, column=0)

# entry
youtube_url_entry = tk.Entry(frame, width=40)
youtube_url_entry.grid(row=1, column=1)

# frame
result_frame = tk.Frame(root)
result_frame.pack(fill='both', expand=0, padx=10)

# Text
text_widget = tk.Text(result_frame, width=80, height=12)
text_widget.pack()

# frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill='both', expand=0, padx=10)

# Button
close_button = tk.Button(bottom_frame, text='종료', command=closeEvent)
close_button.pack(side='right')

download_button = tk.Button(bottom_frame, text="추출 시작", command=clickEvent)
download_button.pack(side='right')

eraseUrl_button = tk.Button(bottom_frame, text="URL 지우기", command=eraseUrl)
eraseUrl_button.pack(side='right')

root.mainloop()
