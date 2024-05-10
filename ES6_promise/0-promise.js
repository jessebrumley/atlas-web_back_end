export default function getPromiseFromAPI() {
  const promise = new Promise((res) => {
    res('Hello!');
  });
  return promise;
}
