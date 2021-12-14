#!/usr/bin/node
const args = process.argv.length;
if (args < 4) {
  console.log('0');
} else {
  const nums = process.argv.sort((a, b) => a - b);
  console.log(nums[nums.length - 2]);
}
