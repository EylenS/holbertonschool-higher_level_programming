#!/usr/bin/node
export function nbOccurences (list, item) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === item) {
      counter++;
    }
  }
  return (counter);
}
