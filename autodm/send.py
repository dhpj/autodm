import ui
import insta

def getMsg():
    # text_area의 현재 텍스트를 가져와서 출력
    msg = ui.text_area.get("1.0", tk.END)
    return msg

def extractLines(msg):
    
    lines = msg.split('\n')
    
    lines = [line for line in lines if line.strip() != '']

    # 결과 확인을 위한 출력
    return lines



def send(flat):
    msg = extractLines(ui.getMsg())

    if flat == "insta":
        instaId = ["dohwe song"]
        for Id in instaId:
            insta.instaSend(Id, msg)