export default class Building {
  constructor(sqft) {
    if (new.target === Building) {
      throw new Error('The method named evacuationWarningMessage should be implemented first');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    return `Building${this._sqft}`;
  }
}
