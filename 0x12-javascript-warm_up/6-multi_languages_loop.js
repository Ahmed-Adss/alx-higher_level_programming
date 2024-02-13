#!/usr/bin/node

const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < arr.length; i++) {
  if (i < arr.length - 1) {
    console.log(arr[i] + '\n');
  } else {
    console.log(arr[i]);
  }
}
