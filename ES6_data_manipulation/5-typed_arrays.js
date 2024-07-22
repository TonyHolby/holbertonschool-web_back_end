function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const newArray = new Int8Array(buffer);
  newArray[position] = value;

  return buffer;
}

export default createInt8TypedArray;
