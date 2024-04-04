import os

import sys

from ui import Ui
import driver


if __name__ == "__main__":
    # init()
    # instaLogin()
    # instaSend("dohwe song", "잘가나 ?")
    driver.setDriverPath("chromedriver")
    Ui()
    
    

    
class CustomDriver(webdriver.Chrome):
    def quit(self):
        
        # 원래의 quit 메서드 호출
        super().quit()
        
        # quit 메서드가 호출된 후 실행할 코드
        print("quit 메서드가 호출된 후 실행되는 코드입니다.")

