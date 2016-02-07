![http://pastiche.info/images/pastiche_128.png](http://pastiche.info/images/pastiche_128.png)

# introduction #

The **pastiche** software framework is an enabler for a broad class of applications where rules of behaviour are modelled for a multitude of asynchronous cooperative entities (known as agents).

Some applications of **pastiche** will be demonstrated at [pastiche.info](http://pastiche.info).

# scenarios #

## info navigation, organisation ##

  * metadada: info **search**/browse
  * mind mapper, semantic idea network
  * Mediashelf
  * photo/music collection sharing
  * story maker: take two or three unrelated terms and try to find a link between them (transitive closure, convex hull, shortest path, ...)

## games ##

  * chess: simultaneous game, strategy builder, collaborative planning
  * puzzle
  * **game**: compete, collaborate, grow, local views on the world
  * Catan
  * Tantrix

## architecture ##

  * urban planning, liquid architecture
  * areas (e.g. shopping, travel, production) and resources, supply/demand

## misc ##

  * collage
  * fragments
  * interactive painting, tablet
  * box world, 3 dof
  * oss, patents
  * dynamic typography: zin-builder (sinnbilder)
  * arty-ficial intelligence
  * [Poème Electronique am Tesla](http://www.tesla-berlin.de/_page.php?aktion=SHOW_PAGE&Page_ID=177)

# mechanisms #

  * state/behaviour
  * structure vs. event (Lévi-Strauss)
  * work (of art), program code vs. process, interaction
  * mobile architecture, mobile agents
  * motion: 6dof motion, rotation, size, shape, sound, colour
  * soa, ajax
  * force fields
  * traces, curiosity, snails, trails
  * history, context
  * mas, fipa, jade, searle (speech acts), dennett (intentional stance)
  * geo-info, context, sensors/actuators/effectors
  * GoogleMap-mash-ups, [GoogleMapsMania](http://googlemapsmania.blogspot.com/), [Nederkaart](http://www.nederkaart.nl/)
  * reasoning, 3apl, prolog
  * visual programming
  * w3c, semweb, rdf, owl
  * libraries: rdflib, pyparsing, karrigell
  * jazz, improvisation
  * interference, doppler sound fields
  * self-organisation
  * distributed reasoning, decision-making
  * emergence
  * just-in-time
  * viewpoint engineering
  * self-configuring, self-repairing, autonomic
  * bricoleur, diy, MAKE, oss
  * [deixis](http://en.wikipedia.org/wiki/Deixis)

# sources of inspiration #

  * technology
  * architecture
  * philosophy
  * arts
    * literature
    * music
    * visual
    * digital, interactive performance
  * sociology, social psychology

  * duchamp, ready-mades
  * Schwitters, Merz-Bau
  * Xenakis
  * Le Corbusier: poème électronique, promenade architecturale, musée à croissance illimitée
  * Gehry
  * Hadid
    * http://www.arcspace.com/architects/hadid/kartal_pendik/kp.html
    * http://www.arcspace.com/architects/hadid/cagliari/cagliari.html
  * Coop Himmelb(l)au
  * OMA: Bordeaux
  * Novak
  * Oosterhuis
  * Superstudio
  * Szeemann: Junggesellenmaschinen
  * Tinguely
  * dada, arp
  * vian
  * gainsbourg
  * sartre: l'être et le néant
  * moholy-nagy
  * lissitzky
  * derrida: deconstruction, différance
  * Kafka: Schloss, Strafkolonie
  * Axelrod: collaboration, competition, PIPD

# experiments #

tbd. [pastiche.info](http://pastiche.info)

# implementation #

  * App/Platform --> Container (Borg)
  * Agency(Agent): control groups of agents, forward messages
  * pastiche as karrigell service
  * p2p vs. server-based
  * mobility, ad-hoc networks, Pyro or Web Services???
  * leasing of AMS registration
  * [django](http://djangoproject/)
  * [dojo](http://dojotoolkit.org/)
  * [rdflib](http://rdflib.net/)

![http://pastiche.googlecode.com/files/python-logo.gif](http://pastiche.googlecode.com/files/python-logo.gif)

# more #

## Emergence and Norms ##
In a Multi-Agent System (MAS) the fundmamental design involves modelling
the behaviour of agents and their interactions. These will lead to
system behaviour that is not explicitly specified, but which emerges as
a result of interacting autonomous entities. This is what we refer to as
emergent behaviour.
As difficult as this is - if we achieve emergent behaviour by specifying
the basic rules that lead to proper interaction - there is a problem
with the limitations. Interaction may lead to emergent behaviour that
goes beyond the desired effects. In such a case it is necessary to take
care for a system to not only enable, but also limit emergent behaviour.
In order to achieve this, we could make use of norms that are applied to
all interaction within the given system. Norms are specified for a
certain society of agents and applied locally for each interaction among
agents. How do norms need to be defined? Who takes care of enforcing
them? What is a good example to experiment with this phenomenon?
There are more interesting questions related to this topic, such as the
formation of clans, the need for cultural awareness [1](1.md) and the
emergence of bricolage (structure/events) [2](2.md).
[1](1.md)
http://home.hccnet.nl/a.meyer/understandingemergenceinmedia/index.html#62
[2](2.md)
http://home.hccnet.nl/a.meyer/understandingemergenceinmedia/index.html#63

## Gaming, Training and Simulation ##
The traditional boundaries between gaming, training and simulation
systems are disappearing as a result of advances in commodity technology
and convergence of home and professional use. The processing power of
standard computers increases rapidly while the cost of high-end
graphical capacity decreases. The same tools can be used to program
these components for creating virtual worlds for specific purposes in
games, training and simulation. All three domains are increasingly using
networked infrastructures, the main difference that remains is the goal
to which they tools are applied. The same environment can server
multiple goals. For example, gamers can enjoy playing a scenario that
can be used to train professionals by providing feedback on their
performance. Some commercial games are already by the army to train
combattants and more are being developed in cooperation of military and
games experts. Games and training applications need more realistic
behaviour of artificial actors. This behaviour can be explored in
simulations for various purposes.
At the moment, TNO and the University of Utrecht are setting up a Centre
for Advanved Gaming and Simulation (AGS).

## Self-Organising Traffic Management ##
Today, traffic is managed centrally from traffic management centres. As
we know these centres cannot handle the problem appropriately. On the
one hand, there is too much information for a central authority to
handle and a global solution cannot be found. On the other hand, there
is not enough information about the goals of individual traffic subjects
and they change plans dynamically. Another problem is that central
planning imposes artificial boundaries on traffic that do not exist in
reality (e.g., at national borders or between highway and city traffic).
Dynamic decentralised traffic management could improve on all these
issues elegantly.
In Delft, the Netherlands Research School for TRAnsport, Infrastructure
and Logistics (TRAIL, http://www.rstrail.nl/) is seeking solutions for
the problems mentioned above. Several PhD students of TRAIL have been
coached by TNO.
Within the ICIS project at DECIS Lab (http://www.decis.nl/) traffic
management is an important topic in the context of crisis management.
Screenshots from a simple first demo are attached. They show emergent
behaviour of (not yet very) intelligent cars.

## Cooperation Models ##
Cooperation among autonomous entities (aka agents) can take various
forms. There are quite a few interaction protocols that have been
standardised (e.g., FIPA: http://www.fipa.org/repository/ips.php3).
Protocols are useful, but they are not sufficient to understand or model
the purpose for which they may be used. A fundamental issue in
cooperation is the distinction in collaborative versus competitive
behaviour. Both models are used in various contexts, but it is not clear
which is better for which situation and why. Simulation and validation
of these models could help to understand their contexts of use.

## Adaptive Decision Support ##
(Decision) support systems are built to support human operators in their
task performance by providing them with real-time appropriate
information in an easy-to-understand format. Their goal is to make
operators more efficient and effective. However, most such systems are
rather static and do not adapt to critical situations - exactly when
they would be most necessary. Also, the filtering of information is a
critical task that current systems mostly try to avoid. This results in
information overload for the operators. Adaptive support systems should
take the context into account with respect to information, time,
individual and social situation. User and information agents need to
collaborate closely and take decisions together, depending on
information timeliness and operator availablity, among others. The
interaction among operators can affect their performance, as well.

## Dynamic Task Allocation ##
We like to think of hybrid communities of actors. Actors may be of
organic or synthetic nature. Organic actors include human beings and
animals, synthetic actors include software agents and robots. In a
hybrid community the various kinds of actors need to cooperate to
achieve individual or social goals. They need to allocate tasks among
each other. The task allocation process is expected to be performed
collaboratively and dynamically, i.e. by several actors together and
depending on a current task at hand. This requires a good understanding
of the properties and capabilities of different actors and means for
them to communicate effectively.

## Peer 2 Peer Networks ##
In peer-to-peer networks (p2p) the members of such a network are in
direct contact without relying on any central server (except for
mediation, but ideally this needs not be the case, either). The
challenge is to find matching pairs or groups of network members that
share a certain interest. This should happen dynamically because each
member can have different interests and roles at different times. The
idea to follow is that it might be a good idea to make use of
recommendations of other known members. It should be possible to reach
any candidate member of an interest group with six links at most. Issues
in a recommendation-based mediator include trust, efficiency and
completeness.

## Collaborative Reasoning and Decision Making ##
In a multi-agent system each agent has an individual view on the world
based on subjective knowledge (beliefs) that is by nature incomplete. As
a society of agents tries to perform tasks collaboratively the agents
need to exchange information and viewpoints. The purpose of this process
is to come to a shared decision and it involves precedures for making
commitments, establishing trust realtionships, making concessions
concessions and reasoning about long-term benefits, among others. The
goal would be to define interaction protocols and reasoning procedures
that allow for collaborative reasoning and decision making under the
assumptions mentioned above.

## Hunters and Gatherers ##
The goal of this initiative was to experiment with the emergence of
social complexity by starting at the beginning: primitive man. Trying to
find the simple basic rules that drive primitive man would enable us to
understand how more complex social behaviour could emerge. This idea is
based on a paper by Jim Doran (www.davidhales.com/hugs). We still need
to find some source of funding for this experiment and probably some
input from an anthropologist would be enlightening.

## Fishermen's Friends ##
I must admit that I forgot what the point was of your study of the
fishermen of Katwijk. What is the question and what was the answer? Can
we simulate the processes you found?

## Crowd and Riot Control, Evacuation ##
In this TNO project we collaborate with social psychologists to create a
simulation of group behaviour. The scenario deals with evacuation in a
tunnel accident (car on fire). Another scenario that is planned to be
implemented later on is about crowd and riot control: hooligans and
their actions in relation to police presence. These simluators should
lead to a platform for simulation human behaviour in situations of
Fight, Fright and Flight (FFFSim).

## Computer Art ##
The visualisation of emergence patterns of social behaviour could
generate works of art of a new kind. What would this look like?
Interaction with viewers would be extremely interesting to look at. Any
ideas?

## Cybersex ##
Grapje! Maybe not. When looking at the relations between humans and
machines the mechanics of the reproductive act is often seen as a
central theme. Look at Junggesellenmaschinen
(http://www.art-service.de/article/junggesellenmaschinen_asthetik_und_naturwissenschaften_medie.html,

http://www.perlentaucher.de/buch/3308.html).

Can we use any of these ideas and apply them to crisis management,
military decision making and network-centric warfare (NCW)? The trend in
the defense world is to move power to the edge
(http://www.dodccrp.org/publications/pdf/Alberts_Power.pdf), i.e. shift
responsibility to the lowest possible instance that can deal with it.
This strategy fits very well with decentralised multi-agent systems.

BDI model for reasoning. BDI stands for
beliefs. desires and intentions
(http://citeseer.ist.psu.edu/122564.html,
http://www.cs.umbc.edu/courses/graduate/691m/spring03/papers/georgeff.pdf).
Does this make any sense to an anthropologist? We are working with the
University of Utrecht on the implemenation of a programming language for
this model: 3APL, http://www.cs.uu.nl/3apl/. Please, have a look at the
deliberation loop of the 3APL interpreter,
http://www.cs.uu.nl/3apl/deliberationloop.html.
This implementation is becoming part of my open source agent platform
spyse (http://spyse.sf.net/).

How could we define our roles? My idea is that you come up with
realistic questions and problem definitions. I could work on a
simulation based on these questions. Together we would need to validate
the results of the simulation (or game) with respect to the problem. Can
we find customers who are interested in funding such activities? Can we
write a paper together? Maybe something to submit to JASSS
(http://jasss.soc.surrey.ac.uk/JASSS.html).