#!/usr/bin/node
exports.callMeMoby = function (a, cb) {
  for (let i = 0; i < a; i++) {
    cb();
  }
};
