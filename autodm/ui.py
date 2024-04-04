import tkinter as tk

import insta

button = None
button2 = None
text_area = None

class Ui:
    def __init__(self):
        global button
        global button2
        global text_area
        root = tk.Tk()
        root.title("Tkinter 기본 윈도우")
        # 버튼 추가
        button = tk.Button(root, text="인스타로그인", command=lambda: insta.instaLogin("dhn_kakao", "indhn^^4556", root))
        button.pack()

        button2 = tk.Button(root, text="인스타발송", command=lambda: send("insta"))
        button2.pack()
        root.after(0, lambda: button2.config(state=tk.DISABLED))

        text_area = tk.Text(root, height=10, width=50)
        text_area.pack()
        text_area.insert(tk.END, "여기에 텍스트를 입력하세요...")
        # GUI 실행
        root.mainloop()