// Building.js
export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new TypeError('The method named evacuationWarningMessage should be implemented first');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    if (this.constructor === Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    return `${this._sqft}`;
  }
}

export class MyClass extends Building {
  evacuationWarningMessage() {
    return `${this._sqft}`;
  }
}
