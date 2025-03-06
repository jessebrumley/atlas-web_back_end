const { createClient, print } = require('redis');
const client = createClient();
const util = require('util');

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    print(err, reply);
  });
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    print(err, reply);
  });
};

const promise_displaySchoolValue = util.promisify(client.get);

async function displaySchoolValue(schoolName) {
  try {
    const result = await promise_displaySchoolValue(schoolName);
    console.log(result);
  } catch (err) {
    console.error(err)
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
