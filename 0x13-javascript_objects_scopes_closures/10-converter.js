#!/usr/bin/node
// Converts base 10 to another base passed as argument with Closure

exports.converter = function (base) {
    function myConverter (n) {
      return n.toString(base);
    }
  
    return myConverter;
  };
