#!/usr/bin/node
let size = 0;
process.argv.forEach((element) => {
  size++;
});

if (size < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
