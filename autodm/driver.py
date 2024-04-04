import os
import sys
import threading
import time

driver = None
driver_path = None



def setDriverPath(driverName):
    if getattr(sys, 'frozen', False):
        # 패키징된 실행 파일의 경우: _MEIPASS를 사용
        current_dir = sys._MEIPASS
    else:
        # 일반 Python 스크립트의 경우: __file__을 사용
        current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, 'drivers', driverName + '.exe').replace("\\", "\\\\")

class BrowserMonitor(threading.Thread):
    def __init__(self, driver):
        threading.Thread.__init__(self)
        self.driver = driver
        self.is_browser_closed = False

    def run(self):
        while not self.is_browser_closed:
            try:
                _ = self.driver.title
            except WebDriverException:
                root.after(0, lambda: button.config(state=tk.NORMAL))
                root.after(0, lambda: button2.config(state=tk.DISABLED))
                self.is_browser_closed = True
            time.sleep(1)