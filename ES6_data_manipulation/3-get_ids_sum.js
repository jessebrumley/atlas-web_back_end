export default function getStudentsIdsSum(array) {
  const initialValue = 0;
  return array.reduce((accumulator, currentValue) => accumulator + currentValue.id, initialValue);
}
