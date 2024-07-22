function cleanSet(set, startString) {
  if (startString === '' || set.size === 0) {
    return '';
  }

  let str = '';

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      if (str.length > 0) {
        str += '-';
      }
      str += value.slice(startString.length);
    }
  }

  return str;
}

export default cleanSet;
