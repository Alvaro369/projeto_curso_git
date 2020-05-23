from selenium import webdriver
import time


class WatsappBot:
    def _init_(self):
        self.mensagem = "este e um robo criado por Alvro Ramos"
        self.grupos = ["Dev react"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang-pt-br')        
        self.driver = webdriver.Chrome(executable_path=r'./chrmedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="Dev react " class="_19RFN _1ovWX _F7Vk">Dev react </span>
        #<div tabindex="-1" class="_3FeAD _1PRhq">
        #<span data-icon="send" class="">
        driver = webdriver.Chrome()
        driver.get('http://web.whatsapp.com')
        #self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)
        for grupo in self.grupos:
            grupo= self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(1)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3FeAD _1PRhq')
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon'send']")
            time.sleep(1)
            botao_enviar.click()
            time.sleep(3)

bot = WatsappBot()
bot.EnviarMensagens()