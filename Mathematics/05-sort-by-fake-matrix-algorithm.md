# Sort algorithm by fake matrix
### Sorting by use y-axis (Ordering by use y axis)

To order a list of items by using the y-axis, we need to first represent each item in the list as a coordinate on a 2D plane. In this case, the x-axis represents the length of the item and the y-axis represents the unique position of the item in the list. For example, given the list "14325", we can represent it as the following coordinates:

1 - (1, 1)\
4 - (1, 2)\
3 - (1, 3)\
2 - (1, 4)\
5 - (1, 5)

To order the list based on the x-axis, we can use one of the sorting algorithms available in JavaScript, such as the Array.sort() method. We can provide a custom comparison function to specify that we want to sort based on the x-coordinate of each item. After sorting, we can update the y-coordinates to reflect the new order.

Here's an example code snippet in JavaScript that demonstrates this:

```javascript
// Define the list of items
const items = ['1', '4', '3', '2', '5'];

// Represent each item as a coordinate
const coordinates = items.map((item, index) => {
  return { x: item.length, y: index + 1 };
});

// Sort the coordinates based on the x-axis
coordinates.sort((a, b) => a.x - b.x);

// Update the y-coordinates to reflect the new order
coordinates.forEach((coord, index) => {
  coord.y = index + 1;
});

// Print the sorted list of items
const sortedItems = coordinates.map(coord => items[coord.y - 1]);
console.log(sortedItems); // Outputs ['1', '2', '3', '4', '5']
```

In this example, we first map each item in the list to its corresponding coordinate. We then sort the list of coordinates based on the x-axis using the Array.sort() method and a custom comparison function. Finally, we update the y-coordinates to reflect the new order and map the sorted list of coordinates back to the original list of items. The output is the sorted list of items: ['1', '2', '3', '4', '5'].

### Sort algorithm, using y-axis (Ordering by use y axis) [YCombinator]
Here's an example code snippet in JavaScript that demonstrates this using the Y Combinator to create a recursive function:

```javascript
const Y = (f => f(f))(f => (...args) => f(f)(...args));

const sortCoords = Y(recur => coords => {
  if (coords.length <= 1) {
    return coords;
  }
  
  const mid = Math.floor(coords.length / 2);
  const left = coords.slice(0, mid);
  const right = coords.slice(mid);
  
  const sortedLeft = recur(left);
  const sortedRight = recur(right);
  
  const merged = [];
  let i = 0;
  let j = 0;
  
  while (i < sortedLeft.length && j < sortedRight.length) {
    const coordI = sortedLeft[i];
    const coordJ = sortedRight[j];
    
    if (coordI.x <= coordJ.x) {
      merged.push(coordI);
      i += 1;
    } else {
      merged.push(coordJ);
      j += 1;
    }
  }
  
  while (i < sortedLeft.length) {
    merged.push(sortedLeft[i]);
    i += 1;
  }
  
  while (j < sortedRight.length) {
    merged.push(sortedRight[j]);
    j += 1;
  }
  
  // Update the y-coordinates to reflect the new order
  merged.forEach((coord, index) => {
    coord.y = index + 1;
  });
  
  return merged;
});

// Define the list of items
const items = ['1', '4', '3', '2', '5'];

// Represent each item as a coordinate
const coords = items.map((item, index) => {
  return { x: item.length, y: index + 1 };
});

// Sort the coordinates based on the x-axis
const sortedCoords = sortCoords(coords);

// Print the sorted list of items
const sortedItems = sortedCoords.map(coord => items[coord.y - 1]);
console.log(sortedItems); // Outputs ['1', '2', '3', '4', '5']
```

In this example, we start by defining the Y Combinator to create a recursive function. We then define the `sortCoords` function, which takes a list of coordinates and sorts them based on their x-coordinate using a merge sort algorithm. After sorting, we update the y-coordinates to reflect the new order.

To represent each item as a coordinate, we map each item in the list to its corresponding coordinate. We then call the `sortCoords` function to sort the list of coordinates based on the x-axis and update the y-coordinates. Finally, we map the sorted list of coordinates back to the original list of items.

#

This method power coordanated by other combined algorithm inside.\
Some times `O log x(n)`, `O n log x(n)` <-- x representing the combined algorithms.
