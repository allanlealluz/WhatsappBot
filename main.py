from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class Whatsappbot:
    def __init__(self):
        self.mensagem = "Mensagem feita a partir de um bot python"
        self.grupos = ['Grupo do role']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def EnviarMensagens(self):
        # <span dir = "auto" title = "Grupo do role" class ="_ccCW FqYAR i0jNr" > Grupo do role </span>
        # <div role="textbox" class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="9" dir="ltr" spellcheck="true"></div>
        # <div tabindex = "-1" class ="_1UWac _1LbR4" >
        # <span data - testid = "send" data - icon = "send" class ="" > < svg viewBox="0 0 24 24" width="24" height="24" class ="" >
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(35)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(10)
            grupo.click()
            chatbox = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(10)
            chatbox.click()
            chatbox.send_keys(self.mensagem)
            botao = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(10)
            botao.click()
            time.sleep(10)


bot = Whatsappbot()
bot.EnviarMensagens()
