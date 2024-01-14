Cloud computing is a **model** for enabling **ubiquitous**, **convenient** and **on-demand network access** to a **shared pool** of configurable **computing resources** that can be rapidly provisioned and released with **minimal management effort** or service provider **interaction**.
## Benefits of cloud computing
Using cloud computing have some great benefits with it:
- Reduced Investments and Proportional Costs
	- No hardware and software upfront payment
- Increased Scalability
	- Pay for resources only when needed
	- No paying for provisioning
	- Abstraction of the infrastructure
- Increased Availability and Reliability
	- Great flexibility: can access the cloud anywhere at any time
	- Data can be stored, downloaded, restored, or processed easily, 
## Problems with the model
When building up a cloud computing infrastructure, there are 4 main concerns.
- Capacity planning
- Cost reduction
- Operational overhead
- Organizational agility
### Capacity Planning
**Capacity planning** is the **process** of **determining** and **fulfilling future demands** of an
organization’s IT **resources**, products, and services.

With **capacity**, we mean the maximum amount of work that an IT resource is capable of delivering in a given period of time.
A **discrepancy** between the **capacity** of an IT resource **and** its **demand** can result in a system becoming either **inefficient** (*over-provisioning*) or unable to fulfill user needs
(*under-provisioning*).
Either way, this could be costly because of too much infrastructure or non enough to satisfy the demand.
For those reasons, the discrepancy between resources and demand should be minimized.

But planning for capacity can be challenging, because it requires to estimate the load fluctuations.
Different capacity planning strategies exist. Some examples are:
- Lead strategy, add capacity in advance
- Lag strategy, add capacity when the current one is reached
- Match strategy, add capacity in small increments, when demand raises
### Cost Reduction

A business is carried out to make a profit. Thus, reducing the cost is desirable to get a higher profit margin.
But obtaining a good balance between cost and business performance can be difficult to maintain.

Two costs need to be accounted for
-  the cost of **acquiring new infrastructure**
-  the cost of its **ongoing ownership**(keeping up the whole infrastructure)

Operational overhead represents a considerable share of IT budgets, often exceeding up-
front investment costs.
### Operational overhead
Aside from acquiring new hardware to add to the pool, there are the costs to keep the whole infrastructure running, in which figures:
- technical personnel payroll
- upgrades and patches
- utility bills and capital expense investments
- security and access control measures
- administrative and accounts staff payroll
### Organizational Agility
A business operates in a environment, that influences it and can be influenced by it.
Businesses need the ability to adapt and evolve to face change caused by internal
and external factors successfully. 

Organizational agility is the measure of an organization’s responsiveness to change and adapt.
## Scaling 
**Scaling** represents the ability of the **IT resource** to **handle** **increased** or **decreased** **usage demands**.

**Horizontal scaling** is the **process** of **increasing** the number of nodes and machines in the **resource pool**. 
It is also called *scaling out*.

**Vertical scaling** is the process of increasing the power of an existing system.
It is also called *scaling up*.

> Vertical scaling is less common in cloud environments due to the downtime required while the replacement is taking place.

![[Pasted image 20240108164722.png|650]]
## Cloud service
A cloud service is **any IT resource** that is made **remotely accessible** via a cloud.
That can be a web-based software of a remote access point.

In this context, the party that provides the cloud-based IT resource is the **cloud provider**, whereas the party that uses it is the **cloud consumer**.
The person or organization that legally owns a cloud service is called a **cloud service**
**owner**, and the person, or organization, that administrate its resources is the **cloud resource administrator**. 
### Service Level Agreement
The cloud provider party is responsible for making the cloud service available to the cloud consumer.
To ensure that the trust relationship is respected by both parties, the Service-level agreement in redacted.

The SLA details the **service-level capabilities promised** by the providers to be delivered
and requirements/expectations stated by consumers. This document is legal binding.
![[Pasted image 20240108171226.png|650]]
### Other Roles
A third-party that conducts **independent security, privacy and performance assessments** of cloud environments assumes the role of the **cloud auditor**.

The party that assumes the responsibility of **managing** and **negotiating** the usage of cloud services between cloud consumers and cloud providers is called the **cloud broker**.

The party responsible for providing the wire-level connectivity between cloud
consumers and cloud providers assumes the role of the cloud carrier.
## Cloud characteristics
An IT environment requires a specific set of characteristics to enable the remote
provisioning of scalable and measured IT resources in an effective manner.

There are six specific characteristics that are common to the majority of cloud environments.
### On-Demand Usage
A cloud consumer can unilaterally access cloud-based IT resources, allowing him to self-provision in freedom.
This means, that the provisioning can be automated.
### Ubiquitous Access
Ubiquitous access represents the ability for a cloud service to be widely accessible. 
This means that it must support a wide range of devices, protocols and interfaces.
### Multitenancy
The characteristic of a software program that enables an instance of the program to
serve different consumers (tenants) whereby each is isolated from the other, is referred
to as multitenancy.
### Elasticity
lasticity is the automated ability of a cloud to transparently scale IT resources, as
required in response to runtime conditions or as pre-determined by the cloud consumer
or cloud provide.

> To put it simple, it must scale.
### Measured Usage
The measured usage characteristic represents the ability of a cloud platform to keep
track of the usage of its IT resources, primarily by cloud consumers.

It is not limited to billing, but also for monitoring and usage reporting.
### Resiliency
The cloud must have a form of failover, in case a resource becomes deficient, the processing is handed over to another redundant implementation.
## Cloud Deployment Models
A cloud deployment model represents a specific type of cloud environment, primarily
distinguished by ownership, size, and access.

there are four common models.
### Public cloud
A public cloud is a publicly accessible cloud environment owned by a third-party cloud
provider. 

A public cloud may be owned, managed, and operated by a business, academic, or
government organization, or some combination of them.
![[Pasted image 20240108174407.png|350]]
### Private cloud 
A private cloud is owned by a single organization.
With a private cloud, the same organization is technically both the cloud consumer and
cloud provider. 

In order to differentiate these roles:
- A separate organizational department typically assumes the responsibility for provisioning the cloud
- Departments requiring access to the private cloud assume the cloud consumer role
![[Pasted image 20240108174509.png|350]]
### Community Clouds
A community cloud shares characteristics of private and public clouds.

 The cloud resources are shared among a number of independent organizations, but with a restricted access.
![[Pasted image 20240108174631.png|450]]
### Hybrid cloud
A hybrid cloud is a cloud environment comprised of two or more different cloud
deployment models.

> For example, a cloud consumer may choose to deploy cloud services processing sensitive data to a private cloud and other, less sensitive cloud services to a public cloud.

![[Pasted image 20240108174748.png]]
## Delivery models
A cloud delivery model represents a specific, pre-packaged combination of IT resources
offered by a cloud provider. 

There are three common cloud delivery models.
### Infrastructure-as-a-Service (IaaS)
The service made available to the client is an IT environment comprised of infrastructure-centric IT resources that can be accessed and managed via cloud service-
based interfaces and tools

> IT resources are typically virtualized and packaged into bundles that simplify up-front runtime scaling and customization of the infrastructure.
### Platform-as-a-Service (PaaS)
The PaaS delivery model represents a pre-defined “ready-to-use” environment typically
comprised of already deployed and configured IT resources.

By working within a ready-made platform, the cloud consumer is spared the administrative burden of setting up and maintaining the bare infrastructure IT resources provided via the IaaS model.
### Software-as-a-Service (SaaS)
A software program positioned as a shared cloud service and made available as a “product” or generic utility represents the typical profile of a SaaS offering.

The SaaS delivery model is typically used to make a reusable cloud service widely
available (often commercially) to a range of cloud consumers.

![[Pasted image 20240108175821.png|550]]
![[Pasted image 20240108175845.png|550]]
### XaaS
XaaS is the latest development in the provisioning of cloud services. 
The acronym has many interpretation, but in general means **X as a Service**,  where X can represent any possible cloud service option.

XaaS is becoming increasingly attractive to customers because it offers these benefits:
- Total costs are controlled and lowered because of outsourcing to experts partners
- Risks of projects are lowered
- Innovation is accelerated.
## Virtualization
**Virtualization** is a **process** that allows for more efficient utilization of physical computer hardware and is the foundation of cloud computing.

Virtualization uses software to create an abstraction layer over computer hardware that allows the hardware elements of a single computer to be divided into multiple virtual computers, commonly called **Virtual Machines** (VMs).

### Virtual machines
Virtual machines (VMs) are **virtual environments** that **simulate** a **physical** compute **in**
**software form**.

Each VM runs its own Operating System (OS) and behaves like an independent computer.
We call the physical machine the **host os** and the os running in the VM the **guest machine**.

For this reason, VMs allows for a good degree of resource utilization, improving ROI along it, and flexibility.
It also scales pretty good and they can be relocated as needed.
#### Hypervisor e VMM
Two components are often referred when talking about VMs.

The **Virtual Machine Monitor** (VMM) is responsible for providing hardware resource abstraction for virtual machines and providing a running environment for guest operating
systems.

**Virtualization platform** (Hypervisor) is responsible for hosting and management of
virtual machines. 

> Hypervisor can also be translated as a virtual machine monitor. We use the term hypervisor to refer to both.

To summarize, A hypervisor is the software layer that coordinates VMs, that serves as an interface between the VM and the actual physical hardware, to ensure that bot have the necessary resources and dont interfere with each other.

##### Bare Metal Virtualization
The hypervisor runs directly on the underlying computer’s physical hardware, interacting
directly with its CPU, memory, and physical storage.

can be further classified in:
- Monolithic: Host the hypervisor/VMM in a single layer that also includes most of the required components, such as the kernel, device drivers, and the I/O stack
- Microkernelized: Uses a very thin, specialized hypervisors that only performs the core tasks of ensuring partition isolation and memory management. This layer does not include the I/O stack or Device Drivers
![[Pasted image 20240108194516.png|450]]
##### Type 2 hypervisor 
It runs as an application in an OS.

Enables quick and easy access to an alternative guest OS alongside the primary
one running on the host system.

But because a Type 2 hypervisor must access computing, memory, and network
resources via the host OS, it introduces latency issues that can affect
performance
![[Pasted image 20240108194628.png|450]]
### Virtual hardware
The “virtual hardware profile” defines the characteristics of the hardware provided to the Guest OS
### Virtualization Techniques
There are multiple approaches to running the Guest OS.
- Full Virtualization: It completely abstract the hardware from the guest OS, transalting all the system call on the fly.
- Paravirtualization: The hypervisor provides an API, that is used by the Guest OS, enabling near bare metal performances.
- HW-assisted Virtualization

