export default class Airport {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  toString() {
    return `[object ${this.code}]`;
  }

  get name() {
    return this._name;
  }
  
  set name(val) {
    if (typeof (val) === 'string') {
      this._name = val;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get code() {
    return this._code;
  }
  
  set code(val) {
    if (typeof (val) === 'string') {
      this._code = val;
    } else {
      throw TypeError('Code must be a string');
    }
  }

}