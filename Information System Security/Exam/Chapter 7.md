## Closed answer questions
###### Question 1
What is the difference between channel security and message/data security?
- [x] channel security provides security properties like authentication (single or mutual), integrity and privacy only during the transit of data inside the communication channel; message/data security provides security properties self- contained in the message
- [ ] both of them support non repudiation
- [ ] channel security requires modification of applications, while message/data security does not require to modify the applications
###### Question 2
TLS is:
- [x] a security protocol used to establish secure transport channels (session level) supporting: peer authentication (server, server + client), message confidentiality, message authentication and integrity, and protection against replay and filtering attacks
- [ ] a security protocol used at application level supporting: peer authentication (server, server + client), message confidentiality, message authentication and integrity, and protection against replay and filtering attacks
- [ ] a security protocol used at network level supporting: peer authentication (server, server + client), message confidentiality, message authentication and integrity, and protection against replay and filtering attacks
###### Question 3
Peer authentication in TLS is implemented:
- [ ] in the TLS handshake phase, by sending the public key (X.509 certificate) to the communicating party
- [x] in the TLS handshake phase, by sending the public key (X.509 certificate) to the peer and by responding to an implicit/explicit asymmetric challenge
- [ ] in the TLS handshake phase, by using a keyed digest (SHA-256 or better)
###### Question 4
confidentiality in TLS is implemented:
- [ ] by using symmetric encryption. The client generates a pre- master secret key used for symmetric encryption of data and sends it protected via public key cryptography (RSA) to the server.
- [x] by using symmetric encryption. The client and server generate in the handshake a one-time key on the fly by using Diffie-Hellman. The key is used for confidentiality of data exchanged. In this way perfect forward secrecy is obtained too
- [ ] by using symmetric encryption. The server generates a session key used for symmetric encryption of data and sends it protected via public key cryptography (RSA, Diffie-Hellman, $\dots$ ) to the client
###### Question 5
Data authentication and integrity in TLS is achieved:
- [ ] by calculation of a keyed digest. Both the client and the server compute a MAC by using (besides the fragment data) a negotiated algorithm, the master secret, and a sequence number
- [x] by calculation of a keyed digest. Both the client and the server compute a MAC by using (besides the fragment data) a negotiated algorithm, a key derived from the master secret (specific for the client or server), and a sequence number
- [ ] by calculation of a keyed digest. Both the client and the server compute a MAC by using (besides the fragment data) a negotiated algorithm, a key derived from the master secret (specific for the client or server), and a sequence number. If session-id is used, then the key for the calculation of the MAC is re-used for several TLS sessions
###### Question 6
The protection from replay/filtering attacks in TLS is achieved:
- [ ] by a sequence number written in the TLS record
- [ ] by a sequence number written in the TCP segment
- [x] by a sequence number computed implicitly in the TLS record
- [ ] by an explicit ACK of each received fragment
- [ ] by an explicit ACK of all the fragments in a receive window
- [ ] none of the above
###### Question 7
Two parties negotiated to use TLS 1.2. Data protection (both authentication and encryption) in the TLS record is possibly achieved by:
- [ ] encrypt-then-authenticate
- [ ] authenticate-then-encrypt
- [ ] authenticated encryption
###### Question 8
What is TLS record protocol ?
- [ ] a protocol specifying the format of a record, which contains the application data protected with the keys and algorithm negotiated in the TLS handshake phase
- [ ] a protocol specifying the format of a TLS record, which contains either application data or handshake messages, or change cipher spec messages, or alert messages protected with the keys and algorithm negotiated in the TLS handshake phase
- [x] none of the above
###### Question 9
Consider a user connecting to a web application layered on HTTP and TLS. At which level/in which phase can the user authentication be performed?
- [ ] at TLS level/during TLS channel establishment, by requesting TLS client authentication (the user needs a X.509 certificate)
- [ ] at HTTP level/during HTTP channel setup, by transmitting username and password with basic or digest authentication
- [ ] at the application level/inside the application, e.g. by creating a form to request username and password
###### Question 10
Considering the user authentication methods discussed in Question 9, which one is considered less risky (from the security point of view)?
- [ ] at TLS level/during TLS channel establishment, by requesting TLS client authentication (the user needs a certificate)
- [ ] at HTTP level/during HTTP channel setup, by transmitting username and password with basic or digest authentication
- [ ] at the application level/inside the application, e.g. by creating a form to request username and password
###### Question 11
A company decided to use the "TLS then HTTP" to allow users access its services. Which are the reasons staying at the basis of its decision ?
- [ ] application developers can handle security internal to applications and the traffic exchanged can be easily analyzed with the IDS
- [ ] application developers delegate security configuration to system administrator and the traffic exchanged is difficult to analyze with the IDS
- [ ] the firewall can distinguish based on ports the secure channels from the unsecure ones
## Open Answer Questions
### Talk about TLS security proprieties with algorithms and keys
TSL is protocol used to establish a secure transport channel that guarantees peer authentication(at least of the server to the client) at the channel creation, confidentiality, integrity and authentication of each message and protection against replay and filtering attacks.
The latter 2 proprieties are guaranteed by the services that TCP provides(TLS use it as a L3 protocol), whereas confidentiality, integrity and authentication are guaranteed by a keyed digest, which is at least as strong as SHA-1.
During the handshake
### TLS, mandatory and optional security properties, say wi th which algorithms and with which keys they are implemented

### What are the data transformation steps when sent via a TLS channel with the TLS_DHE_DSS_WITH_AES_128_CBC_SHA ciphersuite with ZIP

### Describe how TLS client authentication works. Discuss its advantages and disadvantages.

### TLS client authentication vs HTML form-based authentication: advantages, disadvantages and solutions

### A company wants to do TLS client auth on a web server: advantages and disadvantages and precautions to be applied on client and server.

### A web designer must choose between authenticating users via TLS client authentication or HTLM form-based authentication. To illustrate the two solutions, with relative advantages and disadvantages and then suggest the best solution for general internet users

### Suppose you have a website, how could you authenticate the user being able to act only on the network node that hosts the website?

### Considering the TLS-1.0 protocol, explain what security properties it offers and for each of them indicate whether it is mandatory or optional and how it is achieved.

### On an HTTP server it is necessary to authenticate the clients, it is possible to use the SSL client authentication or a form with ID and PSW on a secure channel. Explain the two solutions, advantages and disadvantages of each and say which is preferable.

### TLS-then-proto and proto-then-TLS approaches: explain the functioning, advantages and disadvantages of the two approaches

### What are the data transformation steps when sent over a TLS channel with the DHE-RSA-AES-128-SHA cipher suite?

### Indicate which security properties are available via the TLS-1.2 protocol. For each property indicate whether it is optional or not, the methodology used to implement it and any specific keys or other configuration parameters required.

### You want to control access to web pages hosted by a server by operating only on the configuration of the server itself. Identify the possible techniques that can be used, indicating their advantages and disadvantages