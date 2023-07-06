import requests
from telebot.models import Telesettings

def send_telegram(tg_title,tg_author,tg_mail,tg_description):
    if Telesettings.objects.get(pk=1):
        settings = Telesettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and  text.find('}') and text.rfind('{') and  text.rfind('}'):

            text_slice ="Teма: " +tg_title+"\n"+"Автор: "+tg_author+"\n"+"E-mail: "+tg_mail+"\n"+tg_description
        else:
            text_slice = text

        try:
            reg = requests.post(method, data = {
                'chat_id' : chat_id,
                'text' : text_slice
            })
        except:
            pass

        finally:
            if reg.status_code != 200:
                print('Ошибка отправки')
            elif reg.status_code == 500:
                print('Ошибка 500')
            else:
                print('Все ОК. Сообщение отправлено!')


