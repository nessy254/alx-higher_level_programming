#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Convert arguments to numbers

if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the array in descending order
  args.sort((a, b) => b - a);

  // Find the second largest integer
  const secondLargest = args[1];
  console.log(secondLargest);
}
