export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  get brand() {
    return this.brand;
  }

  get motor() {
    return this.motor;
  }

  get color() {
    return this.color;
  }

  set brand(newBrand) {
    this._brand = newBrand;
  }

  set motor(newMotor) {
    this._motor = newMotor;
  }

  set color(newColor) {
    this._color = newColor;
  }

  cloneCar() {
    return new Car(this.brand, this.motor, this.color);
  }
}
