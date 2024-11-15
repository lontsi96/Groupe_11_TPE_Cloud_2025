print ('bonjout')
15+18
print ('je ne comprends pas encore comment ca marche mais on est dans les essaies')
    #notre programme recupère un nom à l'entrée et renvoie en sortie une version encodé de ce nom dans un premier temps puis demande le nom codé d'un agent pour renvoyer la version claire de ce nom précédemment codé
#ici nous definissons la fonction d'encodage qui prend en entrée un nom clair "agent"
def encoder_nom(agent):
    agent_encode = ""
    for lettre in agent:
        if lettre.isalpha():
            decalage = 3
            if lettre.islower():
                nouveau_code = ord(lettre) + decalage
                if nouveau_code > ord('z'):
                    nouveau_code -= 26
            elif lettre.isupper():
                nouveau_code = ord(lettre) + decalage
                if nouveau_code > ord('Z'):
                    nouveau_code -= 26
            agent_encode += chr(nouveau_code)
        else:
            agent_encode += lettre
    return agent_encode
#ici nous definissons la fonction de décodage qui prend en entrée un nom encodé "agent_encodé"
def decoder_nom(agent_encode):
    agent_decode = ""
    for lettre in agent_encode:
        if lettre.isalpha():
            decalage = -3
            if lettre.islower():
                nouveau_code = ord(lettre) + decalage
                if nouveau_code < ord('a'):
                    nouveau_code += 26
            elif lettre.isupper():
                nouveau_code = ord(lettre) + decalage
                if nouveau_code < ord('A'):
                    nouveau_code += 26
            agent_decode += chr(nouveau_code)
        else:
            agent_decode += lettre
    return agent_decode
# nous définissons maintenant nos variables et réalisons les appels des fonctions définies précédemments pour
#encoder encodé un nom fournit en entré puis, demander la version codé de nom pour le décoder
nom_agent = input("Entrez le nom de l'agent secret : ")
nom_encodé = encoder_nom(nom_agent)
print("Nom encodé de l'agent secret :", nom_encodé)

nom_encodé_input = input("Entrez le nom encodé de l'agent secret : ")
nom_décodé = decoder_nom(nom_encodé_input)
print("Nom décodé de l'agent secret :", nom_décodé)

#NB: notre programme ne prends pas en charge les lettres accentuée ou ne pourra pas correctement decoder le nom fournit avec des accents