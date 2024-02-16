## Closed answer questions

###### Question 1
Alice wants to open a communication channel with Bob.
Which of the following security properties she must implement in order to check that she is really communicating with Bob?
- [ ] A. non-repudiation
- [ ] B. integrity
- [ ] C. availability
- [x] D. peer authentication
- [ ] E. data authentication
- [ ] F. privacy
- [ ] G. accountability
###### Question 2 
Assume Alice sends a message to Bob. Bob knows that he has to perform data authentication. 
What does it mean?:
- [ ] Bob must register the received data in a database
- [ ] Bob must identify Alice (e.g. check her identity card)
- [x] Bob must verify that the data really comes from Alice (for example, by verifying some sort of evidence attached to the data that only Alice may have created)
- [ ] Bob must demonstrate his identity to Alice
###### Question 3
Assume Alice wants to connect to two systems run by Bob.
Alice and Bob must always perform the mutual authentication. What does it mean?
- [x] Alice authenticates to every system run by Bob and each of the two systems of Bob authenticate to Alice
- [ ] Bob authenticates to Alice
- [ ] Alice authenticates to the two systems run by Bob
- [ ] each of the two systems of Bob authenticate to Alice
- [ ] Alice and Bob must identify themselves, e.g. by exchanging their identity cards
###### Question 4 
Assume Alice is entering a password (or a PIN) to access her smartphone. Which security property is implemented by her smartphone for this operation?
- [ ] confidentiality
- [ ] integrity
- [x] authentication
- [ ] availability
- [ ] authorization
###### Question 5
In Windows OS there are two types of users: normal and administrator. Assume a normal user tries to install a program and this operation is denied by the OS.
Which security property the OS has implemented for software installation operation? (we assume the user has already logged in successfully with his credentials):
- [ ] authentication
- [x] authorization
- [ ] traceability
- [ ] availability
###### Question 6
Alice writes some data on her disk. The disk is placed in a secure place. After some time she wants to check whether the data has been modified. Which security property does she have to implement?
- [ ] authentication
- [ ] authorization
- [ ] traceability
- [x] integrity
- [ ] availability
###### Question 7
Alice wants to protect the entrance in a building with a card reader. Which security property/properties must implement the card reader placed at the entrance?
- [x] A. authentication
- [x]  B. authorization
- [ ]  C. non-repudiation
- [ ]  D. integrity
### Basic security attacks
###### Question 1
What is a replay attack?
- [x] A. an attack in which some data (in clear or protected for confidentiality) can be intercepted and then sent more than once to the destination
- [ ] an attack in which only data in clear can be intercepted and then sent more than once to the destination
- [ ] C. an attack in which an attacker intercepts the data, then sends it to another attacker who will send it to the destination
###### Question 2
What is a sniffing attack?
- [x] an attack in which data (in clear or protected) is intercepted while in transmission
- [ ] an attack in which only data in clear can be intercepted
- [ ] an attack in which an attacker intercepts the data, then modifies it, then finally sends it to the destination
###### Question 3
What is an IP spoofing attack?
- [ ] an attack in which the attacker creates fake date and inserts it into a connection
- [x] an attack in which an attacker modifies the IP source address and sends it to a destination
- [ ] an attack in which an attacker modifies the IP destination address and sends it to the destination
- [ ] an attack in which an attacker modifies both the source and the destination addresses in an IP packet
###### Question 4
What kind of countermeasures are applicable for an IP spoofing attack aimed to gain unauthorised access to a remote resource?
- [ ] A. instruct the browser's users to carefully check the URL they are connecting to
- [ ] avoid the use of broadcast networks
- [x] avoid the use of the IP address as "credential" to authenticate and get access to any remote resources
- [ ] install (and regularly update) an anti-malware application on each device
###### Question 5
What is a Denial of Service attack?
- [x] an attack in which the attacker keeps a host busy by exhausting its resources (e.g. mail) so that it cannot provide its services
- [x] an attack in which the attacker keeps a host busy by flooding it with traffic (e.g. DNS or ICMP) so that it cannot provide its services
- [x] an attack in which an attacker keeps a host busy by exhausting its resources (e.g. by injecting a malware that makes continuous calculations) so that to block the use of the host
- [ ] an attack in which an attacker denies the use of a host to a user because he/she is not authorized
###### Question 6
What is Distributed Denial of Service (DOS) attack?
- [x] attack in which the attacker (master) exploits multiple daemons installed on compromised nodes to run (upon  command) a software implementing the DOS attack against one victim
- [ ] attack in which an attacker (master) distributes the DOS software to multiple nodes that run independently the attack against different victims
- [ ] attack in which attackers (masters) collaborate and decide along with the zombies which type of DOS attack to run
###### Question 7
Bob is an attacker who decides to activate a shadow server to attack Alice. What kind of attacks can he perform against Alice (to provoke damage)
- [ ] replay attack
- [x] Denial of Service
- [x] redirect Alice to fake web sites
- [ ] packet sniffing
###### Question 8 
Alice wants to communicate securely with Bob (server).
What kind of security properties must she implement to protect from Man in the Middle attack? Note: we assume Alice and Bob have trusted devices and software
- [ ] server authentication, data authentication, confidentiality of the data exchanged, integrity of the data exchanged
- [ ] server authentication, confidentiality of the data exchanged, integrity of the data exchanged, serialization of each packet
- [x] server authentication, data authentication, confidentiality of the data exchanged, integrity of the data exchanged, and serialization of each packet
- [ ] privacy of the data exchanged, server authentication, data authentication, integrity of the data exchanged, serialization of each packet
###### Question 9
In risk analysis, assets are:
- [ ] any ICT resource, data, and people present or working inside a company
- [ ] any ICT resource, data, and people used for providing a service
- [ ] the ICT resources, data, people, and location used in providing a specific service
- [x] the ICT resources, data, people, and location used in providing the services offered by the company
###### Question 10
In risk analysis, vulnerabilities are:
- [ ] weaknesses in the software that could be exploited by an attacker
- [ ] weaknesses in the design, implementation, configuration and management that could be exploited by an attacker
- [ ] actions an attacker performs to damage an asset
- [x] weaknesses in the design, implementation, configuration and management that could harm assets if exploited by an attacker or by occurrence of unintentional events (natural disasters, mistakes performed by individuals)
###### Question 11
In risk analysis, a security control is:
- [x] a set of operational and management processes, and security mechanisms (including software techniques, algorithms and protocols) used to protect against threats
- [ ] functional and non-functional requirements that need to be satisfied in order to achieve security
- [x] a set of operational and management processes, and security mechanisms (including software techniques, algorithms and protocols) adopted to reduce risks
###### Question 12
In risk analysis, a risk is:
- [x] a qualitative (e.g., low, medium, high, very high) or quantitative (e.g. 10, 15, 25) value calculated based on the impact and the probability of occurrence of a security event
- [ ] a cost calculated based on the countermeasures to be selected and implemented to protect against a security event
- [ ] possible deliberate action/accidental event that can produce the loss of a security property
###### Question 13
What are the security controls and procedures?
- [x] documents expressing 'how' you implement the policies, both for the technical details (such as specific techniques, algorithms used) and organizational details
- [ ] documents expressing the vulnerabilities of a system or product
- [ ] documents expressing the flaws in the implementation of a system of product
###### Question 14
Which of the following is **not** a purpose of doing a risk analysis?
- [x] delegate responsibility
- [ ]  quantify impact of potential threats
- [ ]  identify risks
- [ ]  define the balance between the impact of a risk and the cost of the necessary countermeasure
## Open Answer questions
### Talk about sniffing, spoofing and hijacking attacks and describe the appropriate security measures
Sniffing is a cyber attacks in which an attacker tries to get private information transmitted in clear, like some credentials, listening to the packets, usually level 3 but also level 2, that travels in some connection on the network.
Sniffing can be made unfeasible if the communication is encrypted with a strong enough encryption schema.

Spoofing refers to an attack in which the attackers fakes its address. Usually level 3 address are faked but level 2 ones can be spoofed too.
Implementing authN mechanisms and avoiding address based ones are good countermeasures. 

Hijacking  refers to an attack in which the attackers tries to take control of some connection over the network, to insert, modify or delete traffic by altering the routing path.
To counter it, usually are required confidentiality, authN, integrity and serialization mechanisms of each individual packet.
###  Explain what social engineering is, give an example of this attack, indicate the countermeasures that a company can take to defend itself.
Social engineering is an attacks in which the attacker tries to exploit some psychological weakness of the victim to get some information or to do something.

A good example is phishing, which is an attack in which the attacker sends a fake text to push the use to click a malicious link.

As a good countermeasure, a company can can educate its employees about the risks of this kind of attacks
### Describe a phishing attack and what are the measures to limit it.
A phishing attack is an attack in which a fake text is sent to push the receiver to click on a malicious link. This is done to acquire authentication credentials, other personal data or to install some kind of malware.

Some variations of it are whaling, which targets the higher ups of a company, spear phishing, which uses personal informations, and pharming.

As a good countermeasure, a company can can educate its employees about the risks of this kind of attacks.
### Explain what a connection hijacking attack is, how it can be conducted and what countermeasures can be taken.
An hijacking attack, also called man in the middle, is an attack in which a malicious party take control of some communication over the network to read ,insert, modify or delete traffic by altering the routing path.

An example of it is as follows:
an attacker sniffs a valid session identifier sent in a request from a user to some site, and then uses it to gain unauthorized access to the same web server.

To counter it, it is usually require to adopt measures used to guarantee the authN, serialization, integrity and confidentiality of each individual packet.
### Explain what is meant by food chain malware, clarify why it has this name and illustrate with an example
food chain malware refers to the process from which, when a vulnerability is found, it doesn't pass trough a bug bounty programs, but sold instead in a vulnerability marketplace, then rootkits that exploits it are sold and distributed, just to arrive on a victim device which is vulnerable.  
### Explain what phishing and whaling attacks are.
Phishing is an attack in which the attacker sends some kind of text message to push the receiver to click on a malicious link. This is done to acquire authentication credentials, other personal data or to install some kind of malware.

Whaling is a kind of phishing which targets the higher ups of a company.
### What do the following words mean? Vulnerability, threat and security control? How are they related?
A vulnerability is a weakness of an asset.

A threat is a deliberate action or a accidental event that can produce the loss of a security propriety by exploiting a vulnerability.

Security controls are used to limit or prevent any kinds of threat to an asset.

These concept are used in risk estimation, which is the process in which the security events that poses a threat to the services are at first enumerated and then estimated in a qualitative and quantitative way.
### Explain what DoS means and give examples; why it is difficult to detect a DoS attack? how to defend against these attacks?
DoS stands for Denial of Service and is an attack in which an attacker tries to make a device unable to provide its services.
Some examples of it are the Syn or Ping Flooding attack.

It is quite difficult to detect this kind of attacks, because its difficult to discern if its an attack or a simple malfunction, and there are no actual countermeasure to this kind of attacks, apart for providing more resource that the one the attacker can saturate, but its not always easy an can be quite expensive.
### What is Stuxnet? How does it work and what lessons can we learn from it?
Stuxnet is a malware which is a combination of worm + virus for Windows systems.
It constitutes the prototype of a new type of attack, because it was the first known
case of an attack on SCADA systems, which are systems used to control industrial
plants. Since the computers weren't connected to the Internet, the first vehicle of
infection was probably a maintenance technician's USB stick, and then the malware
spread through shared network drives unprotected

We can learn that physical separation without other protection mechanism is not enough and unnecessary active services can increase the surface of attack.
### Say what the window of exposure is and where you can act to reduce it
The window of exposure is the time frame that starts when the vulnerability is discovered and ends with the moment the patch for it is installed.
Its composed in there phases:
- discovery, in which the patch is discovered
- publication: in which the vulnerability is made known and the vendors are working (hopefully) on a patch
- protection: in which the patch is published and installed

To reduce it one can install the patch as soon as possible.
### Bruce Scheiner wrote "security is a process, not a product" explaining the meaning of this statement and providing a practical example of its implementation with technical elements.
Implementing only a security program, like an antivirus, is often not enough, because it can fail or have some bugs.
Thus, It is usually necessary to reduce the risk of exposure regardless of the products or patches. 
### 13. Define the terms threat, vulnerability and security control, then explain what relationships exist between them and provide an example for each term in the case of a related triad

### 14. Briefly explain the security property called integrity by saying which attacks it protects against both when the data it refers to is stored and when it is transmitted.