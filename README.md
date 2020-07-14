# Targeting with Partial Incentives

Lo spreading attraverso la rete riflette la situazione in cui i comportamenti si trasmettono a cascata da un nodo ad un altro come una epidemia. È un processo per il quale un pezzo di informazione viene diffuso e raggiunge gli individui attraverso le interazioni che esistono tra di loro. Questo processo viene definito formalmente come *Network Cascade*. Esso si occupa del contagio che si diffonde lungo gli archi della rete. I modelli per il Network Cascade permettono di comprendere la diffusione, all'interno di una rete, di informazioni/epidemie. L'obiettivo è cercare di capire cosa può causare e come può avvenire la massimizzazione all'interno della rete, ovvero di selezionare un seed set di taglia minima iniziale così da garantire l'influenza del maggior numero di nodi all'interno della rete. Questo lavoro è stato effettuato da Kempe e Kleinberg nel 2003. 
In questo contesto risulta fondamentale l'identificazione di quei clienti con una maggiore influenza sul mercato per attirare un gran numero di acquirenti. Essi risulterebbero utili a convincere tutti gli altri nodi all'interno della rete, come gli influencer su Instagram. Quindi tramite incentivi, si può convincere un insieme di persone influenti che possono consigliare un prodotto per contribuire alla sua diffusione.
Uno degli algoritmi pensato a tale scopo è il **Targeting with Partial Incentives** (TPI).

L'algoritmo TPI rappresenta una evoluzione dell'algoritmo di *Target Set Selection*, la cui idea alla base prevede l'assegnazione di incentivi ai nodi. Un'assegnazione di *incentivi parziali* ai vertici di una rete *G=(V,E)* con *V={v<sub>1</sub>,...,v<sub>n</sub>* è un vettore *S=(s(v<sub>1</sub>),...,s(v<sub>n</sub>))*, dove *s(v) ∈ {0,1,2,...}* rappresenta la quantità di influenza che inizialmente applichiamo su *v ∈ V*.
Formalmente è definito come segue:
- **Istanza**, una rete *G=(V,E)* con una funzione di soglie *t:V → N*.
- **Problema**, trovare un target vector *s* che minimizza *C(S)=Σ<sub>v ∈ V</sub>s(v)*.
L'algoritmo utilizzato per il calcolo degli incentivi è descritto nell'articolo "Whom to befriend to influence people". 

Per i dettagli sull'implementazione si può visitare il notebook al seguente <a href="https://github.com/fscavone1/TPI-Algorithm/blob/master/documentation.ipynb">link</a>.

## Authors
***Francesca Scavone***, ***Catello Graziuso***, ***Francesco Marzullo*** realizzato per il corso magistrale Reti Sociali dell'anno 2019/2020 presso l'Università degli Studi di Salerno.
