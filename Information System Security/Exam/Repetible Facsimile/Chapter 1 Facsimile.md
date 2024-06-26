## Closed answer questions
###### Question 1
Alice wants to open a communication channel with Bob.
Which of the following security properties she must implement in order to check that she is really communicating with Bob?
- [ ] A. non-repudiation
- [ ] B. integrity
- [ ] C. availability
- [ ] D. peer authentication
- [ ] E. data authentication
- [ ] F. privacy
- [ ] G. accountability
###### Question 2 
Assume Alice sends a message to Bob. Bob knows that he has to perform data authentication. 
What does it mean?:
- [ ] Bob must register the received data in a database
- [ ] Bob must identify Alice (e.g. check her identity card)
- [ ] Bob must verify that the data really comes from Alice (for example, by verifying some sort of evidence attached to the data that only Alice may have created)
- [ ] Bob must demonstrate his identity to Alice
###### Question 3
Assume Alice wants to connect to two systems run by Bob.
Alice and Bob must always perform the mutual authentication. What does it mean?
- [ ] Alice authenticates to every system run by Bob and each of the two systems of Bob authenticate to Alice
- [ ] Bob authenticates to Alice
- [ ] Alice authenticates to the two systems run by Bob
- [ ] each of the two systems of Bob authenticate to Alice
- [ ] Alice and Bob must identify themselves, e.g. by exchanging their identity cards
###### Question 4 
Assume Alice is entering a password (or a PIN) to access her smartphone. Which security property is implemented by her smartphone for this operation?
- [ ] confidentiality
- [ ] integrity
- [ ] authentication
- [ ] availability
- [ ] authorization
###### Question 5
In Windows OS there are two types of users: normal and administrator. Assume a normal user tries to install a program and this operation is denied by the OS.
Which security property the OS has implemented for software installation operation? (we assume the user has already logged in successfully with his credentials):
- [ ] authentication
- [ ] authorization
- [ ] traceability
- [ ] availability
###### Question 6
Alice writes some data on her disk. The disk is placed in a secure place. After some time she wants to check whether the data has been modified. Which security property does she have to implement?
- [ ] authentication
- [ ] authorization
- [ ] traceability
- [ ] integrity
- [ ] availability
###### Question 7
Alice wants to protect the entrance in a building with a card reader. Which security property/properties must implement the card reader placed at the entrance?
- [ ] A. authentication
- [ ]  B. authorization
- [ ]  C. non-repudiation
- [ ]  D. integrity
### Basic security attacks
###### Question 1
What is a replay attack?
- [ ] A. an attack in which some data (in clear or protected for confidentiality) can be intercepted and then sent more than once to the destination
- [ ] an attack in which only data in clear can be intercepted and then sent more than once to the destination
- [ ] C. an attack in which an attacker intercepts the data, then sends it to another attacker who will send it to the destination
###### Question 2
What is a sniffing attack?
- [ ] an attack in which data (in clear or protected) is intercepted while in transmission
- [ ] an attack in which only data in clear can be intercepted
- [ ] an attack in which an attacker intercepts the data, then modifies it, then finally sends it to the destination
###### Question 3
What is an IP spoofing attack?
- [ ] an attack in which the attacker creates fake date and inserts it into a connection
- [ ] an attack in which an attacker modifies the IP source address and sends it to a destination
- [ ] an attack in which an attacker modifies the IP destination address and sends it to the destination
- [ ] an attack in which an attacker modifies both the source and the destination addresses in an IP packet
	- This is a MITM
###### Question 4
What kind of countermeasures are applicable for an IP spoofing attack aimed to gain unauthorised access to a remote resource?
- [ ] A. instruct the browser's users to carefully check the URL they are connecting to
- [ ] avoid the use of broadcast networks
- [ ] avoid the use of the IP address as "credential" to authenticate and get access to any remote resources
- [ ] install (and regularly update) an anti-malware application on each device
###### Question 5
What is a Denial of Service attack?
- [ ] an attack in which the attacker keeps a host busy by exhausting its resources (e.g. mail) so that it cannot provide its services
- [ ] an attack in which the attacker keeps a host busy by flooding it with traffic (e.g. DNS or ICMP) so that it cannot provide its services
- [ ] an attack in which an attacker keeps a host busy by exhausting its resources (e.g. by injecting a malware that makes continuous calculations) so that to block the use of the host
- [ ] an attack in which an attacker denies the use of a host to a user because he/she is not authorized
###### Question 6
What is Distributed Denial of Service (DOS) attack?
- [ ] attack in which the attacker (master) exploits multiple daemons installed on compromised nodes to run (upon  command) a software implementing the DOS attack against one victim
- [ ] attack in which an attacker (master) distributes the DOS software to multiple nodes that run independently the attack against different victims
- [ ] attack in which attackers (masters) collaborate and decide along with the zombies which type of DOS attack to run
###### Question 7
Bob is an attacker who decides to activate a shadow server to attack Alice. What kind of attacks can he perform against Alice (to provoke damage)
- [ ] replay attack
- [ ] Denial of Service
- [ ] redirect Alice to fake web sites
- [ ] packet sniffing
###### Question 8 
Alice wants to communicate securely with Bob (server).
What kind of security properties must she implement to protect from Man in the Middle attack? Note: we assume Alice and Bob have trusted devices and software
- [ ] server authentication, data authentication, confidentiality of the data exchanged, integrity of the data exchanged
- [ ] server authentication, confidentiality of the data exchanged, integrity of the data exchanged, serialization of each packet
- [ ] server authentication, data authentication, confidentiality of the data exchanged, integrity of the data exchanged, and serialization of each packet
- [ ] privacy of the data exchanged, server authentication, data authentication, integrity of the data exchanged, serialization of each packet
###### Question 9
In risk analysis, assets are:
- [ ] any ICT resource, data, and people present or working inside a company
- [ ] any ICT resource, data, and people used for providing a service
- [ ] the ICT resources, data, people, and location used in providing a specific service
- [ ] the ICT resources, data, people, and location used in providing the services offered by the company
###### Question 10
In risk analysis, vulnerabilities are:
- [ ] weaknesses in the software that could be exploited by an attacker
- [ ] weaknesses in the design, implementation, configuration and management that could be exploited by an attacker
- [ ] actions an attacker performs to damage an asset
- [ ] weaknesses in the design, implementation, configuration and management that could harm assets if exploited by an attacker or by occurrence of unintentional events (natural disasters, mistakes performed by individuals)
###### Question 11
In risk analysis, a security control is:
- [ ] a set of operational and management processes, and security mechanisms (including software techniques, algorithms and protocols) used to protect against threats
- [ ] functional and non-functional requirements that need to be satisfied in order to achieve security
- [ ] a set of operational and management processes, and security mechanisms (including software techniques, algorithms and protocols) adopted to reduce risks
###### Question 12
In risk analysis, a risk is:
- [ ] a qualitative (e.g., low, medium, high, very high) or quantitative (e.g. 10, 15, 25) value calculated based on the impact and the probability of occurrence of a security event
- [ ] a cost calculated based on the countermeasures to be selected and implemented to protect against a security event
- [ ] possible deliberate action/accidental event that can produce the loss of a security property
###### Question 13
What are the security controls and procedures?
- [ ] documents expressing 'how' you implement the policies, both for the technical details (such as specific techniques, algorithms used) and organizational details
- [ ] documents expressing the vulnerabilities of a system or product
- [ ] documents expressing the flaws in the implementation of a system of product
###### Question 14
Which of the following is **not** a purpose of doing a risk analysis?
- [ ] delegate responsibility
- [ ]  quantify impact of potential threats
- [ ]  identify risks
- [ ]  define the balance between the impact of a risk and the cost of the necessary countermeasure
## Open Answer questions
### 1. Talk about sniffing, spoofing and hijacking attacks and describe the appropriate security measures

###  2. Explain what social engineering is, give an example of this attack, indicate the countermeasures that a company can take to defend itself.

### 3. Describe a phishing attack and what are the measures to limit it.

### 4. Explain what a connection hijacking attack is, how it can be conducted and what countermeasures can be taken.

### 5. Explain what is meant by food chain malware, clarify why it has this name and illustrate with an example

### 6. Explain what phishing and whaling attacks are.

### 6. What do the following words mean? Vulnerability, threat and security control? How are they related?

### 7. What do the following words mean? Vulnerability, threat, assets and attack? How are they related?

### 8. Explain what DoS means and give examples; why it is difficult to detect a DoS attack? how to defend against these attacks?

### 9. Explain what DoS means and give examples; why it is difficult to detect a DoS attack; how to defend against these attacks.

### 10. What is Stuxnet? How does it work and what lessons can we learn from it?

### 11. Say what the window of exposure is and where you can act to reduce it

### 12. Bruce Scheiner wrote "security is a process, not a product" explaining the meaning of this statement and providing a practical example of its implementation with technical elements.

### 13. Define the terms threat, vulnerability and security control, then explain what relationships exist between them and provide an example for each term in the case of a related triad

### 14. Briefly explain the security property called integrity by saying which attacks it protects against both when the data it refers to is stored and when it is transmitted.