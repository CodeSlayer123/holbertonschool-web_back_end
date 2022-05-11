export default function cleanSet(set, startString) {
  // return set.map((value) => value === "bonjovi")
  let result = '';
  let i = 0;

  if (startString === '' || typeof startString != 'string') {
    return '';
  }
  set.forEach((item) => {
    if (item.startsWith(startString)) {
      if (i !== 0 && i !== set.size) {
        result += '-';
      }
      result += item.substr(startString.length);
      i += 1;
    }
  });
  return result;
}
