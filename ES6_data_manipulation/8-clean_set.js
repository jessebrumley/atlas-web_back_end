export default function cleanSet(set, str = '') {
  let resStr = '';
  if (typeof str !== 'string' || str.length === 0 || !str) {
    return resStr;
  }
  set.forEach((x) => {
    if (x.slice(0, str.length) === str) {
      if (resStr.length !== 0) {
        resStr += '-';
      }
      resStr += x.slice(str.length);
    }
  });
  return resStr;
}
