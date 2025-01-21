import json

# Cargar prefijos personalizados de servidores:
def get_prefix(message):
    with open("prefixes.json", "r") as f:
        new_prefix = json.load(f)

    print("pruebaaaa")

    return new_prefix[str(message.guild.id)]
