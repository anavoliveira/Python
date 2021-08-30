import json

texto = """
{
    "user": "ASD134HFT75U86IOS94UF:anavictoriaavos@itau-unibanco.com.br",
    "accontId": 90,
    "filmes_preferidos": [ "Pulp Fiction", "Clube da Luta" ],
    "contatos": {
        "telefone": "(11) 91111-2222",
        "emails": [ "fulano@gmail.com", "fulano@yahoo.com" ]
    }
}
"""

obj = json.loads(texto)


user = obj["user"]
user = user.split(':',2)
email= user[1].split('@',2)
name= email[0]
print("Usuario:  " + name)
#email = email.split('@',2)
