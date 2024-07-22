function cleanSet(set, startString) {
  if (startString === '' || set.size === 0) {
    return '';
  }

  return Array.from(set).filter((value) => value.startsWith(startString)).map((value) => value.slice(startString.length)).join('-');
}

export default cleanSet;
