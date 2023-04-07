Here's an example Solidity code that uses "FAS" incoterms rule for a hypothetical international trade contract:

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
		if (contractTerms.incoterms == Incoterms.FAS) { 
			// FAS: Seller is responsible for delivering the goods to the port of shipment, and loading them onto the shipping vessel. Buyer is responsible for all other costs and risks. 
			totalCost = contractTerms.price * contractTerms.quantity; 
			// Add shipping costs and insurance costs paid by buyer 
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
		uint256 insuranceCosts = (price * quantity * 1) / 1000; 
		// Assuming a rate of 0.1% of the total price of the goods 
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
This contract is similar to the one using "FOB" incoterms rule, but with a different conditional statement to calculate the total cost of the trade based on the "FAS" incoterms rule.

For "FAS", the seller is responsible for delivering the goods to the port of shipment and loading them onto the shipping vessel, while the buyer is responsible for all other costs and risks. The `calculateTotalCost` function calculates the price of the goods, and adds the shipping costs and insurance costs paid by the buyer using the `calculateShippingCosts` and `calculateInsuranceCosts` helper functions.

The `calculateShippingCosts` and `calculateInsuranceCosts` helper functions are the same as the ones used in the "FOB" example. The `calculateDistanceBetweenPorts` helper function is also the same, assuming a fixed distance of 1000 units between any two ports for simplicity.

---

red more [here](https://github.com/mosi-arch/documents/blob/main/incoterms-issue.md) 
