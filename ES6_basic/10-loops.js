export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];

  for (const value of array) {
    newArray[newArray.indexOf(value)] = appendString + value;
  }

  return newArray;
}
