function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const newArray = new DataView(buffer);
  newArray.setInt8(position, value);

  return newArray;
}

export default createInt8TypedArray;
