export default class Currency {
  constructor(code, name) {
    this._name = name;
    this._code = code;
  }

  set name(val) {
    if (typeof (val) === 'string') {
      this._name = val;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get name() {
    return this._name;
  }

  set code(val) {
    if (typeof (val) === 'string') {
      this._code = val;
    } else {
      throw TypeError('Code must be a string');
    }
  }

  get code() {
    return this._code;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
