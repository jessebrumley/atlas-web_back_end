export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];

  for (const value of newArray) {
    newArray[newArray.indexOf(value)] = appendString + value;
  }

  return newArray;
}
