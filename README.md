## Rapport

### Componenten van de oplossing

1. **GitHub Actions:** GitHub Actions is een CI/CD-service die gebruikt wordt voor het automatiseren van workflows binnen de repository.
   Het voert taken uit zoals het testen van de code bij elke push en pull request en het deployen van de applicatie naar de server.
   Door workflows te definiëren in YAML-bestanden kunnen verschillende stappen, zoals het installeren van dependencies en het uitvoeren van tests, automatisch worden uitgevoerd.

2. **Flask:** Flask is een micro web framework in Python dat gebruikt wordt om de webapplicatie te maken.
   Het biedt een eenvoudig, maar krachtig, platform voor het beheren van routes en het serveren van webinhoud naar gebruikers.
   In dit project wordt Flask gebruikt om een eenvoudige webpagina weer te geven die een Triforce ASCII-art toont.

3. **Digital Ocean en SSH:** Digital Ocean is de cloud service provider die wordt gebruikt om de applicatie te hosten.
   SSH (Secure Shell) wordt gebruikt om veilige verbindingen op te zetten tussen de GitHub Actions en de server.
   Dit maakt het mogelijk om bestanden veilig te synchroniseren en de applicatie op afstand te beheren en te herstarten.

Deze componenten werken samen om een volledige CI/CD pipeline te vormen: GitHub Actions zorgt voor de automatisering van de workflows, 
Flask biedt de webapplicatie, en Digital Ocean en SSH zorgen voor de hosting en veilige toegang.

### Problemen en oplossingen

1. **Probleem:** Het opzetten van de juiste GitHub Actions workflow configuratie voor het testen en deployen.
   
   **Oplossing:** Door de documentatie van GitHub Actions te volgen en verschillende voorbeelden te bekijken,
   heb ik een workflow samengesteld die de applicatie test en vervolgens deployt bij succesvolle tests.
   Dit omvatte het definiëren van jobs en stappen voor het installeren van dependencies en het uitvoeren van tests.

2. **Probleem:** Het correct installeren van dependencies en tools zoals `doctl` binnen de GitHub Actions runner.
   
   **Oplossing:** Ik heb de juiste commando's toegevoegd om `doctl` te downloaden en te installeren, en om ervoor te zorgen dat Python en de vereiste pakketten correct worden geïnstalleerd.
   Hierdoor konden de workflows zonder fouten worden uitgevoerd.

3. **Probleem:** Het configureren van SSH-toegang om bestanden veilig naar de Digital Ocean server te kopiëren.
   
   **Oplossing:** Het gebruik van de `webfactory/ssh-agent` actie om de SSH-sleutel te beheren en het toevoegen van de server aan `known_hosts` om verbindingsproblemen te voorkomen.
   Dit zorgde ervoor dat de server betrouwbaar kon worden benaderd voor het synchroniseren van bestanden en het herstarten van de applicatie.

### Opmerkingen

Het opzetten van een volledige CI/CD pipeline kan complex lijken, maar door de stappen op te splitsen en zorgvuldig te testen, werd het proces beheersbaar. 
Het was leerzaam om verschillende technologieën samen te brengen om een geautomatiseerde deployment op te zetten. 
Het gebruik van GitHub Actions, in combinatie met Flask en Digital Ocean, demonstreert een krachtig en efficiënt ontwikkelingsproces.
