function createInt8TypedArray(length, position, value) {
  const NewArrayBuffer = new ArrayBuffer(length);
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  NewArrayBuffer[position] = value;

  return NewArrayBuffer;
}

export default createInt8TypedArray;
