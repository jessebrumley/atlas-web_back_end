import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmmount) {
    if (typeof (newAmmount) === 'number') {
      this._amount = newAmmount;
    } else {
      throw TypeError('Amount must be a number');
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (newCurrency instanceof Currency) {
      this._currency = newCurrency;
    } else {
      throw TypeError('Currency must be a currency');
    }
  }

  displayFullPrice() {
    return `${this._amount} ${Currency.name} (${Currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return (amount * conversionRate);
  }
}
