## Lambda & Recursion in Functional Programming
### Lambda
Lambda is a type of function in functional programming that takes one or more arguments and returns a single value. 
It is often used to create anonymous functions, which are functions that are not bound to a name. 
Lambda functions are often used to create higher-order functions, which are functions that take other functions as arguments.

### Recursion
Recursion is a type of function in functional programming that calls itself. 
It is often used to solve problems that can be broken down into smaller, simpler sub-problems. 
Recursion is a powerful tool for solving complex problems, but it can also be difficult to debug and 
can lead to stack overflow errors if not used correctly.


### Mathematical Proof:
Let `f(x)` be a function that takes one argument x and returns a single value.

We can define a lambda function as follows:
- `λx.f(x)`

This lambda function takes one argument `x` and returns the value of `f(x)`.

We can define a recursive function as follows:
- `f(x) = f(x)`

This recursive function takes one argument `x` and returns the value of `f(x)`.

Therefore, we can conclude that lambda functions and recursive functions are both types of functions in functional programming.

### Y Combinator
Y Combinatoris a type of function in functional programming that takes a function as an argument and returns a new function. 
It is often used to create recursive functions, which are functions that call themselves. 
Y Combinator is a powerful tool for solving complex problems, but it can also be difficult to debug and can lead to 
stack overflow errors if not used correctly.

### Mathematical Proof:
Let `f(x)` be a function that takes one argument x and returns a single value.

We can define a Y Combinator as follows:
- `Y(f) = λx.f(λy.x(x)(y))`

This Y Combinator takes one argument f and returns a new function that takes one argument x and returns the value of `f(λy.x(x)(y))`.

Therefore, we can conclude that Y Combinator is a type of function in functional programming.

#

### Examples:

- lambda chain "y combinator" recursion, javascript
```js
function YCombinator(func) {
    return (function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    })(function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    });
}
```

- lambda chain "y combinator" recursion, python
```python
def YCombinator(func):
    return (lambda x: func(lambda y: (x(x))(y)))(lambda x: func(lambda y: (x(x))(y)))
```

- lambda chain "y combinator" recursion, c lang
```c
int YCombinator(int (*func)(int)) {
    return ((int (*)(int))(lambda (int x) {
        return func((int (*)(int))(lambda (int y) {
            return (x(x))(y);
        }));
    }))((int (*)(int))(lambda (int x) {
        return func((int (*)(int))(lambda (int y) {
            return (x(x))(y);
        }));
    }));
}
```

- using "y combinator" for ,merkle proof, code in javascript - solution 1
```js
function YCombinator(func) {
    return (function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    })(function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    });
} 
function merkleProof(data) {
    return YCombinator(function(f) {
        return function(data) {
            if (data.length === 1) {
                return data[0];
            }
            let mid = Math.floor(data.length / 2);
            let left = data.slice(0, mid);
            let right = data.slice(mid);
            let hash = left.concat(right).reduce((acc, cur) => acc + cur);
            return f([hash, ...f(left), ...f(right)]);
        };
    })(data);
} 
```

- using "y combinator" for ,merkle proof, code in js! - solution 2

```js
function YCombinator(func) {
    return (function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    })(function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    });
} 
function merkleProof(data) {
    return YCombinator(function(f) {
        return function(data) {
            if (data.length === 1) {
                return data[0];
            }
            uint mid = data.length / 2;
            bytes32[] memory left = new bytes32[](mid);
            bytes32[] memory right = new bytes32[](data.length - mid);
            for (uint i = 0; i < mid; i++) {
                left[i] = data[i];
            }
            for (uint i = mid; i < data.length; i++) {
                right[i - mid] = data[i];
            }
            bytes32 hash = keccak256(abi.encodePacked(left) + abi.encodePacked(right));
            return f([hash, ...f(left), ...f(right)]);
        };
    })(data);
}
```

- comparison 2 array by same length, code in javascript (use "y combinator" )
```js
function YCombinator(func) {
    return (function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    })(function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    });
} 
function compareArrays(arr1, arr2) {
    return YCombinator(function(f) {
        return function(arr1, arr2) {
            if (arr1.length === 0) {
                return true;
            }
            if (arr1[0] !== arr2[0]) {
                return false;
            }
            return f(arr1.slice(1), arr2.slice(1));
        };
    })(arr1, arr2);
}
```

- Compute number pi to 1000 digits, then slice the prime numbers from that. code in javascript
```js
// Compute number pi to 1000 digits
const pi = Math.PI.toPrecision(1000); 
// Slice the prime numbers from that
function getPrimeNumbers(pi) {
    let primeNumbers = [];
    for (let i = 0; i < pi.length; i++) {
        if (isPrime(pi[i])) {
            primeNumbers.push(pi[i]);
        }
    }
    return primeNumbers;
} 
// Check if a number is prime
function isPrime(num) {
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return num > 1;
}
```

- Compute number pi to 1000 digits, then slice the prime numbers from that. code in javascript and using "y combinator" for comparison
```js
function YCombinator(func) {
    return (function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    })(function(x) {
        return func(function(y) {
            return (x(x))(y);
        });
    });
} 
// Compute number pi to 1000 digits
const pi = Math.PI.toPrecision(1000); 
// Slice the prime numbers from that
function getPrimeNumbers(pi) {
    let primeNumbers = [];
    for (let i = 0; i < pi.length; i++) {
        if (YCombinator(function(f) {
            return function(num) {
                for (let i = 2; i < num; i++) {
                    if (num % i === 0) {
                        return false;
                    }
                }
                return num > 1;
            };
        })(pi[i])) {
            primeNumbers.push(pi[i]);
        }
    }
    return primeNumbers;
}
```

Functional programming make better life for code & coder!
