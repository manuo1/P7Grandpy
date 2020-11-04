INTRO_MAX_SIZE = 500
"""
##############################################################################
below, the introductory messages of each part of grandpy's answer
##############################################################################
"""
INTRO_NAME = [
    "<br>OK, Tu veux des infos sur cet endroit:<br>",
    "<br>Je vois, je connais bien cet endroit :<br>",
]
INTRO_ADDRESS = [
    "<br>Alors je te donne déjà l’adresse :<br>",
    "<br>Cela se situe à l’adresse suivante :<br>",
]
INTRO_MAP = [
    "<br>Si tu ne situes pas, regarde la carte :<br>",
    "<br>Je peux te montrer sur une carte :<br>",
    "<br>Jette un œil sur la carte pour te repérer:<br>",
]
INTRO_DESCRIPTION = [
    "<br>J’avais discuté avec un riverain avant la visite, sais-tu que ",
    "<br>Quand j’y étais le guide m’avait expliqué que ",
    "<br>C’est un super endroit à l’école on m’avais dit que ",
    "<br>Mamie y est allée elle m’a raconté que ",
]
"""
##############################################################################
below, the answers in case of problems
##############################################################################
"""
ANSWER_TO_PROBLEM = {
    'blank_new_user_message': 'ANWS_BLANK',
    'nonallowed_characters': 'ANWS_NONALLOWED',
    'cant_find_location': 'ANWS_CANT_FIND',
}
ANWS_BLANK = [
    "Parle plus fort, je ne t’entends pas.",
    "Essaye avec des mots, je ne lis pas dans les pensées.",
    "Il ne manque pas quelque chose ?",
    "Attend, je mets de lunettes mais je ne vois rien.",
]
ANWS_CANT_FIND = [
    "Ça me dit quelque chose mais pas moyen de me souvenir",
    "Tu es certain que cet endroit existe ? Jamais entendu parler.",
]
ANWS_NONALLOWED = [
    "Petit chenapan ! Tu ne devrais pas utiliser ces caractères !",
    "Allé, on va dire que tu n’as pas fait exprès d’utiliser ces caractères…",
]
