const request = require('supertest');
const app = require('./index');

describe('Music API', () => {
  // Test 1: Check if /genres endpoint is working
  test('GET /genres should return status 200 and list of genres', async () => {
    const response = await request(app).get('/genres');
    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });

  // Test 2: Check if a non-existing genre returns 404
  test('GET /genres/nonexistent should return status 404', async () => {
    const response = await request(app).get('/genres/nonexistent');
    expect(response.status).toBe(404);
    expect(response.body.error).toBe('Genre not found');
  });

  // Test 3: Check if valid artist returns correct details
  test('GET /artists/:identifier should return artist details', async () => {
    const response = await request(app).get('/artists/5578942');
    expect(response.status).toBe(200);
    expect(response.body.id).toBe(5578942);
    expect(response.body.name).toBe("Doja Cat");
  });
  

  // Test 4: Check if invalid artist returns 404
  test('GET /artists/nonexistent should return status 404', async () => {
    const response = await request(app).get('/artists/nonexistent');
    expect(response.status).toBe(404);
    expect(response.body.error).toBe('Artist not found');
  });
});
