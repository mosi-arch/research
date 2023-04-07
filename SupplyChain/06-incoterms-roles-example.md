## Example solidity code about "insurance incoterms roles"
Here is an example Solidity code for an insurance smart contract that involves incoterms roles:

```solidity
pragma solidity ^0.8.0;

contract Insurance {

  enum IncotermsRole { 
    Buyer, 
    Seller, 
    Carrier, 
    InsuranceProvider 
  }

  struct Incoterms {
    IncotermsRole buyer;
    IncotermsRole seller;
    IncotermsRole carrier;
    IncotermsRole insuranceProvider;
  }

  mapping (uint256 => Incoterms) incotermsRoles;

  function setIncotermsRoles(
    uint256 orderNumber, 
    IncotermsRole _buyer, 
    IncotermsRole _seller, 
    IncotermsRole _carrier, 
    IncotermsRole _insuranceProvider
  ) public {
    Incoterms memory newIncoterms = Incoterms(_buyer, _seller, _carrier, _insuranceProvider);
    incotermsRoles[orderNumber] = newIncoterms;
  }

  function getIncotermsRoles(uint256 orderNumber) public view returns (Incoterms memory) {
    return incotermsRoles[orderNumber];
  }
}
```

This code defines an enum `IncotermsRole` that represents the different roles involved in an incoterm agreement (Buyer, Seller, Carrier, and Insurance Provider). The `Incoterms` struct is used to store the roles for a specific order. The `setIncotermsRoles` function allows the roles to be set for a specific order, and the `getIncotermsRoles` function allows the roles to be retrieved for a specific order. This can be useful in determining which party is responsible for insurance coverage in case of loss or damage during shipment.

### Example solidity code about "insurance incoterms role = EXW"
Here is an example of Solidity code related to an insurance contract with Incoterms role set to EXW:
```solidity
pragma solidity ^0.8.0;

contract InsuranceContract {
  string public incotermsRole;

  constructor() {
    incotermsRole = "EXW";
  }

  function setIncotermsRole(string memory _role) public {
    incotermsRole = _role;
  }
}
```

This contract initializes the `incotermsRole` variable to "EXW" and allows it to be updated through the `setIncotermsRole` function.

#### Look at all roles [here](https://github.com/mosi-arch/documents/blob/main/incoterms-issue.md)
- EXW 
- FCA 
- FAS 
- FOB 
- CPT 
- CFR 
- CIF 
- CIP 
- DPU 
- DAP 
- DDP
