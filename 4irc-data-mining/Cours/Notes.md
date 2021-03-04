# Notes sur les différents cours de Data Mining

## Introduction

## Données ouvertes liées

> Utilisation des données de Wikidata.


Lancement en 2009.

Le *Linked Open Data* ou « données ouvertes liées » consiste à rendre libre de toute licence des bases de données préalablement liées entre elles selon le modèle du Linked Data de Tim Berners-Lee.
Le fait que les données soient libres permet leur accès et leur réutilisation sans aucune restriction.

Liens peuvent être des Relations entre les objets des bases de données. Liaison entre les différens concepts.

Avantages : Possibilités de récupérer toutes les données d'une database. Mais on peut également récupérer les données des autres sites web. On parle ici de database comme mySQL, PostgreSQL, des base de données **structurées**.

Extension à de nombreuses database de différents domaines.

Les données structurées sont donc des informations qui vont permettre, aux robots des différents moteurs de recherche, de mieux comprendre le contenu de votre site internet.

Wikidata -> strucuturée
Wikipédia -> non structurée

## Représentation , manipulation, prétraitements des données


#### 2.3.1.Propriétés ACID

- Atomicité: chaque transaction se fait au complet ou pas du tout.

- Cohérence: Tous les nœuds du système voient exactement les mêmes données au même moment.

- Isolation: Toute transaction doit apporter la base de données d'un état valide à un autre.

- Durabilité: Indépendamment des pertes de puissance, des plantages, une transaction une fois engagée
dans la base de données doit rester dans cet état.

Théorème CAP :
Coherence Availability Partitionning


Web crawlers : naviguer dans l'ensemble en utilisant des hyperliens


### Prétraitement des données

#### Nettoyage des données

**4.1.1 Erreurs de syntaxe**


**4.1.2 Erreurs sémantiques**

Définition :

Une erreur sémantique survient lorsque le programmeur conçoit mal son programme c'est une erreur liée au raisonnement du programmeur. On l'appelle aussi l'erreur de logique. Lors d'une erreur sémantique, le programme peut continuer de s'exécuter mais ne fournira pas le résultat souhaité.

**4.1.3 Erreurs de Couverture**

Données Exif : Métadonnées d'une image (ex : appareil, modèle, etc...)

Attention à ne pas avoir de valeurs manquantes pour le traitements des données.

**4.2.1. Traitement des erreurs syntaxiques**

Validation à l'aide d'un schéma (par exemple, XSD, JSONP)

XSD : https://www.w3schools.com/xml/schema_intro.asp

JSONP : https://www.w3schools.com/js/js_json_jsonp.asp

Transformation de données

**5.1 Langages de programmation**

