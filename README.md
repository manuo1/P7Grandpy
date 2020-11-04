# **GrandPy**

## DESCRIPTION

Grandpy est une application qui permet d&#39;obtenir des informations sur des lieux.

Il suffit de poser une question à Grandpy, quelle que soit la formulation si la question contient un lieu, Grandpy répondra en indiquant l&#39;adresse, une carte, une description et un lien vers la page Wikipédia.

## INSTALATION

Le programme a été développé en langage python dans un environnement virtuel et interagit avec les API de Google Maps et Media Wiki.

Pour le faire fonctionner vous devez :

**1. Installer :**

Python

pip

**2. Posséder une clé d&#39;identifiant Google Maps API**

Si vous n&#39;en possédez pas, voir ici : [cloud.google.com](https://cloud.google.com/)

**3. Renseigner la clé sur le fichier de configuration**

Ouvrez le fichier :

main\grandpy\data\_search\api\_config\prod\_google\_maps\_api\_key.yaml

Et remplacez :

&#39;your public api key&#39; **et**&#39;your private api key&#39;

Par votre clé Google (Les &#39; &#39; sont importants)

(Deux clés sont demandées, si vous voulez utiliser cette application en local vous n&#39;avez pas besoin de deux clés, il suffit de renseigner deux fois la même. Si vous souhaitez déployer cette application vous devrez posséder deux clés, la clé privée ne sera pas visible par les utilisateurs, mais la clé publique le serra. A vous de limiter l&#39;utilisation de celle-ci avec les restrictions proposées par le tableau de bord de la Google Cloud Plateform)

**4. Dans un terminal placer vous dans le fichier &#39;main&#39; et lancez l&#39;installation avec :**

pip install.r requirements.txt

**5. Lancez l&#39;application avec :**

python run.py

**6. Ouvrez votre navigateur internet et rendez-vous à l&#39;adresse :**

http://127.0.0.1:5000/

## **FONCTIONNEMENT**

Saisissez votre question dans la zone prévue à cet effet puis validez en appuyant sur Entrée ou en cliquant sur Envoyer.

## Grandpy est en ligne

Vous pouvez lui poser vos questions ici : [**Grandpy**](https://grandpy-mo1.herokuapp.com/)
