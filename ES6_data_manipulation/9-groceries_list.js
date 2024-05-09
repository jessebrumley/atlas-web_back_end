export default function groceriesList() {
  const groceries = {
    Apples: 10, Tomatoes: 10, Pasta: 1, Rice: 1, Banana: 5,
  };
  const groceriesList = new Map();
  for (const [key, val] of Object.entries(groceries)) {
    groceriesList.set(key, val);
  }
  return groceriesList;
}
