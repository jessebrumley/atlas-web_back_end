const request = require('request');
const { expect } = require('chai');

describe('Home page', function () {
  it('should return status code 200', function (done) {
    request('http://localhost:7865', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return "Welcome to the payment system"', function (done) {
    request('http://localhost:7865', function (error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  it('should return status 200 and correct response when id is a number', function (done) {
    request.get('http://localhost:7865/cart/9', function (err, res, body) {
      if (err) return done(err);
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 9');
      done();
    });
  });

  it('should return status 404 when id is not a number', function (done) {
    request.get('http://localhost:7865/cart/X', function (err, res, body) {
      if (err) return done(err);
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
