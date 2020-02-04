#!/usr/bin/node
let size = 0;
process.argv.forEach((element) => {
  size++;
});

if (size < 3) {
  console.log('No argument');
} else {
  for (let i = 2; i < size; i++) { console.log(process.argv[i]); }
}
