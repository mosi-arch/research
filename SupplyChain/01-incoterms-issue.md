## well, now the issue time [[ref of full issue](https://www.sciencedirect.com/science/article/pii/S2666659621000044)] :

#### Table 1. Cost allocation for incoterms (International Chamber of Commerce 2020)
Incoterm	Loading at origin	Export customs declaration	Carriage to port of export	Unloading of truck in port of export	Loading on vessel/airplane in port of export	Carriage (sea/air) to port of import	Insurance	Unloading in port of import	Loading on truck in port of import	Carriage to place of destination	Import customs clearance	Import duties and taxes	Unloading at destination

| Incoterm	| Loading at origin	| Export customs declaration	| Carriage to port of export	| Unloading of truck in port of export	| Loading on vessel/airplane in port of export	| Carriage (sea/air) to port of import	| Insurance	| Unloading in port of import	| Loading on truck in port of import	| Carriage to place of destination	| Import customs clearance	| Import duties and taxes	| Unloading at destination |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EXW	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer |
| FCA	| Seller	| Seller	| B/S	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer |
| FAS	| Seller	| Seller	| Seller	| Seller	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer |
| FOB	| Seller	| Seller	| Seller	| Seller	| Seller	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer |
| CPT	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Buyer	| B/S	| B/S	| Seller	| Buyer	| Buyer	| Buyer |
| CFR	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer |
| CIF	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer	| Buyer |
| CIP	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| B/S	| B/S	| Seller	| Buyer	| Buyer	| Buyer |
| DPU	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Buyer	| Buyer	| Seller |
| DAP	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Buyer	| Buyer	| Buyer |
| DDP	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Seller	| Buyer |

#### Table 2. Applying principles of fairness at varying levels of abstraction.
|||||||
|---|---|---|---|---|---|
| **Substantive Rules	Maximin Principle**	| Difference Principle	| International Relative Gains	| Majoritarian Social Contract	| Pluralistic Social Contract	| International Commercial Contract |
| **Selection Procedures (Local)**	| Maximin Constrained Optimization	| Individual Rational Choice	| National Gains from Trade	| Laissez Faire App Design	| Ethically Optimized App Design	| Incoterms (EXW, CIF, etc.) |
| **Selection Procedures (General)**	| Maximin Pareto Efficiency	| Original Position	| Harm Principle	| Distributed Consensus	| Distributed Consensus	| UPICC (Favor Contractus) |
| **Theoretical Assumptions**	| Utility Maximization	| Agent Neutrality	| Autarky	| Nodes Without Agreement	| Nodes Without Agreement	| Enterprises Without Agreement |

#### Table 3. Describing the role of class attributes.
|||
|---|---|
| Class	| Description |
| **ApiKey**	| Includes departure/arrival GPS coordinates, and LCL/FCL container designations, concatenated as string of integers. |
| **LogisticsService**	| Interface for exchanging transport data (e.g. route and port information) between third party vendor and application. |
| **PortFee**	| Attributes refer to the financial cost for each stage in the maritime supply chain, and carbon cost for journey. |
| **Incoterm**	| Each type of incoterm stored as binary array representing the order of buyer or seller responsibility relative to PortFee attributes. |
| **Action**	| Uses Incoterm and PortFee objects, along with data returned from LogisticsService to construct array of payoffs for each route. |
| **BaseContract**	| Superclass for Import and Export contracts. Defines blockchain address for buyer and seller. Receives ApiKey and decision parameters. |
| **ExportContract**	| Allows seller to confirm shipment dispatched as per decision and carrier. Also enables settlement of payment. |
| **ImportContract**	| Allows buyer to confirm shipment received, decision, and settlement of payment. |
| **Options**	| Allows buyer or seller to abort contract (electronically not legally). |
| **State**	| Defines status of smart contract on blockchain ledger. |

---

I solved the problem in/on/by solidity, coordination with solidity smart contract & incoterms rules. actually i sold the full solution by some bitcoin , and here we have just 4 contract example for "Sea and Inland Waterway Transport"... "this 4 items just for example and different by sold items"

#

#### Damage expert
Tips: Proof of Coverage ... [example information](https://github.com/mosi-arch/documents/blob/main/proof-of-coverage.md) 

#

check the: [FOB](https://github.com/mosi-arch/documents/blob/main/blockchain-and-supplychain.md) - [FAS](https://github.com/mosi-arch/documents/blob/main/incoterms-FAS.md) - [CFR](https://github.com/mosi-arch/documents/blob/main/incoterms-CFR.md) - [CIF](https://github.com/mosi-arch/documents/blob/main/incoterms-CIF.md) .
