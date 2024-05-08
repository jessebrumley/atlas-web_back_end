export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  toNumber() {
    return this._size;
  }

  toString() {
    return this._location;
  }

  get size() {
    return this._size;
  }

  set size(value) {
    if (typeof (value) === 'number' || value >= 0) {
      this._size = value;
    } else {
      throw TypeError('Size must be a positive number');
    }
  }

  get location() {
    return this.location;
  }

  set location(newLocation) {
    if (typeof (newLocation) === 'string') {
      this._location = newLocation;
    } else {
      throw TypeError('Location must be a string');
    }
  }
}
