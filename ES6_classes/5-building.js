export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building) {
      if (!(this.evacuationWarningMessage)) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
    this.sqft = sqft;
  }

  set sqft(val) {
    if (typeof (val) === 'number') {
      this._sqft = val;
    } else {
      throw TypeError('sqft must be a number');
    }
  }

  get sqft() {
    return this._sqft;
  }
}
