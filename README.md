DESCRIPTION
============
Grandpy est une application qui permet d’obtenir des informations sur des lieux.
Il suffit de poser une question à Grandpy, quelle que soit la formulation si la question contient un lieu, Grandpy répondra en indiquant l’adresse, une carte, une description et un lien vers la page Wikipédia.

INSTALATION
============
Le programme a été développé en langage python dans un environnement virtuel et interagit avec les API de Google Maps et Media Wiki.

Pour le faire fonctionner vous devez :

	1. Installer:

		- Python
		- pip

	2. Posseder une clé d'identifiant Google Maps API

		Si vous n'en possédez pas, voir ici : [cloud.google.com](https://cloud.google.com/)

	3. Renseigner la clé sur le fichier de configuration

		Ouvrez le fichier :
			main\grandpy\data_search\api_config\prod_google_maps_api_key.yaml
		Et remplacez :
			'your public api key' __et__ 'your private api key'
		Par votre clé Google (Les ' ' sont importants)
		*(Deux clés sont demandées, si vous voulez utiliser cette application en
		local vous n’avez pas besoin de deux clés, il suffit de renseigner
		deux fois la même.
		Si vous souhaitez déployer cette application vous devrez posséder deux clés,
		la clé privée ne serra pas visible par les utilisateurs, mais la clé
		publique le serra. A vous de limiter l’utilisation de celle-ci avec les
		restrictions proposées par le tableau de bord de la
		Google Cloud Plateform)*


	4. Dans un terminal placer vous dans le fichier « main »
			et lancez l’installation avec :

		pip install.r requirements.txt

	5. Lancez l'application avec :

		python run.py

	6. Ouvrez votre navigateur internet et rendez vous à l'adresse :

		http://127.0.0.1:5000/

FONCTIONNEMENT
===============

	Saisissez votre question dans la zone prévue à cet effet puis validez
	en appuyant sur Entrée ou en cliquant sur Envoyer.
