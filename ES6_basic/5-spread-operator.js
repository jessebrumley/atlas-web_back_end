export default function concatArrays(...args) {
  let result = [];
  args.forEach(arg => {
  result = result.concat(arg);
  });
  return result;
}
