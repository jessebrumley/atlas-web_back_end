import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  set floors(val) {
    if (typeof (val) === 'number') {
      this._floors = val;
    } else {
      throw TypeError('Floors must be a number');
    }
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
