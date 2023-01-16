from pymino import *
from pymino.ext import *
import aminofix
from time import sleep

client = aminofix.Client()

bot = Bot(
    command_prefix="!",
    community_id = "24821733"
)  

email = input("Email: ")
password = input("Password: ")

@bot.on_ready()
def ready():
     print(f"{bot.profile.nickname} acaba de iniciar sesion!")



@bot.on_error()
def error(error: Exception):
     print(f"An error has occurred: {error}")
bot.run(email, password)
client.login(email,password)

clients = client.sub_clients(size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community: "))-1]

def remover():
    for i in range(0, 1000, 100):
        users= bot.community.fetch_following(userId = bot.profile.userId,start=i, size = 100, comId =  communityid)._data
        print(users)
        if users:
            for user in users:
                usuario = user['uid']
                print(usuario)
                try:
                    bot.community.unfollow(userId= usuario, comId = communityid)
                    print(usuario, " removido")
                except Exception as e:
                    print(e)
                    print(usuario, " no se pudo dejar de seguir, esperando 3 segundos")
                    sleep(3)
        else:
            print("Todos los usuarios fueron removidos")
            break;
remover()