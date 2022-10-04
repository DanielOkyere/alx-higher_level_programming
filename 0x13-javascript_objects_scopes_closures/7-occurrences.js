#!/usr/bin/node

/**
 * nbOccurences - returns the number of occurences
 * @list: list to search
 * @searchElement: the search element
 * Return: The number of occurence
 */
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.map((el) => {
    if (el === searchElement) counter += 1;
    return el;
  });

  return counter;
};
