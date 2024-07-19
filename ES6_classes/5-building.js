export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new TypeError('The method named evacuationWarningMessage should be implemented first');
    }
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
