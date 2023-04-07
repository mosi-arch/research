Here's an example Solidity code that uses "CFR" incoterms rule for a hypothetical international trade contract:

```solidity
pragma solidity ^0.8.0; 

contract InternationalTradeContract { 
	// Enum to define the different incoterms rules 
	enum Incoterms { 
		FOB, FAS, CFR, CIF 
	} 
	
	// Struct to represent the contract terms 
	struct ContractTerms { 
		uint256 price; 
		// Price of goods 
		uint256 quantity; 
		// Quantity of goods 
		Incoterms incoterms; 
		// Incoterms rule used 
		string portOfLoading; 
		// Port of loading 
		string portOfDestination; 
		// Port of destination 
	} 
	
	// Function to calculate the total cost of the trade based on the incoterms rule 
	function calculateTotalCost(ContractTerms memory contractTerms) public view returns (uint256) { 
		uint256 totalCost; 
		if (contractTerms.incoterms == Incoterms.CFR) { 
			// CFR: Seller is responsible for delivering the goods to the port of shipment and loading them onto the shipping vessel. Seller also pays for the shipping costs and insurance costs up to the port of destination. Buyer is responsible for all other costs and risks. 
			totalCost = contractTerms.price * contractTerms.quantity; 
			// Add shipping costs and insurance costs paid by seller 
			totalCost += calculateShippingCosts(contractTerms.portOfLoading, contractTerms.portOfDestination); 
			totalCost += calculateInsuranceCosts(contractTerms.price, contractTerms.quantity); 
		} 
		return totalCost; 
	} 
	
	// Helper function to calculate shipping costs 
	function calculateShippingCosts(string memory portOfLoading, string memory portOfDestination) private pure returns (uint256) { 
		// Calculate shipping costs based on the distance between the two ports 
		uint256 distance = calculateDistanceBetweenPorts(portOfLoading, portOfDestination); 
		uint256 shippingCosts = distance * 100; 
		// Assuming a fixed rate of $100 per unit of distance 
		return shippingCosts; 
	}
	
	// Helper function to calculate insurance costs 
	function calculateInsuranceCosts(uint256 price, uint256 quantity) private pure returns (uint256) { 
		uint256 insuranceCosts = (price * quantity * 2) / 1000; 
		// Assuming a rate of 0.2% of the total price of the goods 
		return insuranceCosts; 
	} 
	
	// Helper function to calculate the distance between two ports 
	function calculateDistanceBetweenPorts(string memory port1, string memory port2) private pure returns (uint256) { 
		// Implementation details not provided in this example 
		// Could use an external API or a pre-populated mapping of port distances 
		// For simplicity, assume a fixed distance of 1000 units 
		return 1000; 
	} 
}
```
This contract is similar to the ones using "FOB" and "FAS" incoterms rules, but with a different conditional statement to calculate the total cost of the trade based on the "CFR" incoterms rule.

For "CFR", the seller is responsible for delivering the goods to the port of shipment and loading them onto the shipping vessel. The seller is also responsible for paying the shipping costs and insurance costs up to the port of destination. The buyer is responsible for all other costs and risks. The `calculateTotalCost` function calculates the price of the goods, and adds the shipping costs and insurance costs paid by the seller using the `calculateShippingCosts` and `calculateInsuranceCosts` helper functions.

---

red more [here](https://github.com/mosi-arch/documents/blob/main/incoterms-issue.md) 
