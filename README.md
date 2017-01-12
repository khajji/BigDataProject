BigDataProject
==============

Submetrics is a TV-Shows content-based recommender system ! What does that mean ?
In a first step this tool analyzes subtitles of hundreds of TV-shows according to certain topics. Based on this analysis, it produces for each TV-show a distribution over the topics. For example, if we consider the show Homeland, the resulting distribution is :

44% (Counter)-terrorism
12% Politics
12% Relationship
10% British
8% Army
...
We call this distribution a feature vector. 

In a second step, Submetrics acts as recommender system. Based on a TV-show you like, it recommends you shows that have the most similar features. Handy, right ? 
The distribution over the topics, that is the so called features, are obtained by a Java M/R implementation of the LDA algorithm. Here is the current version of the graph representing clusters of similar shows and some labelled topics we identified in them : 

![alt tag](http://www.submetrics.org/img/showsclusters.jpg)

The goal of the project is to analyze the content of TV-Shows according to certain topics, via a subtitles analysis. In order to achieve that, we acquired a large data set of subtitles of good quality (~1100 shows) and then, using an hadoop implementation of the LDA algorithm, analyze the topics present in each show.
As a result, we have differents things :
For each TV-show, we have a detailed information page that contains the topic composition.
A content-based recommender systems for TV-shows, where given one TV-show, the system can propose the most similar TV-shows to the latter.

This project was conducted in the scope of the Big Data course at Ecole Polytechnique Federale de Lausanne (EPFL). 
The tool and website are currently in an early stage so stay tuned ! 

Thank you for your interest,

the Submetrics team
Nils Bouchardon Nassim Drissi El Kamili Simon-Pierre Genot Khalil Hajji Claire Musso Gregory Rozhdestvenskiy Florian Simond Raphael von Aarburg
